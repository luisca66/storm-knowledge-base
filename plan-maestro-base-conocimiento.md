---
titulo: "Plan Maestro Original del Knowledge Base"
tipo: contexto
ultima_actualizacion: 2026-06-12
relacionado_con:
  - CLAUDE.md
  - README.md
  - index.md
estado: completo
---

# Plan Maestro: Base de Conocimiento para IA — Storm Studios Learning

> Documento histórico de abril de 2026. Conserva la intención y arquitectura iniciales; el estado operativo vigente vive exclusivamente en `CLAUDE.md`.

**Autor:** Luis (Storm Studios Learning)  
**Fecha:** Abril 2026  
**Propósito:** Estructurar toda la información del proyecto, método pedagógico y contexto técnico en un formato que cualquier IA presente o futura pueda consumir para colaborar activamente en el desarrollo del curso en línea y las herramientas digitales.

---

## 1. Visión General

Este plan construye un **Knowledge Base (KB)** — una base de conocimiento en texto plano que funciona como el "cerebro compartido" entre Luis y cualquier IA colaboradora. No es un archivo muerto: es un sistema vivo que se actualiza conforme el proyecto avanza.

### Principios de diseño

- **Markdown puro (.md)** como formato universal. Legible por humanos, consumible por cualquier modelo de lenguaje sin conversión.
- **Una verdad, un lugar.** Cada pieza de información vive en un solo archivo. Sin duplicados.
- **Metadatos al inicio.** Cada documento abre con un bloque YAML frontmatter que le dice a la IA qué es, cuándo se actualizó y cómo se relaciona con el resto.
- **Modular y navegable.** Estructura de carpetas que refleja la arquitectura real del proyecto.
- **Versionado con fecha.** Cada cambio significativo se marca con fecha en el documento.

---

## 2. Arquitectura de Carpetas

```
storm-knowledge-base/
│
├── README.md                          ← Índice maestro y guía de navegación
├── CHANGELOG.md                       ← Registro cronológico de cambios importantes
│
├── 00-contexto/
│   ├── quien-soy.md                   ← Bio profesional, experiencia, filosofía
│   ├── vision-proyecto.md             ← Visión a largo plazo, metas, métricas de éxito
│   ├── stack-tecnologico.md           ← Herramientas, plataformas, infraestructura actual
│   └── decisiones-clave.md            ← Registro de decisiones importantes y su razonamiento
│
├── 01-metodo-pedagogico/
│   ├── filosofia-ensenanza.md         ← Principios pedagógicos fundamentales
│   ├── estructura-curso.md            ← Mapa completo del curso: lecciones, orden, dependencias
│   ├── lecciones/
│   │   ├── leccion-01-escalas-mayores.md
│   │   ├── leccion-02-escalas-menores.md
│   │   └── ...                        ← Una por lección, con objetivos, contenido, ejercicios
│   ├── ejercicios/
│   │   ├── tipos-de-ejercicio.md      ← Taxonomía de ejercicios y su propósito
│   │   └── reglas-validacion.md       ← Reglas de validación MIDI por tipo de ejercicio
│   └── progresion-estudiante.md       ← Cómo avanza un estudiante, criterios de dominio
│
├── 02-plataforma-web/
│   ├── arquitectura.md                ← Estructura del sitio Next.js, rutas, componentes clave
│   ├── funcionalidades.md             ← Features actuales y roadmap
│   ├── maestro-virtual.md             ← Documentación del validador MIDI
│   ├── secuenciador.md                ← Documentación del secuenciador Storm Studios
│   └── decisiones-tecnicas.md         ← Por qué Next.js, por qué Vercel, etc.
│
├── 03-apps-herramientas/
│   ├── indice-apps.md                 ← Catálogo de todas las apps con estado y propósito
│   ├── entrenamiento-auditivo/
│   │   ├── app-android-overview.md    ← Las 7 apps de Android: qué hacen, cómo se relacionan
│   │   └── godot-juegos.md            ← Los juegos de Godot: niveles, mecánicas, estado
│   ├── elefantito-matematico.md       ← Spec completo del juego de matemática mental
│   └── otras-apps.md                  ← Apps personales, de Esteban, de la sobrina, etc.
│
├── 04-contenido-musical/
│   ├── repertorio.md                  ← Piezas, arreglos, material musical usado en el curso
│   ├── archivos-midi.md               ← Inventario de MIDIs, convenciones de nombre, ubicación
│   └── audio-assets.md                ← Estado de migración de audio, URLs, hosting
│
├── 05-operaciones/
│   ├── flujo-trabajo.md               ← Cómo trabaja Luis día a día, herramientas, procesos
│   ├── infraestructura.md             ← Vercel, Zoho Mail, Google Drive, Firebase — estado actual
│   ├── migraciones-pendientes.md      ← Tareas de migración (ej: audio de Dreamhost a GDrive)
│   └── asesoria-ia.md                 ← Notas sobre asesorías de IA a terceros
│
└── 06-diario-proyecto/
    ├── 2025-01.md                     ← Entradas mensuales: qué se hizo, qué se aprendió
    ├── 2025-02.md
    ├── ...
    └── 2026-04.md
```

