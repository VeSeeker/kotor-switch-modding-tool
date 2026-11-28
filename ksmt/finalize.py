from .util import CheckFinalizedExists, CheckInitializedExists, CheckCaseSensitive, Error, Warning, Success, K1TitleID, K2TitleID, YesNo, rmrf, rootDir, fileListDir, MirrorFolders, file_sha256
from .backup import Backup
import os
import shutil
from .tga2tpc import converter, tex2tga
import struct
from .imageresize import downscale, resize, extent_center, crop, save
from concurrent.futures import ThreadPoolExecutor, as_completed

cycleTextures = {
    "PLC_Kiosk1.tga": "00d627a12e94a68b58d8eb182b2b03645e145df04a463937a1f77c8ead67fcef",
    "PLC_CompPnl.tga": "d32d6cea0a440a78b5424b361ecde427b33753e723b98d5e1f92ba3b0e36fde7",
    "PLC_CompPnl_b.tga": "d32d6cea0a440a78b5424b361ecde427b33753e723b98d5e1f92ba3b0e36fde7",
    "PLC_Desk1.tga": "e8953d8d1e9d44c3141c69679517c04cd6295ddccfe8595191682bade7a1e8ff",
    "PLC_Sign.tga": "f010020e59eefd2cb1229b9e00545ca2b63b26944e065c24680b613c1342debd",
    "PLC_RepTab.tga": "8a4daabeb84ee39b723a6a0c16abcf8965823ca4ca8bc206f5f1646bf700538c",
    "PLC_RepTab2.tga": "f6b4bf29917d9d38add969b4e95fb539a317f0adc3bd80f4df59427017517a3f",
    "vurt": "31e9b9a69d30799c7c0b082d8b186099cd29da44955efe4b119f789a71605a6c"
}
jcBlasterTextures = [
    "JC_FX_Laser_B2.tga",
    "JC_FX_Laser_G2.tga",
    "JC_FX_Laser_R2.tga",
    "JC_FX_Laser_W2.tga",
    "JC_FX_Laser_Y2.tga"
]
hiResBeamEffects = {
    "Fx_Lightning.tga": "3645bda08723b36c9cad1516373426caa395a97ecc5e5b248ee09329f54e0fea",
    "Fx_Drain.tga": "bb199d073ab6742bca459b7ecd14dfa3badd93026739fd319d8767e93d2f6dc1"
}
computer = {
    "lbl_compover.tga": "6aed2664531e60268d1481db5c469a07d51142a8ff311493fbdcb3a96115c177"
}
tslBadIcons = {
    "iw_hldoblst_001.tga": "1f87454d86e1a2840ddfc9f57a7ddfeaf3d716e8c78e174036ccbb48d1ff101a",
    "iw_hldoblst_002.tga": "d4a17bfaffba4c023964fa17bee3adfbf50d979b3e45f6d162fbc4bad5ad6549",
    "iw_hldoblst_003.tga": "f4065a834b5a09dd678adf6c1ba349f58ec8d66b46ac1d3ecfe84d1c108f245a",
    "iw_hldoblst_004.tga": "6ef324151f75b63494bba3977331d453b60a7640b40af6df324e8ceee252e695",
    "iw_hvrptbltr_001.tga": "a073385fedc1e8c962493d574aca5f1bc0b18fa6e3587eee93cddabd300aa2a0",
    "iw_hvrptbltr_002.tga": "63b97f25821f43c0678d0e762ae021aa7ecf63826dc9064498da8bafefc7d8a6",
    "iw_hvrptbltr_003.tga": "6ba6c6bd7c538133b5d3fa85c9b9d0237c46f98ee353d8444088625a3d896e51",
    "iw_hvyblstr_001.tga": "0a207afaa1c47d190a7c98fceb1fe2e9e7e1700ff580eaaa0e425f3dea7cb1b5",
    "iw_hvyblstr_002.tga": "4f86e90192c4edb71212a28dda3af6b1792aa89a6053c27895a73bf08c94fb0a",
    "iw_hvyblstr_003.tga": "c70c45db68d9114bbacd80781637c3df5877870c8a1dbbe74628847a84f50537",
    "iw_hvyblstr_004.tga": "06b554858f561811b1af25bfdcc00ce3b075ea9fa5715e16a29db326777da120",
    "iw_hvyblstr_005.tga": "de74d1c6354cf31c49cc95fcc1d2b80ea04a2a0567ae28a305a8ef7fabde68c0",
}
# Don't put extension, put them all in lowercase
K1extraDownscaleTextures = [
    "jc_ithoriancz01",
    "lts_lotrim01",
    "lts_lotrim02",
    "lts_lotrim04",
    "lts_lotrim09",
    "lts_lotrim10",
    "lts_loflr05",
    "lta_flalpha",
    "lta_flr01a",
    "lta_flr01",
    "lta_sail02",
    "lta_sand01",
    "lta_wall00",
    "lta_wll01",
    "lta_wll01_00a",
    "lda_bark04",
    "lda_flr01",
    "lyv_wall03",
    "lyv_wall04",
    "lyv_wall05",
    "lyv_wall08",
    "lyv_wall09",
    "lun_grss02",
    "lun_wll01",
    "lun_wll02"
]
K2extraDownscaleTxtures = [
    "per_cl01",
    "per_gr02",
    "per_wl01",
    "tel_stl3",
    "tel_stl4",
    "tel_stl5",
    "tel_stl6",
    "tel_stl7",
    "nar_cr8",
    "nar_fl04",
    "nar_wl01",
    "nar_wl10"
]

