# AGENTS.md — Schema Maestro del Knowledge Base
## Storm Studios Learning · Luis Cárdenas

> Este archivo es el punto de entrada obligatorio para cualquier sesión de trabajo en este KB.
> Lo lee Codex al inicio. Define quién es Luis, cómo está organizado el KB, y cómo se mantiene.

---

## 1. Quién es Luis

**Luis Cárdenas** — músico profesional (35 años de carrera), maestro de música (30 años), compositor y desarrollador de software por IA ("vibe coder"). Mexicano. Creador del método pedagógico **"Los Seres Musicales"**, que integra neurociencia, fisiología y filosofía yóguica aplicada al aprendizaje musical.

Está construyendo **Storm Studios Learning**: plataforma freemium de educación musical en línea.

**Perfil técnico:** Next.js/TypeScript en Vercel, apps Android (Android Studio → delegadas a Codex), juegos en Godot 4, apps HTML/vanilla JS. No tiene formación formal en programación — construye con IA.

**Filosofía sobre IA:** "El futuro está en mis datos, no en mis habilidades para usar la IA." Este KB existe para que la IA tenga todo el contexto necesario para ser un colaborador real, no un asistente genérico.

---

## 2. Propósito del KB

Este Knowledge Base es el **cerebro externalizado de Luis**. Funciona según el patrón LLM Wiki de Andrej Karpathy:

- **Raw sources** (`07-fuentes/`) → documentos originales, inmutables. Libros, transcripts de video, artículos.
- **The wiki** (todo lo demás) → archivos generados y mantenidos por Codex en colaboración con Luis.
- **Este schema** (`AGENTS.md`) → instrucciones permanentes para Codex sobre cómo operar el KB.

El KB NO es un archivo de notas. Es la base de entrenamiento para que una IA futura pueda construir el proyecto de forma autónoma.

---

## 3. Estructura de carpetas

```
storm-knowledge-base/
│
├── AGENTS.md              ← ESTE ARCHIVO — leer siempre primero
├── README.md              ← presentación pública del proyecto
├── index.md               ← catálogo navegable de todos los archivos
├── log.md                 ← registro cronológico de sesiones e ingestas
├── CHANGELOG.md           ← historial de cambios significativos
│
├── 00-contexto/           ← Quién es Luis, qué está construyendo, por qué
│   ├── quien-soy.md           ← biografía, linaje pedagógico, viaje con IA
│   ├── vision-proyecto.md     ← modelo de negocio, escalera de valor, metas
│   ├── stack-tecnologico.md   ← todas las tecnologías en uso
│   ├── decisiones-clave.md    ← decisiones estratégicas y su por qué
│   └── insights.md            ← bandeja de entrada de ideas diarias
│
├── 01-metodo-pedagogico/  ← El núcleo intelectual del proyecto
│   ├── filosofia-ensenanza.md ← 7 principios, El Camino de la Señal
│   ├── estructura-curso.md    ← ~60 lecciones, propedéutico + progresión
│   ├── progresion-estudiante.md ← cómo avanza el alumno
│   ├── clases-ia/             ← sistema operativo de las clases personalizadas
│   │   └── INSTRUCCIONES_CLASES_IA.md ← reglas específicas para dar clases de IA
│   ├── ejercicios/
│   │   ├── tipos-de-ejercicio.md
│   │   └── reglas-validacion.md
│   └── lecciones/             ← archivos individuales por lección
│
├── 02-plataforma-web/     ← La plataforma Next.js en Vercel
│   ├── arquitectura.md
│   ├── funcionalidades.md
│   ├── maestro-virtual.md     ← validador MIDI en tiempo real
│   ├── secuenciador.md        ← Storm Sequencer v3.0
│   └── decisiones-tecnicas.md
│
├── 03-apps-herramientas/  ← Las 10+ apps Android y web
│   ├── indice-apps.md         ← catálogo completo
│   ├── elefantito-matematico.md
│   ├── otras-apps.md
│   └── entrenamiento-auditivo/
│
├── 04-contenido-musical/  ← Assets: MIDI, audio, repertorio
│   ├── archivos-midi.md
│   ├── audio-assets.md
│   └── repertorio.md
│
├── 05-operaciones/        ← Cómo funciona el proyecto día a día
│   ├── flujo-trabajo.md
│   ├── asesoria-ia.md
│   ├── infraestructura.md
│   └── migraciones-pendientes.md
│
├── 06-diario-proyecto/    ← Registro mensual de progreso
│   └── 2026-04.md
│
├── 07-fuentes/            ← RAW SOURCES — solo lectura, nunca modificar
│   ├── indice-fuentes.md      ← catálogo de todas las fuentes
│   ├── libros/                ← 22+ libros en Markdown
│   └── videos/                ← transcripts de videos procesados
│
└── 07-fuentes/
    └── llm-wiki-karpathy.md  ← Referencia de arquitectura (Karpathy) — solo lectura
```

