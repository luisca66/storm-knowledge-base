# log.md — Registro de Sesiones
## Storm Studios Learning KB

> Registro cronológico append-only de todo lo que ocurre en el KB.
> Cada entrada documenta qué se hizo, qué se ingresó, qué se aprendió.
> Formato de entrada: `## [FECHA] tipo | descripción`
> Tipos: `ingest` | `entrevista` | `actualización` | `lint` | `sesion`

---

## [2026-06-25] ingest | Resumen diario ainews — 24 de Junio de 2026

**Archivos generados:**
- `07-fuentes/ainews/202606/resumen_20260624.md` — resumen de noticias de IA del 24 de junio de 2026

**Archivos modificados:**
- `07-fuentes/ainews/202606/indice_general.md` — entrada para el 24 de junio de 2026 añadida al índice general
- `07-fuentes/indice-fuentes.md` — registrado periodo de junio de 2026

**Temas principales del día:**
- Surge AI y la Escuela del AGI (evaluaciones Riemann bench, conjetura de Erdős refutada).
- Optimización para el engagement vs. florecimiento humano (Hemingway bench, Claude, reward hacking).
- Lanzamiento de SeeDance 2.5 (video 4K, 30s) y regulaciones VFX en Hollywood.
- YC G stack (23 especialistas de IA) y memoria con grafos (Graphify).
- Loop of loops e iMessage Hermes updates.
- Alianzas de Anthropic con tradiciones de sabiduría, interpretabilidad y desalineación por trampa.

---

## [2026-06-24] ingest | Resumen diario ainews — 23 de Junio de 2026

**Archivos generados:**
- `07-fuentes/ainews/202606/resumen_20260623.md` — resumen de noticias de IA del 23 de junio de 2026

**Archivos modificados:**
- `07-fuentes/ainews/202606/indice_general.md` — entrada para el 23 de junio de 2026 añadida al índice general

**Temas principales del día:**
- Veto a Fable 5, controles de exportación y vulnerabilidades explotadas por IA.
- Preferencias del G7, Catch-22 de lanzamientos y restricción a modelos chinos.
- Ecosistemas exponenciales, capital de tokens y Microsoft Build.
- Crisis de costos, licencias por asiento y enrutamiento en loops agénticos.
- Fuga de cerebros en Google DeepMind (Shazeer, Jumper).
- Midjourney Medical (ultrasonido preventivo eludiendo FDA).
- Estudio de Oxford sobre persuasión conversacional de modelos frente a humanos.
- Adquisición de Cursor por SpaceX y lanzamiento del hub de código agéntico Origin.

---

## [2026-06-12] sesion | Diagnóstico y ruta hacia la autonomía operativa

**Pregunta:** qué falta para que el KB pase de continuidad a autonomía y qué no está funcionando todavía.

**Conclusión:** la IA ya puede orientarse y comprender el ecosistema, pero todavía no puede completar de forma confiable el ciclo ejecución → verificación → recuperación. El bloqueo no es una falta de permiso; son datos operativos dispersos, criterios de aceptación incompletos, ausencia de runbooks y falta de automatización entre el KB y los repos.

**Ruta registrada:**
1. Inventariar repos, rutas, comandos, ambientes, servicios y activos críticos.
2. Cerrar un primer circuito autónomo con Lección 1 + Maestro Virtual.
3. Documentar respaldo, restauración y rollback.
4. Replicar el patrón en el piloto móvil P03.
5. Automatizar la preparación matutina y el cierre nocturno de clases.

**Archivos modificados:** `05-operaciones/flujo-trabajo.md`, `CLAUDE.md`, `index.md`, `CHANGELOG.md`, `log.md`.

---

## [2026-06-12] lint | Revisión de salud tras consolidación y trabajo operativo

**Disparador:** Luis pidió una valoración general del KB después de varias sesiones intensivas.

**Resultado general:** el nivel de continuidad está cumplido y el KB ya produce síntesis superiores a sus fuentes individuales. La arquitectura conceptual es fuerte; el cuello de botella restante es operativo.

**Verificaciones:**
- Git sincronizado con `origin/main` al iniciar.
- 346 archivos Markdown: 173 en `clases-ia`, 123 raw sources y 50 archivos del wiki/sistema fuera de ambos.
- 147 referencias de frontmatter revisadas: 0 rotas.
- 116 enlaces Markdown relativos revisados: 0 rotos.
- 7 páginas de síntesis con 1,871 líneas acumuladas.
- 13 borradores, todos concentrados en lecciones/reglas, apps auxiliares, contenido musical y operaciones.

**Problemas corregidos:**
- `index.md` tenía conteos y fecha anteriores al trabajo del 12 de junio.
- `estructura-curso.md` decía simultáneamente “5 publicadas” y “solo Lección 1 activa”.
- `maestro-virtual.md` mezclaba el estado viejo de dummies con la reconstrucción Next.js.
- `indice-apps.md` conservaba “Play Store en evaluación” pese a la decisión web-gratis/móvil-de-paga.
- Migración Empresas no había propagado a Julio ni tenía frontmatter en su entrevista fundacional.
- El insight del KB como activo acumulativo fue procesado hacia `tecnologia-al-servicio-del-metodo.md`.
- Enlaces locales heredados de Windows fueron normalizados en `insights.md`.
- La convención de frontmatter ahora reconoce explícitamente los 169 archivos heredados de `clases-ia` y evita una migración mecánica sin valor.

**Lectura estratégica:** el trabajo de los últimos días corrigió la inversión detectada el 10 de junio: el KB ya empezó a bajar de la síntesis hacia la operación. Aun así, `04-contenido-musical/`, `05-operaciones/`, las reglas de validación y las fichas de lecciones siguen siendo la principal deuda para alcanzar autonomía.

---

## [2026-06-12] entrevista | Estructura del Curso y Maestro Virtual

**Origen:** Prioridad #1 de CLAUDE.md (nivel operativo del KB). Faltaba mapear el estado real de las lecciones de la plataforma.

**Conocimiento capturado:**
- **La reconstrucción en Next.js:** El número de ~60 lecciones es un cálculo histórico (corales del último alumno). Actualmente, en la plataforma solo está publicada la Lección 1 debido a que los videos son nuevos y la estructura se está rearmando.
- **Borrador de secuencia:** L1 Mayores, L2 Modos (en evaluación), L3 Menores, L4 Acordes 5ª Mayor, L6 Acordes 5ª Menor, L7 Cuarteto vocal (SATB).
- **El Maestro Virtual:** Su meta última no es solo calificar tareas gratis, sino "obligar" a una IA a componer acatando las reglas de Luis. 
- **Flujo de codificación de reglas:** PDF del curso → LLM de frontera (Fable) lee y traduce paso a paso → Pruebas de fuego en un validador HTML aislado → Integración a Next.js.

**Archivos tocados:**
- `01-metodo-pedagogico/estructura-curso.md`: Re-escrita la sección de lecciones asumiendo el estado post-migración.
- `02-plataforma-web/maestro-virtual.md`: Añadido el flujo de trabajo humano-IA.
- `log.md`: Cierre de la sesión operativa.

## [2026-06-12] entrevista | Entrevista Fundacional de Migración Empresas

**Origen:** Pendiente prioritario de CLAUDE.md para extraer la visión de la nueva línea de asesoría `09-migracion-empresas` sin duplicar manuales técnicos.

**Conocimiento capturado:**
- **El dolor real del cliente:** FOMO y miedo a la irrelevancia. Compran la "sabiduría empírica de un no-programador" (el ecosistema de Luis) y el enfoque casual de decirle a la IA "hazlo tú".
- **Concepto de Migrar:** Pasar de un chatbot a un Gemelo Digital en el borde, con agentes y "líneas rojas" inviolables (ExO 3.0).
- **Proceso de 90 días:** Diagnóstico → Backcasting → Plan → Gemelo Digital.
- **Modelo de negocio:** Mismo que las clases de IA. Actualmente 1,000 MXN por sesión de 1.5 a 2 horas, subirá a 1,500 MXN por persona.
- **El rol de Luis (Socio Builder):** Reducir fricciones en los "detallitos estúpidos" que detienen la adopción de IA. Meta final: que el cliente necesite menos sesiones.
- **Cartera activa:** Pilotos con "Voces Imaginarias" y "Julio" (microfinanciera).

**Archivos tocados:**
- Creado `09-migracion-empresas/entrevista_fundacional.md`.
- Modificado `09-migracion-empresas/README.md` (eliminados pendientes, añadido enlace al nuevo documento).
- Actualizado `CLAUDE.md` (§7: pendiente marcado como completado).
- Actualizados `index.md` y `log.md`.

## [2026-06-12] ingest | ainews junio días 4-12 → ai-radar.md (Fable 5 es el evento del mes)

**Disparador:** chequeo de continuidad de Luis ("qué podemos seguir avanzando"). El pendiente #2 de CLAUDE.md §7 era el radar atrasado (cerraba el 06-03, faltaba Fable 5 / Mythos 5). Se eligió esta vía por ser autónoma (no requiere entrevista).

**Fuentes procesadas:** `07-fuentes/ainews/202606/` resúmenes del 04, 08, 09, 10, 11 y 12 de junio (ya estaban en el repo e índice; el trabajo fue la síntesis al wiki).