def Finalize(gameNum):

    print("Running checks")

    if gameNum == "1":
        targetFolderName = K1TitleID
        extraDownscaleTextures = K1extraDownscaleTextures
    elif gameNum == "2":
        targetFolderName = K2TitleID
        extraDownscaleTextures = K2extraDownscaleTxtures
    else:
        Error(f"Invalid game number: {gameNum}")
        return False
    targetFolderPath = os.path.join(rootDir, targetFolderName)

    k2Languages = ["English", "French", "German", "Italian", "Japanese", "Spanish"]

    if gameNum == "1":
        localizedPath = targetFolderPath
    else:
        for i in range(len(k2Languages)):
            print(f"[{i}] {k2Languages[i]}")
        while True:
            idx = 100
            choice = input("Select game language (I have only tested English so good luck): ")
            if choice.isdigit():
                idx = int(choice)
            if idx in range(len(k2Languages)):
                break
            else:
                print("Please enter a valid number")
        localizedPath = os.path.join(targetFolderPath, "Localized", k2Languages[idx])

    if CheckCaseSensitive():
        Warning(f"Case sensitive folder detected, this can cause undesired outcomes")
    else:
        Success(f"Case insensitive folder detected")

    if not CheckInitializedExists(gameNum):
        Error(f"Cannot finalize when no initialized folder exists")
        return False

    if CheckFinalizedExists(gameNum):
        Warning(f"Kotor {gameNum} has already been finalized")

        if YesNo(f"Delete finalized folder?"):
            rmrf(targetFolderPath)
        else:
            Error("Cannot finalize when finalized folder already exists")
            return False

    switchFolders = os.path.join(fileListDir, f"K{gameNum}SwitchFolders.txt")
    switchFiles = os.path.join(fileListDir, f"K{gameNum}SwitchFiles.txt")
    initFolder = os.path.join(rootDir, f"K{gameNum}romfs")
    overrideDir = os.path.join(initFolder, "override")

    # This should be fine because it needs to be case insensitive, so it finds override and Override. Maybe add a check here that warns about case sensitivity again

    if not os.path.isfile(switchFolders):
        Error(f"Missing file list: {switchFolders}")
        return False
    else:
        print(f"{switchFolders} present")

    if not os.path.isfile(switchFiles):
        Error(f"Missing file list: {switchFiles}")
        return False
    else:
        print(f"{switchFiles} present")

    Backup(gameNum, False)

    # Here the bash version deletes dialog.tlk and swplayer.ini if they are unmodified. I'm not really sure what the point of that is, so I'm leaving that out for now.

    # print("Finding mod files")
    '''
    modFiles = []
    for root, dirs, filenames in os.walk(initFolder):
        for filename in filenames:
            modFiles.append(filename)
    '''
    # print(f"Found {len(modFiles)} modded files")

    print("Building Switch file set")

    switchTpcs = set()

    with open(switchFiles, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.replace("\n", '')
            directory, fullName = os.path.split(i)
            root, extension = os.path.splitext(fullName)
            if extension.lower() == ".tpc":
                switchTpcs.add(root.lower())
    print(f"Found {len(switchTpcs)} Switch .tpc files")

    print("Checking for duplicate textures")

    # Check if local tga/txi/dds files have a local tpc file in the same directory, and if not, check if they are part of the Switch's .tpc files, and if so, add them to dupTga
    invalidPath = os.path.join(initFolder, "ConvertMe")
    def MoveListToInvalidFolder(fileList):
        os.makedirs(invalidPath, exist_ok=True)
        for i in fileList:
            pt = os.path.join(overrideDir, i)
            shutil.move(pt, os.path.join(invalidPath, i))
            root, extension = os.path.splitext(i)
            maybeTxi = f"{root}.txi"
            if os.path.exists(os.path.join(overrideDir, maybeTxi)):
                shutil.move(os.path.join(overrideDir, maybeTxi), os.path.join(invalidPath, maybeTxi))
        Warning(f"Convert the files in {invalidPath} to .tpc, move them to override, delete {invalidPath}, and then re-run finalize")
        return
    modTpcSet = set()
    dupTga = []
    dupDds = []

    for i in os.listdir(overrideDir):
        root, extension = os.path.splitext(i)
        if extension.lower() == ".tpc":
            modTpcSet.add(root.lower())
    for j in os.listdir(overrideDir):
        root, extension = os.path.splitext(j)
        if (root.lower() not in modTpcSet) and (root.lower() in switchTpcs):
            if extension.lower() == ".tga":
                dupTga.append(j)
            elif extension.lower() == ".dds":
                dupDds.append(j)

    def ReadTgaSize(path):
        try:
            with open(path, "rb") as f:
                header = f.read(18)
        except OSError:
            return None
        if len(header) < 18:
            return None
        return struct.unpack_from("<HH", header, 12)
    def ReadTpcSize(path):
        try:
            with open(path, "rb") as f:
                header = f.read(128)
        except OSError:
            return None
        if len(header) < 128:
            return None
        return struct.unpack_from("<HH", header, 8)

    if len(dupTga) + len(dupDds) > 0:
        Warning(f"{len(dupTga) + len(dupDds)} files would be overridden by a base game .tpc file")

        convertTga = YesNo(f"Convert {len(dupTga) + len(dupDds)} files to .tpc using tga2tpc-py?")
        if not convertTga:
            MoveListToInvalidFolder(dupTga + dupDds)
            return False
    downS = YesNo("Downscale all 4K modded textures?")
    extraDownS = YesNo("Extra downscales? (VeSeeker's modding guide)")
    fourKTpc = []
    fourKTga = []
    if downS:
        tga4K = 50000000
        tpc4K = 21000000
        for i in os.listdir(overrideDir):
            root, extension = os.path.splitext(i)
            size = os.path.getsize(os.path.join(overrideDir, i))
            if extension.lower() == ".tpc":
                if size > tpc4K:
                    fourKTpc.append(i)
            elif extension.lower() == ".tga":
                if size > tga4K:
                    imgSize = ReadTgaSize(os.path.join(overrideDir, i))
                    if imgSize is None:
                        Warning(f"Couldn't read the size of {i}, skipping")
                        continue
                    width, height = imgSize
                    if (width >= 4096) and (height >= 4096):
                        fourKTga.append(i)
        print(f"Found {len(fourKTpc)} 4K .tpc files and {len(fourKTga)} 4K .tga files")

    oneNineTwo = []
    resBeams = []
    comp = []
    jcBlast = []
    tslBad = []
    cycles = dict()
    oneNineTwoSize = 22000
    for key, _ in cycleTextures.items():
        cycles[key] = []

    # Build CycleTextures dictionary

    print("Finding problematic textures")
    for i in os.listdir(overrideDir):
        root, extension = os.path.splitext(i)
        if extension.lower() == ".tga":
            size = os.path.getsize(os.path.join(overrideDir, i))
            if size < oneNineTwoSize:
                imgSize = ReadTgaSize(os.path.join(overrideDir, i))
                if imgSize is None:
                    Warning(f"Couldn't read the size of {i}, skipping")
                    continue
                width, height = imgSize
                if width == 192 and height == 192:
                    oneNineTwo.append(i)
                    continue
                elif width == 172 and height == 172:
                    oneNineTwo.append(i)
                    continue
        if i in hiResBeamEffects:
            if file_sha256(os.path.join(overrideDir, i)) == hiResBeamEffects[i]:
                resBeams.append(i)
        elif i in computer:
            if file_sha256(os.path.join(overrideDir, i)) == computer[i]:
                comp.append(i)
        elif root in cycleTextures:
            if extension.lower() == ".txi":
                cycles[root].append("txi")
                continue
            shasha = file_sha256(os.path.join(overrideDir, i))
            if shasha == cycleTextures[i] or shasha == cycleTextures["vurt"]:
                cycles[root].append("tga")
        elif i in jcBlasterTextures:
            jcBlast.append(i)
        elif i in tslBadIcons:
            shasha = file_sha256(os.path.join(overrideDir, i))
            if shasha == tslBadIcons[i]:
                tslBad.append(i)

    cnt = 0
    tot = len(oneNineTwo) + len(resBeams) + len(comp) + len(jcBlast) + len(tslBad)
    for i in oneNineTwo:
        pth = os.path.join(overrideDir, i)
        save(resize(pth, 256, 256, True), pth)
        cnt += 1
        print(f"\rFixed {cnt}/{tot}", end='', flush=True)

    for i in resBeams:
        pth = os.path.join(overrideDir, i)
        save(resize(pth, 512, 512, True), pth)
        cnt += 1
        print(f"\rFixed {cnt}/{tot}", end='', flush=True)

    for i in comp:
        pth = os.path.join(overrideDir, i)
        save(resize(pth, 1024, 256, True), pth)
        cnt += 1
        print(f"\rFixed {cnt}/{tot}", end='', flush=True)

    for i in jcBlast:
        pth = os.path.join(overrideDir, i)
        save(extent_center(pth, 256, 256), pth)
        cnt += 1
        print(f"\rFixed {cnt}/{tot}", end='', flush=True)

    for i in tslBad:
        pth = os.path.join(overrideDir, i)
        save(extent_center(pth, 256, 256), pth)
        cnt += 1
        print(f"\rFixed {cnt}/{tot}", end='', flush=True)

    print("")
    badParams = ["proceduretype", "numx", "numy", "fps", "defaultwidth", "defaultheight"]

    if len(cycles) > 0:
        print(f"Fixing cycle textures")

    for key, value in cycles.items():
        if len(value) == 2:
            nx = None
            ny = None
            txiPath = os.path.join(overrideDir, f"{key}.txi")
            with open(txiPath, 'r', encoding='utf-8') as file:
                params = file.readlines()
            for i in range(len(params)):
                params[i] = params[i].replace("\n", '')
                if params[i].split()[0] == "numx":
                    tobe = params[i].split()[1]
                    if tobe.isdigit():
                        nx = int(tobe)
                elif params[i].split()[0] == "numy":
                    tobe = params[i].split()[1]
                    if tobe.isdigit():
                        ny = int(tobe)

            tgaName = f"{key}.tga"
            pth = os.path.join(overrideDir, tgaName)
            save(crop(pth, nx, ny), pth)
            if tgaName in fourKTga:
                fourKTga.remove(tgaName)

            newParams = []
            for j in params:
                if j.split()[0] not in badParams:
                    newParams.append(j)
            with open(txiPath, 'w') as f:
                f.write("\n".join(newParams))

    def _convert_in_threads(jobs, convert_one, worker_limit=8):
        if not jobs:
                return [], []

        successes = []
        failures = []

        with ThreadPoolExecutor(max_workers=min(worker_limit, len(jobs))) as pool:
            future_to_name = {
                pool.submit(convert_one, source, output): name
                for name, source, output in jobs
            }

            for future in as_completed(future_to_name):
                name = future_to_name[future]
                try:
                    future.result()
                    successes.append(name)
                except Exception as exc:
                    Error(f"Failed to convert {name}: {exc}")
                    failures.append(name)

                print(
                    f"\rConverted files {len(successes)}/{len(jobs)}, "
                    f"{len(failures)} failures",
                    end="",
                    flush=True,
                )

        print()  # Finish the progress line
        return successes, failures

    tex2tga_options = tex2tga.TextureOptions()
    failedDds = []
    ddsCompleted = 0
    if len(dupDds) > 0:
        print("Converting DDS files to TGA")
    for i in dupDds:
        root, _ = os.path.splitext(i)
        newTga = os.path.join(overrideDir, f"{root}.tga")
        try:
            tex2tga.convert_file(os.path.join(overrideDir, i), newTga, tex2tga_options)
            ddsCompleted += 1
            dupTga.append(f"{root}.tga")
        except tex2tga.TextureConversionError as exc:
            Error(f"Failed to convert {i} to TGA: {exc}")
            failedDds.append(i)
        except Exception as exc:
            Error(f"Unexpected failure on {i}: {type(exc).__name__}: {exc}")
            failedDds.append(i)
        print(f"\rConverted {ddsCompleted}/{len(dupDds)}, {len(failedDds)} failures", end='', flush=True)
    print("")
    if len(failedDds) > 0:
        MoveListToInvalidFolder(failedDds)
        return False

    tpc_jobs = []
    if len(fourKTpc) > 0:
        print("Converting TPC files to TGA for downscaling")
    for i in fourKTpc:
        root, _ = os.path.splitext(i)
        newTga = os.path.join(overrideDir, f"{root}.tga")
        tpc_jobs.append((i, os.path.join(overrideDir, i), newTga))
    converted_tpc, failedTpcConvert = _convert_in_threads(
        tpc_jobs,
        lambda source,
        output: tex2tga.convert_file(source, output, tex2tga_options)
    )

    dupTga.extend(f"{os.path.splitext(name)[0]}.tga" for name in converted_tpc)

    def _downscale_one(path, percent):
        save(downscale(path, percent), path)

    def _downscale_in_threads(paths, percent = 50, worker_limit=8):
        paths = list(dict.fromkeys(paths))
        if not paths:
            return
        completed = 0
        failures = []

        with ThreadPoolExecutor(max_workers=min(worker_limit, len(paths))) as pool:
            future_to_path = {
                pool.submit(_downscale_one, path, percent): path
                for path in paths
            }
            for future in as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    future.result()
                    completed += 1
                except Exception as exc:
                    failures.append(path)
                    Error(f"Failed to downscale {os.path.basename(path)}: {exc}")
                print(
                    f"\rDownscaled {completed}/{len(paths)}, "
                        f"{len(failures)} failures",
                            end='',
                        flush=True,
                )
        print()

    if len(failedTpcConvert) > 0:
        print("Failed to convert some TPC files to TGA for downscaling")
        for i in failedTpcConvert:
            fourKTpc.remove(i)
    downScaleMe = [
        os.path.join(overrideDir, f"{os.path.splitext(name)[0]}.tga")
        for name in fourKTpc
    ]
    downScaleMe.extend(
        os.path.join(overrideDir, name)
        for name in fourKTga
    )
    _downscale_in_threads(downScaleMe)

    converter_options = converter.ConversionOptions().normalised()

    if len(dupTga) > 0:
        print("Converting textures to TPC")

    tga_jobs = []
    for i in dupTga:
        root, _ = os.path.splitext(i)
        newTpc = os.path.join(overrideDir, f"{root}.tpc")
        tga_jobs.append((i, os.path.join(overrideDir, i), newTpc))

    converted_tga, failedFiles = _convert_in_threads(tga_jobs, lambda source, output: converter.convert_file(source, output, converter_options),)
    for name in converted_tga:
        modTpcSet.add(os.path.splitext(name)[0].lower())

    if len(failedFiles) > 0:
        MoveListToInvalidFolder(failedFiles)
        return False


    if os.path.isdir(invalidPath):
        Error(f"{invalidPath} needs to be deleted before finalizing")
        if YesNo(f"Delete {invalidPath}?"):
            rmrf(invalidPath)
        else:
            return False

    print("Cleaning up redundant texture files")
    redTpc = []
    redTga = []
    badExt = [".tga", ".txi", ".dds"]
    for i in os.listdir(overrideDir):
        root, ext = os.path.splitext(i)
        if ext.lower() == ".tpc":
            redTpc.append(root)
    for i in os.listdir(overrideDir):
        root, ext = os.path.splitext(i)
        if ext.lower() in badExt:
            if root in redTpc:
                redTga.append(i)
    print(f"Found {len(redTga)} redundant files")
    for i in redTga:
        os.remove(os.path.join(overrideDir, i))
    Success("Cleaned up redundant files")

    exTpc = []
    exTga = []
    conTpc = []

    if extraDownS:
        print("Performing extra downscales")
        for i in os.listdir(overrideDir):
            root, ext = os.path.splitext(i)
            if root.lower() not in extraDownscaleTextures:
                continue
            if ext.lower() == ".tpc":
                newTga = os.path.join(overrideDir, f"{root}.tga")
                conTpc.append((i, os.path.join(overrideDir, i), newTga))
                exTpc.append(i)
            elif ext.lower() == ".tga":
                exTga.append(i)

        converted_tpc, failedTpcConvert = _convert_in_threads(
        conTpc,
        lambda source,
        output: tex2tga.convert_file(source, output, tex2tga_options)
        )

        downScaleMe = [
            os.path.join(overrideDir, f"{os.path.splitext(name)[0]}.tga")
            for name in converted_tpc
        ]
        downScaleMe.extend(
            os.path.join(overrideDir, name)
            for name in exTga
        )
        _downscale_in_threads(downScaleMe)

        tpcJobs = []
        for i in converted_tpc:
            root, ext = os.path.splitext(i)
            oldTga = f"{root}.tga"
            tpcJobs.append((oldTga, os.path.join(overrideDir, oldTga), os.path.join(overrideDir, i)))

        converted_tga, failedFiles = _convert_in_threads(tpcJobs, lambda source, output: converter.convert_file(source, output, converter_options),)

        for i in converted_tpc:
            root, _ = os.path.splitext(i)
            badTga = os.path.join(overrideDir, f"{root}.tga")
            badTxi = os.path.join(overrideDir, f"{root}.txi")
            if os.path.isfile(badTga):
                os.remove(badTga)
            if os.path.isfile(badTxi):
                os.remove(badTxi)

    print(f"Mirroring Kotor {gameNum} Switch ROM folder structure")

    if MirrorFolders(targetFolderName, f"K{gameNum}SwitchFolders.txt"):
        Success("Mirrored Switch ROM folder structure")
    else:
        Error("Switch ROM folder structure mirroring failed")
        return False

    # The rest of the logic

    print("Building Switch file dictionary")

    allSwitchFiles = dict()

    with open(switchFiles, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.replace("\n", '')
            _, fullName = os.path.split(i)
            allSwitchFiles[fullName.lower()] = i

    Success(f"Indexed {len(allSwitchFiles)} Switch files")

    print("Finding modded base game files")

    vanillaModFiles = []

    for root, _, filenames in os.walk(initFolder):
        for i in filenames:
            if i.lower() in allSwitchFiles:
                vanillaModFiles.append(os.path.join(root, i))

    count = 0
    for i in vanillaModFiles:
        _, fullName = os.path.split(i)
        shutil.move(i, os.path.join(targetFolderPath, allSwitchFiles[fullName.lower()]))
        count += 1
        print(f"\rMoving modded base game files: {count}/{len(vanillaModFiles)}", end='', flush=True)
    print("")

    newTextures = []
    textureExt = [".tga", ".txi", ".tpc", ".dds"]
    new2da = []
    newLocalized = []
    basicFile = []
    saves = []
    tempSavesDir = os.path.join(rootDir, "tempSaves")
    os.makedirs(tempSavesDir, exist_ok=True)

    for i in os.listdir(os.path.join(initFolder, "saves")):
        saves.append(i)
    for i in saves:
        shutil.move(os.path.join(initFolder, "saves", i), os.path.join(tempSavesDir, i))

    for root, _, filenames in os.walk(initFolder):
        relPath = os.path.relpath(root, initFolder).split(os.sep)[0]
        lowRelPath = relPath.lower()
        for i in filenames:
            if lowRelPath == "override":
                _, ext = os.path.splitext(i)
                if ext.lower() in textureExt:
                    newTextures.append(os.path.join(root, i))
                elif ext.lower() == ".2da":
                    new2da.append(os.path.join(root, i))
                else:
                    basicFile.append(os.path.join(root, i))
            elif lowRelPath == "docs":
                newLocalized.append(os.path.join(root, i))
            elif lowRelPath == "streamvoice":
                newLocalized.append(os.path.join(root, i))
            elif lowRelPath == "streamwaves":
                newLocalized.append(os.path.join(root, i))
            elif lowRelPath == "lips":
                newLocalized.append(os.path.join(root, i))
            else:
                basicFile.append(os.path.join(root, i))
    targetOverride = os.path.join(targetFolderPath, "override")

    if gameNum == "1":
        texPath = os.path.join(targetOverride, "Textures")
        twoDAPath = os.path.join(targetOverride, "2da")
    else:
        texPath = os.path.join(targetOverride, "textures")
        twoDAPath = os.path.join(targetOverride, "2DA")

    if len(newTextures) > 0:
        print("Moving modded textures files")
        cnt = 0
    for i in newTextures:
        _, name = os.path.split(i)
        shutil.move(i, os.path.join(texPath, name))
        cnt += 1
        print(f"\rMoved texture files: {cnt}/{len(newTextures)}", end='', flush=True)
    print("")

    if len(new2da) > 0:
        print("Moving modded 2da files")
        cnt = 0
    for i in new2da:
        _, name = os.path.split(i)
        shutil.move(i, os.path.join(twoDAPath, name))
        cnt += 1
        print(f"\rMoved 2da files: {cnt}/{len(new2da)}", end='', flush=True)
    print("")

    if len(newLocalized) > 0:
        print("Moving localized files")
        cnt = 0
    for i in newLocalized:
        path, name = os.path.split(i)
        relPath = os.path.relpath(path, initFolder)
        shutil.move(i, os.path.join(localizedPath, relPath, name))
        cnt += 1
        print(f"\rMoved localized files: {cnt}/{len(newLocalized)}", end='', flush=True)
    print("")

    if len(basicFile) > 0:
        print("Moving remaining files")
        cnt = 0
    for i in basicFile:
        path, name = os.path.split(i)
        relPath = os.path.relpath(path, initFolder)
        shutil.move(i, os.path.join(targetFolderPath, relPath, name))
        cnt += 1
        print(f"\rMoved remaining files: {cnt}/{len(basicFile)}", end='', flush=True)
    print("")

    for i in saves:
        shutil.move(os.path.join(tempSavesDir, i), os.path.join(targetFolderPath, "saves", i))
    rmrf(tempSavesDir)

    Success(f"Finalized folder created at {targetFolderPath}")

    # Check if there are any files left in the init folder, and if not, delete the init folder

    deleteAfter = True
    for root, dirs, filenames in os.walk(initFolder):
        if len(filenames) > 0:
            Warning(f"{len(filenames)} files left in initialized folder")
            deleteAfter = False
        for i in filenames:
            print(i)
    if deleteAfter:
        print("Clearing initialized folder (A backup still exists)")
        rmrf(initFolder)

    return True
