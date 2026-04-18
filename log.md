# log.md — Registro de Sesiones
## Storm Studios Learning KB

> Registro cronológico append-only de todo lo que ocurre en el KB.
> Cada entrada documenta qué se hizo, qué se ingresó, qué se aprendió.
> Formato de entrada: `## [FECHA] tipo | descripción`
> Tipos: `ingest` | `entrevista` | `actualización` | `lint` | `sesion`

---

## [2026-04-16] sesion | GitHub setup + .gitattributes

**Repo:** https://github.com/luisca66/storm-knowledge-base
**Branch:** main
**Commit inicial:** 70 archivos, 7.05 MB
**Acción:** Creado `.gitattributes` para normalizar line endings (LF en repo, automático en Windows)
**Pendiente:** Hacer commit y push del .gitattributes desde la máquina de Luis

**Workflow para otras máquinas:**
```bash
git clone https://github.com/luisca66/storm-knowledge-base.git
```
**Workflow para sincronizar cambios:**
```bash
git pull          # bajar cambios
git add .
git commit -m "descripción"
git push          # subir cambios
```

---

## [2026-04-16] ingest | Curso Integral de Composición Musical (Hernández Medrano)

**Fuente:** `07-fuentes/libros/curso-medrano.txt` + `curso-medrano.pdf` (62 pp.)
**Autor:** Humberto Hernández Medrano (alumno de Shostakovich)
**Relevancia:** Máxima — es el texto base del método que Luis enseña

**Archivos wiki afectados (6):**
- `07-fuentes/indice-fuentes.md` → nuevo registro como fuente primaria
- `08-sintesis/como-enseno-armonia.md` → llenado sustancialmente con arquitectura del curso (5 bloques)
- `01-metodo-pedagogico/estructura-curso.md` → mapa completo de ~60 lecciones en 5 bloques

**Estructura del curso documentada:**
- Bloque 1: Elementos y fundamentos (propedéutico + escalas)
- Bloque 2: Armonía diatónica SATB (acordes, enlaces, cadencias, tetracordes)
- Bloque 3: Acordes con séptima y novena (V7, VII7, II7, V9)
- Bloque 4: Modulación (1er, 2do, 3er grado de parentesco tonal)
- Bloque 5: Figuración melódica + armonía cromática

**Pendiente:** preguntas a Luis sobre su voz pedagógica (qué modificó, errores del alumno, criterios de avance)

---

## [2026-04-16] actualización | Reglas de calidad anti-RAG + 08-sintesis/

**Cambios en CLAUDE.md:**
- Agregada sección 6b con 3 reglas de calidad del sistema:
  - Regla 1: Escritura activa obligatoria (cada sesión modifica archivos)
  - Regla 2: Prevención de duplicación semántica (buscar antes de crear)
  - Regla 3: Páginas de síntesis como producto de mayor valor

**Archivos creados en 08-sintesis/:**
- `el-musico-como-atleta.md` — síntesis de 6 libros de entrenamiento físico
- `modelos-mentales-aprendizaje-musical.md` — neurociencia + filosofía aplicadas al aprendizaje
- `como-enseno-armonia.md` — estructura para capturar el conocimiento tácito de Luis sobre armonía
- `tecnologia-al-servicio-del-metodo.md` — filosofía tecnológica del proyecto
- `estrategia-freemium-musical.md` — modelo de negocio como extensión pedagógica

**Fuente:** Recomendaciones de ChatGPT sobre sistemas tipo Karpathy — evaluadas, adoptadas e implementadas.

---

## [2026-04-16] sesion | Arquitectura del KB + ingest Karpathy

**Trabajo realizado:**
- Creación de `CLAUDE.md` — schema maestro del KB con estructura, workflows y reglas
- Creación de `index.md` — catálogo completo y navegable de todos los archivos
- Creación de este `log.md` — registro cronológico de sesiones
- Procesado transcript: "The Real Problem With AI Agents Nobody's Talking About" → `07-fuentes/videos/`
- Ingesta de proyecto LLM Wiki de Andrej Karpathy → `LLM Wiki/llm-wiki.md`

**Insights clave de esta sesión:**
- El video de AI Agents confirma que el KB de Luis es la solución correcta al problema de "conocimiento tácito no articulado"
- El patrón LLM Wiki de Karpathy (raw sources / wiki / schema) describe exactamente lo que estamos construyendo — ahora formalizado
- Nuevo archivo propuesto: `00-contexto/ritmos-y-decisiones.md` para capturar ritmos operativos de Luis

