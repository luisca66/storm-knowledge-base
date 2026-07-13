"""Lint del KB — verificación reproducible.

Uso: python herramientas/lint_kb.py   (desde la raíz del repo)

Verifica las tres capas mecánicas de salud del KB:
  [1] referencias `relacionado_con` del frontmatter apuntan a archivos/carpetas que existen
  [2] enlaces markdown relativos (.md) resuelven a un archivo real; los enlaces file:/// se marcan
  [3] todo archivo del wiki principal tiene frontmatter

Es la parte "enforce, don't instruct" del lint: no depende de que el modelo
recuerde qué revisar. La revisión de juicio (borradores estancados, duplicación
semántica, contradicciones) sigue siendo humana/IA — ver CLAUDE.md §5.

Las bibliotecas especializadas pueden contener transcripts crudos fuera de
`07-fuentes/`; su README de catálogo sigue siendo wiki y sí requiere frontmatter.
"""
import re
import urllib.parse
from pathlib import Path

root = Path(".")
allfiles = {p.as_posix() for p in root.rglob("*") if ".git" not in p.parts}


def es_fuente_cruda(p: Path) -> bool:
    """Reconoce fuentes inmutables generales o de una biblioteca especializada."""
    if "07-fuentes" in p.parts:
        return True
    return (
        "09-migracion-empresas" in p.parts
        and "videos" in p.parts
        and p.name != "README.md"
    )

# 1. Referencias relacionado_con en frontmatter
broken, checked = [], 0
for p in root.rglob("*.md"):
    if ".git" in p.parts or es_fuente_cruda(p):
        continue
    text = p.read_text(encoding="utf-8")
    m = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        continue
    rc = re.search(r"relacionado_con:\n((?:[ \t]+-[ \t]+.*\n?)+)", m.group(1))
    if not rc:
        continue
    for line in rc.group(1).strip().splitlines():
        target = line.strip().lstrip("-").strip().strip('"')
        checked += 1
        if target.rstrip("/") not in allfiles and not Path(target.rstrip("/")).is_dir():
            broken.append((p.as_posix(), target))

print(f"[1] relacionado_con: {checked} verificadas, {len(broken)} rotas")
for b in broken:
    print("   ROTA:", b[0], "->", b[1])

# 2. Enlaces markdown relativos
badlinks, nlinks = [], 0
for p in root.rglob("*.md"):
    if ".git" in p.parts or es_fuente_cruda(p) or "clases-ia" in p.parts:
        continue
    for m in re.finditer(r"\]\(([^)#\s]+\.md)(#[^)]*)?\)", p.read_text(encoding="utf-8")):
        href = m.group(1)
        if href.startswith("file:"):
            badlinks.append((p.as_posix(), href))
            continue
        if href.startswith("http"):
            continue
        nlinks += 1
        if not (p.parent / urllib.parse.unquote(href)).resolve().exists():
            badlinks.append((p.as_posix(), href))

print(f"[2] enlaces .md relativos: {nlinks} verificados, {len(badlinks)} rotos")
for b in badlinks:
    print("   ROTO:", b[0], "->", b[1])

# 3. Frontmatter presente en el wiki principal
sin_fm = []
EXENTOS = {"CLAUDE.md", "AGENTS.md", "log.md", "README.md"}
for p in root.rglob("*.md"):
    if ".git" in p.parts or es_fuente_cruda(p) or "clases-ia" in p.parts:
        continue
    if p.name in EXENTOS:
        continue
    if not p.read_text(encoding="utf-8").startswith("---"):
        sin_fm.append(p.as_posix())

print(f"[3] frontmatter: {len(sin_fm)} archivos sin frontmatter")
for f in sin_fm:
    print("   SIN FM:", f)

ok = not broken and not badlinks and not sin_fm
print("\nRESULTADO:", "OK - KB sano" if ok else "HAY HALLAZGOS - corregir arriba")
