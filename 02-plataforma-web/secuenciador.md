---
titulo: "Secuenciador Storm Studios"
tipo: spec
ultima_actualizacion: 2026-05-02
relacionado_con:
  - 02-plataforma-web/maestro-virtual.md
  - 00-contexto/decisiones-clave.md
estado: en_progreso
---

# Secuenciador Storm Studios

## Resumen
El Storm Sequencer es el orgullo técnico de la plataforma. Es un secuenciador MIDI construido en HTML/JavaScript por Luis con sus IAs (Gemini, ChatGPT y Claude), que resuelve un problema que ningún DAW comercial resuelve: exportar notas MIDI con metadatos enarmónicos (G# vs Ab). Nació como herramienta independiente y fue integrado posteriormente a la plataforma Next.js.

---

## Historia y origen

El Sequencer fue creado por Luis en colaboración con sus herramientas de IA — Gemini, ChatGPT y Claude — antes de que existiera la plataforma Next.js. Nació como archivo HTML independiente, motivado por una necesidad técnica específica: el Maestro Virtual necesitaba saber si una nota estaba escrita como G# o Ab, y ningún DAW disponible exportaba esa información.

Una vez construido, fue integrado a la plataforma Next.js como componente embebido — mantuvo su naturaleza de HTML/JavaScript puro para preservar el control fino sobre el comportamiento MIDI.

**Esto lo convierte en una pieza única:** no existe un secuenciador comercial equivalente que resuelva este problema de la misma forma. Es software custom diseñado específicamente para el ecosistema Storm Studios Learning.

---

## El diferenciador técnico: enarmónica en MIDI

El formato MIDI estándar representa cada nota como un número (0–127). El número 66, por ejemplo, puede ser F# o Gb — suenan idéntico en afinación temperada, pero son armónicamente distintos. Un archivo MIDI estándar no distingue entre ellos.

El Storm Sequencer **sabe armonía**. Conoce la tonalidad del ejercicio, y al exportar el MIDI incluye `key_signature` meta-messages que especifican la armadura de clave. Con esa información, el Maestro Virtual puede resolver inequívocamente si la nota 66 es F# o Gb en el contexto del ejercicio — y validar si el alumno escribió la nota correcta.

Esto no es un detalle técnico menor. Es la condición que hace posible la validación armónica real. Sin ella, el Maestro Virtual solo podría validar alturas absolutas, no función armónica.

---

## Función pedagógica

El Storm Sequencer tiene un rol específico en el curso en línea: **es la herramienta de entrega de tareas**. El alumno escribe el ejercicio de la lección, y lo exporta como MIDI para validación con el Maestro Virtual. No está diseñado como herramienta de exploración o composición libre — ese rol lo cumple Cubase en las clases presenciales.

Esta distinción es intencional: el entorno en línea prioriza la validación precisa. El alumno necesita una herramienta que genere exactamente el MIDI que el Maestro Virtual requiere.

---

## Cubase vs. Storm Sequencer

| Contexto | Herramienta | Función |
|----------|-------------|---------|
| Curso en línea | Storm Sequencer | Entrega de tareas + validación con Maestro Virtual |
| Clases presenciales | Cubase | Exploración, composición libre, producción, tareas creativas |

En presencial, Luis puede asignar composición libre desde etapas tempranas según el alumno. El Sequencer en línea no replica esa funcionalidad — son herramientas con propósitos distintos.

---

## Historial de Cambios
- **2026-04-07** — Creación inicial (borrador)
- **2026-04-16** — Función pedagógica y diferenciador técnico documentados
- **2026-05-02** — Historia y origen añadidos. El Sequencer como orgullo técnico del proyecto: construido con IAs (Gemini, ChatGPT, Claude), HTML/JS puro integrado a Next.js. Estado: en_progreso.
