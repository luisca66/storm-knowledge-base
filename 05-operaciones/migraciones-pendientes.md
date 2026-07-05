---
titulo: "Migraciones Pendientes"
tipo: catalogo
ultima_actualizacion: 2026-07-03
relacionado_con:
  - 05-operaciones/infraestructura.md
  - 04-contenido-musical/audio-assets.md
estado: completo
---

# Migraciones Pendientes

## No hay migraciones pendientes (2026-07-03)

## Migración de Audio Assets — ✅ RESUELTA

**Estado:** Completada (no por la vía que este archivo predecía).

**Historia:** los archivos de audio estaban en **Dreamhost** (cancelado) y **Mediafire** (cancelado), con URLs hardcodeadas en el codebase de Next.js. El plan original (abril 2026) era moverlos a **Google Drive**.

**Desenlace:** el audio terminó en **Cloudflare**, no en Drive, y la migración ya está hecha. Los videos, por su parte, viven en **YouTube** (incrustados con su liga). No quedan assets huérfanos ni URLs muertas de este lado. Detalle del estado actual en [audio-assets.md](../04-contenido-musical/audio-assets.md).

## Otras migraciones

Ninguna registrada al 2026-07-03.

> **Nota de mantenimiento:** este archivo se conserva como registro histórico y como lugar donde anotar la próxima migración cuando surja. Mientras diga "no hay migraciones pendientes", el lint no debe tratarlo como deuda.

## Historial de Cambios
- **2026-07-03** — Migración de audio marcada como resuelta (vía Cloudflare, no Drive; video en YouTube). Ya no hay migraciones pendientes. Estado: borrador → completo.
- 2026-04-07: Creación inicial (borrador).
