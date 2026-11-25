"""NumPy re-implementation of a few ImageMagick operations.

Layout: every operation has an array-level function (`*_array`) that works on
ndarrays, and a path-level wrapper that loads, applies, and returns an array.
Compose array-level functions when chaining; don't pass arrays to path wrappers.
"""
import numbers

import numpy as np
from PIL import Image, ImageOps


# ---------------------------------------------------------------- helpers
def _as_hwc(img):
    a = np.asarray(img)
    if a.ndim == 2:
        return a[:, :, None], True
    if a.ndim == 3:
        return a, False
    raise ValueError("expected (H, W) or (H, W, C) array")


def _maxval(dtype):
    return np.iinfo(dtype).max if np.issubdtype(dtype, np.integer) else 1.0


def _check_size(name, v):
    if isinstance(v, bool) or not isinstance(v, numbers.Integral) or v < 1:
        raise ValueError(f"{name} must be a positive integer, got {v!r}")
    return int(v)


# ---------------------------------------------------------------- I/O
def load(path, auto_orient=False):
    """Load an image as an ndarray.

    auto_orient=False matches ImageMagick's default (it only rotates with
    -auto-orient). Pass True to apply EXIF orientation.
    Output is (H, W) or (H, W, C) with C in {2, 3, 4}.
    """
    im = Image.open(path)
    if auto_orient:
        im = ImageOps.exif_transpose(im)

    has_trns = "transparency" in im.info
    mode = im.mode
    if mode == "P":
        im = im.convert("RGBA" if has_trns else "RGB")
    elif mode == "PA":
        im = im.convert("RGBA")
    elif mode == "RGBa":
        im = im.convert("RGBA")
    elif mode == "La":
        im = im.convert("LA")
    elif mode == "1":
        im = im.convert("L")
    elif mode in ("CMYK", "YCbCr", "LAB", "HSV"):
        im = im.convert("RGB")
    elif mode in ("L", "RGB") and has_trns:
        # tRNS on grayscale/RGB: Pillow keeps it only in .info
        im = im.convert("LA" if mode == "L" else "RGBA")
    # remaining modes (L, LA, RGB, RGBA, I, I;16*, F) pass through unchanged
    return np.asarray(im)


def save(arr, path, jpeg_background=(255, 255, 255), **save_kwargs):
    """Save an ndarray. Alpha is composited over `jpeg_background` for formats
    that can't store it (JPEG, BMP). Extra kwargs go to PIL (e.g. quality=92)."""
    a = np.asarray(arr)
    ext = str(path).lower().rsplit(".", 1)[-1]
    if ext in ("jpg", "jpeg", "bmp") and a.ndim == 3 and a.shape[2] in (2, 4):
        mx = _maxval(a.dtype)
        alpha = a[..., -1:].astype(np.float32) / mx
        col = a[..., :-1].astype(np.float32)
        bg = np.array(jpeg_background, dtype=np.float32)
        if col.shape[2] == 1:
            bg = bg[:1]
        col = col * alpha + bg * (mx / 255.0) * (1.0 - alpha)
        a = np.floor(np.clip(col, 0, mx) + 0.5).astype(a.dtype)
        if a.shape[2] == 1:
            a = a[:, :, 0]
    Image.fromarray(a).save(path, **save_kwargs)


# ---------------------------------------------------------------- extent
def extent_center_array(img, width, height):
    """-gravity center -background black -extent WxH
    Pads with black (opaque if there is an alpha channel) or crops, centered."""
    width = _check_size("width", width)
    height = _check_size("height", height)
    a, squeeze = _as_hwc(img)
    h, w, c = a.shape

    bg = np.zeros(c, dtype=a.dtype)
    if c in (2, 4):                      # gray+alpha / RGBA: "black" is opaque
        bg[-1] = _maxval(a.dtype)
    out = np.empty((height, width, c), dtype=a.dtype)
    out[:] = bg

    ox = int((width - w) / 2)            # truncate toward zero (matches ImageMagick 6.9)
    oy = int((height - h) / 2)
    x0, y0 = max(ox, 0), max(oy, 0)
    x1, y1 = min(ox + w, width), min(oy + h, height)
    if x1 > x0 and y1 > y0:
        out[y0:y1, x0:x1] = a[y0 - oy:y1 - oy, x0 - ox:x1 - ox]
    return out[:, :, 0] if squeeze else out


def extent_center(path, width, height, **load_kwargs):
    return extent_center_array(load(path, **load_kwargs), width, height)


# ---------------------------------------------------------------- filters
def _lanczos3(x):
    x = np.abs(x)
    return np.where(x < 3.0, np.sinc(x) * np.sinc(x / 3.0), 0.0)


def _mitchell(x):
    B = C = 1.0 / 3.0
    x = np.abs(x)
    near = ((12 - 9*B - 6*C) * x**3 + (-18 + 12*B + 6*C) * x**2 + (6 - 2*B)) / 6
    far = ((-B - 6*C) * x**3 + (6*B + 30*C) * x**2
           + (-12*B - 48*C) * x + (8*B + 24*C)) / 6
    return np.where(x < 1.0, near, np.where(x < 2.0, far, 0.0))


_FILTERS = {"lanczos": (_lanczos3, 3.0), "mitchell": (_mitchell, 2.0)}