**Hallazgo central:** el **9 de junio Anthropic lanzó Claude Fable 5** (y Mythos 5 restringido a Glasswing) — el primer modelo de clase superior a Opus (≈10B params), y el wiki no lo tenía. Es el evento que parte junio en dos.

**Archivos tocados (4):**
- `00-contexto/ai-radar.md` — síntesis de junio extendida a días 1-12 (nuevas secciones 15-22), Sección 3 con tabla de modelos actualizada y 3 conceptos pedagógicos nuevos (imaginación de tareas, alfabetización de modelos, playbook AEO local), changelog.
- `CHANGELOG.md` y `log.md` — esta entrada.
- (Pendiente CLAUDE.md §7 — ver abajo.)

**Conocimiento capturado:**
- Fable 5: jerarquía haiku→sonnet→opus→fable; Mythos = mismos pesos sin guardarraíles; benchmarks (SWEBench Pro 80.3, Frontier Code 29.3); **sale de las suscripciones el 22-23 jun** → API a $10/$50; consume tokens 2x. Daily driver sigue siendo Opus 4.8 para el 90-95% del trabajo.
- "De dar tareas a dar responsabilidades" (Ryberg) / "imaginación de tareas" (Nate Jones) — el nuevo gap de adopción.
- Las tres controversias de Fable (clasificadores, degradación silenciosa revertida en <24h, retención 30 días no revertida) — relevante para privacidad en asesorías PYMES.
- Crisis de costos concreta: Uber capa gasto; la **auditoría de tokens por rol** como servicio vendible para PYMES (conecta con Efecto Santiago).
- AEO local con método (Caleb Ulku): entity matching, reseñas con atributos específicos, `llm.txt` casi inútil → playbook para el website de Luis y el de Mario.

**Pendiente para próxima sesión:**
- Propagar la tabla de modelos a `conceptos_no_olvidar.md` y `leccion_01` en clases-ia (requiere leer `INSTRUCCIONES_CLASES_IA.md` antes de editar).
- Evaluar si el playbook AEO local merece ampliar `08-sintesis/estrategia-freemium-musical.md` §5 con los pasos concretos (hoy solo cross-link).
- Cerrar junio en el radar al terminar el mes (días 13-30).

---

## [2026-06-11] entrevista | Propósito del KB — el mapa real del ecosistema

**Origen:** Tras la consolidación del schema, Luis ofreció entrevista para dejar el propósito totalmente claro. Tres preguntas, hallazgos mayores:

**1. El mapa corregido:** Storm Studios = el estudio físico en casa (5.1 Genelec + gym), centro de operaciones. Las **clases particulares** (taller de composición e instrumentos, entrenamientos físicos, clases/asesorías de IA) son **la vaca lechera actual**. Storm Studios Learning = el website: produce $0 hoy por diseño; es legado + promotor de las clases + futuro ingreso pasivo. El schema decía "SSL = el proyecto de vida" — corregido en CLAUDE.md §1 y vision-proyecto.

**2. La prueba de la vacación (nivel 2 del propósito):** éxito = irse unos meses y que las entradas sigan llegando: venta de apps móviles + libros/manuales en Amazon + (teórico) YouTube. Única función docente sin Luis: el Maestro Virtual corrigiendo armonía. La escena del "martes cualquiera" (la IA prepara las clases del día, recuerda lo importante, reporta noticias de IA, guarda contexto nocturno) **ya existe en ~70%** — el 30% faltante es integración automática.

**3. Decisión nueva — apps:** web gratis siempre + móviles de paga a precio bajo (Android e iOS, ambas en desarrollo). Evaluada con honestidad a petición de Luis ("no me des por mi lado"): estrategia sólida; métrica correcta = tráfico al embudo, no el ingreso directo; piloto con P03 antes de portar el catálogo; pago único, nunca suscripción. Supersede la decisión Play Store del 05-22. También documentada la postura: **sin límites a priori a la autonomía de la IA**.

**4. Identidad:** el vibe coding = los estudios diarios de Luis (como la guitarra), ya monetizados vía clases de IA — el Paradigma de No-Compartimentación aplicado a sí mismo. → quien-soy.md.

**Lint colateral:** contradicción detectada entre stack-tecnologico.md ("10 apps en Google Play") y la decisión Play Store del 05-22 (descarga directa desde website) — marcada por verificar en CLAUDE.md §7.

**Archivos tocados (9):** CLAUDE.md (§1, §7), vision-proyecto.md (resumen, apps, escalera +1 peldaño, "La prueba de la vacación", "La escena objetivo", tabla de ingresos, Palestriniano), decisiones-clave.md (2 decisiones nuevas + Play Store actualizada), quien-soy.md, stack-tecnologico.md (iOS), estrategia-freemium-musical.md (§3), log.md, CHANGELOG.md, index.md.

---

## [2026-06-11] actualización | Consolidación del schema — CLAUDE.md fuente única

**Origen:** Luis preguntó si el propósito del KB queda claro al leerlo. La revisión (primera sesión con Fable 5) encontró tres problemas de fondo:
1. **Dos formulaciones de propósito con ambición distinta** — README pedía continuidad ("colaborar sin re-explicar"); CLAUDE.md pedía autonomía ("construir el proyecto de forma autónoma"). La distancia entre ambas es exactamente el hallazgo #1 de la auditoría del 06-10 (el KB piensa pero no opera).
2. **Alcance desactualizado** — CLAUDE.md §2 hablaba de "el proyecto" en singular cuando el KB ya cubre tres líneas (plataforma, clases/asesorías IA, Migración Empresas).
3. **Jerarquía de entrada en conflicto** — tres archivos se declaraban "leer primero", e index.md describía a AGENTS.md como maestro y a CLAUDE.md como "histórico".

**Divergencia confirmada entre los schemas gemelos:** AGENTS.md tenía la regla del doble reglamento de clases-ia y el pendiente de localStorage; CLAUDE.md no. Quinto señalamiento del problema — ahora resuelto de raíz.

**Cambios:**
- `CLAUDE.md` reescrito como schema maestro único y agnóstico de agente: propósito en dos niveles (continuidad ✅ / autonomía pendiente), alcance de tres líneas, tabla de jerarquía de archivos de entrada, contenido único de AGENTS.md fusionado, §7 adelgazado (estados → index.md, historial → log.md, fuentes → indice-fuentes.md; solo quedan la fecha y los pendientes prioritarios).
- `AGENTS.md` reducido a stub de redirección.
- `README.md` redefinido como portada del repo privado; secciones de convenciones e instrucciones (duplicadas y ya divergidas — su lista de tipos de frontmatter era distinta a la del schema) reemplazadas por puntero. Estado: completo.
- `index.md` jerarquía corregida.
- Decisión registrada con razonamiento y alternativas en `00-contexto/decisiones-clave.md` (borrador → en_progreso).
- Nuevos pendientes capturados en §7 desde la auditoría: entrevistas operativas (lecciones, reglas de validación, infraestructura), radar atrasado (falta Fable 5 / Mythos 5), respaldo del KB fuera de GitHub.

---

## [2026-06-10] entrevista | Migración Empresas — apertura de nueva línea de negocio

**Hallazgo:** Migración Empresas no estaba documentado en el KB. Luis confirmó que es un proyecto nuevo y que ya está generando ingresos.

**Frontera confirmada:**
- Migración Empresas agrupa proyectos empresariales con repositorios propios.
- Voces Imaginarias vive dentro de Migración Empresas y tiene proyecto y repo independientes.
- `clases-ia` registra únicamente lo aprendido por Carmen, Mario, Montse, Karla y Dayana al usar ese contexto real.
- La estrategia, operación y arquitectura de cada empresa no se duplican en los expedientes de alumnos.

**Cambios realizados:**
- Creada `09-migracion-empresas/README.md` como fuente canónica.
- Creado `09-migracion-empresas/proyectos/indice-proyectos.md`.
- Reclasificada la carpeta grupal de Voces Imaginarias como bitácora pedagógica.
- Eliminados del CSV de clases los cinco registros duplicados del proyecto empresarial.
- Actualizados schema, índice, README, visión, biografía, asesorías, changelog y referencias de alumnos.

**Siguiente pregunta de entrevista:** definir qué significa exactamente "migrar" una empresa y qué transformación compra el cliente.

---

## [2026-06-10] entrevista | Apertura del expediente de Dayana

**Conocimiento aportado por Luis:**
- Dayana tiene 38 años, trabaja con Carmen y Mario y ya esta avanzando en sus clases de IA.
- Es coproductora externa, pero forma parte fundamental del equipo.
- Su asistencia a las clases grupales es irregular.
- Curso fundamentos de chatbots gratuitos con Gemini, ChatGPT y Claude: seleccion de modelos, niveles de pensamiento, deep research y thinking.
- Despues curso agentes con Codex y Antigravity; no tiene acceso a Cowork ni Claude Code.
- Ya sabe usar Codex y Antigravity.
- En la clase grupal mas reciente creo su cuenta de GitHub.
- Participa con Montse, Carmen, Mario y Karla en el arranque del cerebro digital de Voces Imaginarias.

**Cambios realizados:**
- Se creo `03_alumnos/dayana_38/` con perfil, diagnostico y carpetas operativas.
- Se agrego a Dayana en `09_base_de_datos/alumnos.csv`.
- Los datos todavia desconocidos quedaron como `pendiente`.
- Se actualizaron el contexto, estado, pendientes, changelog, indice y schema maestro para reflejar 11 alumnos.
- Se reconstruyo su ciclo inicial y se actualizaron sesiones, avances y proyectos.
- Se creo una fuente unica para el proyecto grupal en `04_sesiones/grupos/voces_imaginarias/`.
- Se establecio que Luis narra cada clase grupal una sola vez y el agente distribuye evidencia individual a los cinco expedientes.

