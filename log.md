# log.md — Registro de Sesiones
## Storm Studios Learning KB

> Registro cronológico append-only de todo lo que ocurre en el KB.
> Cada entrada documenta qué se hizo, qué se ingresó, qué se aprendió.
> Formato de entrada: `## [FECHA] tipo | descripción`
> Tipos: `ingest` | `entrevista` | `actualización` | `lint` | `sesion`

---

## [2026-05-21] lint | Chequeo de consistencia completo del KB

**Problemas detectados y resueltos:**
1. ✅ CLAUDE.md sección 7 desactualizada → actualizada a sesión 4 (2026-05-21)
2. ✅ `ai-radar.md` y `ritmos-y-decisiones.md` no aparecían en index.md → agregados
3. ✅ Estadísticas de index.md obsoletas → corregidas (256+ archivos, 26 libros, 7 alumnos)
4. ✅ `filosofia-ensenanza.md` seguía como "en_progreso" en CLAUDE.md → marcado como completo
5. ✅ `clases-ia/` sin conexión a síntesis principales → conectado vía `relacionado_con:`
6. ⚠️ `luis-como-ingeniero-neural.md` (9 KB) desbalanceada vs su importancia → pendiente enriquecer con datos reales de alumnos
7. ⚠️ 10 libros con `[verificar autor]` en indice-fuentes.md → pendiente verificar

**Archivos modificados:** CLAUDE.md, index.md, CHANGELOG.md, log.md, 08-sintesis/como-enseno-armonia.md, 08-sintesis/luis-como-ingeniero-neural.md

---

## [2026-05-21] actualizacion | Desanidación de repo clases-ia

**Acciones:**
- Se eliminó el sub-directorio `.git` interno de la carpeta `01-metodo-pedagogico/clases-ia/`.
- Se removió la carpeta del archivo `.gitignore` del repositorio principal.
- Se agregaron todos los archivos de `clases-ia` al control de versiones del repositorio `storm-knowledge-base`.

**Conocimiento capturado:**
- Se resolvió un error arquitectónico donde `clases-ia` operaba como un repositorio anidado ("git dentro de git"). A partir de ahora, toda la carpeta pertenece orgánicamente al monorepo principal.

---

## [2026-05-21] entrevista | El Paradigma de No-Compartimentación (Campo Unificado)

**Acciones:**
- Actualización estructural profunda en base a entrevista con Luis. Se corrige el sesgo reduccionista del KB que confinaba la neurociencia al "cuarteto vocal" o al "entrenamiento auditivo" por separado.
- Archivos `08-sintesis/luis-como-ingeniero-neural.md` y `08-sintesis/modelos-mentales-aprendizaje-musical.md` modificados para incluir el "Axioma del Ecosistema Unificado".

**Conocimiento capturado:**
- **La No-Compartimentación**: Los alumnos presenciales son multi-instrumentistas (guitarra, bajo, piano, batería) y usuarios de herramientas (IA, apps). Todas las fuentes (Kahneman, Barrett, Levitin, Tsatsouline, Sadhguru, Rock, Agüera y Arcas) aplican simultáneamente a *todas* las tareas del taller.
- El taller opera como un campo unificado. No se puede aislar la mielinización (Kahneman) del silencio interior (Sadhguru) o de la gestión del presupuesto corporal (Barrett) por cada instrumento. Si el alumno toca un compás de batería o usa un prompt de IA, invoca toda la arquitectura neurocognitiva del método al mismo tiempo.

---

## [2026-05-21] sesion | Repo clases-ia incorporado + Integración de Elefantito Matemático

