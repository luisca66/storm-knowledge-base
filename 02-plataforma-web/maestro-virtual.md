---
titulo: "Maestro Virtual"
tipo: spec
ultima_actualizacion: 2026-04-07
relacionado_con:
  - 01-metodo-pedagogico/ejercicios/reglas-validacion.md
  - 02-plataforma-web/arquitectura.md
  - 02-plataforma-web/secuenciador.md
estado: borrador
---

# Maestro Virtual

## Resumen
El validador automático de ejercicios MIDI. Recibe el archivo MIDI del estudiante, aplica reglas de validación por lección, y devuelve retroalimentación.

## Arquitectura
- `midi-parser.ts` — parseo del archivo MIDI
- `scale-validator.ts` — reglas de validación de escalas
- API route — endpoint que recibe el MIDI y devuelve resultado

## Problema Enarmónico
[LLENAR: Explicación detallada del problema F#/Gb y cómo se resolvió con key_signature meta-messages]

## Estado por Lección

| Lección | Validador | Estado |
|---------|-----------|--------|
| 1 - Escalas Mayores | Implementado y desplegado | Completo |
| 2 - Escalas Menores | Especificado en documento de handoff | [LLENAR] |
| 3+ | [LLENAR] | |

## Documento de Handoff — Lección 2
[LLENAR: Copiar o referenciar el documento de handoff existente]

## Historial de Cambios
- 2026-04-07: Creación inicial (borrador)