**Siguiente pregunta de entrevista:** definir que significa y que debe lograr el cerebro digital de Voces Imaginarias.

---

## [2026-06-10] actualización | Sincronización del registro de alumnos de clases-ia

**Disparador:** Luis preguntó qué alumnos estaban registrados y se detectó que Esteban tenía expediente propio, pero no aparecía en `09_base_de_datos/alumnos.csv`.

**Cambios realizados:**
- Se agregó `esteban_33` a `alumnos.csv` usando únicamente información existente en su perfil.
- Los datos no confirmados quedaron marcados como pendientes o por confirmar.
- `PROJECT_CONTEXT.md` y `00_instrucciones/ultimo_estado.md` se actualizaron para reflejar los 10 alumnos actuales.

**Resultado:** las 10 carpetas de `03_alumnos/` tienen ahora una fila correspondiente en el registro general.

---

## [2026-06-10] lint | Auditoría completa del proyecto (Fable 5)

**Disparador:** Luis pidió auditoría completa + opinión + qué mejorar.

**Corregido en esta pasada (mecánico):**
1. ✅ **El árbol de carpetas del schema (§3) no incluía `08-sintesis/`** — la carpeta más valiosa del KB era invisible en su propio mapa. Además `07-fuentes/` aparecía duplicado, faltaban `ainews/`, `2026-05.md` del diario y la nota sobre `clases-ia/`. Corregido en **CLAUDE.md y AGENTS.md** (idénticos).
2. ✅ `index.md` stats: "256+" archivos → real 332 (clases-ia: 169).

**Hallazgos estructurales (recomendaciones, no ejecutadas — detalle en la conversación):**
- **El KB está invertido respecto al embudo:** 08-sintesis florece (7 páginas ricas) mientras lo operativo que el lanzamiento necesita sigue en esqueleto: 02-plataforma-web (4/5 borrador), lecciones (2 de ~65, ambas [LLENAR]), reglas-validacion vacío, 04/05 clavados en 2026-04-07 (16 archivos). El objetivo declarado del KB ("que una IA pueda construir el proyecto de forma autónoma") hoy se cumple para el *pensamiento* pero no para la *operación*.
- **ai-radar 8 días atrás:** cubre jun 1-2; hay ainews hasta jun 10. **Fable 5 / Mythos 5 (lanzado jun 9) no existe en el wiki** — y la tabla de modelos de Sección 3 (material "actualizar inmediatamente" para clases) sigue con Opus 4.8 como tope.
- **clases-ia = 53% del KB** sin movimiento desde 06-01 — si está pausado, decirlo en el schema; si está activo, faltan registros de sesión.
- **CLAUDE.md §7 crece sin límite** y duplica log/index (ya produjo 1 falso pendiente) → recomendación: §7 mínimo + puntero a log.md.
- **AGENTS.md/CLAUDE.md duplicados** (4º lint) → recomendación: AGENTS.md como stub que apunte a CLAUDE.md.
- **Single point of failure:** todo vive en GitHub + máquinas locales → recomendación: `git bundle` mensual a disco/Drive.
- Menores: godot-juegos.md sigue borrador/04-07 pese a entrevista 06-04 (pendiente conocido); README descrito como "presentación pública" (es portada del repo privado); 2 archivos con `ultima_actualizacion: YYYY-MM-DD` (plantillas).

**Lo que está funcionando (validado):** criterio de éxito del KB cumplido (respuestas nivel 2 mejores que cualquier fuente individual — caso AEO/paradoja de la legibilidad); log append-only impecable; pipeline ainews corriendo solo; separación fuentes/wiki respetada; honestidad intelectual (matiz del AP del 06-04).

**Archivos modificados:** CLAUDE.md (árbol §3), AGENTS.md (árbol §3), index.md (stats), log.md.

---

## [2026-06-09] ingest | Resumen diario ainews — tarea automatizada

**Archivos generados:**
- `07-fuentes/ainews/resumen_opus_20260609.md` — resumen principal, 8,566 palabras, prosa narrativa en español
- `07-fuentes/ainews/resumen_basico_opus_20260609.md` — resumen básico, 1,464 palabras, lenguaje accesible

**Fuentes procesadas (5 transcripts de `transcripts_hoy/`):**
- `aishowpod.txt` (16,160 palabras) → 5,139 palabras asignadas — IPO Anthropic, ensayo "When AI Builds Itself", EO Trump, Sanders/Trump soberanía, crisis presupuesto tokens (Uber/Microsoft/OpenAI), Apple WWDC, OpenAI Codex work agent, roll-up contable, educación superior, Alli Miller methodology
- `matthew.txt` (4,940 palabras) → 1,571 palabras asignadas — Claude Fable 5 firsthand: benchmarks, Stripe migration, demos, UltraCode, verbosity, anti-distillation redirect, loops
- `caleb.txt` (4,565 palabras) → 1,452 palabras asignadas — SEO en era de agentes, entity matching, Bing Webmaster Tools AI tab, LLM.txt, reseñas con atributos
- `wes.txt` (3,214 palabras) → 1,022 palabras asignadas — system card Fable 5: capability layer, multi-agent turf wars, anti-acceleration limits, biorisk/proteínas
- `alex.txt` (2,565 palabras) → 816 palabras asignadas — workflow práctico Fable 5: mental shift, plan mode, loops, demo app, deadline 22 junio

**Noticias principales del día:** Lanzamiento Claude Fable 5 / Mythos 5 (10T parámetros, mismo modelo distinta capa de seguridad)

---

## [2026-06-08] ingest | Resumen diario ainews — tarea automatizada

**Archivos generados:**
- `07-fuentes/ainews/resumen_opus_20260608.md` — resumen principal, 8,572 palabras, prosa narrativa en español
- `07-fuentes/ainews/resumen_basico_opus_20260608.md` — resumen básico, 1,359 palabras, lenguaje accesible

**Fuentes procesadas (7 transcripts de `transcripts_hoy/`):**
- `peter.txt` (21,772 palabras) — Moonshots / Peter Diamandis con Dave, Wissner-Gross, Immad Mak
- `extra.txt` (14,394 palabras) — Big Technology Podcast / Kantrowitz + Seagler
- `aiengineer.txt` (7,318 palabras) — AI Engineering: Pyannote AI + Arize AI
- `aiforhumans.txt` (6,477 palabras) — AI For Humans: Gavin + Kevin
- `mattwolfe.txt` (6,053 palabras) — Matt Wolfe / Microsoft Build en persona
- `nate.txt` (4,329 palabras) — Nate Jones: token burn dashboard
- `aiadvantage.txt` (3,276 palabras) — AI Advantage: ChatGPT memory + Codex plugins

**Temas principales del día:**
- IPO de Anthropic (S-1 confidencial ante la SEC)
- ChatGPT alcanza 1 billón de MAUs; Claude crece 640% YoY a 56M
- Microsoft Build 2026: 7 modelos MAI, Scout agent, Project Solara, GitHub Copilot app
- Nvidia RTX Spark chip (GPU+CPU, 128GB unificada) en Computex
- Super app convergence: Codex + Atlas + ChatGPT fusionándose; Google IO post-mortem
- Trump AI Executive Order (voluntario, 30 días pre-release)
- Verve-102: inyección única edición de gen PCSK9, -62% LDL sostenido
- Nuevos modelos: Neotron 3 Ultra (550B OW), Gemma 4 12B, Minimax M3
- Speaker diarization (Pyannote AI) + observabilidad de agentes (Arize)
- Token burn dashboard como retroalimentación metacognitiva (Nate Jones)

---

## [2026-06-04] lint | Checada de salud del KB

**Disparador:** Luis pidió "darle una checada" al proyecto.

**Chequeos realizados:**
- `git status` limpio antes de empezar.
- Revisión de últimos commits.
- Revisión de `AGENTS.md`, `CLAUDE.md`, `index.md`, `CHANGELOG.md`, `log.md`.
- Búsqueda de placeholders, borradores, pendientes explícitos y estados de frontmatter.
- Chequeo mecánico de `relacionado_con`: sin referencias rotas reales fuera de ejemplos/templates.

**Problemas detectados y resueltos:**
1. `AGENTS.md` estaba congelado en 2026-05-26 mientras `CLAUDE.md` e `index.md` ya estaban en 2026-06-03 → sincronizado.
2. La convención de `tipo:` no aceptaba `spec` ni `sintesis`, aunque el KB ya los usa en archivos reales → schema ampliado.
3. `index.md` marcaba los archivos de `02-plataforma-web/` como `borrador`, pero sus frontmatter están en `en_progreso` → corregido.
4. `index.md` e `indice-apps.md` todavía describían Elefantito Matemático como `en_progreso`/6 niveles; la ficha actual lo marca `completo` con 20 niveles → corregido.

**Pendientes que siguen abiertos:**
- `04-contenido-musical/` y `05-operaciones/` siguen siendo las zonas más vacías del KB.
- `progresion-estudiante.md` aún necesita entrevista para criterios de dominio y gamificación.
- `08-sintesis/tecnologia-al-servicio-del-metodo.md` aún necesita completar apps de entrenamiento auditivo.
- Decisión de fondo: consolidar `AGENTS.md` y `CLAUDE.md` para evitar divergencia futura.

