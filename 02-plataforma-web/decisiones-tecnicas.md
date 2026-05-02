---
titulo: "Decisiones Técnicas de la Plataforma"
tipo: decision
ultima_actualizacion: 2026-05-02
relacionado_con:
  - 00-contexto/decisiones-clave.md
  - 00-contexto/stack-tecnologico.md
  - 02-plataforma-web/arquitectura.md
estado: en_progreso
---

# Decisiones Técnicas de la Plataforma

## Resumen
Por qué se eligió cada tecnología del stack, y cuál es la lógica detrás de cada decisión. El contexto clave: Luis opera como "vibe coder" — construye con IA sin formación formal en programación. Las decisiones tecnológicas favorecen ecosistemas bien documentados, fuerte soporte de IA, y costos bajos.

---

## Por qué Next.js (con App Router)

Next.js es el framework más popular del ecosistema React, con documentación extensa y soporte masivo de herramientas de IA. Para Luis, que construye con Claude Code y otras IAs, esto es crítico: un framework popular garantiza que la IA tenga contexto de calidad para implementar cambios.

Ventajas concretas para el proyecto:
- **App Router** — estructura de rutas basada en carpetas, intuitiva para crecer por secciones
- **Server-side rendering** — mejor SEO que una SPA pura (importante para posicionamiento del curso)
- **API routes** — el Maestro Virtual vive dentro del mismo proyecto, sin necesidad de servidor separado
- **MDX nativo** — el contenido del curso (lecciones) se puede escribir en Markdown con componentes React

---

## Por qué TypeScript

TypeScript agrega tipado estático a JavaScript. Para un proyecto construido con IA, el tipado cumple una función crítica: le da a la IA contexto sobre qué estructuras de datos espera cada función. Sin tipos, la IA genera código válido sintácticamente pero puede pasar datos incorrectos entre módulos.

En el Maestro Virtual en particular, los tipos formalizan el "contrato" entre el parser MIDI y el validador — qué estructura devuelve uno y qué estructura espera el otro. Esto reduce errores de integración.

---

## Por qué Vercel

Vercel es la plataforma de hosting creada por el mismo equipo que Next.js. El resultado es integración perfecta: deploy automático en cada push a GitHub, sin configuración.

La decisión económica también importa: el plan Hobby de Vercel es **gratuito** y suficiente para el tráfico actual del sitio. Sin costos de infraestructura hasta que la escala lo requiera.

---

## Por qué Firebase

Firebase (Google) provee una base de datos en tiempo real en formato JSON, con SDK para JavaScript. Para el estado actual del proyecto, cumple dos funciones:

1. **Almacenamiento de datos del curso** — progreso del alumno, resultados de validación del Maestro Virtual
2. **Autenticación** — [verificar con Luis si está implementada]

La decisión de Firebase sobre alternativas (PostgreSQL, Supabase, etc.) responde al mismo criterio que Next.js: es un servicio ampliamente documentado, con SDKs oficiales, y con fuerte soporte de IAs de código.

**[VERIFICAR CON LUIS: uso actual de Firebase, qué datos almacena, si hay autenticación implementada]**

---

## Por qué Tailwind CSS v4

Tailwind es un framework de utilidades CSS que elimina la necesidad de escribir CSS personalizado. Para desarrollo con IA, Tailwind tiene una ventaja enorme: las clases son legibles en el HTML, lo que permite a la IA entender el estilo visual sin leer archivos CSS separados.

---

## Por qué next-intl

La plataforma está disponible en español e inglés desde el inicio (`/es/` y `/en/`). next-intl es la librería de internacionalización más usada en Next.js App Router. La decisión de internacionalizar desde el principio (en lugar de añadirla después) evita una migración costosa cuando el proyecto alcance audiencia en inglés.

---

## Por qué HTML/vanilla JS para el Storm Sequencer

El Sequencer no está construido en React/Next.js — es HTML y JavaScript puro, embebido en la plataforma. Razones probables:

1. **El Sequencer existía antes que la plataforma** — fue construido como herramienta independiente y luego integrado
2. **Rendimiento** — un secuenciador MIDI en tiempo real requiere control fino sobre el audio, que es más directo en JS puro que con el overhead de React
3. **Portabilidad** — como HTML/JS puro, puede funcionar como página standalone sin el framework

**[VERIFICAR CON LUIS: historia del Sequencer, por qué no se migró a React]**

---

## Decisiones pendientes de documentar

- [ ] Por qué Zoho Mail sobre alternativas (Gmail Business, etc.)
- [ ] Estado y uso actual de Firebase (¿autenticación implementada? ¿qué datos almacena?)
- [ ] Historia del Storm Sequencer (¿cuándo se construyó? ¿quién lo construyó? ¿versiones anteriores?)
- [ ] Decisión sobre audio assets: ¿Dreamhost → dónde migrar?

---

## Historial de Cambios
- **2026-04-07** — Creación inicial (borrador)
- **2026-05-02** — Archivo llenado con razonamiento detrás de cada tecnología del stack. Pendientes marcados para verificar con Luis. Estado: en_progreso.
