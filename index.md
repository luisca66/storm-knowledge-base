---
titulo: "Índice del Knowledge Base"
tipo: catalogo
ultima_actualizacion: 2026-07-13
estado: en_progreso
---

# Índice — Storm Studios Learning KB

> Catálogo navegable de todos los archivos del KB.
> Cualquier IA lo consulta después de leer el schema maestro `CLAUDE.md`.
> Actualizar con cada sesión.

---

## 🗂 Archivos de sistema

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [CLAUDE.md](CLAUDE.md) | **Schema maestro — única fuente de verdad** para cualquier IA: quién es Luis, propósito, estructura, workflows, reglas, estado | ✅ activo |
| [AGENTS.md](AGENTS.md) | Stub de redirección a CLAUDE.md (para Codex y agentes que buscan ese nombre) | ✅ activo |
| [README.md](README.md) | Portada del repo (privado): presentación y mapa de navegación | ✅ activo |
| [index.md](index.md) | Este archivo — catálogo navegable | ✅ activo |
| [log.md](log.md) | Registro cronológico de sesiones e ingestas | ✅ activo |
| [CHANGELOG.md](CHANGELOG.md) | Historial de cambios significativos al KB | en_progreso |
| [plan-maestro-base-conocimiento.md](plan-maestro-base-conocimiento.md) | Plan original de construcción del KB | referencia |
| [herramientas/lint_kb.py](herramientas/lint_kb.py) | Script de verificación reproducible: referencias, enlaces y frontmatter. Primer paso del Lint y del Cierre de Mes | ✅ activo |

---

## 00 · Contexto

*Quién es Luis, qué está construyendo, por qué.*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [quien-soy.md](00-contexto/quien-soy.md) | Biografía completa, linaje pedagógico (Shostakovich→Medrano→Cárdenas), viaje con IA | **completo** |
| [vision-proyecto.md](00-contexto/vision-proyecto.md) | Modelo freemium, escalera de valor, YouTube, cursos avanzados, "la beca" | **completo** |
| [stack-tecnologico.md](00-contexto/stack-tecnologico.md) | Next.js 16/React 19/TS/Vercel, Android, Godot 4, Firebase, herramientas IA | en_progreso |
| [ai-radar.md](00-contexto/ai-radar.md) | Radar de IA activo: herramientas que Luis usa + tendencias estratégicas (actualizar mensual) | en_progreso |
| [ritmos-y-decisiones.md](00-contexto/ritmos-y-decisiones.md) | Ritmos operativos de Luis: bloques fijos, sistema ainews, rutinas | en_progreso |
| [decisiones-clave.md](00-contexto/decisiones-clave.md) | Decisiones estratégicas y su justificación (fuente única del schema, apps de paga, autonomía IA, Play Store) | en_progreso |
| [insights.md](00-contexto/insights.md) | Bandeja de entrada de ideas diarias | en_progreso |

---

## 01 · Método Pedagógico

*El núcleo intelectual: Los Seres Musicales, El Camino de la Señal.*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [filosofia-ensenanza.md](01-metodo-pedagogico/filosofia-ensenanza.md) | 7 principios, comparativa tradicional vs. método, rol de la tecnología, Elefantito Matemático, Aristóteles | **completo** |
| [estructura-curso.md](01-metodo-pedagogico/estructura-curso.md) | ~60 lecciones: propedéutico P01-P04, escalas, armonía cromática, modulación | en_progreso |
| [progresion-estudiante.md](01-metodo-pedagogico/progresion-estudiante.md) | Cómo avanza el alumno: entrada al website, propedéutico, herramientas y criterios de dominio | en_progreso |
| [ejercicios/tipos-de-ejercicio.md](01-metodo-pedagogico/ejercicios/tipos-de-ejercicio.md) | Tipos de ejercicio disponibles en la plataforma | borrador |
| [ejercicios/reglas-validacion.md](01-metodo-pedagogico/ejercicios/reglas-validacion.md) | Reglas de validación del Maestro Virtual | borrador |
| [lecciones/leccion-01-escalas-mayores.md](01-metodo-pedagogico/lecciones/leccion-01-escalas-mayores.md) | Lección 1: Escalas Mayores | borrador |
| [lecciones/leccion-02-escalas-menores.md](01-metodo-pedagogico/lecciones/leccion-02-escalas-menores.md) | Lección 2: Escalas Menores | borrador |
| [clases-ia/](01-metodo-pedagogico/clases-ia/) | Sistema integrado para clases personalizadas de IA (alumnos, sesiones, reportes) | **completo** |
| [INSTRUCCIONES_CLASES_IA.md](01-metodo-pedagogico/clases-ia/INSTRUCCIONES_CLASES_IA.md) | Reglamento específico para planear y operar clases de IA (Doble lectura obligatoria) | **completo** |