---

## [2026-06-04] entrevista | Apps de entrenamiento auditivo — el método precede a la tecnología

**Archivos:** `08-sintesis/tecnologia-al-servicio-del-metodo.md` (sección apps completada — era [Pendiente]), `03-apps-herramientas/indice-apps.md` (nueva sección "Origen y evolución" + orden de uso cognitivo), `08-sintesis/entrenamiento-oido-absoluto.md` (nota de linaje Burge en Premisa central).

**Pregunta:** orden y momento de uso de las apps de oído en el camino del alumno (capa operativa que faltaba; la teoría ya estaba en entrenamiento-oido-absoluto.md §10).

**Conocimiento capturado:**
- **La metodología precede a las apps.** Cronología: pre-2024 ejercicios a mano (heredados de **David Lucas Burge** + evolución propia), ejecutados por los alumnos programándolos en **Cubase** → 2024 libro (Amazon Kindle oct 2024) + primeros intentos en Python → 2025 Android vibe-coding (automatiza lo de Cubase) → 2026 explosión con Claude Code. Las apps **automatizaron un método existente, no lo crearon**.
- Esto es la prueba histórica de la tesis del archivo de síntesis: la tecnología llegó a un método maduro. Efecto Santiago a escala de catálogo (las apps escalan lo ya validado, no descubren).
- **Orden de apps cognitivas:** primero Memoria, luego Matemáticas Mentales (Elefantito).
- **Estado de uso honesto:** el último alumno "vintage" se fue a mediados de 2025; desde entonces solo Luis ha usado las apps. Codifican método validado, esperan primer alumno.

**Pendiente que sigue:** documentar el juego auditivo en Godot (13 niveles, `[LLENAR: estado]`); precisar el orden de uso de las 8 apps de oído relativo al avance en lecciones.

---

## [2026-06-04] entrevista | Oído absoluto — el matiz honesto (prodigio vs. parches, el viaje basta)

**Archivos:** `08-sintesis/entrenamiento-oido-absoluto.md` (§2 nueva subsección + §1 rebajado + §12 actualizada), `03-apps-herramientas/indice-apps.md` (apps de AP clarificadas + nota de AP).

**Conocimiento capturado (matiza y mejora la síntesis, que sobrevendía el AP):**
- **El AP se entrena desde el principio**, en paralelo con el desglose, progresivo. Es el terreno más controversial del método.
- **Posición honesta de Luis:** la cultura dice que el AP es genético; quienes dicen que se desarrolla en adultos, Luis sospecha que producen un **desarrollo falso** = "parches mentales" que imitan al AP sin ser la habilidad genuina del prodigio. Luis **no afirma replicar el AP del prodigio.**
- **La tesis del viaje:** no importa si nunca se desarrolla del todo, porque siempre se siente el progreso → algo cambia físicamente en el cerebro → esa habilidad naciente impacta profundamente la comprensión musical. El método apuesta al **gradiente, no al umbral**.
- **Timeline:** 5–10 años de trabajo serio (con entusiasmo y conocimiento de los principios fisiológicos/neurológicos), o no llegar nunca.
- **Las dos apps de AP:** Multitímbrico = la del taller (principal); Guitarra Clásica = app personal de Luis (es concertista de guitarra clásica), publicada como extra porque ya existe.

**Efecto en el KB:** §1 de la síntesis rebajado de "la tesis del don queda desmontada" a "gradiente, no umbral"; afirmación más sólida y honesta. **Cierra el catálogo completo de apps de oído.**

---

## [2026-06-04] entrevista | La secuencia del oído relativo + diseño multitímbrico

**Archivos:** `03-apps-herramientas/indice-apps.md` (nota de secuencia del oído relativo + diseño multitímbrico), `08-sintesis/entrenamiento-oido-absoluto.md` (mapa de apps §10 reorganizado).

**Conocimiento capturado:**
- **Tras Desglose, el oído relativo se entrena simultáneo y exhaustivo (meses):** Intervalos (las dos apps a la vez — Reconocer + Cantados; percibir y producir se desarrollan por separado aunque comparten corteza), Grados (función tonal, igual o más importante que intervalos), Acordes (5ª/tríadas → 13ª).
- **Grados solo tiene versión Reconocer** (Mayor/Menor). Luis se dio cuenta en la entrevista de que **falta programar Grados Cantados** — ya tiene ideas. → Pendiente nuevo.
- **Diseño multitímbrico (todas las apps):** piano, coro, corno, fagot, cello o multitímbrico. Razón: la música es multitímbrica, no solo piano (el instrumento con que casi todos entrenan el oído, sesgando la percepción a un timbre). Entrenar a través de timbres desata la identidad de la nota de su envoltura tímbrica (coherente con timbre = perfil de armónicos, §5).

**Pendiente generado:** programar app **Grados Cantados**.

---

## [2026-06-04] entrevista | Los juegos Godot y el Videojuego Total de Entrenamiento Auditivo

**Archivos:** `03-apps-herramientas/indice-apps.md` (sección Godot reescrita, era stub `[LLENAR]`), `00-contexto/vision-proyecto.md` (nuevo horizonte lejano en La Visión Completa).

**Pregunta:** qué es el juego auditivo en Godot y su estado.

**Conocimiento capturado:**
- **Dos juegos Godot reales:** (1) **Oído Absoluto** — terminado, "quedó hermoso", 5 niveles en 5 mundos (cocodrilito, personaje esférico, unicornio volador pedido por Kari —novia de Luis—, nave espacial, +otros). (2) **Intervalos** — en desarrollo, versión nueva: enemigos que acechan, el enemigo produce la nota base y pide un intervalo; el alumno canta la nota correcta ~1.5 s para cargar el arma *y* la escribe a mano; con ambas correctas dispara.
- **La visión grande (nueva en el KB):** el **Videojuego Total de Entrenamiento Auditivo** — un juego donde *toda* la mecánica se resuelve con habilidades auditivas (desglose, AP, acordes, grados), mundos oníricos con personajes etéreos, narrativa auditiva progresiva. Condicionado a "si vivo para hacerla realidad" y a IAs futuras (estima Claude Opus 7, probablemente). Los juegos Godot actuales son la semilla.
- Los juegos también han sido motor del aprendizaje de Luis como vibe coder, ligado a modernizar clases y dar mejores asesorías de IA.
- Dato corregido: la cifra "13 niveles" del KB no estaba verificada; lo confirmado es 5 niveles en el juego de AP.

---

## [2026-06-04] entrevista | Desglose — la operación fundacional del oído

**Archivos:** `08-sintesis/entrenamiento-oido-absoluto.md` (nueva sección en §5 + reorden del mapa de apps §10), `03-apps-herramientas/indice-apps.md` (Desglose detallado + nota fundacional). Consultado `07-fuentes/libros/Los_Seres_Musicales.md` (definición de Ser Musical, confirmada consistente con el KB).

**Pregunta:** orden de uso de las 8 apps de oído.

**Conocimiento capturado:**
- **Desglose es la app fundacional** y donde todos los alumnos vienen más atrasados (Luis incluido en su propio desarrollo). Mecánica: toca 2–7 notas simultáneas (piano, corno, coro, cello, fagot, multitímbrico); el alumno **canta** cada nota y la app la valida al afinar. **Sensible a la nota, no a la octava** → rango C2–C7. Progresión: principiante 2 notas en rango vocal → con los años 7 notas en todo el rango instrumental.
- **Axioma:** "si no puedes desglosar lo que estás escuchando, simplemente no lo estás escuchando." Escuchar = descomponer, no recibir.
- **Prerrequisito del AP:** las apps de oído absoluto suponen que el oído puede separar fundamental+armónicos; sin esa capacidad no hay sustrato fisiológico ni neurológico para el AP. El timbre ES el perfil de armónicos → desglosar armónicos es anclar la frecuencia limpia de su envoltura tímbrica. Conecta con la tesis de la corteza selectiva (§2) y con la progresión del atleta (§ el-musico-como-atleta).
- Dato corregido en el KB: Desglose es 2–7 notas (antes figuraba 2–5).

**Definición de Ser Musical (del libro, confirmada):** quien maneja el lenguaje musical como su idioma natal — escucha y entiende cada nota/frase sin partitura y puede transcribir. El taller transforma a los no-prodigios en seres musicales modificando estructuras cerebrales (entrenamiento selectivo de la corteza). Esencia: intención consciente. Ya consistente con filosofia-ensenanza / luis-como-ingeniero-neural (Camino de la Señal).

---

## [2026-06-04] entrevista | El porqué de Memoria + Matemáticas — gimnasio del cerebro en la era de la IA

**Archivos:** `03-apps-herramientas/indice-apps.md` (App Memoria detallada + porqué del orden), `03-apps-herramientas/elefantito-matematico.md` (Propósito Pedagógico ampliado), `08-sintesis/tecnologia-al-servicio-del-metodo.md` (sección Elefantito + argumento anti-zombie).

**Pregunta:** por qué el alumno empieza por Memoria y Matemáticas Mentales (la capa de preparación cognitiva).