---

## 3. Formato Estándar de Documento

Cada archivo .md del KB debe seguir esta estructura:

```markdown
---
titulo: "Nombre descriptivo del documento"
tipo: contexto | leccion | spec | decision | diario | catalogo
ultima_actualizacion: 2026-04-07
relacionado_con:
  - ruta/a/otro-documento.md
  - ruta/a/otro-mas.md
estado: borrador | en_progreso | completo | requiere_revision
---

# Título del Documento

## Resumen
[2-3 oraciones que le dicen a la IA de qué trata este documento
y por qué es relevante]

## Contenido Principal
[El contenido real, organizado con headers claros]

## Contexto y Decisiones
[Por qué las cosas son como son — esto es CRÍTICO para la IA.
No solo el "qué" sino el "por qué"]

## Estado Actual y Pendientes
[Qué está hecho, qué falta, qué bloquea el avance]

## Historial de Cambios
- 2026-04-07: Creación inicial
- [fecha]: [descripción del cambio]
```

---

## 4. El README Maestro

El archivo más importante de todo el KB es `README.md`. Es el punto de entrada para cualquier IA. Debe contener:

1. **Quién es Luis** — en 1 párrafo.
2. **Qué es Storm Studios Learning** — en 1 párrafo.
3. **Cuál es el objetivo de este KB** — para qué está leyendo esto la IA.
4. **Mapa de navegación** — qué hay en cada carpeta, con links.
5. **Convenciones** — cómo leer los metadatos, qué significan los estados.
6. **Instrucciones para la IA** — cómo debe usar este KB, qué priorizar, qué tono usar.

Este archivo es el equivalente a un "system prompt" persistente. Escríbelo pensando en que es lo primero que va a leer un modelo que no te conoce.

---

## 5. Prioridades de Documentación

Basado en tus prioridades (curso en línea → apps → legado → método), este es el orden de ataque:

### Fase 1: Cimientos (Semanas 1-2)
Lo que necesita cualquier IA para empezar a ser útil.

- [ ] `README.md` — el índice maestro
- [ ] `00-contexto/quien-soy.md` — tu bio y filosofía
- [ ] `00-contexto/vision-proyecto.md` — a dónde vas
- [ ] `00-contexto/stack-tecnologico.md` — con qué trabajas
- [ ] `01-metodo-pedagogico/estructura-curso.md` — el mapa del curso

### Fase 2: El Curso (Semanas 3-6)
El corazón del proyecto.

- [ ] `01-metodo-pedagogico/filosofia-ensenanza.md`
- [ ] Las primeras 5 lecciones documentadas individualmente
- [ ] `02-plataforma-web/maestro-virtual.md` (ya tienes docs del Maestro Virtual)
- [ ] `02-plataforma-web/arquitectura.md`

### Fase 3: Ecosistema de Apps (Semanas 7-10)
Tu arsenal de herramientas.

- [ ] `03-apps-herramientas/indice-apps.md` — catálogo completo
- [ ] Documentación de las 7 apps de entrenamiento auditivo
- [ ] `03-apps-herramientas/elefantito-matematico.md` (ya tienes el spec)
- [ ] `03-apps-herramientas/godot-juegos.md`

### Fase 4: Operaciones y Legado (Semanas 11+)
Lo que sostiene todo.

- [ ] `05-operaciones/infraestructura.md`
- [ ] `05-operaciones/migraciones-pendientes.md`
- [ ] `04-contenido-musical/` — inventario de assets
- [ ] Comenzar el diario del proyecto

---

## 6. Estrategia de Captura: Cómo Documentar sin Perder Tiempo

