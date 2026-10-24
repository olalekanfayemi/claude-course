"""Read .txt/.md files in data/, split into overlapping chunks, write index.json."""
import json, pathlib, re

DATA = pathlib.Path(__file__).parent / "data"
OUT = pathlib.Path(__file__).parent / "index.json"

def chunk_text(text, size=700, overlap=120):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if p.startswith("#") and cur:          # a heading starts a new chunk
            chunks.append(cur); cur = p; continue
        if len(cur) + len(p) + 2 <= size:
            cur = (cur + "\n\n" + p).strip()
        else:
            if cur:
                chunks.append(cur)
            cur = (cur[-overlap:] + "\n\n" + p).strip() if cur and overlap else p
            while len(cur) > size * 1.5:       # very long paragraph: hard split
                chunks.append(cur[:size]); cur = cur[size - overlap:]
    if cur:
        chunks.append(cur)
    return chunks

def build():
    files = sorted(list(DATA.glob("*.txt")) + list(DATA.glob("*.md")))
    out = []
    for f in files:
        for n, c in enumerate(chunk_text(f.read_text(encoding="utf-8", errors="ignore")), 1):
            out.append({"id": f"{f.stem}#{n}", "source": f.name, "text": c})
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"Read {len(files)} files, wrote {len(out)} chunks to {OUT.name}")
    return out

if __name__ == "__main__":
    build()