**Conocimiento capturado:**
- **App Memoria = sistema fonético clásico:** cada dígito se asocia a consonante(s); las vocales no cuentan, así los números se vuelven palabras memorizables. La app lo deja listo para practicar y jugar cronometrado.
- **El orden y su porqué:** primero Memoria (retener números con fluidez = construir la plantilla), luego Matemáticas Mentales (el cálculo rápido exige sostener resultados intermedios grandes en memoria de trabajo). "Memoria es primero y es todo".
- **El argumento de fondo (tesis civilizatoria):** así como quien entra al taller entra al gimnasio físico, el alumno empieza por el desarrollo *físico del cerebro*. En la era de "todo lo hace ChatGPT", mantener el cerebro irrigado es urgente por dos razones: (1) no perderlo por desuso; (2) no caer en consumidor pasivo de corporaciones que nos necesitan comprando lo innecesario. Conecta con Karpathy ("no puedes tercerizar tu entendimiento") y con el Sándwich Humano (el humano que encuadra/juzga necesita un cerebro en forma).

---

## [2026-06-03] corrección | El KB es privado — nunca público (aclaración de Luis)

**Disparador:** Luis señaló que una redacción mía ("el KB no debe volverse *todo* público") implicaba erróneamente que parte del KB podría publicarse. No es así: **el KB es privado y nunca se publica.**

**La separación correcta, ahora explícita:**
- **KB** = cerebro externalizado privado de Luis (y la IA que colabora). Nunca público.
- **Website / YouTube / Kindle** = artefactos públicos, *redactados usando* el KB como fuente.
- **AEO / legibilidad para agentes aplica solo al website**, jamás al KB. "Alimentar la capa pública" = redactar el website con el KB, no exponerlo.

**Por qué importa:** es parte del foso. La síntesis profunda del método (el "mecanismo") se queda privada; lo público expone identidad + resultados, no el cómo (paradoja de la legibilidad).

**Archivos modificados:** `08-sintesis/estrategia-freemium-musical.md` (§5 corregida en 3 puntos + aclaración + historial), `CLAUDE.md` (§2 — privacidad del KB hecha explícita y permanente), `log.md`. Memoria guardada: `kb-es-privado`.

---

## [2026-06-03] actualización | Recomendación AEO evaluada contra el radar — la paradoja de la legibilidad

**Archivos:** `00-contexto/ai-radar.md` (Sección 2 — 6º lente), `08-sintesis/estrategia-freemium-musical.md` (§5).

**Contexto:** Luis pidió leer el ai-radar a fondo (incluidas fuentes crudas) para *evaluar* la recomendación de AEO contra lo que el campo realmente dice, no solo registrarla.

**Hallazgo clave (estaba solo en fuentes crudas, faltaba en el wiki):** la **paradoja de la legibilidad** de Nate B. Jones (`ainews/202605/resumen_20260504.md`). El trabajo durable debe ser legible para ser *valorado* pero no tan legible como para ser *ejecutado sin ti*. Dos errores: invisible (sin crédito) vs. demasiado explícito (delegable/automatizable). Salida: **legibilidad parcial** — resultados sí, mecanismo no; mucho del trabajo durable es instinto calibrado no articulable ("no es un proceso; es lo que eres"). → Añadido como **6º lente del marco conceptual** del radar.

**Evaluación de la recomendación:** estaba direccionalmente bien pero le faltaba este concepto, que la *afila*. Refinamientos integrados a §5:
1. **Guardrail de legibilidad parcial:** exponer identidad + resultados (para ser descubrible/recomendable), NO el mecanismo del método (para no ser replicable). Es la misma lógica del video irreducible (§7) aplicada a la capa pública.
2. **El KB no debe volverse todo público:** la síntesis profunda del método es el activo durable; publicarla parseable sería regalar el foso.
3. **Schema markup:** corregido de "no hacer" a "prioridad baja, no cero" — útil para descubrimiento local, después de la página canónica. El vector real de Luis es conversacional, no de mapas.

**Archivos modificados:** ai-radar.md (6º lente + historial), estrategia-freemium-musical.md (§5 guardrail + historial), log.md.

---

## [2026-06-03] actualización | AEO como recomendación operativa + pasada de consistencia

**Archivos:** `08-sintesis/estrategia-freemium-musical.md` (§5), `00-contexto/ai-radar.md` (§13).

**Contexto:** Luis pidió mi opinión sobre si invertir en AEO (hacer la plataforma legible por agentes) y luego pidió revisar el KB porque el ai-radar ya tiene mucho material de AEO.

**Pasada de consistencia (AEO en el KB):** el AEO está bien cubierto como *tendencia* en `ai-radar.md` en 5 lugares (economía de la interpretación/mayo, §13 fin del SEO orgánico/Condé Nast, "Deja de construir para humanos"/Karpathy marzo, Sección 3 conceptos 2 y 8 con aplicación a alumnos Mariana/Mario). La separación correcta quedó establecida: **ai-radar = la tendencia; estrategia-freemium = la aplicación a Storm Studios.** Cross-link recíproco añadido entre ambos (ai-radar §13 ↔ freemium §5). Sin duplicación.

**Recomendación registrada (§5 "AEO en modo faro"):** sí pero casi gratis y sin robar tiempo a grabar. Razones: (1) el activo caro ya existe (KB en Markdown); (2) la lógica de faro lo amplifica — el alumno ideal 1/1000 es justo quien pregunta a su IA; (3) coherente con el legado (método legible por agentes sobrevive a Luis). Prioridad #1 (grabar) no se mueve. El 20% que rinde: una página pública canónica + nombres literales + dejar que el KB la alimente. NO hacer schema markup elaborado todavía. Punto de fondo: el mejor AEO de Luis es ser genuinamente único (unicidad = descubribilidad). Aprobada por Luis como recomendación.

**Resultado:** AEO sale de preguntas abiertas (§10); quedan 2 menores. 

**Archivos modificados:** estrategia-freemium-musical.md (§5 + §10 + historial), ai-radar.md (§13 cross-link), CLAUDE.md, log.md.

---

## [2026-06-03] entrevista | Cursos avanzados — precios, modalidad y la prueba viviente del músico-atleta

**Archivos:** `08-sintesis/estrategia-freemium-musical.md` (nueva §8), `08-sintesis/el-musico-como-atleta.md` (Premisa central), `00-contexto/vision-proyecto.md` (Fuentes de Ingreso + cursos avanzados).

**Pregunta:** los tres cursos avanzados (público, orden, precio, modalidad) — de las preguntas abiertas de la síntesis freemium.

**Conocimiento capturado:**
- **Todos los cursos avanzados ya existen y Luis ya los ha impartido.** Lo escaso no es el producto — es el alumno. Realidad actual: **~1 alumno cada 3 años** completa hasta Film Scoring. (Corrige vision-proyecto, que los marcaba como "Futuro".)
- **Oferta completa:** Contrapunto, Análisis, Film Scoring, **+ Taller de Ingeniería de Audio y Producción Musical** (no estaba documentado en el KB — ligado al estudio 5.1) **+ formación física** (Luis tiene gym propio, integrada al intensivo).
- **Cliente:** "tiene lana, porque es caro" + **"vocación de hierro"** (estudiar todo Y pagar). "Uno de mil, literalmente" — confirma empíricamente el 1/1000 y el foso de las §2/§4.
- **Modalidad:** Contrapunto y Análisis pueden ser en línea; Film Scoring e Ingeniería de Audio son **presencial-only** (mezcla en 5.1 Genelec). La presencia física es parte esencial.
- **Precio:** intensivo presencial "todo lo extra" = **$20,000 MXN/mes** (3 hrs diarias, incluye formación física); en línea (Contrapunto/Análisis) = **$1,250 MXN/clase**.
- **La prueba viviente:** el último alumno que terminó Film Scoring **también se hizo campeón en Miami en Musclemania Men's Physique.** Mismo alumno, mismo periodo, tope musical + tope físico. → integrado en `el-musico-como-atleta.md`: la tesis pasa de "Luis es la prueba" a "el método es **replicable**".

**Resultado:** §8 nueva en freemium (cursos avanzados); secciones renumeradas (dos líneas 8→9, preguntas 9→10). Quedan ~3 preguntas menores (AEO, orden de lanzamiento, profundizar conversión). Prueba de replicabilidad añadida a el-musico-como-atleta. vision-proyecto corregido y con precios.

**Pendiente que genera:** documentar el **Taller de Ingeniería de Audio y Producción Musical** como curso propio (hoy solo mencionado) — candidato a `01-metodo-pedagogico/estructura-curso.md` o ficha en `03-apps-herramientas`/operaciones.

---

## [2026-06-03] entrevista | Estrategia freemium — YouTube, el faro y el video irreducible

**Archivo:** `08-sintesis/estrategia-freemium-musical.md` (nueva §7).

**Pregunta:** rol de YouTube en el modelo (de las 5 preguntas abiertas de §8 que dejó la reescritura del mismo día).

