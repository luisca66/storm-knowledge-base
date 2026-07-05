---
titulo: "Plan de Mejoras Estructurales del KB — Julio 2026"
tipo: spec
ultima_actualizacion: 2026-07-03
relacionado_con:
  - 05-operaciones/flujo-trabajo.md
  - 05-operaciones/infraestructura.md
  - 00-contexto/ritmos-y-decisiones.md
estado: completo
---

# Plan de Mejoras Estructurales del KB — Julio 2026

> **Para el agente que ejecute este plan (Opus):** este documento es autocontenido. Fue redactado por Fable 5 el 2026-07-03 tras el lint general, y aprobado por Luis. Ejecuta las tareas en orden; cada una tiene pasos concretos y criterio de verificación. Al terminar cada tarea: registrar en `log.md`, y al final commit + push (regla de Luis: nunca dejar el working tree sucio). Cuando todo esté hecho, marcar este archivo como ejecutado (ver §Cierre).

**Objetivo común:** convertir prácticas que hoy dependen de la memoria o de la buena voluntad de cada modelo en **sistema versionado** — verificación reproducible, rituales documentados y cero duplicación.

---

## Tarea 1 — Documentar el workflow "Cierre de Mes" en CLAUDE.md §5

**Por qué:** el cierre de junio (2026-07-03) combinó: cerrar el mes en el radar + crear el diario mensual + lint + reconciliar índices + generar respaldo. Funcionó muy bien, pero solo existe como historia en `log.md`. Debe ser un workflow con nombre que cualquier IA ejecute idéntico.

**Pasos:**
1. En `CLAUDE.md`, sección **5. Workflows**, agregar un workflow nuevo después de "Lint del KB":

```markdown
### Cierre de Mes (ejecutar el día 1 de cada mes, o al primer día hábil de sesión)

1. **Cerrar el mes en `00-contexto/ai-radar.md`:** sintetizar los días faltantes desde
   `07-fuentes/ainews/YYYYMM/indice_general.md` (+ resúmenes diarios si hace falta detalle).
   Actualizar encabezado del mes, señales, modelos, frases y la Sección 3 (filtro pedagógico).
2. **Crear el diario mensual** `06-diario-proyecto/YYYY-MM.md` desde log.md y CHANGELOG.md
   (formato: hitos narrativos + balance del mes).
3. **Correr el lint completo** (`herramientas/lint_kb.py` — ver Tarea 2) y corregir hallazgos.
4. **Reconciliar archivos de control:** index.md (estadísticas), CLAUDE.md §7, CHANGELOG.md.
5. **Generar respaldo:** `git bundle create "C:\Users\Luis\Documents\storm-kb-backup-YYYYMMDD.bundle" --all`
   + `git bundle verify`. Recordar a Luis copiarlo a Drive/disco externo.
6. **Registrar en log.md** (`## [FECHA] lint | Cierre de mes YYYY-MM`), commit y push.
```

2. Verificar que el texto no contradiga los workflows existentes (el Cierre de Mes *incluye* al Lint, no lo reemplaza).

**Verificación:** el workflow aparece en §5; la nota de mantenimiento de `ai-radar.md` ("actualizar mensualmente") ahora puede referenciarlo.

---

## Tarea 2 — Crear `herramientas/lint_kb.py` (verificación reproducible)

**Por qué:** los chequeos del lint de julio se hicieron con un script temporal que murió con la sesión. La verificación no debe depender de que cada modelo reescriba (bien) sus propios chequeos. Es "enforce, don't instruct" aplicado al KB, y ataca la capa débil del diagnóstico de autonomía (`flujo-trabajo.md`): verificación.

**Pasos:**
1. Crear la carpeta `herramientas/` en la raíz del repo.
2. Crear `herramientas/lint_kb.py` con este contenido (probado el 2026-07-03; ajustar si hace falta):

```python
"""Lint del KB — verificación reproducible.
Uso: python herramientas/lint_kb.py   (desde la raíz del repo)
Salida esperada (2026-07-03): 165 refs OK, 119 enlaces OK, 0 roturas.
"""
import re
import urllib.parse
from pathlib import Path

root = Path(".")
allfiles = {p.as_posix() for p in root.rglob("*") if ".git" not in p.parts}

