---
titulo: "Secuenciador Storm Studios"
tipo: spec
ultima_actualizacion: 2026-04-16
relacionado_con:
  - 02-plataforma-web/maestro-virtual.md
  - 00-contexto/decisiones-clave.md
estado: borrador
---

# Secuenciador Storm Studios

## Resumen
El secuenciador MIDI propio de Storm Studios Learning. Herramienta obligatoria para los estudiantes. Exporta key_signature meta-messages que resuelven el problema enarmónico.

## Función pedagógica

El Storm Sequencer tiene un rol específico y acotado en el curso en línea: **es la herramienta de entrega de tareas**. El alumno escribe el ejercicio de la lección en el Sequencer y lo valida con el Maestro Virtual. No está diseñado como herramienta de exploración o composición libre — ese rol lo cumple Cubase en las clases presenciales.

Esta distinción es intencional: el entorno en línea prioriza la validación precisa sobre la expresividad. El alumno necesita una herramienta que genere el MIDI correcto para que el Maestro Virtual pueda hacer su trabajo.

## Diferenciador técnico clave

Exporta `key_signature` meta-messages que los DAWs comerciales (incluido Cubase) no incluyen por defecto. Esto resuelve el problema enarmónico: sin esa información, un Fa# y un Solb suenan igual pero son armónicamente distintos. El Maestro Virtual necesita esa información para validar correctamente.

Esta es la razón por la que el Sequencer propio existe — no por comodidad, sino porque ningún DAW comercial produce el MIDI que el Maestro Virtual requiere.

## Cubase (clases presenciales)

En el contexto presencial, Cubase cumple un rol mucho más amplio: composición, exploración armónica, programación rítmica de canciones conocidas, producción. Luis puede introducir tareas creativas desde etapas tempranas dependiendo del alumno. El Sequencer en línea no replica esta funcionalidad — son herramientas con propósitos distintos.

## Historial de Cambios
- 2026-04-07: Creación inicial (borrador)
