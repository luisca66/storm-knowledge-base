# CLAUDE.md — Schema Maestro del Knowledge Base
## Storm Studios Learning · Luis Cárdenas

> **Este archivo es la única fuente de verdad del schema.** Lo lee cualquier IA al inicio de cada sesión
> (Claude lo carga automáticamente; Codex y otros agentes llegan aquí redirigidos desde `AGENTS.md`).
> Define quién es Luis, qué cubre el KB, cómo está organizado y cómo se mantiene.

---

## 1. Quién es Luis

**Luis Cárdenas** — músico profesional (35 años de carrera), maestro de música (30 años), compositor y desarrollador de software por IA ("vibe coder"). Mexicano. Creador del método pedagógico **"Los Seres Musicales"**, que integra neurociencia, fisiología y filosofía yóguica aplicada al aprendizaje musical.

Trabaja desde **Storm Studios** — su estudio físico en casa: estudio 5.1 Genelec completo + gimnasio. Desde ahí opera **tres líneas activas**:

1. **Clases particulares** (presenciales o en línea) — **la vaca lechera hoy**: taller de composición e instrumentos, entrenamientos físicos, y las clases/asesorías de IA (11 alumnos en `01-metodo-pedagogico/clases-ia/`; `05-operaciones/asesoria-ia.md`).
2. **Storm Studios Learning** — el website (plataforma freemium de educación musical, `02-plataforma-web/`). Hoy produce $0 por diseño; su propósito es triple: **legado** (el curso completo), **promotor** de las clases y asesorías, y a futuro **ingreso pasivo** (apps móviles de paga, libros en Amazon, YouTube).
3. **Migración Empresas** — línea empresarial de IA, activa y con ingresos (`09-migracion-empresas/`).

**Perfil técnico:** Next.js/TypeScript en Vercel, apps Android (Android Studio → delegadas a los agentes de IA), juegos en Godot 4, apps HTML/vanilla JS. No tiene formación formal en programación — construye con IA.

**Filosofía sobre IA:** "El futuro está en mis datos, no en mis habilidades para usar la IA." Este KB existe para que la IA tenga todo el contexto necesario para ser un colaborador real, no un asistente genérico.

---

## 2. Propósito del KB

Este Knowledge Base es el **cerebro externalizado de Luis** — de su ecosistema completo (las tres líneas), no de un solo producto. Funciona según el patrón LLM Wiki de Andrej Karpathy:

- **Raw sources** (`07-fuentes/`) → documentos originales, inmutables. Libros, transcripts de video, artículos.
- **The wiki** (todo lo demás) → archivos generados y mantenidos por la IA en colaboración con Luis.
- **Este schema** (`CLAUDE.md`) → instrucciones permanentes para cualquier IA sobre cómo operar el KB.

**El propósito tiene dos niveles:**

1. **Hoy — continuidad:** que cualquier IA pueda leer estos archivos y colaborar con Luis sin que él explique todo desde cero cada vez. *Este nivel ya se cumple.*
2. **Mañana — autonomía:** que una IA futura pueda construir y operar el proyecto de forma autónoma. *Este nivel exige documentación operativa (lecciones, reglas de validación, infraestructura) que aún está incompleta — ver pendientes en §7.*

El KB NO es un archivo de notas. Es la base de entrenamiento del nivel 2.

**El KB es privado — nunca público.** Es el cerebro externalizado de Luis, exclusivamente para él y para la IA que colabora con él. Ningún archivo del KB se publica jamás. Cuando el proyecto tenga artefactos públicos (el **website**, YouTube, Kindle), esos se *redactan usando* el KB como fuente, pero el KB en sí no se expone. Cualquier discusión de AEO / legibilidad para agentes aplica **solo al website**, no al KB. Esta separación es deliberada y es parte del foso: la síntesis profunda del método (el "mecanismo") se queda privada; lo público expone identidad y resultados, no el cómo (ver la paradoja de la legibilidad en `00-contexto/ai-radar.md` y su aplicación en `08-sintesis/estrategia-freemium-musical.md` §5).