# 1. Referencias relacionado_con en frontmatter
broken, checked = [], 0
for p in root.rglob("*.md"):
    if ".git" in p.parts or "07-fuentes" in p.parts:
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
    if ".git" in p.parts or "07-fuentes" in p.parts or "clases-ia" in p.parts:
        continue
    for m in re.finditer(r"\]\(([^)#\s]+\.md)(#[^)]*)?\)", p.read_text(encoding="utf-8")):
        href = m.group(1)
        if href.startswith(("http", "file:")):
            badlinks.append((p.as_posix(), href)) if href.startswith("file:") else None
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
    if ".git" in p.parts or "07-fuentes" in p.parts or "clases-ia" in p.parts:
        continue
    if p.name in EXENTOS:
        continue
    if not p.read_text(encoding="utf-8").startswith("---"):
        sin_fm.append(p.as_posix())

print(f"[3] frontmatter: {len(sin_fm)} archivos sin frontmatter")
for f in sin_fm:
    print("   SIN FM:", f)

ok = not broken and not badlinks and not sin_fm
print("\nRESULTADO:", "OK — KB sano" if ok else "HAY HALLAZGOS — corregir arriba")
```

3. Ejecutarlo y confirmar que la salida da 0 roturas (estado al cierre del 2026-07-03).
4. Documentar su existencia: una línea en el workflow "Lint del KB" de `CLAUDE.md` §5 ("correr `python herramientas/lint_kb.py` como primer paso") y una fila en `index.md` si se considera archivo de sistema.

**Verificación:** `python herramientas/lint_kb.py` corre desde la raíz y reporta "OK — KB sano".

---

## Tarea 3 — Adelgazar el registro de ainews en log.md (solo hacia adelante)

**Por qué:** `log.md` supera las 1,400 líneas y la mayoría son ingestas diarias de ainews cuyos "temas del día" **duplican** el índice mensual (`07-fuentes/ainews/YYYYMM/indice_general.md`) — contra la regla de fuente única.

**Pasos:**
1. **NO reescribir entradas históricas** — log.md es un ledger append-only; lo ya escrito se queda.
2. Cambiar la convención hacia adelante: editar el encabezado de `log.md` (las líneas de formato bajo el título) agregando:
   > Las ingestas diarias de ainews se registran en **una sola línea**: `## [FECHA] ingest | ainews YYYY-MM-DD → ver 07-fuentes/ainews/YYYYMM/indice_general.md`. El detalle de temas vive únicamente en el índice mensual.
3. Documentar el mismo cambio en `00-contexto/ritmos-y-decisiones.md` (sección del sistema ainews), con el porqué (fuente única, log legible).
4. Si el proceso de ingesta lo ejecuta una tarea programada/skill de Openclaw-Cowork, avisar a Luis que el prompt de esa tarea debe actualizarse — el agente de este plan probablemente no tiene acceso a esa configuración.

**Verificación:** la siguiente ingesta de ainews produce una entrada de 1 línea en log.md.

---

## Tarea 4 — Recordatorio automático del Cierre de Mes

**Por qué:** el ritual no debe depender de la memoria de nadie.

**Pasos:**
1. Crear una tarea programada (skill `schedule` / scheduled tasks de Cowork) que el **día 1 de cada mes a las 9:00** dispare una sesión con el prompt:
   > "Ejecuta el workflow Cierre de Mes de CLAUDE.md §5 para el mes que acaba de terminar."
2. Si el entorno no permite crear la tarea programada, dejar el pendiente anotado en `CLAUDE.md` §7 y decírselo a Luis explícitamente.

**Verificación:** la tarea aparece listada en las tareas programadas, o el pendiente quedó registrado.

---

## Tarea 5 — Borradores estancados (REQUIERE DECISIÓN DE LUIS — preguntar antes de actuar)

Luis no expresó preferencia todavía. Preguntarle al inicio de la sesión:

- `04-contenido-musical/` (3 archivos) y `05-operaciones/migraciones-pendientes.md` llevan desde abril en `borrador`.
- **Opción A:** entrevista corta (10-15 min) para llenar lo esencial.
- **Opción B:** marcarlos como "esqueleto intencional — llenar cuando la plataforma lo exija" (dejan de contar como deuda en los lints).
- **Opción C:** dejarlos como están.

Ejecutar lo que Luis elija; si no está disponible, saltar esta tarea sin tocar nada.

---

## Cierre (al completar el plan)

1. Actualizar este archivo: `estado: completo` → agregar al final una sección "## Ejecución" con fecha, agente y resultado por tarea.
2. Actualizar `CLAUDE.md` §7: quitar el pendiente de este plan o marcar ✅.
3. Registrar en `log.md` y `CHANGELOG.md`; actualizar `index.md` si cambió algo catalogable.
4. Commit + push. Regenerar el bundle solo si es día de cierre de mes.

---
## Historial de Cambios
- **2026-07-03** — Creación del plan (Fable 5), aprobado por Luis para ejecución por Opus.
