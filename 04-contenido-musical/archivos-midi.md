---
titulo: "Archivos MIDI"
tipo: catalogo
ultima_actualizacion: 2026-07-03
relacionado_con:
  - 02-plataforma-web/maestro-virtual.md
  - 02-plataforma-web/secuenciador.md
estado: completo
---

# Archivos MIDI

## No existe una biblioteca MIDI del lado de Storm Studios

Confirmado por Luis (2026-07-03): **el proyecto no almacena archivos MIDI.** El MIDI es un **formato de paso**, no un asset que se guarde.

El flujo real:

1. La lección plantea una tarea de armonía.
2. El **alumno genera el MIDI en su propia computadora** (con el Storm Sequencer u otra herramienta compatible).
3. Lo **sube al Maestro Virtual**, que lo valida en tiempo real (por eso el secuenciador debe exportar los meta-mensajes de `key_signature` — ver [decisiones-clave.md](../00-contexto/decisiones-clave.md)).
4. **No se persiste nada:** ni el MIDI del alumno ni un "MIDI correcto" de referencia viven en el repo, en Drive ni en el servidor.

## Implicación

Este archivo existía para inventariar una biblioteca que no existe. Se conserva como **nota aclaratoria** para que ninguna IA futura busque (ni intente crear) un catálogo de MIDIs. La lógica de validación vive en [maestro-virtual.md](../02-plataforma-web/maestro-virtual.md); la generación, en [secuenciador.md](../02-plataforma-web/secuenciador.md).

## Historial de Cambios
- **2026-07-03** — Reescrito desde el esqueleto `[LLENAR]`: entrevista con Luis confirma que no hay biblioteca MIDI (formato de paso, generado por el alumno, validado y no guardado). Estado: borrador → completo.
- 2026-04-07: Creación inicial (borrador).