El mayor riesgo de este plan es que se sienta como "más trabajo". Estas son las estrategias para minimizar la fricción:

### 6.1 Sesiones de dictado con IA
En lugar de sentarte a escribir, abre una conversación con Claude y **habla en voz alta** sobre el tema. Luego pídele que lo estructure en el formato del KB. 15 minutos de conversación pueden producir un documento completo.

### 6.2 Documentar mientras trabajas
Cada vez que resuelvas un problema técnico, tomes una decisión de diseño, o completes una lección: antes de cerrar, pasa 5 minutos agregando una entrada al archivo correspondiente.

### 6.3 Reutilizar lo que ya existe
Ya tienes specs (Elefantito Matemático), docs de handoff (Maestro Virtual Lección 2), y conversaciones con Claude llenas de contexto. Esos se pueden convertir directamente a archivos del KB con mínima edición.

### 6.4 El diario como red de seguridad
Si no tienes tiempo de documentar algo formalmente, anota una entrada rápida en el diario mensual. Es mejor tener una nota desordenada que no tener nada.

---

## 7. Preparación para IAs Futuras

### 7.1 Por qué Markdown y no otro formato

| Formato | Pros | Contras |
|---------|------|---------|
| Markdown | Universal, ligero, versionable con Git, legible sin herramientas | Sin formato visual rico |
| PDF | Buena presentación | Difícil de editar, pesado para IA |
| Word/DOCX | Formato visual rico | Propietario, XML internamente, más difícil de parsear |
| JSON/YAML | Muy estructurado | Difícil de escribir y leer para humanos |
| Base de datos | Consultas potentes | Requiere infraestructura, overkill para este caso |

Markdown gana porque optimiza para el caso de uso real: un humano escribe, una IA lee, ambos pueden navegar.

### 7.2 Cómo entregarle el KB a una IA

Cuando llegue el momento de trabajar con un modelo más avanzado:

1. **Empieza siempre por el README.md** — es el punto de entrada.
2. **Carga por contexto, no todo junto.** Si la tarea es sobre el curso, carga `01-metodo-pedagogico/`. Si es sobre una app, carga `03-apps-herramientas/`.
3. **El frontmatter YAML le dice a la IA qué priorizar.** Un documento marcado como `estado: requiere_revision` le señala que necesita atención.
4. **El CHANGELOG.md da contexto temporal.** La IA puede entender qué cambió recientemente y qué está estancado.

### 7.3 Compatibilidad futura

Este formato es compatible con:
- **Context windows grandes** — los modelos futuros podrán consumir el KB completo de una vez.
- **RAG (Retrieval Augmented Generation)** — si algún día quieres montar un sistema que busque dentro del KB automáticamente.
- **Git** — puedes versionar todo el KB en un repositorio y tener historial completo de cambios.
- **Cualquier plataforma** — Google Drive, GitHub, local, lo que sea.

---

## 8. Herramientas Recomendadas

- **Almacenamiento:** Google Drive (ya tienes Gemini Pro) o un repo Git privado en GitHub.
- **Editor:** VS Code con extensión de Markdown preview, o Obsidian si prefieres algo más visual.
- **Versionado:** Git (incluso si solo haces commits manuales de vez en cuando, tener historial es invaluable).
- **Captura rápida:** Conversaciones con Claude → exportar → limpiar → agregar al KB.

---

## 9. Métricas de Progreso

Para saber si el KB está funcionando, hazte estas preguntas cada mes:

1. ¿Puedo abrir una conversación nueva con una IA, pasarle los archivos relevantes, y que entienda mi proyecto sin que yo tenga que explicar todo de nuevo? **Si sí, el KB funciona.**
2. ¿Cuántos archivos tienen estado `completo`? **Meta: 50% a los 3 meses.**
3. ¿El diario del proyecto se está actualizando? **Si no, estás perdiendo contexto valioso.**
4. ¿Las IAs con las que trabajo producen mejores resultados que hace un mes? **El indicador final.**

---

## Siguiente paso inmediato

Crea la carpeta `storm-knowledge-base/` en tu Google Drive o en un repo Git, y escribe el `README.md`. Ese solo archivo, bien hecho, ya te pone en una posición significativamente mejor para cualquier colaboración futura con IA.

---
## Historial de Cambios
- **2026-06-12** — Clasificado como documento histórico y conectado al schema vigente; contenido original conservado.