**Conocimiento capturado:**
- **El video de YouTube ES la lección completa** — pantalla grabada con las mismas herramientas gratuitas (propedéutico + Storm Sequencer). Contiene todo lo necesario para hacer la tarea. No es teaser ni contenido aparte.
- **El video es irreducible:** "no hay resumen posible que lo enseñe, no hay atajos. O ves el video o no entiendes nada." El alumno es cautivo por la naturaleza de lo que se enseña, no por restricción artificial. → Es el principio "no atajos" del método hecho formato, y un **foso involuntario** en la era de la IA: lo valioso es lo que no se deja resumir/parsear.
- **El website es un faro, no un embudo de volumen:** "es para unos pocos", pero esos pocos aprenden armonía tradicional estilo Shostakovich sí o sí. Función primaria = señalar "aquí estoy", no convertir a escala.
- **Regalías de YouTube:** ingreso potencial real si hay flujo importante, pero secundario; el canal es faro, el ingreso es subproducto del alcance.
- **Bilingüe (EN/ES) por diseño** — duplica el alcance, coherente con la escala de legado.
- **El loop que paga el cuello de botella:** grabar es lo más lento e indelegable, pero hoy es "casi un hobby con el que aprendo a usar IA" — skill que YA monetiza vía asesorías de IA cobradas. El tiempo de producción compone hacia la otra línea. Cadencia: ~1 lección/semana (2/semana si se liberan las mañanas).

**Resultado:** §7 nueva; secciones renumeradas (dos líneas 7→8, preguntas abiertas 8→9). Quedan 4 preguntas abiertas (cursos avanzados, AEO, validar 1/1000, precio presencial).

**Archivos modificados:** estrategia-freemium-musical.md (nueva §7 + renumeración + historial), log.md.

---

## [2026-06-03] sintesis | Reescritura de estrategia-freemium-musical (borrador → en_progreso)

**Archivo:** `08-sintesis/estrategia-freemium-musical.md`.

**Origen:** la página llevaba en `borrador` sin crecer desde la sesión 1 (2026-04-16) — señalado en 4 lints. Era un stub que además duplicaba parcialmente `vision-proyecto.md`.

**Decisión editorial (Regla 2 — no duplicar):** `vision-proyecto.md` (completo) ya tiene los *hechos* del modelo (escalera, embudo, la beca, 1/1000). La síntesis no debía repetirlos — se reescribió como **capa de tesis**: *por qué* el modelo es defendible. Una página nivel 2 real, no un resumen.

**7 secciones:**
1. El modelo de negocio ES el método (regalar el método completo es lo que lo hace creíble).
2. La gratuidad como filtro, no como embudo de marketing (la conversión 1/1000 baja es el mecanismo de selección del método, no un bug).
3. La escalera de valor como gradiente de profundidad neural (no de features).
4. El foso defensivo: las 10,000 horas (Gladwell) hacen lo presencial no comoditizable.
5. Las fuerzas macro de IA que protegen el modelo (Jevons cognitiva, "no outsourcear entendimiento", la bifurcación, AEO) — conexión directa con el AI Radar.
6. "La beca" como paciencia compuesta (lente Bogle: largo plazo + horizonte de legado vs. los IPOs forzados de los labs).
7. Las dos líneas (plataforma + asesorías IA) como el mismo motor.

**§8 — agenda de 5 preguntas abiertas para Luis:** YouTube (tipo/frecuencia/rol), los 3 cursos avanzados (público/precio/orden), AEO operativo, validar el 1/1000 con datos reales, lógica de precio presencial.

**Lentes nuevas integradas:** Bogle (Little Book of Common Sense Investing), Gladwell (Outliers), AI Radar (síntesis abr–jun 2026).

**Archivos modificados:** estrategia-freemium-musical.md (reescrito), index.md (estado + descripción + stats: síntesis 7 todas en_progreso), CLAUDE.md (§7 síntesis activa + pendiente convertido en "entrevista pendiente"), log.md.

**Pendiente que genera:** entrevista a Luis para poblar §8.

---

## [2026-06-03] actualización | AI Radar — síntesis de junio 2026 abierta (días 1-2)

**Archivo:** `00-contexto/ai-radar.md` (Sección 2 — Síntesis mensual).

**Fuentes:** `07-fuentes/ainews/202606/` — resumen_20260601.md, resumen_20260602.md, indice_general.md (únicos días disponibles; junio apenas comienza).

**Decisión de método:** la nota de mantenimiento dice sintetizar "al cerrar cada mes". Con solo 2 días, se abre la sección como **"En curso (días 1-2)"** marcada como parcial — aporta valor ahora sin esperar al cierre. Se completará conforme entren los resúmenes.

**Tema central emergente:** la **era de la escasez de tokens** (fin del subsidio de IA). Uber quemó su presupuesto anual en 4 meses, Microsoft canceló Copilot interno, GitHub Copilot terminó su tarifa plana, Anthropic limita el subsidio a Claude Code directo. Goldman proyecta 120 cuatrillones de tokens/mes para 2030. Propuesta: tarifa plana por "empleado cognitivo".

**7 temas + señales + modelos:** Opus 4.8 / inteligencia de orquestación / auto-fork / Dynamic Workflows; "Enforce, don't instruct" (WorkOS/Case — agentes mienten, SHA-256, menos contexto = mejor 77%→97%); calidad de datos 5:1 (Snorkel); paradoja del empleo + Altman/Amodei moderan retórica; encíclica Magnifica Humanitas con confesión de Chris Olah en el Vaticano; crisis de percepción anti-tech (FBI categoría nueva); temporada de IPOs (Anthropic $965B + S-1).

**Ganchos pedagógicos integrados (no solo resumen):**
- Escasez de tokens → costos de clases-ia + criterio de automatización / Efecto Santiago.
- "Menos contexto = mejor resultado" → valida el KB **anti-RAG** (Regla 3: síntesis > acumulación) y la verificación obligatoria del output (coral perfecto agéntico).
- Calidad de datos 5:1 → principio pedagógico de calidad sobre cantidad.
- "Trabajo de medio a medio" → confirma el Sándwich Humano (mayo §9).

**Archivos modificados:** ai-radar.md (sección junio + frontmatter + historial + relacionado_con), CLAUDE.md (pendiente actualizado), log.md.

---

## [2026-06-03] actualización | Cierre del backlog de insights + falso pendiente corregido (Opus 4.8)

**Chequeo general de salud + procesamiento del pendiente #1 (backlog de insights).**

**Hallazgo principal:** el "backlog" de `insights.md` era más pequeño de lo que sugería el conteo crudo (67 viñetas / 10 ✅). Desglose real:
- Bloque 2026-04-09 (~57 viñetas): ya procesado el 2026-06-03 vía banner → `entrenamiento-oido-absoluto.md`. Se conserva como material crudo intencionalmente.
- Bloques 2026-05-01 y 2026-05-27: ya tenían ✅.
- **Único pendiente real:** 4 insights del 2026-04-16.

**Acción:** los 4 insights del 2026-04-16 ya estaban integrados al wiki desde el 2026-04-17 (confirmado por `log.md:561`) pero nunca recibieron su ✅ — hueco de contabilidad, no de contenido. Verificado destino por grep y marcados:
- redes neuronales/música como vehículo → `luis-como-ingeniero-neural.md`, `como-enseno-armonia.md`, `quien-soy.md`
- coral perfecto/mastery-based → `como-enseno-armonia.md`, `modelos-mentales-aprendizaje-musical.md`
- secuenciador vs Cubase → `secuenciador.md`, `como-enseno-armonia.md`
- apps auditivas = corazón → `filosofia-ensenanza.md`

Resultado: **buzón de insights sin pendientes activos.**

**Falso pendiente corregido en CLAUDE.md:** la línea "verificar autor de 3 libros (Amino Acid, Philosophy, Civilización Artificial)" se arrastraba desde lints previos, pero los 3 ya tienen autor asignado en `indice-fuentes.md` desde el 2026-05-21 (Wolfe, Cave, Lassalle). Reemplazada por el único marcador realmente abierto: `[verificar canal]` de "A Little Bit of Philosophy — PHI 101".

**Archivos modificados:** insights.md, CLAUDE.md, log.md.

---

## [2026-06-03] sintesis | Nueva página nivel 2 — El entrenamiento del oído absoluto

**Archivo creado:** `08-sintesis/entrenamiento-oido-absoluto.md`

**Origen:** procesamiento del backlog de ~40 insights `[oído]`/`[método]` del 2026-04-09 en `insights.md`, que llevaban más de un año sin archivo destino. Material original y denso de Luis sobre teoría del oído — el candidato más fuerte a síntesis identificado en el lint del mismo día.

**Estructura (12 secciones):**
1. Por qué existe la página (el AP como caso límite de la tesis "ingeniero neural").
2. Tesis central: el AP no es don, es corteza selectiva aislable; "unlocking is the way".
3. AP como imagen mental (analogía del teléfono / propiocepción del tono); el relativo contamina al absoluto; gramática posicional ("ahí es do").
4. La matriz movible: absoluto / grado / intervalo / acorde como libre selección sobre cualquier nota.
5. Método: desintegrar → entrenar por separado → reintegrar; criterio "una sola respuesta correcta alcanzable solo con la corteza correcta".
6. Automaticidad: el intelecto echa a perder el AP (S1 puro, link Kahneman); el punto de inflexión del desbloqueo.
7. Hipótesis del sample rate: velocidad/ritmo como resolución temporal, no mielina; frecuencia + tiempo como únicos ejes.
8. El oído como lenguaje (centros de lenguaje vs. mecánicos).
9. Condiciones físicas: calentamiento del oído, contaminación de la señal, esfuerzo invisible.
10. Mapa de las 8 apps a cada capa de percepción + ejercicios crudos derivados de insights.
11. Respaldo neurocientífico (enlazado a modelos-mentales, no repetido): Levitin, Barrett, Agüera y Arcas.
12. Preguntas abiertas (agenda de investigación de Luis): cómo lo hacen los prodigios, grados-color, sample rate, medir el desbloqueo, la gramática del método.