---

## 02 · Plataforma Web

*La plataforma Next.js hosteada en Vercel: stormstudios.com.mx*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [arquitectura.md](02-plataforma-web/arquitectura.md) | Arquitectura técnica de la plataforma | en_progreso |
| [funcionalidades.md](02-plataforma-web/funcionalidades.md) | Features actuales y planeadas | en_progreso |
| [maestro-virtual.md](02-plataforma-web/maestro-virtual.md) | Validador MIDI en tiempo real integrado al curso | en_progreso |
| [secuenciador.md](02-plataforma-web/secuenciador.md) | Storm Sequencer v3.0 — secuenciador MIDI en el navegador | en_progreso |
| [decisiones-tecnicas.md](02-plataforma-web/decisiones-tecnicas.md) | Decisiones técnicas relevantes y su contexto | en_progreso |

---

## 03 · Apps y Herramientas

*11 apps (9 oído + 2 cognitivas), todas publicadas como webapps gratuitas + Storm Sequencer + herramientas auxiliares.*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [indice-apps.md](03-apps-herramientas/indice-apps.md) | Catálogo completo: 11 webapps gratuitas, móviles de paga en tiendas, piloto P03 y Sequencer | en_progreso |
| [elefantito-matematico.md](03-apps-herramientas/elefantito-matematico.md) | App web/Android de matemática mental: 20 niveles, tutores bilingües, técnicas Arthur Benjamin | **completo** |
| [otras-apps.md](03-apps-herramientas/otras-apps.md) | Apps adicionales no categorizadas | borrador |
| [entrenamiento-auditivo/app-android-overview.md](03-apps-herramientas/entrenamiento-auditivo/app-android-overview.md) | Overview de apps de entrenamiento auditivo | borrador |
| [entrenamiento-auditivo/godot-juegos.md](03-apps-herramientas/entrenamiento-auditivo/godot-juegos.md) | Juegos educativos en Godot 4 | borrador |

---

## 04 · Contenido Musical

*Cómo se sirve el contenido de la plataforma (audio en Cloudflare, video en YouTube) y la obra musical de Luis (discografía con IA, a futuro).*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [archivos-midi.md](04-contenido-musical/archivos-midi.md) | Nota: no hay biblioteca MIDI — el alumno lo genera y sube al Maestro Virtual, no se guarda | **completo** |
| [audio-assets.md](04-contenido-musical/audio-assets.md) | Audio en Cloudflare, video en YouTube; migración vieja resuelta | **completo** |
| [discografia-ia.md](04-contenido-musical/discografia-ia.md) | Plan a futuro: canciones de Luis hechas con IA, como discos (reemplaza a repertorio.md) | borrador (plan) |

---

## 05 · Operaciones

*Cómo funciona el proyecto día a día.*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [flujo-trabajo.md](05-operaciones/flujo-trabajo.md) | Mapa contextual de proyectos y forma de registrar desarrollos externos al KB; no es centro operativo | en_progreso |
| [mapa-contextual-proyectos.md](05-operaciones/mapa-contextual-proyectos.md) | Lista viva de proyectos del ecosistema de Luis con estado contextual y próximos temas a recordar | en_progreso |
| [plan-mejoras-kb-2026-07.md](05-operaciones/plan-mejoras-kb-2026-07.md) | Plan autocontenido de mejoras estructurales (Fable 5 → Opus): cierre de mes, lint versionado, log ainews, recordatorio | **completo** (ejecutado) |
| [asesoria-ia.md](05-operaciones/asesoria-ia.md) | Relación entre asesorías de IA y Migración Empresas; modelo de acompañamiento | en_progreso |
| [infraestructura.md](05-operaciones/infraestructura.md) | Infraestructura técnica: Vercel, Cloudflare, respaldo del KB | borrador |
| [migraciones-pendientes.md](05-operaciones/migraciones-pendientes.md) | Sin migraciones pendientes; la de audio se resolvió vía Cloudflare | **completo** |

