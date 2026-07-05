---
titulo: "Audio y Video de la Plataforma"
tipo: catalogo
ultima_actualizacion: 2026-07-03
relacionado_con:
  - 00-contexto/stack-tecnologico.md
  - 05-operaciones/infraestructura.md
estado: completo
---

# Audio y Video de la Plataforma

## Cómo se sirve el contenido hoy (2026-07-03)

Confirmado por Luis:

- **Audio (samples y músicas de la plataforma):** alojado en **Cloudflare**. Todos los samples y las músicas del sitio se sirven desde ahí.
- **Video:** vive en **YouTube**, y el sitio lo incrusta con su liga correspondiente. No se hostea video propio.

## La migración vieja quedó resuelta

Este archivo describía antes una migración pendiente: el audio estaba en **Dreamhost** (hosting cancelado) y **Mediafire** (cancelado), con URLs hardcodeadas en el codebase de Next.js, y el plan era moverlo a Google Drive.

**Ese plan quedó superado:** el audio terminó en **Cloudflare**, no en Drive, y la migración **ya está hecha**. No hay assets huérfanos ni URLs muertas pendientes de este lado. (Ver el cierre en [migraciones-pendientes.md](../05-operaciones/migraciones-pendientes.md).)

## Nota

No se mantiene un inventario archivo-por-archivo del audio: es infraestructura de la plataforma (Cloudflare), no un catálogo curado. Si en algún momento hace falta auditar qué se sirve, se genera desde el codebase. La **obra musical propia** de Luis (canciones hechas con IA) es otra cosa y vive en [discografia-ia.md](discografia-ia.md).

## Historial de Cambios
- **2026-07-03** — Reescrito desde el esqueleto: entrevista con Luis confirma audio en Cloudflare y video en YouTube; la migración Dreamhost→Drive quedó resuelta (vía Cloudflare). Estado: borrador → completo.
- 2026-04-07: Creación inicial (borrador).