**Pendiente identificado:**
- Entrevistar a Luis para `ritmos-y-decisiones.md`
- Completar títulos de lecciones 3-5 del propedéutico en `estructura-curso.md`
- Completar conexión matemática mental / Elefantito en `filosofia-ensenanza.md`

---

## [2026-04-16] ingest | The Real Problem With AI Agents Nobody's Talking About

**Fuente:** Video de YouTube (transcript) — autor no identificado
**Procesado a:** `07-fuentes/videos/The Real Problem With AI Agents Nobody's Talking About.md`
**Archivos wiki afectados:** Ninguno directamente (análisis compartido en conversación)
**Relevancia:** Alta — valida arquitectura del KB, introduce concepto de "conocimiento tácito compilado"

---

## [2026-04-16] ingest | LLM Wiki — Andrej Karpathy

**Fuente:** Repositorio GitHub de Andrej Karpathy
**Procesado a:** `LLM Wiki/llm-wiki.md`
**Archivos wiki afectados:** Generó `CLAUDE.md`, `index.md`, `log.md`
**Relevancia:** Alta — provee arquitectura formal para el KB (raw sources / wiki / schema)

---

## [2026-04-16] actualización | stack-tecnologico.md

**Archivos modificados:** `00-contexto/stack-tecnologico.md`
**Cambio:** Documentación completa del stack desde website scrape

---

## [2026-04-16] actualización | estructura-curso.md

**Archivos modificados:** `01-metodo-pedagogico/estructura-curso.md`
**Cambio:** Estructura del propedéutico y ~60 lecciones documentadas desde website + entrevista
**Pendiente:** Títulos de lecciones 3-5 del propedéutico

---

## [2026-04-16] actualización | indice-apps.md

**Archivos modificados:** `03-apps-herramientas/indice-apps.md`
**Cambio:** Corrección de 7 a 10 apps (verificado con website), catálogo completo

---

## [2026-04-09] sesion | Ingesta masiva de fuentes + insights

**Trabajo realizado:**
- 22 libros catalogados en `07-fuentes/indice-fuentes.md`
- 56 insights diarios capturados en `00-contexto/insights.md`
- `vision-proyecto.md` completado via entrevista

**Archivos creados/actualizados:**
- `07-fuentes/indice-fuentes.md` — catálogo de 22 libros
- `00-contexto/insights.md` — 56 entradas 2026-04-09
- `00-contexto/vision-proyecto.md` — completo

---

## [2026-04-09] ingest | 22 libros (lote)

**Fuentes:** Libros de la biblioteca personal de Luis en `H:\Libros\Libros completos MD`
**Procesados a:** `07-fuentes/libros/` (copiados) + `07-fuentes/indice-fuentes.md` (catalogados)
**Áreas cubiertas:** Neurociencia, filosofía, entrenamiento físico, nutrición, inversión, matemática mental

---

## [2026-04-09] actualización | vision-proyecto.md

**Archivos modificados:** `00-contexto/vision-proyecto.md`
**Método:** Entrevista a Luis
**Cambio:** Modelo de negocio completo — freemium, escalera de valor, "la beca", YouTube, cursos avanzados

---

## [2026-04-09] actualización | filosofia-ensenanza.md

**Archivos modificados:** `01-metodo-pedagogico/filosofia-ensenanza.md`
**Método:** Lectura del libro "Los Seres Musicales" (sin entrevistar a Luis)
**Cambio:** 7 principios pedagógicos, tabla comparativa, El Camino de la Señal
**Pendiente:** Conexión matemática mental / Elefantito Matemático

---

## [2026-04-07] sesion | Fundación del KB

**Trabajo realizado:**
- Lectura del capítulo "Interludio: ¿quién soy?" del libro Los Seres Musicales
- Entrevista a Luis para completar quien-soy.md
- Creación de insights.md
- Estructura base del KB creada (carpetas, archivos borrador)

**Archivos creados:**
- `00-contexto/quien-soy.md` — completo
- `00-contexto/insights.md` — creado
- Estructura de carpetas completa

---

## [2026-04-07] ingest | Los Seres Musicales (libro de Luis)

**Fuente:** `07-fuentes/libros/Los_Seres_Musicales.md`
**Archivos wiki afectados:** `quien-soy.md`, `filosofia-ensenanza.md`
**Relevancia:** Máxima — es el libro que contiene el método pedagógico completo de Luis

---

*Log mantenido por Claude. No eliminar entradas anteriores — solo agregar al inicio.*