### Jerarquía de archivos de entrada

| Archivo | Rol |
|---------|-----|
| `CLAUDE.md` | **Schema maestro — única fuente de verdad.** Cualquier agente lo lee primero |
| `AGENTS.md` | Stub de redirección hacia este archivo (para Codex y agentes que buscan ese nombre) |
| `README.md` | Portada del repo (privado): presentación y mapa de navegación |
| `index.md` | Catálogo navegable con el estado de cada archivo |
| `log.md` | Historial cronológico de sesiones e ingestas |

Ningún otro archivo debe declararse "leer primero". Si este schema contradice a otro archivo de sistema, manda este schema — y hay que corregir el otro.

---

## 3. Estructura de carpetas

```
storm-knowledge-base/
│
├── CLAUDE.md              ← ESTE ARCHIVO — schema maestro, única fuente de verdad
├── AGENTS.md              ← stub → redirige a CLAUDE.md
├── README.md              ← portada del repo (privado)
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
│   ├── clases-ia/             ← sistema operativo de las clases personalizadas de IA
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
│   ├── 2026-04.md
│   └── 2026-05.md
│
├── 07-fuentes/            ← RAW SOURCES — solo lectura, nunca modificar
│   ├── indice-fuentes.md      ← catálogo de todas las fuentes
│   ├── libros/                ← 26+ libros en Markdown
│   ├── videos/                ← transcripts de videos procesados
│   ├── ainews/                ← resúmenes diarios de IA (YYYYMM/), fuente continua
│   └── llm-wiki-karpathy.md   ← Referencia de arquitectura (Karpathy) — solo lectura
│
├── 08-sintesis/           ← PÁGINAS DE SÍNTESIS (nivel 2) — el producto más valioso del KB
│   ├── luis-como-ingeniero-neural.md   ← la visión central
│   ├── como-enseno-armonia.md
│   ├── modelos-mentales-aprendizaje-musical.md
│   ├── el-musico-como-atleta.md
│   ├── tecnologia-al-servicio-del-metodo.md
│   ├── entrenamiento-oido-absoluto.md
│   └── estrategia-freemium-musical.md
│
└── 09-migracion-empresas/ ← Línea empresarial de IA, activa y con ingresos
    ├── README.md
    └── proyectos/
        └── indice-proyectos.md
```

> Nota: `01-metodo-pedagogico/clases-ia/` (sistema de clases personalizadas de IA: 11 alumnos, currículum, sesiones) vive dentro de 01 y es la subcarpeta más grande del KB (~173 archivos).

---

## 4. Convenciones de archivos

### Frontmatter obligatorio

Todo archivo del KB (excepto raw sources, este CLAUDE.md y el stub AGENTS.md) debe tener:

```yaml
---
titulo: "Nombre descriptivo"
tipo: contexto | catalogo | decision | tecnico | diario | fuente | spec | sintesis
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

**Lo que la IA hace:**
- Escribe y mantiene todos los archivos del wiki
- Hace preguntas para extraer conocimiento tácito de Luis
- Propone conexiones entre conceptos y archivos
- Mantiene consistencia entre archivos (ej. mismo número de apps en todos lados)
- Actualiza `index.md` y `log.md` en cada sesión
- **Acatar doble reglamento en clases-ia:** si trabaja planificando clases de IA o editando perfiles de alumnos, debe leer y obedecer obligatoriamente `01-metodo-pedagogico/clases-ia/INSTRUCCIONES_CLASES_IA.md`

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

El KB solo crece si la IA escribe, no solo lee.

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

**Criterio de éxito del KB:** Si en 2-3 semanas una pregunta compleja sobre el proyecto produce una respuesta mejor que cualquier fuente individual ingresada → el sistema está funcionando. *(Cruzado por primera vez en junio 2026: la respuesta sobre AEO salió de la paradoja de la legibilidad que el radar había capturado un mes antes.)*

---

## 7. Estado actual (actualizar en cada sesión)

**Última actualización:** 2026-06-12 — `ai-radar.md` puesto al día (días 1-12 de junio): integrado el lanzamiento de Fable 5 / Mythos 5 y la crisis de costos; tabla de modelos y conceptos pedagógicos de la Sección 3 actualizados.

El detalle del estado vive donde corresponde — no duplicarlo aquí:
- **Estado por archivo** → `index.md` (catálogo con estados y estadísticas)
- **Historial de sesiones e ingestas** → `log.md`
- **Cambios significativos** → `CHANGELOG.md`
- **Decisiones y su porqué** → `00-contexto/decisiones-clave.md`

**Pendiente prioritario:**
- **Documentación operativa (nivel 2 del propósito)** — hallazgo central de la auditoría 2026-06-10: el KB piensa pero no opera. Próximas entrevistas deben ser operativas: lista de las ~65 lecciones (aunque sea títulos), las 6 reglas de validación del Maestro Virtual, infraestructura. `04-contenido-musical/` y `05-operaciones/` en borrador desde abril
- `ai-radar.md` → ✅ al día al 2026-06-12 (Fable 5 / Mythos 5 integrados, tabla de modelos actualizada). **Pendiente derivado:** propagar la nueva tabla de modelos a `conceptos_no_olvidar.md` y `leccion_01` dentro de clases-ia (requiere leer `INSTRUCCIONES_CLASES_IA.md`); cerrar junio en el radar al terminar el mes (días 13-30)
- `09-migracion-empresas/` → completar entrevista fundacional: significado de "migrar", problema que compra el cliente, entregables, proceso, precio y cartera activa
- `luis-como-ingeniero-neural.md` → integrar a Dayana y validar conexiones por alumno con datos de sesiones reales
- `entrenamiento-oido-absoluto.md` → poblar §12 con datos de alumnos que desbloqueen AP; desarrollar la "gramática posicional" (§3)
- `tecnologia-al-servicio-del-metodo.md` → completar sección de apps de entrenamiento auditivo
- `estrategia-freemium-musical.md` → 2 preguntas menores en §10 (orden de lanzamiento de avanzados, dato de conversión)
- **Documentar el Taller de Ingeniería de Audio y Producción Musical** — curso real ya impartido, ligado al estudio 5.1; necesita ficha propia
- Ingestar `Originals` (Grant) → conectar con liderazgo creativo / método
- Verificar **canal/origen** de "A Little Bit of Philosophy — PHI 101" (`[verificar canal]` en `indice-fuentes.md`)
- Verificar si el progreso del alumno en localStorage es un problema a resolver pronto
- **Respaldo del KB** fuera de GitHub (`git bundle` mensual a disco o Drive) — el activo central tiene hoy un solo punto de falla
- **Documentar las clases particulares como línea completa** (entrevista 2026-06-11): alcance y precios de instrumento/composición y entrenamientos físicos — la vaca lechera real apenas quedó esbozada en la tabla de ingresos
- **Ejecutar la estrategia de apps de paga** (decidida 2026-06-11, ver `decisiones-clave.md`): documentar el toolchain iOS en `stack-tecnologico.md`, reflejar web-gratis/móvil-de-paga en `indice-apps.md`, y correr el piloto con las 2 apps de P03
- **Contradicción por verificar:** `stack-tecnologico.md` dice "10 apps en Google Play" pero la decisión Play Store del 2026-05-22 describe distribución por descarga directa desde el website — ¿cuáles están dónde?

---

*Este archivo es mantenido por la IA que colabora con Luis (Claude, Codex o cualquier agente futuro). Última revisión: 2026-06-11 (consolidación: fuente única, propósito en dos niveles, alcance de tres líneas).*