---

## 4. Convenciones de archivos

### Frontmatter obligatorio

Todo archivo del KB (excepto raw sources y este AGENTS.md) debe tener:

```yaml
---
titulo: "Nombre descriptivo"
tipo: contexto | catalogo | decision | tecnico | diario | fuente
ultima_actualizacion: YYYY-MM-DD
relacionado_con:
  - ruta/relativa/al/archivo.md
estado: borrador | en_progreso | completo | requiere_revision
---
```

### Estados
- `borrador` → estructura creada, contenido mínimo o vacío
- `en_progreso` → contenido parcial, activamente en desarrollo
- `completo` → contenido sustancial, refleja la realidad actual
- `requiere_revision` → completado anteriormente, pero necesita actualización

### Historial de cambios
Cada archivo modificado debe tener al final:

```markdown
---
## Historial de Cambios
- **YYYY-MM-DD** — descripción del cambio
```

---

## 5. Workflows

### Ingesta de nueva fuente (libro, video, artículo)

1. El archivo original va en `07-fuentes/libros/` o `07-fuentes/videos/` — **no se modifica**
2. Actualizar `07-fuentes/indice-fuentes.md` con entrada del nuevo documento
3. Leer la fuente y extraer insights relevantes para el proyecto
4. Actualizar los archivos del wiki afectados (máx 10-15 archivos por fuente)
5. Procesar insights relevantes hacia `00-contexto/insights.md`
6. Registrar en `log.md`: `## [FECHA] ingest | Título de la fuente`

### Entrevista a Luis (captura de conocimiento tácito)

1. Identificar el archivo objetivo del KB
2. Hacer preguntas conversacionales — una a la vez, escuchar con atención
3. Estructurar respuestas en el formato del KB (no transcribir literal)
4. Capturar el **"por qué"** detrás de cada decisión, no solo el "qué"
5. Actualizar `ultima_actualizacion` y `estado`
6. Registrar en `log.md`: `## [FECHA] entrevista | Archivo actualizado`

### Lint del KB (revisión de salud)

Periódicamente verificar:
- Archivos en `borrador` que llevan mucho tiempo sin avanzar
- Referencias cruzadas rotas (`relacionado_con` apuntando a archivos inexistentes)
- Contradicciones entre archivos (ej. número de apps, número de lecciones)
- Insights en `insights.md` sin procesar (sin ✅) que ya tienen archivo destino
- Archivos `requiere_revision` que no han sido actualizados
- **Duplicación semántica**: archivos con temas solapados → fusionar o crear jerarquía
- **Páginas de síntesis huérfanas**: síntesis que no se actualizan al ingresar nuevas fuentes

### Respuesta a preguntas del proyecto

1. Leer `index.md` para identificar archivos relevantes
2. Leer esos archivos específicos
3. Sintetizar respuesta con referencias a los archivos fuente
4. Si la respuesta genera nuevo conocimiento valioso → archivarla en el wiki

---

## 6. Reglas de colaboración

**Lo que Codex hace:**
- Escribe y mantiene todos los archivos del wiki
- Hace preguntas para extraer conocimiento tácito de Luis
- Propone conexiones entre conceptos y archivos
- Mantiene consistencia entre archivos (ej. mismo número de apps en todos lados)
- Actualiza `index.md` y `log.md` en cada sesión
- **Acatar doble reglamento en clases-ia:** Si trabaja planificando clases de IA o editando perfiles de alumnos, debe leer y obedecer obligatoriamente `01-metodo-pedagogico/clases-ia/INSTRUCCIONES_CLASES_IA.md`.

**Lo que Luis hace:**
- Decide qué fuentes ingresar
- Responde preguntas de entrevista
- Valida el contenido generado
- Marca insights como procesados (✅) cuando ya están en otro archivo

**Idioma:** Español. Tú con Luis. Tono profesional cálido. Código y términos técnicos en inglés.

**Regla de oro:** No inventar información. Si algo no se sabe, preguntar. Cada dato tiene un único archivo de verdad — usar `relacionado_con` para referencias cruzadas, nunca duplicar contenido.

---

## 6b. Reglas de calidad del sistema (anti-RAG)

Estas tres reglas evitan que el KB se degrade en un simple buscador de documentos.

### Regla 1 — Escritura activa obligatoria

El KB solo crece si Codex escribe, no solo lee.

- **Cada interacción relevante** (entrevista, análisis, respuesta compleja) → modificar o crear al menos 1 archivo del wiki
- **Cada fuente ingresada** → tocar entre 5 y 15 archivos existentes (no solo crear uno nuevo)
- **Cada respuesta valiosa** → evaluar si merece convertirse en página de síntesis o actualizar una existente
- Si una sesión termina sin haber modificado ningún archivo → la sesión no aportó al KB