**Decisión editorial:** las preguntas que Luis dejó abiertas en los insights NO se resolvieron inventando — se preservaron como §12. La página enlaza la neurociencia ya documentada en lugar de duplicarla.

**Archivos modificados:** entrenamiento-oido-absoluto.md (nuevo), insights.md (backlog marcado procesado), index.md (síntesis 6→7), CLAUDE.md (síntesis activa + pendiente actualizado), log.md, CHANGELOG.md.

---

## [2026-06-03] lint | Revisión de salud + sincronización de estados (Opus 4.8)

**Inconsistencias detectadas y corregidas:**
1. ✅ Archivos de control clavados en 2026-05-29 pese al trabajo del 01-02 jun → `CLAUDE.md` §7, `index.md` y `CHANGELOG.md` sincronizados a 2026-06-03.
2. ✅ Pendiente fantasma en `CLAUDE.md`: "Ingestar 3 videos al wiki" seguía listado pese a que el commit 77b8b48 (06-01) ya los ingirió → eliminado; sesión 06-01 registrada en "Fuentes ingresadas".
3. ✅ Contradicción de estados: `index.md` marcaba como `borrador` a el-musico-como-atleta, modelos-mentales y como-enseno-armonia, pero sus frontmatter dicen `en_progreso` → columna Estado de la sección 08 corregida.
4. ✅ `06-diario-proyecto/2026-05.md` existía pero no estaba en `index.md` → agregado.
5. ✅ Video "This Could Save Your Life" figuraba como "(por clasificar)" → reclasificado como ingerido (longevidad sistémica → el-musico-como-atleta sección 8).
6. ✅ **Duplicación de contenido:** `Los_Seres_Musicales.md` en la raíz era copia byte a byte (533 KB) de `07-fuentes/libros/Los_Seres_Musicales.md` → eliminado de la raíz (`git rm`).
7. ✅ Estadísticas de `index.md` actualizadas (síntesis 5 en_progreso + 1 borrador; última sesión 2026-06-03).