def _resample_axis(a, n_out, kernel, support, axis, work_dtype):
    n_in = a.shape[axis]
    if n_out == n_in and kernel is _lanczos3:
        return a                         # Lanczos is exactly interpolating at 1:1; Mitchell is not (IM applies it too)
    scale = n_out / n_in
    fscale = max(1.0, 1.0 / scale)       # widen kernel when shrinking (antialias)
    r = support * fscale
    centers = (np.arange(n_out) + 0.5) / scale

    start = np.ceil(centers - r - 0.5).astype(np.int64)
    taps = int(np.ceil(2 * r)) + 1
    idx = start[:, None] + np.arange(taps)[None, :]

    wts = kernel((idx + 0.5 - centers[:, None]) / fscale)
    wts[(idx < 0) | (idx >= n_in)] = 0.0  # drop out-of-range taps, renormalize
    wts /= wts.sum(axis=1, keepdims=True)
    idx = np.clip(idx, 0, n_in - 1)

    a = np.moveaxis(a, axis, 0)
    out = np.zeros((n_out,) + a.shape[1:], dtype=work_dtype)
    shape = (-1,) + (1,) * (a.ndim - 1)
    for t in range(taps):                 # loop over taps: low memory
        out += wts[:, t].astype(work_dtype).reshape(shape) * a[idx[:, t]]
    return np.moveaxis(out, 0, axis)


# ---------------------------------------------------------------- resize
def crop_array(img, width, height, x=0, y=0):
    """-crop WxH+x+y +repage   (default: from the top-left corner)
    If the box runs past the image edge it is clipped, not padded, so the
    result can be smaller than WxH (same as ImageMagick). Raises if the box
    lies entirely outside the image."""
    width = _check_size("width", width)
    height = _check_size("height", height)
    a = np.asarray(img)
    if a.ndim not in (2, 3):
        raise ValueError("expected (H, W) or (H, W, C) array")
    h, w = a.shape[:2]
    x0, y0 = max(int(x), 0), max(int(y), 0)
    x1, y1 = min(int(x) + width, w), min(int(y) + height, h)
    if x1 <= x0 or y1 <= y0:
        raise ValueError("crop box lies outside the image")
    return a[y0:y1, x0:x1].copy()


def crop(path, width, height, x=0, y=0, auto_orient=False):
    return crop_array(load(path, auto_orient=auto_orient), width, height, x, y)

def resize_array(img, width, height, force=False, rounding=None, filter=None):
    """-resize WxH   (force=False: fit inside box, keep aspect)
       -resize WxH!  (force=True : exactly WxH, ignore aspect)

    rounding: None = "nearest" (round half up), which matched ImageMagick
              6.9.12 Q16 for RGB, RGBA and gray TGAs. Plain RGB *PNGs* matched
              "floor" instead, so pass rounding="floor" if you compare PNGs.
    filter:   None = auto, or "lanczos" / "mitchell". Auto uses Mitchell for
              alpha and enlargement, Lanczos otherwise. Caveat: IM6 also used
              Mitchell for 8-bit gray *PNGs* (palette-class) but not for gray
              TGAs, so pass filter="mitchell" if you need that PNG behavior.
    """
    width = _check_size("width", width)
    height = _check_size("height", height)
    a, squeeze = _as_hwc(img)
    h, w, c = a.shape
    dtype = a.dtype
    is_int = np.issubdtype(dtype, np.integer)
    mx = _maxval(dtype)

    if force:
        nw, nh = width, height
    else:
        sx, sy = width / w, height / h
        if sx <= sy:
            nw, nh = width, max(1, int(h * sx + 0.5))
        else:
            nh, nw = height, max(1, int(w * sy + 0.5))

    if (nw, nh) == (w, h):
        return np.array(img, copy=True)

    has_alpha = c in (2, 4)
    if filter is None:
        name = "mitchell" if (has_alpha or nw * nh > w * h) else "lanczos"
    else:
        name = filter
    kernel, support = _FILTERS[name]

    # float32 holds <=16-bit ints exactly enough; wider ints / float64 need float64
    work = np.float32 if dtype.itemsize <= 2 or dtype == np.float32 else np.float64
    f = a.astype(work)
    if has_alpha:                         # premultiply so transparent pixels don't bleed
        alpha = f[..., -1:] / mx
        f[..., :-1] *= alpha

    f = _resample_axis(f, nw, kernel, support, axis=1, work_dtype=work)
    f = _resample_axis(f, nh, kernel, support, axis=0, work_dtype=work)

    if has_alpha:
        alpha = np.clip(f[..., -1:] / mx, 0.0, 1.0)
        np.divide(f[..., :-1], alpha, out=f[..., :-1], where=alpha > 0)

    if is_int:
        mode = rounding or "nearest"
        f = np.floor(f + 0.5) if mode == "nearest" else np.floor(f)
        f = np.clip(f, np.iinfo(dtype).min, mx).astype(dtype)
    else:
        f = f.astype(dtype)               # float data: no [0, 1] clipping
        if has_alpha:
            f[..., -1] = np.clip(f[..., -1], 0.0, 1.0)
    return f[:, :, 0] if squeeze else f


def resize(path, width, height, force=False, auto_orient=False, **resize_kwargs):
    """Path wrapper. resize_kwargs (rounding=, filter=) go to resize_array."""
    return resize_array(load(path, auto_orient=auto_orient), width, height,
                        force, **resize_kwargs)


def downscale_array(img, percent, **kw):
    """-resize N%   (uniform scale, 0 < percent <= 100)"""
    if not 0 < percent <= 100:
        raise ValueError("percent must be in (0, 100]")
    a, _ = _as_hwc(img)
    h, w = a.shape[:2]
    nw = max(1, int(w * percent / 100 + 0.5))
    nh = max(1, int(h * percent / 100 + 0.5))
    return resize_array(img, nw, nh, force=True, **kw)


def downscale(path, percent, auto_orient=False, **resize_kwargs):
    return downscale_array(load(path, auto_orient=auto_orient), percent,
                           **resize_kwargs)