### Regla 2 — Prevención de duplicación semántica

Antes de crear cualquier archivo nuevo:

1. Buscar en `index.md` si ya existe un archivo con tema similar
2. Si existe → ampliar ese archivo, no crear uno nuevo
3. Si hay dos archivos con el mismo tema → fusionarlos (el más completo absorbe al otro)
4. Señales de alerta: dos archivos cuyos títulos son sinónimos, o cuyo `relacionado_con` se apunta mutuamente sin ser archivos de categorías distintas

### Regla 3 — Páginas de síntesis (nivel 2)

Las páginas de síntesis son el producto más valioso del KB. Se diferencian del resto porque:
- **No provienen de una sola fuente** — son acumulación de múltiples libros, entrevistas e insights
- **Representan el pensamiento de Luis**, no un resumen de otro autor
- **Crecen con el tiempo** — cada nueva fuente relevante las enriquece
- **Responden preguntas complejas** que ningún archivo individual puede responder solo

Viven en `08-sintesis/`. Ejemplos para este proyecto:
- Cómo Luis enseña armonía (síntesis de método + experiencia + neurociencia)
- El músico como atleta (síntesis de libros de entrenamiento físico aplicados)
- Modelos mentales del aprendizaje musical (síntesis filosófica + pedagógica)
- Tecnología al servicio del método (síntesis de decisiones técnicas + pedagogía)

**Criterio de éxito del KB:** Si en 2-3 semanas una pregunta compleja sobre el proyecto produce una respuesta mejor que cualquier fuente individual ingresada → el sistema está funcionando.

---

## 7. Estado actual del proyecto (actualizar en cada sesión)

**Última actualización:** 2026-05-26 (Elefantito Matemático documentado)

**Archivos completos:** quien-soy.md, vision-proyecto.md, stack-tecnologico.md, indice-fuentes.md, funcionalidades.md, decisiones-tecnicas.md, filosofia-ensenanza.md

**Archivos en progreso:** estructura-curso.md, indice-apps.md, elefantito-matematico.md, secuenciador.md, maestro-virtual.md

**Páginas de síntesis activas (08-sintesis/):**
- `luis-como-ingeniero-neural.md` ← la más importante — visión central del proyecto
- `como-enseno-armonia.md` ← **en progreso** — completo en lo sustancial: Medrano + Sadhguru + Levitin + visión civilizatoria (cosmos/cuerpo/mente) + IA como extensión del método
- `modelos-mentales-aprendizaje-musical.md` ← **en progreso** — sólido: Kahneman + Barrett + Agüera y Arcas + Levitin + Gladwell + Rock
- `el-musico-como-atleta.md` ← **en progreso** — llenado con 6 libros de fitness
- `tecnologia-al-servicio-del-metodo.md` ← **en progreso** — tres capas de tecnología llenadas + criterio de automatización (Efecto Santiago) integrado
- `estrategia-freemium-musical.md` ← borrador

**Fuentes ingresadas:** 33 fuentes total:
- 22 libros originales + Curso Medrano + LLM Wiki + 1 video
- Sesión 2026-04-22: Inner Engineering, Kahneman, Barrett x2, A Little Bit of Philosophy (copiada)
- Sesión 2026-05-01: What Is Intelligence (Agüera y Arcas), This Is Your Brain on Music (Levitin), 6 libros de fitness, A Little Bit of Philosophy U03L04 + U04L04
- Sesión 2026-05-02: Outliers (Gladwell), Your Brain at Work (Rock)

**Fuentes no ingresadas aún:** libros filosóficos generales, libros económicos

**Repo GitHub:** https://github.com/luisca66/storm-knowledge-base

**Pendiente prioritario:**
- `03-apps-herramientas/elefantito-matematico.md` → confirmar si el HTML legacy de 8 niveles sigue enlazado y si las técnicas avanzadas de Arthur Benjamin siguen planeadas para niveles futuros
- `08-sintesis/tecnologia-al-servicio-del-metodo.md` → completar secciones Storm Sequencer y apps de entrenamiento auditivo
- `modelos-mentales-aprendizaje-musical.md` → sección Sadhguru (silencio interior) aún pendiente
- `02-plataforma-web/` → funcionalidades ✅, maestro-virtual ✅, secuenciador ✅, decisiones-tecnicas ✅ — pendiente: arquitectura.md (revisar si necesita actualización)
- `04-contenido-musical/`, `05-operaciones/` → archivos en borrador pendientes
- Verificación pendiente: ¿el progreso del alumno (localStorage) es un problema a resolver pronto?

---

*Este archivo es mantenido por Codex. Última revisión: 2026-05-26 (Elefantito Matemático documentado).*