**Acciones:**
- Clonado `https://github.com/luisca66/clases-ia` en `01-metodo-pedagogico/clases-ia/`.
- Registrado el repo en `index.md`.
- Agregado `01-metodo-pedagogico/clases-ia/` a `.gitignore` del KB padre para mantenerlo como repositorio Git independiente.
- Procesados e integrados los insights de **Elefantito Matemático** (gym del cerebro/córtex prefrontal/Sistema 2) y del **Módulo de memoria** (mnemotecnia clásica) en [filosofia-ensenanza.md](file:///C:/Users/Luis/Documents/storm-knowledge-base/01-metodo-pedagogico/filosofia-ensenanza.md).
- Marcados como resueltos y procesados en [insights.md](file:///C:/Users/Luis/Documents/storm-knowledge-base/00-contexto/insights.md).
- Actualizado [index.md](file:///C:/Users/Luis/Documents/storm-knowledge-base/index.md) para reflejar [filosofia-ensenanza.md](file:///C:/Users/Luis/Documents/storm-knowledge-base/01-metodo-pedagogico/filosofia-ensenanza.md) como **completo**.

**Estado observado:**
- Rama interna clases-ia: `main`, sincronizada con `origin/main`.
- Último commit: `1b263a1 Preparar kit operativo de leccion 1`.
- El proyecto tiene estructura operativa para clases de IA: método, currículo, alumnos, sesiones, ejercicios, prompts, fuentes, base ligera y reportes.
- El archivo de filosofía de enseñanza queda completado en su totalidad al resolver la sección de matemática mental que estaba marcada como pendiente.

---

## [2026-05-06] sesion | ai-radar.md + ainews registrado + 2 libros nuevos

**Archivos creados / modificados:**
- `00-contexto/ai-radar.md` — CREADO. Documento vivo con dos secciones: (1) Herramientas que Luis usa actualmente (stack IA, sistema ainews, Openclaw + Cowork audio); (2) Tendencias que informan sus asesorías (síntesis estratégica abril-mayo 2026 con 5 conceptos clave: Enlightenment Gap, Karpathy Loop, Phase of Economics, bifurcación, "no puedes tercerizar tu entendimiento").
- `07-fuentes/indice-fuentes.md` — Sistema ainews registrado como fuente continua (mar-may 2026). Originals (Grant) y Shadows of Forgotten Ancestors (Sagan) registrados como libros nuevos — pendiente ingestar.

**Contexto de la sesión:**
- Luis está dando asesorías de IA cobradas — el ainews es la columna vertebral de su radar estratégico
- El sistema ainews (Openclaw → Cowork → audio 55 min → bici) es una innovación pedagógica propia: conocimiento sin costo marginal de tiempo
- Los dos nuevos libros aparecieron en el folder durante el período intercesión

---

## [2026-05-02 sesión 3] plataforma | Documentación completa de 02-plataforma-web/ + ingest Gladwell + Rock + entrevista de verificación

**Archivos modificados:**
- `02-plataforma-web/funcionalidades.md` → llenado completo: páginas activas, estado de lecciones (~10 de ~60), catálogo de 10 apps Android, modalidades de estudio
- `02-plataforma-web/maestro-virtual.md` → expansión mayor: arquitectura (midi-parser.ts, scale-validator.ts, API route), problema enarmónico y solución, estado por lección (5 niveles Medrano), lecciones actuales son dummies
- `02-plataforma-web/secuenciador.md` → historia y origen: construido por Luis con Gemini+ChatGPT+Claude, HTML/JS antes de Next.js, integrado después
- `02-plataforma-web/decisiones-tecnicas.md` → llenado completo: razonamiento por cada tecnología del stack; Firebase corregido (localStorage, no Firebase en producción confirmada)
- `00-contexto/vision-proyecto.md` → plataforma como embudo para presencial, intención de legado ("para cuando muera"), Film Scoring en estudio 5.1

**Ingestas:**
- `Outliers` (Gladwell) → `modelos-mentales-aprendizaje-musical.md`: estudio Ericsson, práctica deliberada, sin naturales ni trabajadores, contexto/ecosistema, trabajo significativo, proverbio del arrozal
- `Your Brain at Work` (Rock) → `modelos-mentales-aprendizaje-musical.md`: PFC como cuello de botella (Yerkes-Dodson), endurecimiento via ganglios basales (3 repeticiones = LTP), chunking, director metacognitivo

**Entrevista de verificación — conocimiento capturado:**
- Maestro Virtual = codificación del Curso Medrano completo en código (una instancia Claude hace la conversión)
- Lecciones actuales en plataforma son DUMMIES
- ~60 corales como referencia del último alumno presencial — número puede variar
- Progress del alumno = localStorage (browser-local), Firebase desconocido/no confirmado
- Storm Sequencer = construido por Luis con sus IAs, HTML que se integró luego a Next.js — "orgullo de la plataforma"
- Contrapunto y Film Scoring no serán gratuitos — cursos con Luis directamente
- Film Scoring se mezcla en 5.1 en estudio propio
- Plataforma = embudo para presencial, no el producto final
- Intención de legado: dejar el método documentado para que se quede en el mundo

---

## [2026-05-01 sesión 2] entrevista | como-enseno-armonia.md — visión civilizatoria + IA

**Archivo afectado:** `08-sintesis/como-enseno-armonia.md`

**Conocimiento capturado:**
- **La visión civilizatoria**: lo que Luis realmente enseña es cómo funciona el cosmos, el cuerpo y la mente. La música es el vehículo más completo — posiblemente el único camino completo — pero no el único posible. El impacto del método no es musical: es humano.
- **IA como extensión del método**: todos los alumnos trabajan hoy con IA; Luis ya da asesorías cobradas de IA. El objetivo: moldear el cerebro para interactuar *menos* con las IAs. La distinción clave es qué se delega: IA como amplificador (tú eres el creador, tus redes crecen) vs. IA como sustituto (delegas el trabajo cognitivo, pierdes conexiones).
- **La pregunta de diagnóstico**: ¿Usas la IA para hacer más de lo que ya eres, o para no tener que ser nada?

---

## [2026-05-01] ingest | 9 fuentes ingresadas (lote)

**Fuentes procesadas:**
1. `What Is Intelligence?` (Blaise Agüera y Arcas, Google Research, 2025)
2. `This Is Your Brain on Music` (Daniel J. Levitin)
3. `Speed` (J. Barnes) — velocidad neuromotora para combate
4. `Speed Training` (Loren Christensen) — velocidad como eficiencia neural
5. `Super Joints` (Pavel Tsatsouline) — movilidad articular rusa
6. `Full Body Flexibility` — flexibilidad activa vs. pasiva
7. `Essentials of Strength Training and Conditioning` (NSCA, 4a ed.)
8. `A Guide to Amino Acid and Protein Nutrition` — síntesis neural
9. `A Little Bit of Philosophy` — U03 L04 (Filosofía de la Mente) + U04 L04 (Aristóteles y la Virtud)

**Archivos wiki afectados (4):**
- `08-sintesis/modelos-mentales-aprendizaje-musical.md` → dos nuevas secciones principales: (1) Agüera y Arcas: inteligencia como predicción, transfer learning, períodos críticos, convergencia Barrett+predicción; (2) Levitin: schemas musicales, anticipación, multidimensionalidad del oído, neuroplasticidad, dopamina y memoria. Secciones huérfanas de Levitin completadas.
- `08-sintesis/el-musico-como-atleta.md` → archivo llenado de borrador a en_progreso: 7 secciones sustanciales (sistema neuromuscular, velocidad neuromotora, flexibilidad articular, fuerza y resistencia, nutrición, dimensiones integradas, Luis como caso de estudio).
- `08-sintesis/como-enseno-armonia.md` → nueva sección: "El oído como destino: lo que confirma la neurociencia (Levitin)" — schemas como modelos predictivos, por qué el método funciona sin memorizar reglas.
- `01-metodo-pedagogico/filosofia-ensenanza.md` → nueva sección "Aristóteles y la virtud como hábito" — validación filosófica más antigua del principio de mielinización. Aristóteles agregado a Influencias Intelectuales.

**Conocimiento capturado:**

*Agüera y Arcas:*
- Inteligencia = capacidad de modelar, predecir e influir en el futuro propio (def. funcional de Helmholtz, 1860s)
- Aprendizaje = aprender a representar (construir embeddings internos del mundo)
- Transfer learning: el dominio profundo en un área construye andamiaje para áreas adyacentes → valida la apuesta por SATB como cimiento neural
- Períodos críticos: los fonemas/sonidos se aprenden en ventanas sensibles tempranas; el adulto puede aprenderlos pero a mayor costo → explica por qué el método es largo e intensivo
- Convergencia con Barrett: ambos dicen lo mismo desde ángulos distintos (neurobiología vs. computación)

*Levitin:*
- La anticipación es el corazón de la música: el compositor controla las expectativas del oyente
- Schemas musicales se forman desde el vientre materno; a los 5 años el niño reconoce progresiones armónicas de su cultura
- El cerebro construye una realidad musical multidimensional desde una señal 1D (frecuencia)
- Incluso pequeña exposición a lecciones musicales crea estructuras neurales duraderas
- Dopamina y memoria: cuando te importa el material, recuerdas mejor → el coral perfecto como requisito garantiza el involucramiento genuino
- Neuroplasticidad confirmada: la región cerebral del movimiento de la mano izquierda en violinistas crece con la práctica

*Fitness (6 libros):*
- Adaptaciones neurales ocurren ANTES que las musculares (primeras 8 semanas = aprendizaje motor)
- Velocidad = eficiencia neuromotora, no fuerza bruta
- Relajación entre movimientos = precondición fisiológica para la velocidad siguiente
- Efecto ideomotor: la visualización activa prepara los circuitos motores (= ejercicio de visualización del método)
- Movilidad activa vs. pasiva: la pasiva sin activa genera lesiones; la active flexibility desarrolla el rango controlado
- Aminoácidos esenciales para síntesis de neurotransmisores (dopamina, serotonina) — nutrición del sistema nervioso

*Aristóteles (Ética Nicomáquea):*
- Virtudes del carácter solo se adquieren mediante práctica — el conocimiento intelectual de la regla no basta
- El violinista virtuoso como ejemplo propio de Aristóteles: teoría ≠ habilidad
- Eudaimonia = florecimiento = alcanzar el máximo potencial de la naturaleza humana
- Validación filosófica de 2,400 años del principio de mielinización como construcción de disposiciones habituales

---

## [2026-04-22] actualización | A Little Bit of Philosophy copiado a fuentes

**Acción:** Curso PHI 101 copiado a `07-fuentes/libros/a-little-bit-of-philosophy/`
**Estructura:** 4 unidades, 17 lecciones — U01 historia/griegos, U02 epistemología, U03 metafísica/mente, U04 ética
**Registrado en:** `07-fuentes/indice-fuentes.md`
**Pendiente:** Ingestar al wiki — prioridad: U03 L04 (filosofía de la mente) y U04 L04 (Aristóteles y virtud)

---

## [2026-04-22] ingest | Seven and a Half Lessons + How Emotions Are Made (Barrett)

**Fuentes:**
- `07-fuentes/libros/Seven and a half lessons about the brain - Complete.md`
- `07-fuentes/libros/How Emotions are made - Complete.md`
**Autora:** Lisa Feldman Barrett
**Relevancia:** Máxima — Barrett es la base científica principal del método. Luis la cita directamente en Los Seres Musicales y la usa en el taller.

**Archivos wiki afectados (3):**
- `08-sintesis/modelos-mentales-aprendizaje-musical.md` → dos secciones Barrett escritas: (1) cerebro para sobrevivir / allostasis / aversión al esfuerzo / un cerebro no tres; (2) cerebro construye la realidad / emoción construida / aprender = actualizar modelos predictivos. Conexión Barrett+Kahneman documentada.
- `08-sintesis/como-enseno-armonia.md` → nueva sección: por qué el camino es largo (aversión al esfuerzo evolutiva, Barrett)
- `07-fuentes/indice-fuentes.md` → ambos libros marcados INGESTED

**Conocimiento capturado:**
- El cerebro no evolucionó para pensar — evolucionó para gestionar el cuerpo (allostasis)
- Anticipación ganó a reacción en la evolución del Cámbrico — base del principio de anticipación de Luis
- Un cerebro integrado, no tres en guerra — desmonta el mito reptiliano/límbico/racional
- La aversión al esfuerzo es evolutiva: el cerebro maximiza eficiencia energética → explica por qué "tocar por tocar" destruye el aprendizaje
- El cerebro construye la realidad desde predicciones (How Emotions Are Made) → aprender = actualizar modelos predictivos
- El ejercicio de visualización antes de ejecutar = construir el modelo predictivo correcto antes de gastar energía ejecutando
- Barrett + Kahneman = pareja conceptual central del método (mencionados juntos en Los Seres Musicales)

---

## [2026-04-22] ingest | Thinking Fast and Slow (Kahneman)

**Fuente:** `07-fuentes/libros/Thinking Fast and Slow - Complete.md`
**Autor:** Daniel Kahneman
**Relevancia:** Alta — Sistema 1/Sistema 2 es el modelo cognitivo central del método. Luis lo usa directamente en el taller y es lectura obligatoria asignada. Los Seres Musicales lo cita explícitamente.

**Archivos wiki afectados (3):**
- `08-sintesis/modelos-mentales-aprendizaje-musical.md` → sección principal de Kahneman escrita: S1/S2, migración de aprendizaje, anticipación vs. reacción, metacognición, "el yogui y el automático". Estado cambiado a en_progreso.
- `08-sintesis/como-enseno-armonia.md` → los tres errores del coral reinterpretados en clave Kahneman (errores de Sistema 1)
- `07-fuentes/indice-fuentes.md` → Kahneman marcado como INGESTED

**Conocimiento capturado:**
- S1 = automático, heurísticas, camino de menor energía → origen de los errores del alumno
- S2 = deliberado, consciente, se agota → herramienta de corrección y construcción
- La mielinización = migración de S2 a S1 (esto conecta Kahneman con la neurobiología del método)
- Anticipación = S2 activo 150ms antes del error (cita directa de Luis en Los Seres Musicales)
- "El yogui y el automático" = nomenclatura propia de Luis para S2/S1

**Pendiente:**
- Ingestar *What is Intelligence* — identificar autor y procesar
- Conectar Kahneman con Barrett (cerebro predictivo) en modelos-mentales.md

---

## [2026-05-02] actualización | 02-plataforma-web — tres archivos de borrador a en_progreso

**Método:** Scraping de stormstudios.com.mx + conocimiento del stack documentado en KB

**Archivos modificados (3):**
- `02-plataforma-web/funcionalidades.md` → llenado completo: páginas activas, lecciones publicadas (~10/60), herramientas integradas, catálogo de 10 apps, modalidades de estudio, pendientes
- `02-plataforma-web/maestro-virtual.md` → llenado: propósito pedagógico, arquitectura técnica, explicación completa del problema enarmónico y solución con key_signature, estado por lección
- `02-plataforma-web/decisiones-tecnicas.md` → llenado: razonamiento detrás de Next.js, TypeScript, Vercel, Firebase, Tailwind, next-intl, y el Sequencer en vanilla JS

**Pendientes para verificar con Luis:**
- Estado actual de Firebase (¿autenticación implementada? ¿qué datos almacena?)
- Historia del Storm Sequencer (¿cuándo se construyó? ¿versiones anteriores?)
- Implementar validador Lección 2 (Escalas Menores)
- Precios en el sitio

---

## [2026-05-02] ingest | Outliers (Gladwell) + Your Brain at Work (Rock)

**Fuentes:**
- `07-fuentes/libros/Outliers_Complete.md` — Malcolm Gladwell
- `07-fuentes/libros/Your Brain at Work_Complete.md` — David Rock

**Archivos wiki afectados (2):**
- `08-sintesis/modelos-mentales-aprendizaje-musical.md` → sección Gladwell expandida de stub a completa (10,000 horas, práctica deliberada, no hay naturales/grinders, ecosistema, trabajo significativo). Nueva sección Rock: PFC como cuello de botella, hardwiring via basal ganglia, "director" metacognitivo, chunking, curva Yerkes-Dodson.
- `07-fuentes/indice-fuentes.md` → ambos libros marcados INGESTED

**Conocimiento capturado:**

*Gladwell/Ericsson (Outliers):*
- No hay "naturales" ni "grinders" en el estudio de Ericsson — la práctica deliberada lo explica todo
- La condición que Gladwell suavizó: no son 10,000 horas brutas, sino práctica deliberada con retroalimentación
- Mozart "desarrolló tarde" — nadie escapa la regla
- El ecosistema importa: llegar a 10,000 horas requiere contexto favorecedor
- Trabajo significativo = autonomía + complejidad + conexión esfuerzo-recompensa → el método de Luis cumple las tres

*Rock (Your Brain at Work):*
- PFC = recurso escaso, costoso, frágil ante amenaza/incertidumbre
- Hardwiring: 3 repeticiones bastan para iniciar long-term potentiation; el basal ganglia toma el control, libera la PFC
- Chunking: cada ítem en memoria de trabajo puede representar millones de bits → los expertos no tienen más memoria, tienen chunks más ricos
- Curva Yerkes-Dodson: el sweet spot entre aburrimiento y sobrecarga maximiza el rendimiento de la PFC
- El "director" (metacognición) se fortalece con práctica → cambia la estructura del cerebro

**Pendiente para próxima sesión:**
- Sección Sadhguru en modelos-mentales: silencio interior como condición del aprendizaje
- `filosofia-ensenanza.md` → conexión matemática mental / Elefantito
- Hacer git push

---

## [2026-04-22] ingest | Inner Engineering (Sadhguru)

**Fuente:** `07-fuentes/libros/Inner Engineering - Complete.md`
**Autor:** Sadhguru
**Relevancia:** Alta — fuente filosófica directa de la postura pedagógica central de Luis (no motivar, filtro natural, el método como tecnología)

**Archivos wiki afectados (4):**
- `08-sintesis/como-enseno-armonia.md` → tres nuevas secciones: el método como sadhana/tecnología, el filtro natural (hacer esperar), transmisión viva vs. información muerta
- `01-metodo-pedagogico/filosofia-ensenanza.md` → nueva sección "La Filosofía del Maestro: No Motivar a Nadie" con raíces filosóficas completas en Sadhguru. Entrada en Influencias Intelectuales expandida.
- `08-sintesis/luis-como-ingeniero-neural.md` → conexión Sadhguru expandida: "reordenamiento del sistema" y transformación dimensional
- `07-fuentes/indice-fuentes.md` → Inner Engineering marcado como INGESTED

**Conocimiento capturado hoy:**
- El guru como "dispeller of darkness", no como maestro/motivador — raíz directa del no-motivar de Luis
- La *willingness* como único filtro real del aprendiz (Sadhguru) = el coral perfecto como puerta (Luis)
- El método como sadhana (tecnología/dispositivo) vs. doctrina — distinción crítica para entender Los Seres Musicales
- Transmisión viva: el proceso no puede aprenderse de un libro, requiere retroalimentación en tiempo real
- Reorganización del sistema: Sadhguru provee el marco conceptual para "ingeniero neural"

**Pendiente para próxima sesión:**
- Ingestar *Thinking Fast and Slow* (Kahneman) — Sistema 1 vs. 2 conecta directamente con mielinización y método
- Ingestar *What is Intelligence* — identificar autor y procesar
- Continuar entrevista: visión civilizatoria (pendiente desde sesión 2026-04-17)
- `filosofia-ensenanza.md` → conexión matemática mental / Elefantito Matemático
- Hacer git push

---

## [2026-04-17] entrevista | ritmos-y-decisiones.md — creado

**Archivos modificados:** `00-contexto/ritmos-y-decisiones.md` (nuevo)
**Método:** Entrevista a Luis
**Contenido capturado:** Bloques fijos (Esteban Coppel diario, Adriana+Alejandra lunes/jueves, Jonás viernes, Bruno domingos, asesoría IA martes), sistema de IA en background (Openclaw + tarea Cowork → resumen 55 min para escuchar en bici), rutinas de guitarra y gym, contexto: campeón Musclemania Las Vegas a los 52 años.

---

## [2026-04-17] sesion | Entrevista — cómo enseño armonía + archivo de insights

**Trabajo realizado:**
- 5 insights del 2026-04-16 archivados en `00-contexto/insights.md`
- Entrevista a Luis para `08-sintesis/como-enseno-armonia.md`

**Archivos modificados:**
- `00-contexto/insights.md` — 5 insights archivados
- `08-sintesis/como-enseno-armonia.md` — nueva sección: visión de escucha directa, problema neurológico del tiempo, filosofía de no motivar (influencia Sadhguru / Inner Engineering)
- `CLAUDE.md` — estado actualizado
- `log.md` — esta entrada

**Conocimiento capturado hoy:**
- La meta final del método: escucha directa sin mediación (sin partitura, sin nomenclatura, sin análisis consciente)
- El obstáculo real es biológico: sin neurología de prodigio, toma muchos años
- Luis no trata de motivar a nadie — postura llegada con los años y las enseñanzas de Sadhguru
- El método filtra por sí solo: su exigencia es el filtro natural
- Conexión identificada: Inner Engineering (Sadhguru) → pedagogía de Luis → pendiente de ingestar

**Pendiente para próxima sesión:**
- Leer Inner Engineering para extraer conexiones con la pedagogía de Luis
- Continuar entrevista: más sobre la visión civilizatoria
- `filosofia-ensenanza.md` → conexión matemática mental / Elefantito Matemático
- `00-contexto/ritmos-y-decisiones.md` → archivo nuevo (ritmos operativos de Luis)
- Hacer git push

---

## [2026-04-17] actualización | insights.md — 5 insights del 2026-04-16 archivados

**Archivos modificados:** `00-contexto/insights.md`
**Cambio:** 5 insights capturados en sesión del 16/04 e integrados al archivo. Temas: redes neuronales / música como vehículo, mastery-based learning (coral perfecto), secuenciador vs Cubase, apps auditivas como núcleo del proyecto, visión civilizatoria.

---

## [2026-04-16] git push | Sesión completa subida a GitHub

**Commit:** `9a46b51` — 8 archivos, 785 KB
**Repo:** https://github.com/luisca66/storm-knowledge-base
**Nuevas fuentes detectadas en el push:**
- `Thinking Fast and Slow` (Kahneman) — Sistema 1 vs. Sistema 2, conexión directa con mielinización y método
- `What is Intelligence` — pendiente de identificar autor y procesar

**Acción:** Ambos registrados en `indice-fuentes.md`. Pendiente de ingestar al wiki.

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