**Pendientes señalados (requieren a Luis o sesión dedicada):**
- ⚠️ Síntesis nueva candidata: "El entrenamiento del oído absoluto" — el backlog de ~40 insights de [oído] del 2026-04-09 en `insights.md` no tiene archivo destino. Material original denso de Luis; ideal para nivel 2.
- ℹ️ Decisión de fondo (3er lint que lo señala): consolidar `CLAUDE.md` y `AGENTS.md` en una fuente única.
- ⚠️ 3 libros con `[verificar autor]` en `indice-fuentes.md` (Amino Acid, Philosophy Beginner's Guide, Civilización Artificial).
- ⚠️ `estrategia-freemium-musical.md` sigue en borrador sin crecer desde 2026-04-16.

**Referencias cruzadas:** verificadas, sin enlaces rotos.

**Archivos modificados:** CLAUDE.md, index.md, CHANGELOG.md, log.md; eliminado Los_Seres_Musicales.md (raíz).

---

## [2026-06-01] entrevista | Storm Sequencer — modos, cifrado activo, arquitectura pedagógica

**Archivos actualizados:**
- `02-plataforma-web/secuenciador.md`: 4 nuevas secciones — modos Melodía Simple / Cuarteto SATB, el cifrado como ejercicio activo (no análisis automático), arquitectura del propedéutico (4 lecciones), momento "wow" del alumno nuevo.
- `08-sintesis/tecnologia-al-servicio-del-metodo.md`: sección [Pendiente] del Storm Sequencer completada — modelo de simultaneidad (teoría + escritura al mismo tiempo), acción doble del cifrado (nota + función armónica), arquitectura de dos modos con destino explícito.

**Conocimiento capturado:**
- El Cuarteto SATB es el **destino final del curso completo** (~60 lecciones). No es una función avanzada — es el horizonte hacia el que apunta todo el método desde la lección 1.
- El cifrado es ejercicio activo del alumno: escribe la nota Y el numeral romano. La herramienta no genera el análisis — el alumno lo articula.
- Luis modela en video: teoría y escritura simultáneas, no secuenciales. La regla se vuelve audible mientras se explica.
- El propedéutico tiene 4 lecciones dentro del mismo website antes de iniciar el curso principal.

---

## [2026-06-01] ingest | 3 videos ingresados al wiki — El problema aguas arriba, ExO 3.0, Longevidad sistémica

**Videos ingresados:**
1. "The Real Problem With AI Agents Nobody's Talking About" → `modulo_agentes.md` (nueva sección "El problema aguas arriba"), `conceptos_no_olvidar.md` (sección 18 + concepto transversal), `tecnologia-al-servicio-del-metodo.md` (mención en sección IA).
2. "Singularidad Organizacional — ExO 3.0" (Diamandis + Ismail) → `tecnologia-al-servicio-del-metodo.md` (nueva sección completa: Coase reformulado, stack 6 capas, 5 fosos defensivos, pasaporte del agente). Moonshots raw transcript no requiere ingesta separada — cubierto por el destilado.
3. "This Could Save Your Life" (Dr. William Lee) → `el-musico-como-atleta.md` (sección 8: longevidad sistémica — 5 prácticas con traducción directa al músico). Dimensión "Longevidad sistémica" añadida a la tabla del sistema en sección 6.

**Archivos modificados:** modulo_agentes.md, conceptos_no_olvidar.md, tecnologia-al-servicio-del-metodo.md, el-musico-como-atleta.md, indice-fuentes.md, log.md

**Conocimiento capturado:**
- El problema aguas arriba: instalar un agente ≠ saber usarlo. El cuello de botella real es la claridad de intención upstream, no la potencia del modelo. OS del agente: soul.md + identity.md + user.md + heartbeat.md.
- ExO 3.0 conecta directamente con la arquitectura del KB: el stack de 6 capas (Propósito→Sentir→Interpretar→Decidir→Orquestar→Aprender) describe exactamente lo que CLAUDE.md + síntesis + agentes implementan. Los 5 fosos defensivos identifican datos propietarios + marca personal como los activos más profundos de Storm Studios.
- Longevidad sistémica: el músico de alto rendimiento que no cuida la longevidad optimiza para el presente a costa del futuro. Sueño oncológico = consolidación de memoria motora (el sistema consolida durante el sueño profundo, no durante la práctica).

---

## [2026-05-29] actualización | Pendientes del lint resueltos — escritura activa (Opus 4.8)

**Acciones (resolución de pendientes detectados en el lint):**
- `08-sintesis/tecnologia-al-servicio-del-metodo.md`: integrado el insight del criterio de automatización (2026-05-27) en la sección "La IA en el flujo de trabajo de Luis", vinculado al Efecto Santiago y a la mielinización S2→S1. Frontmatter actualizado.
- `00-contexto/insights.md`: insight "criterio de automatización con IA" marcado ✅ (ya integrado).
- `08-sintesis/luis-como-ingeniero-neural.md`: el archivo ya estaba sólido; se agregó la nueva sección "La prueba empírica: el framework aplica a no-músicos" con tabla método-musical↔clases-IA y casos reales (Mario, Bruno, Karla, Esteban).
- `AGENTS.md`: sincronizado con CLAUDE.md (alumnos 8→10, videos 1→4, notas de síntesis actualizadas) para frenar la divergencia detectada en el lint.

**Conocimiento capturado:**
- El criterio de automatización es el Efecto Santiago aplicado a la IA: la inversión inicial en dominar la herramienta siempre paga; el umbral de decisión es "tiempo de verificación < tiempo de hacerlo manual".
- La tesis "Luis es ingeniero neural, no maestro de música" queda respaldada empíricamente: el mismo framework produce la misma estructura pedagógica al enseñar IA a no-músicos (Mario, Karla, Esteban).

**Pendiente que sigue requiriendo a Luis / sesión dedicada:**
- Ingerir al wiki los 3 videos (Diamandis/Ismail, ExO 3.0, This Could Save Your Life) — transcripts grandes, merecen sesión propia.
- Verificar canal/autor de videos marcados [verificar canal].
- Validar las conexiones por alumno en luis-como-ingeniero-neural.md con datos de sesiones reales.
- Decisión de fondo: consolidar CLAUDE.md y AGENTS.md en una fuente única (hoy se sincronizan a mano).

**Archivos modificados:** tecnologia-al-servicio-del-metodo.md, luis-como-ingeniero-neural.md, insights.md, CLAUDE.md, AGENTS.md, log.md

---

## [2026-05-29] lint | Revisión completa de salud del KB (Opus 4.8)

**Inconsistencias detectadas y corregidas:**
1. ✅ `index.md` — alumnos "7" → **10** reales (faltaban julio, montse, esteban); videos "1" → **4**; última sesión 2026-05-26 → 2026-05-29.
2. ✅ `index.md` — sección Videos solo listaba 1 de 4. Agregados This Could Save Your Life, Diamandis/Ismail, ExO 3.0.
3. ✅ `indice-fuentes.md` — agregados 3 videos (Diamandis/Ismail, ExO 3.0, This Could Save Your Life) a la tabla; fecha frontmatter 2026-05-06→2026-05-29.
4. ✅ `CLAUDE.md` sección 7 — alumnos clases-ia 8→10 (faltaban Karla, Montse); videos 1→4. (El resto de la sección ya había sido actualizado a 2026-05-29 por la sesión previa.)
5. ℹ️ `.gitignore` — verificado: `.claude/` ya estaba ignorado (correcto; el harness crea worktrees ahí dentro del repo).

**Pendientes señalados (requieren a Luis o trabajo de ingesta):**
- ⚠️ 3 videos nuevos están como transcripts crudos pero no ingeridos al wiki (síntesis pendiente).
- ⚠️ 3 libros con "(verificar autor)" en indice-fuentes: L14 Amino Acid, L17 Philosophy A Beginner's Guide, L22 Civilización Artificial.
- ⚠️ Insight 2026-05-27 "criterio de automatización" sigue sin integrar a `tecnologia-al-servicio-del-metodo.md`.
- ⚠️ `luis-como-ingeniero-neural.md` sigue marcada en_progreso/borrador pese a su importancia central.
- ℹ️ Decisión de criterio: CLAUDE.md vs AGENTS.md conviven con riesgo de divergencia. Conviene definir uno como fuente única.

**Archivos modificados:** index.md, indice-fuentes.md, CLAUDE.md, .gitignore, log.md

---

## [2026-05-29] actualización | Síntesis mayo 27-28 integrada al KB — Opus 4.8, Sándwich Humano, métricas agénticas

**Acciones:**
- `ai-radar.md`: síntesis mayo extendida a días 27-28. Nuevas secciones 8-11: Opus 4.8 + Dynamic Workflows, El Sándwich Humano + Paradoja de Jevons Cognitiva, métricas agénticas (Nate Jones), señales días 27-28 (Glasswing, comprensión 67%, DeepSeek V4 precio corregido, RALPH Loop). Modelos: Opus 4.8 agregado, Mythos jerarquía confirmada. Sección 3: tabla actualizada (4.7→4.8), concepto 6 (Sándwich Humano) con aplicación por alumno, resumen ejecutivo ampliado.
- `conceptos_no_olvidar.md`: tabla de modelos actualizada (Opus 4.7 → Opus 4.8). Sección 17 (El Sándwich Humano) creada. Concepto transversal agregado.
- `08-sintesis/luis-como-ingeniero-neural.md`: nueva sección "Luis en la era agéntica — el Sándwich Humano como método". Conexión con Jevons Cognitiva y Dynamic Workflows.
- Pull del commit de laptop: `plan_clase_01.docx` de Esteban (33), resumen ainews 20260528 (completo y básico), índice_general actualizado.
- Push previo de 2 commits pendientes: transcripts EXO 3.0 y Diamandis/Ismail.

**Conocimiento capturado:**
- El Sándwich Humano (Wes Roth / Dan Shipper): arquitectura de colaboración humano-IA donde el dominio profundo del humano es el encuadre inicial y el juicio final. La ejecución se delega — el criterio no.
- Paradoja de Jevons Cognitiva: cuando la ejecución se abarata, el volumen total de trabajo explota y el cuello de botella migra al juicio. El conocimiento de dominio de Luis se vuelve más valioso, no menos.
- Opus 4.8: mismo precio, fast mode 2x (era 6x), Dynamic Workflows con cientos de subagentes en paralelo, honestidad 4x mejorada.
- Mythos jerarquía confirmada: haiku→sonnet→opus→mythos. Llega en semanas.
- La comprehensión de código (no la generación) es el 67% del uso real de IA en ingeniería — dato aplicable al argumento de que la IA no reemplaza sino transforma.

---

## [2026-05-27] sesion | Curriculum clases-ia completado + ai-radar tres meses + modo Q&A pedagógico

**Acciones:**
- Commit y push del perfil de Karla (pendiente de sesión anterior).
- Reestructura completa de `02_curriculum/` (Opción B): creada `leccion_06_flujo_chat_md_agente.md`, reescritos `modulo_chats_ia.md`, `modulo_agentes.md`, `modulo_codex.md` con evidencia real; 9 módulos pendientes convertidos a stubs honestos con PENDIENTE header.
- Creado `00_instrucciones/conceptos_no_olvidar.md` — referencia de instructor con 15 temas y señales de avance.
- `ai-radar.md` actualizado completamente: síntesis marzo (nuevo, 6 temas), abril (expandido de tabla a síntesis narrativa completa, 9 temas), mayo 1-17 (existente), mayo 18-26 (nuevo: Google IO, Gemini 3.5 Flash/Omni/Spark, alineamiento, Erdős, AEO), nueva Sección 3 (filtro pedagógico mensual con acciones por alumno).
- Tabla de modelos actualizada: Gemini 3.1 Pro → 3.5 Flash en 3 archivos.
- Corrección: Carmen es productora de cine y comerciales, no musical.

**Conocimiento capturado:**
- AEO (Agent Experience Optimization): concepto nuevo no cubierto en curriculum. La presencia digital ahora tiene dos audiencias — humanos y agentes. El sitio web de Mario, la bio de Mariana, el catálogo de Carmen deben ser legibles para agentes, no solo para ojos humanos.
- El flujo pedagógico Q&A funciona: Luis pregunta un concepto → KB responde con aplicación por perfil de alumno + señal de avance.

**Pendientes:**
- Continuación del modo Q&A pedagógico (Luis preguntará más conceptos en futuras sesiones).
- Workflow mensual ai-radar confirmado: Luis actualiza ainews diario, síntesis se genera al cierre del mes.

---

## [2026-05-26] entrevista | Progresión del estudiante — experiencia inicial

**Acciones:**
- Iniciada la población de `01-metodo-pedagogico/progresion-estudiante.md`.
- Capturado el recorrido ideal desde la llegada al website hasta la entrada al curso de armonía.

**Conocimiento capturado:**
- La experiencia debe comunicar que el alumno está frente a un curso profesional, no un producto motivacional de resultados rápidos.
- El website debe filtrar naturalmente: quien busca atajos se va; quien reconoce el valor descubre herramientas que serían imposibles de pagar o encontrar en una escuela tradicional.
- El video de introducción ayuda al alumno a diagnosticar si ya puede empezar armonía o si debe cursar el propedéutico.
- El propedéutico prepara al alumno con notas, ritmo, intervalos y uso del Storm Sequencer.
- Las herramientas están integradas al ecosistema: videos, apps, juegos web gratuitos, apps Android gratuitas y versiones iPhone de pago.

---

## [2026-05-26] actualización | Elefantito Matemático documentado como herramienta cognitiva

**Acciones:**
- Llenado `03-apps-herramientas/elefantito-matematico.md`, que seguía en borrador con placeholders.
- Expandida la sección de Elefantito en `08-sintesis/tecnologia-al-servicio-del-metodo.md`.
- Actualizado `index.md` para registrar `AGENTS.md` como schema maestro, reflejar estados y última sesión.
- Actualizados `AGENTS.md` y `CLAUDE.md` para remover el pendiente viejo de `filosofia-ensenanza.md` y registrar los pendientes nuevos.
- Actualizado `CHANGELOG.md`.

**Conocimiento capturado:**
- Elefantito Matemático no es una app lateral del catálogo: es preparación neural para el método.
- Su función pedagógica es entrenar el cuello de botella prefrontal: atención, memoria de trabajo, inhibición de respuesta automática e intención consciente.
- El módulo de memoria se entiende como complemento del principio "Memoria es primero y es todo": la memoria es la plantilla que permite que el cuerpo ejecute correctamente.

**Pendientes nuevos/verificados:**
- Pendiente original refinado tras revisar el repo actual: confirmar si el HTML legacy de 8 niveles sigue enlazado y si las técnicas avanzadas de Arthur Benjamin siguen planeadas para niveles futuros.
- Verificado después en la misma sesión: la app Memoria aparece como app separada en el catálogo, no como módulo interno de Elefantito.

---

## [2026-05-26] actualización | Elefantito Matemático corregido desde el repo actual del website

**Acciones:**
- Revisado `C:\Users\Luis\Documents\claude_code\nuevo-website\storm-studios`.
- Identificada la versión actual Next.js de Elefantito en `components/apps/elefantito-nextjs/` y la ruta `app/[locale]/apps/matematicas-mentales/jugar/page.tsx`.
- Corregido `03-apps-herramientas/elefantito-matematico.md` para reflejar la app real: 6 niveles desbloqueables, tutor bilingüe, audio narrado, progreso en `localStorage`, mecánica de 20 barriles, música y efectos en Cloudflare R2.
- Actualizado `03-apps-herramientas/indice-apps.md`.
- Corregido `01-metodo-pedagogico/filosofia-ensenanza.md` para distinguir versión Next.js vigente (6 niveles) vs. HTML legacy (8 niveles).
- Corregido el insight procesado de Elefantito en `00-contexto/insights.md` para no dejar el dato de 8 niveles como estado actual.
- Ajustada la síntesis `08-sintesis/tecnologia-al-servicio-del-metodo.md` con la nueva capa pedagógica del tutor.

**Conocimiento capturado:**
- Hay una implementación legacy en `public/apps/elefantito.html` con selector de 8 niveles y récord diario local.
- La versión vigente integrada al website parece ser la Next.js de 6 niveles.
- La app Memoria aparece como herramienta separada en el catálogo, no como módulo interno de Elefantito.

**Pendientes nuevos/verificados:**
- Confirmar si el HTML legacy sigue enlazado o puede archivarse.
- Revisar si la ficha pública del catálogo debe corregirse de "8 niveles" a "6 niveles".
- Verificar si las técnicas avanzadas de Arthur Benjamin siguen planeadas para niveles futuros.

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
