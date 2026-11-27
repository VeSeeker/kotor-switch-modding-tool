import os, yaml, re, sys
from pathlib import Path

def text(v):
    if isinstance(v, list):
        return "\n".join(v)
    return (v or "").strip()

def slug(s):  # GitHub-style anchor; other renderers may differ
    return re.sub(r"[^\w\- ]", "", s.lower()).replace(" ", "-")

def assign(nodes, prefix=""):
    for i, n in enumerate(nodes, 1):
        if n["id"] in numbers:
            sys.exit(f"Duplicate id: {n['id']}")
        numbers[n["id"]] = f"{prefix}{i}"
        titles[n["id"]] = n["title"]
        assign(n.get("children", []), f"{prefix}{i}.")

def resolve(s):
    def sub(m):
        i = m.group(1)
        if i not in numbers:
            sys.exit(f"Unresolved ref: {i}")
        return f"[{numbers[i]} {titles[i]}](#{slug(numbers[i] + ' ' + titles[i])})"
    return re.sub(r"\{\{ref:([\w\-]+)\}\}", sub, s)

def render(nodes, depth=1):
    blocks = []
    for n in nodes:
        head = [f"{'#' * (depth + 1)} {numbers[n['id']]} {n['title']}"]
        if n.get("subtitle"):
            head.append(f"#### {n['subtitle']}")
        blocks.append("\n".join(head))

        if n.get("type") == "mod":
            mod = [f"- **Author:** {n.get('author', '')}"]
            dl = " ".join(f"[{d['label']}]({d['url']})" for d in n.get("downloads", []))
            mod.append(f"- **Download:** {dl}")
            method_suffix = "" if n.get("download_instructions") or n.get("install") else "\\"
            mod.append(f"- **Method:** {', '.join(n.get('method', []))}{method_suffix}")
            if n.get("download_instructions"):
                mod.append(f"**Download instructions:** {text(n['download_instructions'])}\\")
            if n.get("install"):
                mod.append(f"**Installation instructions:** {resolve(text(n['install']))}\n")
            mod.append("---")
            blocks.append("\n".join(mod))

        if n.get("body"):
            blocks.append(resolve(text(n["body"])))
        blocks += render(n.get("children", []), depth + 1)
    return blocks

data = yaml.safe_load(Path(os.path.join(os.getcwd(), "K1Guide.yaml")).read_text(encoding="utf-8"))
numbers, titles = {}, {}

assign(data["sections"])
blocks = [f"# {data['title']}\n#### By {data['author']}"] + render(data["sections"])

out = blocks[0]
for prev, block in zip(blocks, blocks[1:]):
    # no blank line after a horizontal rule, blank line everywhere else
    out += ("\n" if prev.endswith("---") else "\n\n") + block
Path(os.path.join(os.getcwd(), "K1Guide.md")).write_text(out + "\n", encoding="utf-8")
print(f"Built K1Guide.md ({len(numbers)} sections)")

data = yaml.safe_load(Path(os.path.join(os.getcwd(), "K2Guide.yaml")).read_text(encoding="utf-8"))
numbers, titles = {}, {}

assign(data["sections"])
blocks = [f"# {data['title']}\n#### By {data['author']}"] + render(data["sections"])

out = blocks[0]
for prev, block in zip(blocks, blocks[1:]):
    # no blank line after a horizontal rule, blank line everywhere else
    out += ("\n" if prev.endswith("---") else "\n\n") + block
Path(os.path.join(os.getcwd(), "K2Guide.md")).write_text(out + "\n", encoding="utf-8")
print(f"Built K2Guide.md ({len(numbers)} sections)")