---

## 06 · Diario del Proyecto

*Registro mensual de progreso y reflexiones.*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [2026-04.md](06-diario-proyecto/2026-04.md) | Diario de abril 2026 | en_progreso |
| [2026-05.md](06-diario-proyecto/2026-05.md) | Diario de mayo 2026 (hito: propedéutico completo) | en_progreso |
| [2026-06.md](06-diario-proyecto/2026-06.md) | Diario de junio 2026 (síntesis del oído, Migración Empresas, schema único, veto a Fable) | **completo** |

---

## 07 · Fuentes (Raw Sources — solo lectura)

*Documentos originales. No modificar. Claude los lee para extraer conocimiento al wiki.*

### Índice principal
| Archivo | Descripción |
|---------|-------------|
| [indice-fuentes.md](07-fuentes/indice-fuentes.md) | Catálogo de todas las fuentes con autor, área de impacto y ruta |

### Libros destacados (23 de 27 ingresados)

| Libro | Área de impacto principal |
|-------|--------------------------|
| [Los Seres Musicales](07-fuentes/libros/Los_Seres_Musicales.md) | Método pedagógico — libro de Luis |
| [How Emotions Are Made](07-fuentes/libros/How%20Emotions%20are%20made%20-%20Complete.md) | Neurociencia del aprendizaje |
| [Seven and a Half Lessons About the Brain](07-fuentes/libros/Seven%20and%20a%20half%20lessons%20about%20the%20brain%20-%20Complete.md) | Neurociencia |
| [This Is Your Brain on Music](07-fuentes/libros/This%20is%20your%20Brain%20on%20Music%20-%20Complete.md) | Neurociencia musical |
| [Your Brain at Work](07-fuentes/libros/Your%20Brain%20at%20Work_Complete.md) | Productividad cognitiva |
| [Inner Engineering](07-fuentes/libros/Inner%20Engineering%20-%20Complete.md) | Filosofía yóguica |
| [Death](07-fuentes/libros/Death%20-%20Complete.md) | Filosofía — Sadhguru |
| [Outliers](07-fuentes/libros/Outliers_Complete.md) | Formación de maestría / las 10,000 horas |
| [Essentials of Strength Training and Conditioning](07-fuentes/libros/ESSENTIALS_of_STRENGTH_TRAINING_and_CONDITIONING_Complete.md) | Entrenamiento físico aplicado a músicos |
| [Full Body Flexibility](07-fuentes/libros/Full%20body%20flexibility%20-%20Complete.md) | Flexibilidad / físico del músico |
| [Speed Training](07-fuentes/libros/Speed%20Training%20-%20Complete.md) | Velocidad de ejecución |
| [Speed](07-fuentes/libros/Speed%20-%20Complete.md) | Velocidad |
| [Super Joints](07-fuentes/libros/Super%20Joints%20-%20Complete.md) | Movilidad articular |
| [A Guide to Amino Acid and Protein Nutrition](07-fuentes/libros/A%20Guide%20to%20Amino%20Acid%20and%20Protein%20Nutrition%20-%20Complete.md) | Nutrición del músico |
| [Mental Math](07-fuentes/libros/Mental%20Math%20-%20Complete.md) | Matemática mental / Elefantito Matemático |
| [Energy, A Beginner's Guide](07-fuentes/libros/Energy%2C%20A%20Beginners%20Guide.md) | Energía / física aplicada |
| [Philosophy, Beginner's Guide](07-fuentes/libros/Philosophy%2C%20Beginners%20Guide%20-%20Complete.md) | Filosofía base |
| [Lecciones Preliminares de Filosofía](07-fuentes/libros/Lecciones%20preliminares%20de%20filosof%C3%ADa.md) | Filosofía en español |
| [Little Book of Common Sense Investing](07-fuentes/libros/Little%20Book%20Of%20Common%20Sense%20Investing_Complete.md) | Inversión / negocio |
| [How Countries Go Broke](07-fuentes/libros/How%20Countries%20go%20Broke.md) | Macroeconomía |
| [The New China Playbook](07-fuentes/libros/The%20New%20China%20Playbook.md) | Geopolítica / negocios |
| [Civilización Artificial](07-fuentes/libros/Civilizaci%C3%B3n%20Artificial.md) | IA y sociedad |
| [Originals](07-fuentes/libros/Originals%20-%20Complete.md) | Liderazgo creativo / método — disciplina por razonamiento, elogio de carácter, rol del mentor |

### Videos (transcripts procesados)

| Video | Tema | Relevancia |
|-------|------|-----------|
| The Real Problem With AI Agents Nobody's Talking About | Agentes de IA, knowledge bases, conocimiento tácito | Fuente canónica en el repo operativo; ingerido al wiki |
| This Could Save Your Life | Longevidad sistémica (Dr. William Lee) — 5 prácticas aplicadas al músico | Fuente canónica en el repo operativo; ingerido → el-musico-como-atleta.md |
| [Moonshots — Organizational Singularity (Diamandis/Ismail)](07-fuentes/videos/moonshots-organizational-singularity-peter-diamandis-salim-ismail.md) | Singularidad organizacional, ExO 3.0, transformación empresarial con IA | Alta — clases de IA / asesorías |
| Singularidad Organizacional — ExO 3.0 | ExO 3.0, modelo organizacional exponencial | Fuente canónica en el repo operativo |
| [Corpus de Migración Empresas](09-migracion-empresas/corpus-videos.md) | Registro de 15 fuentes operativas: fricción, workflows, cambio, datos, MTP, gobernanza y backcasting | Síntesis y cautelas; transcripts en `D:\codex\migracion-empresas\00-fuente\videos\` |

---

## 08 · Síntesis (Nivel 2)

*Páginas que no provienen de una sola fuente. Acumulan conocimiento de múltiples libros, entrevistas e insights. Son donde aparece la inteligencia real del sistema.*

| Archivo | Descripción | Fuentes principales | Estado |
|---------|-------------|---------------------|--------|
| [el-musico-como-atleta.md](08-sintesis/el-musico-como-atleta.md) | El cuerpo del músico como sistema atlético: velocidad, flexibilidad, fuerza, nutrición, longevidad | 6 libros de fitness + This Could Save Your Life | en_progreso |
| [modelos-mentales-aprendizaje-musical.md](08-sintesis/modelos-mentales-aprendizaje-musical.md) | Neurociencia + psicología + filosofía aplicadas al aprendizaje musical | Barrett ×2, Levitin, Gladwell, Rock, Agüera y Arcas, Sadhguru | en_progreso |
| [como-enseno-armonia.md](08-sintesis/como-enseno-armonia.md) | El enfoque específico de Luis para enseñar armonía — conocimiento tácito | Medrano + Sadhguru + Levitin + entrevistas | en_progreso |
| [tecnologia-al-servicio-del-metodo.md](08-sintesis/tecnologia-al-servicio-del-metodo.md) | Por qué cada decisión técnica existe en función de la pedagogía | Método + video AI Agents + Karpathy + Elefantito | en_progreso |
| [estrategia-freemium-musical.md](08-sintesis/estrategia-freemium-musical.md) | Por qué el modelo freemium es defendible: el negocio ES el método. Foso 10k horas + fuerzas macro de IA + paciencia compuesta | Entrevista + Bogle + Gladwell + AI Radar | en_progreso |
| [luis-como-ingeniero-neural.md](08-sintesis/luis-como-ingeniero-neural.md) | **La premisa central del proyecto:** Luis modula redes neuronales usando la música como laboratorio — el framework aplica a cualquier habilidad | Entrevista directa 2026-04-16 | **en_progreso** |
| [entrenamiento-oido-absoluto.md](08-sintesis/entrenamiento-oido-absoluto.md) | Teoría operativa del oído absoluto: corteza selectiva, imagen mental, matriz de las 4 percepciones, automaticidad, hipótesis del sample rate, mapa a las 8 apps | Backlog insights oído 2026-04-09 + Levitin + Barrett + Agüera y Arcas | en_progreso |

---

## 09 · Migración Empresas

*Línea empresarial de IA activa y con ingresos. Este KB solo registra contexto; el trabajo real vive en `D:\codex\migracion-empresas`.*

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| [entrevista_fundacional.md](09-migracion-empresas/entrevista_fundacional.md) | Síntesis estratégica: Gemelo Digital ExO 3.0, dolor del cliente, proceso, rol de Builder | **completo** |
| [README.md](09-migracion-empresas/README.md) | Visión, límites y relación con las otras líneas de negocio | en_progreso |
| [indice-proyectos.md](09-migracion-empresas/proyectos/indice-proyectos.md) | Catálogo de empresas y proyectos activos (Voces Imaginarias, Julio) | en_progreso |
| [corpus-videos.md](09-migracion-empresas/corpus-videos.md) | Registro y síntesis de 15 fuentes canónicas del repositorio operativo | en_progreso |

---

## 📚 Referencias externas

| Recurso | Descripción |
|---------|-------------|
| [LLM Wiki (Karpathy)](07-fuentes/llm-wiki-karpathy.md) | Patrón de arquitectura para knowledge bases con LLMs — base conceptual de este KB |

---

## 📊 Estadísticas del KB

| Métrica | Valor |
|---------|-------|
| Total archivos .md (incluye clases-ia) | 370 (clases-ia: 174, ainews: 90) + `herramientas/lint_kb.py` |
| Archivos wiki principales completos | 10 (sin sistema, referencias históricas y clases-ia) |
| Archivos wiki en_progreso | 29 |
| Archivos wiki borrador | 8 |
| Páginas de síntesis | 7 (todas en_progreso) |
| Libros ingresados | 27 |
| Libros registrados pendientes | 1 (Shadows of Forgotten Ancestors) |
| Videos y destilados | 1 transcript general en el KB + 15 fuentes operativas registradas para Migración Empresas |
| Sistema ainews | mar–jul 2026 (activo) |
| Alumnos en clases-ia | 11 perfilados |
| Última sesión de trabajo | 2026-07-13 |

---

*Mantenido por la IA que colabora con Luis. Actualizado: 2026-07-13 (corpus de Migración Empresas registrado; fuentes crudas trasladadas al proyecto operativo).*

---
## Historial de Cambios
- **2026-07-13** — Corpus de Migración Empresas registrado: 15 fuentes canónicas en el repo operativo, copias crudas retiradas del KB, estadísticas recalculadas y frontera KB/operación aclarada.
- **2026-07-09** — Mapa contextual de 29 proyectos creado; estados de website, apps, Maestro Virtual, juegos, Migración Empresas, discografía y stack móvil reconciliados.
- **2026-07-08 (2)** — Lint de salud Codex: KB mecánicamente sano; `05-operaciones/flujo-trabajo.md` reencuadrado como mapa contextual de proyectos, no como centro operativo.
- **2026-07-08** — Julio abierto en `ai-radar.md`; ingesta de *Originals* (Grant): catálogo de libros actualizado (23/27), estadísticas recalculadas (365 archivos, última sesión).
- **2026-07-03 (2)** — Actualización de Luis: catálogo de apps corregido a 11 webapps publicadas (Cantar Acordes documentada); descripción de la sección 03 actualizada.
- **2026-07-03** — Lint de Fable 5: diario de junio agregado al catálogo (completo); estadísticas recalculadas (364 archivos; conteo de estados ahora excluye consistentemente archivos de sistema); sistema ainews extendido a julio; última sesión actualizada.
- **2026-06-12** — Estadísticas recalculadas; Migración Empresas, apps y última sesión reconciliadas con el estado real del KB.
