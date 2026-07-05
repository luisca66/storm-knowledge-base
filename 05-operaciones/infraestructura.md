---
titulo: "Infraestructura"
tipo: contexto
ultima_actualizacion: 2026-07-03
relacionado_con:
  - 00-contexto/stack-tecnologico.md
  - 05-operaciones/migraciones-pendientes.md
  - 05-operaciones/flujo-trabajo.md
estado: borrador
---

# Infraestructura

## Resumen
Estado actual de toda la infraestructura de Storm Studios Learning.

## Servicios Activos

| Servicio | Proveedor | Plan | Costo | Propósito |
|----------|-----------|------|-------|-----------|
| Hosting web | Vercel | Hobby (gratis) | $0 | stormstudios.com.mx |
| Audio/samples y assets | Cloudflare | [LLENAR] | [LLENAR] | Samples y músicas de la plataforma se sirven desde aquí (2026-07-03) |
| Video | YouTube | — | $0 | Videos de lecciones, incrustados con su liga |
| Email | Zoho Mail | Standard | [LLENAR] | Email profesional |
| Almacenamiento | Google Drive | Vía Gemini Pro | [LLENAR] | Archivos generales |
| Base de datos | Firebase | [LLENAR] | [LLENAR] | Datos de la app |

## Servicios Cancelados
- **Dreamhost:** Hosting anterior. Cancelado. **Audio assets ya migrados a Cloudflare** (2026-07-03) — migración cerrada.
- **Mediafire:** Almacenamiento anterior. Cancelado.

## Dominio
- stormstudios.com.mx — [LLENAR: registrar, dónde se administra DNS]

## Respaldo del KB (rutina mensual)

El KB es el activo central del proyecto y hasta julio 2026 tenía un solo punto de falla (GitHub + copia local en la misma PC). Rutina de respaldo acordada:

1. **Qué:** un `git bundle` con todo el historial del repo — un solo archivo que permite restaurar el KB completo con `git clone archivo.bundle`.
2. **Comando** (desde la raíz del repo):
   ```
   git bundle create "C:\Users\Luis\Documents\storm-kb-backup-YYYYMMDD.bundle" --all
   ```
3. **Cadencia:** mensual, al cerrar cada mes (junto con el cierre del radar de IA).
4. **Destino final:** el bundle se genera en `Documents` y **Luis debe copiarlo a Google Drive o a un disco externo** — mientras viva solo en la misma PC, protege contra corrupción del repo pero no contra falla del disco.
5. **Verificación:** `git bundle verify archivo.bundle` debe decir "okay".

*Primer respaldo generado: 2026-07-03 (`storm-kb-backup-20260703.bundle`).*

## Historial de Cambios
- 2026-04-07: Creación inicial (borrador)
- 2026-07-03: Sección de respaldo del KB — rutina mensual de `git bundle` documentada y primer respaldo generado (pendiente de §7 del schema).
- 2026-07-03: Registrados Cloudflare (audio/samples) y YouTube (video) como servicios activos; nota de Dreamhost actualizada (audio ya migrado a Cloudflare, migración cerrada).
