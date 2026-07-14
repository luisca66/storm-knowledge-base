---
titulo: "Registro de Cambios"
tipo: diario
ultima_actualizacion: 2026-07-13
estado: en_progreso
---

# Registro de Cambios (CHANGELOG)

## 2026-07-13 — Corpus de Migración Empresas y frontera operativa
- **15 fuentes operativas consolidadas** en `D:\codex\migracion-empresas\00-fuente\videos\`: los 14 videos seleccionados por Luis y Moonshots, con catálogo crítico. El KB conserva solo el registro y los aprendizajes, no copias crudas.
- **Frontera canónica aclarada por Luis:** el KB solo registra contexto. El repo principal `D:\codex\migracion-empresas` mantiene metodología y expedientes; el proyecto operativo real de Voces es `D:\codex\migracion-empresas\voces-imaginarias`, mientras `03-clientes/voces-imaginarias/` es el expediente del asesor.
- **Referencias reparadas:** índice global, índice de fuentes y síntesis apuntan a la ficha del corpus. El schema fija que las fuentes específicas de un proyecto viven en su repo operativo; lint final sano.
- **Método operativo actualizado en su repo propio:** fricción antes que herramientas, agentes por flujo y no por organigrama, backcasting desde capacidades, MTP separado de permisos, datos gobernados/portables, adopción por utilidad y retiro explícito del flujo anterior.

## 2026-07-09 — Mapa contextual de proyectos creado
- **Mapa contextual de 29 proyectos/contextos:** creado `05-operaciones/mapa-contextual-proyectos.md` a partir de entrevista con Luis. Confirma qué está vivo, pausado, terminado o pendiente dentro del ecosistema: website, curso, Maestro Virtual, Sequencer, apps, juegos, libros, clases, clases IA, Migración Empresas, discografía, ainews y el KB mismo.
- **Reconciliaciones importantes:** Intervalos - Cantados completo ya integrado como webapp; propedéutico terminado, lecciones 1-3 terminadas y Lección 4 en producción; apps móviles esperan suscripciones developer y port iPhone; manuales de apps pasan de Kindle al website; Maestro Virtual listo aprox. hasta Lección 6 y con futuro como codificación del método para IAs futuras; juegos Godot en espera de GPU/presupuesto; Migración Empresas vivo con Voces Imaginarias como cliente activo.
- **Precisión estratégica sobre las clases:** el website se confirma como faro/promotor de Luis para cachar al alumno uno-entre-mil que quiera estudiar el curso completo y volverse músico profesional. Los cursos avanzados son caros por diseño; Luis no persigue ese alumno, lo espera.
- **Archivos actualizados:** `vision-proyecto.md`, `funcionalidades.md`, `maestro-virtual.md`, `indice-apps.md`, `godot-juegos.md`, `stack-tecnologico.md`, `09-migracion-empresas/`, `discografia-ia.md`, `index.md`, `CLAUDE.md`.

## 2026-07-08 — Julio abierto en el radar + ingesta de Originals (Grant)
- **Reencuadre del propósito del KB:** Luis aclara que el KB no existe para que la IA futura opere los proyectos desde aquí. Cada proyecto vive y se trabaja en su propio repo/contexto; el KB registra historia, desarrollos, decisiones y conexiones para que la IA pueda dar mejores ideas, corregir contradicciones y ayudar a planear estrategias. `CLAUDE.md` y `flujo-trabajo.md` ajustados de "autonomía operativa" a "memoria estratégica / mapa contextual".
- **`ai-radar.md`: julio abierto (días 1-7).** Cierre de la trilogía de junio — Fable 5 regresa (1 jul) junto a **Claude Sonnet 5**; el 7 de julio Fable sale de Claude Max y se confirma la cronología del veto (3 semanas offline, Tom Brown en vez de Amodei). Temas nuevos: impuesto de ciberseguridad, caso Figma/Palantir, "planifica caro, ejecuta barato" (68% de ahorro), permiso político como foso. Tabla de modelos de la Sección 3 revalidada al 7 de julio; **propagación a clases-ia pendiente deliberadamente**.
- **Ingesta de *Originals* (Adam Grant):** nuevo **Principio 8** en `filosofia-ensenanza.md` (disciplina por razonamiento, elogio de carácter) — cierra el paralelo que el radar señaló en mayo con el alineamiento de Claude ("las reglas no escalan, los principios sí"), ahora con evidencia independiente de psicología del desarrollo. Matiz de mentores en `como-enseno-armonia.md`; cross-ref en `luis-como-ingeniero-neural.md`. Catálogo de libros: 23/27 ingresados.
- 2 insights (cultura fuerte vs. culto, niche picking) quedan sin integrar en `insights.md` — candidatos futuros para Migración Empresas / método. Reconciliación posterior: ya fueron revisados con Luis el mismo día; se conservan como referencia, sin necesidad activa hoy.

## 2026-07-03 (3ª sesión — ejecución del plan de mejoras, Opus)
- **Workflow "Cierre de Mes" institucionalizado** en `CLAUDE.md` §5: el ritual mensual (radar + diario + lint + reconciliación + respaldo) deja de vivir solo en el log y pasa a ser un workflow con nombre.
- **Lint reproducible:** `herramientas/lint_kb.py` versionado en el repo — verifica referencias, enlaces y frontmatter automáticamente ("enforce, don't instruct"). El workflow de Lint lo lista como primer paso. Registrado en `index.md`.
- **Log de ainews adelgazado (hacia adelante):** convención de 1 línea por ingesta diaria documentada en `log.md` y `ritmos-y-decisiones.md` (regla de fuente única). Histórico intacto.
- **Recordatorio automático:** tarea programada local `cierre-de-mes-kb` (día 1 de cada mes, 9:00) que dispara el workflow.
- **Tarea 5 — `04-contenido-musical/` desatorado** (entrevista con Luis): audio en Cloudflare + video en YouTube (migración vieja cerrada); no hay biblioteca MIDI (formato de paso); `repertorio.md` → **`discografia-ia.md`** (plan a futuro: canciones de Luis con IA como discos, independiente del método). 3 archivos pasan a `completo`; `infraestructura.md` registra Cloudflare/YouTube. **Plan de mejoras 5/5 ejecutado.**

## 2026-07-03 (2ª sesión — actualización de Luis)
- **Contradicción de distribución de apps resuelta:** sin descarga directa de APKs; webapps gratuitas en el website + móviles de paga en Play Store/App Store. **11 webapps ya publicadas** — se documenta **Cantar Acordes** (faltaba en el catálogo). Intervalos – Cantados: 4/12 niveles en vivo, versión completa lista para migrar.
- **Decisión nueva:** los libros (Los Seres Musicales y siguientes) serán **obras de consulta — legado y reputación, no ingreso** — decisión tomada con la señal del −57% sobre la mesa. Documentada en `decisiones-clave.md`, reflejada en `vision-proyecto.md` y anotada junto a la señal en `ai-radar.md` §30.
- **Precio de clases capturado:** $1,500 MXN/sesión (dato inicial en la tabla de ingresos; entrevista completa de la vaca lechera sigue pendiente).

## 2026-07-03
- **Primera sesión con Fable 5 — lint general del KB.** 165 referencias `relacionado_con` y 119 enlaces markdown verificados; únicas roturas: 4 enlaces `file:///` con ruta de la máquina anterior en `log.md`, corregidos a rutas relativas. Frontmatter e insights sin pendientes (buzón limpio).
- **`ai-radar.md`: junio cerrado (días 13-29).** Arco central: el veto de exportación a Fable/Mythos 5 y el régimen de licencias de facto (carta de Lutnick). Nuevas secciones 23-30 + señales + modelos + frases; encabezado del mes: "El mes del interruptor de apagado" (trilogía economía→capacidad→gobernanza). Sección 3: 2 conceptos pedagógicos nuevos (soberanía del contexto, riesgo político de stack) y nota de cierre sobre suspensión/regreso de Fable + Sonnet 5. La propagación de la tabla de modelos a clases-ia se pospone deliberadamente a la apertura del radar de julio.
- **Diario de junio creado** (`06-diario-proyecto/2026-06.md`, completo): reconstrucción del mes más denso del KB desde log/CHANGELOG, con balance de métricas.
- **Respaldo del KB inaugurado:** rutina mensual de `git bundle` documentada en `05-operaciones/infraestructura.md` y primer bundle generado en `Documents`. Pendiente de Luis: copiarlo a Drive/disco externo.
- **Pendiente resuelto:** canal de "A Little Bit of Philosophy — PHI 101" verificado — Barry F. Vaughan, Mesa Community College (`indice-fuentes.md` actualizado).
- `index.md`: estadísticas recalculadas (364 archivos, ainews extendido a julio); `CLAUDE.md` §7 actualizado.

## 2026-06-12
- **Autonomía operativa definida:** `05-operaciones/flujo-trabajo.md` distingue orientación, ejecución, verificación, recuperación y aprendizaje. Diagnóstico actual: continuidad intelectual fuerte, pero ejecución parcial y verificación/recuperación débiles. Orden acordado: inventario operativo → circuito Lección 1/Maestro Virtual → respaldo/rollback → piloto P03 → automatización diaria.
- **Lint de salud Codex:** 346 archivos Markdown; 147 referencias `relacionado_con` y 116 enlaces relativos verificados sin roturas. Reconciliados estados de curso/Maestro Virtual, cartera de Migración Empresas, distribución de apps, metadatos e índice. Documentada la excepción heredada de frontmatter en `clases-ia`.
- **`ai-radar.md` puesto al día (iba 9 días atrás).** Síntesis de junio extendida de "días 1-2" a "días 1-12" con el lanzamiento de **Claude Fable 5 / Mythos 5 (9 jun)** como evento central — antes ausente del wiki. Integradas las tres controversias (clasificadores agresivos, degradación silenciosa revertida en <24h, retención de 30 días), la crisis de costos concreta (Uber, alfabetización de modelos), la temporada de IPOs, Microsoft Build (eval privado), Apple WWDC y el playbook AEO local de Caleb Ulku.
- **Sección 3 (clases) actualizada:** tabla de modelos con Fable 5 como tope de capacidad pero Opus 4.8 como daily driver real (matiz honesto: 2x tokens, sale de suscripción el 22-23 jun, falsos positivos). Tres conceptos pedagógicos nuevos: imaginación de tareas, alfabetización de modelos (auditoría de tokens como servicio para PYMES), y playbook AEO local para Mario y el website.
- Pendiente derivado: propagar la tabla de modelos a `conceptos_no_olvidar.md` y `leccion_01` dentro de clases-ia (requiere leer `INSTRUCCIONES_CLASES_IA.md`).

## 2026-06-11
- **Entrevista de propósito:** mapa del ecosistema corregido — Storm Studios es el estudio físico; las clases particulares (composición, instrumentos, entrenamientos físicos, IA) son la vaca lechera; SSL es el website ($0 hoy por diseño: legado + promotor + futuro pasivo). Documentadas "La prueba de la vacación" y la escena objetivo del "martes cualquiera" (~70% ya existe) en vision-proyecto.
- **Decisión nueva:** apps web gratis + móviles de paga (Android/iOS) — la escalera de valor gana un peldaño; supersede la decisión Play Store del 05-22; piloto P03 acordado. Documentada también la postura "sin límites a priori a la autonomía de la IA".
- quien-soy: nueva subsección "El vibe coding como estudio diario" (No-Compartimentación aplicada a Luis mismo). stack-tecnologico: iOS en desarrollo, contradicción de apps publicadas señalada.
- **Consolidación del schema (decisión de fondo resuelta):** `CLAUDE.md` es la única fuente de verdad, redactado agnóstico de agente; `AGENTS.md` reducido a stub de redirección. Se acaba la sincronización manual señalada por 5 lints — con divergencia real ya confirmada entre las copias.
- `CLAUDE.md` §2 reescrito: propósito en dos niveles (continuidad hoy / autonomía mañana), alcance explícito de las tres líneas de negocio, jerarquía de archivos de entrada.
- `CLAUDE.md` §7 adelgazado: el detalle del estado vive en index/log/CHANGELOG; solo quedan fecha y pendientes prioritarios.
- `README.md` redefinido como portada del repo privado (estado: completo); `index.md` corrige la jerarquía invertida de archivos de sistema.
- Decisión documentada en `00-contexto/decisiones-clave.md` (borrador → en_progreso).

## 2026-06-10
- Creada `09-migracion-empresas/` como fuente canónica para la nueva línea empresarial de Luis, ya activa y con ingresos.
- Creado el índice de proyectos con Voces Imaginarias como primer caso confirmado y repo propio.
- Corregida la frontera con `clases-ia`: ahí solo se documenta el aprendizaje del equipo; la operación empresarial vive en Migración Empresas y en cada repo.
- Actualizados schema, índice, README, visión del proyecto, biografía y asesorías de IA.

## 2026-06-04
- **Lint de salud Codex:** `AGENTS.md` sincronizado con el estado real del 2026-06-03 y `CLAUDE.md`; convención de frontmatter ampliada para permitir `spec` y `sintesis`, tipos ya usados por el KB.
- `index.md` corregido: archivos de `02-plataforma-web/` pasan de `borrador` a `en_progreso`, Elefantito pasa a `completo`, estadísticas recalculadas sin sistema/clases-ia.
- `03-apps-herramientas/indice-apps.md` corregido: Elefantito Matemático actualizado de 6 a 20 niveles desbloqueables.
- Chequeo de referencias cruzadas: sin roturas reales detectadas fuera de ejemplos/templates.

## 2026-06-03
- **Síntesis nueva (nivel 2):** creada `08-sintesis/entrenamiento-oido-absoluto.md` a partir del backlog de ~40 insights de oído del 2026-04-09. Teoría operativa del oído absoluto: corteza selectiva, imagen mental, matriz de las 4 percepciones, automaticidad (Kahneman), hipótesis del sample rate, mapa a las 8 apps y agenda de preguntas abiertas. Backlog marcado como procesado en `insights.md`. Páginas de síntesis: 6 → 7.
- **Lint de salud del KB** (Opus 4.8): sincronización general de archivos de control que habían quedado clavados en 2026-05-29 pese al trabajo del 01-02 de junio.
- `CLAUDE.md` §7 actualizada a 2026-06-03: ingesta de 3 videos confirmada (pendiente fantasma eliminado), sesión 06-01 registrada, pendientes reordenados (síntesis del oído absoluto y decisión CLAUDE/AGENTS promovidas).
- `index.md`: estados de síntesis corregidos (el-musico-como-atleta, modelos-mentales, como-enseno-armonia: borrador → en_progreso, alineados con sus frontmatter); diario `2026-05.md` agregado al catálogo; video "This Could Save Your Life" reclasificado como ingerido; estadísticas y fecha actualizadas.
- **Duplicado eliminado:** `Los_Seres_Musicales.md` de la raíz (copia byte a byte de `07-fuentes/libros/Los_Seres_Musicales.md`) — violaba la regla de no duplicar contenido.
- `CHANGELOG.md` actualizado con las entradas faltantes de 05-29, 06-01 y 06-02.

## 2026-06-01
- **Entrevista — Storm Sequencer:** `02-plataforma-web/secuenciador.md` ampliado con 4 secciones (modos Melodía Simple / Cuarteto SATB, el cifrado como ejercicio activo, arquitectura del propedéutico de 4 lecciones, momento "wow"). Capturado: el Cuarteto SATB es el destino final del curso completo (~60 lecciones).
- **Ingesta de 3 videos al wiki:** "The Real Problem With AI Agents" → modulo_agentes.md + conceptos_no_olvidar.md; "ExO 3.0" + "Diamandis/Ismail" → `08-sintesis/tecnologia-al-servicio-del-metodo.md` (sección completa: Coase reformulado, stack 6 capas, 5 fosos defensivos); "This Could Save Your Life" → `08-sintesis/el-musico-como-atleta.md` (sección 8: longevidad sistémica).
- `00-contexto/ai-radar.md`: mayo cerrado completo (días 29-31).

## 2026-05-26
- `01-metodo-pedagogico/progresion-estudiante.md` iniciado mediante entrevista: experiencia profesional/no motivacional, recorrido inicial, propedéutico y descubrimiento de herramientas.
- `03-apps-herramientas/elefantito-matematico.md` llenado: propósito pedagógico, conexión con córtex prefrontal/Sistema 2, módulo de memoria y pendientes de verificación.
- `08-sintesis/tecnologia-al-servicio-del-metodo.md` expandido: Elefantito documentado como tecnología que resuelve el cuello de botella prefrontal y de memoria del aprendizaje musical.
- `index.md` actualizado: `AGENTS.md` registrado como schema maestro, estado de Elefantito y síntesis tecnológica corregidos a `en_progreso`; última sesión actualizada.
- `AGENTS.md` y `CLAUDE.md` actualizados: pendiente viejo de filosofia-ensenanza removido; nuevos pendientes de Elefantito y tecnología registrados.
- Segunda pasada sobre Elefantito desde el repo `nuevo-website/storm-studios`: documentada versión Next.js actual con 6 niveles, tutor bilingüe, audio narrado, progreso local y versión HTML legacy.
- `01-metodo-pedagogico/filosofia-ensenanza.md` corregido para distinguir versión actual Next.js de 6 niveles vs. versión HTML legacy de 8 niveles.
- `00-contexto/insights.md` corregido para que el insight procesado de Elefantito no deje el dato legacy de 8 niveles como estado actual.

## 2026-05-21
- **Lint completo del KB** (sesión 4): chequeo de consistencia de todo el proyecto. 7 problemas detectados y resueltos.
- `CLAUDE.md` sección 7 actualizada: fecha, archivos completos (+ filosofia-ensenanza.md), clases-ia documentada, pendientes actualizados.
- `index.md` actualizado: agregados `ai-radar.md` y `ritmos-y-decisiones.md` a sección 00-contexto; estadísticas corregidas (256+ archivos, 26 libros, 7 alumnos clases-ia, sesión 2026-05-21); descripción de `filosofia-ensenanza.md` expandida.
- `08-sintesis/como-enseno-armonia.md` → `relacionado_con` conectado a `clases-ia/03_alumnos/`.
- `08-sintesis/luis-como-ingeniero-neural.md` → `relacionado_con` conectado a `clases-ia/01_metodo/patrones_detectados_en_alumnos.md`.

## 2026-04-09
- `01-metodo-pedagogico/filosofia-ensenanza.md` llenado desde el libro: principios fundamentales, tabla comparativa, rol de la tecnología, influencias intelectuales. Estado: `en_progreso`.
- `01-metodo-pedagogico/estructura-curso.md` llenado: propedéutico completo (P01-P04), estructura general, progresión inicio-fin. Estado: `en_progreso`.
- `03-apps-herramientas/indice-apps.md` llenado: 10 apps completas (8 oído + 2 cognitivas) + Storm Sequencer. Estado: `en_progreso`.
- `00-contexto/stack-tecnologico.md` llenado: stack completo web, Android, juegos, email, almacenamiento, flujo IA. Estado: `en_progreso`.
- `README.md` actualizado: párrafo "Quién es Luis" completado con apellido Cárdenas y linaje Shostakovich-Medrano-Cárdenas.
- `00-contexto/quien-soy.md` actualizado: apellido Cárdenas y linaje pedagógico agregados.
- `00-contexto/vision-proyecto.md` completado: modelo freemium, escalera de valor, fases del proyecto, fuentes de ingreso. Estado: `completo`.
- 17 libros copiados desde H:\Libros\Libros completos MD a `07-fuentes/libros/`.
- `07-fuentes/indice-fuentes.md` poblado con catálogo completo: autor, área de impacto y ruta de cada libro.
- Nueva carpeta `07-fuentes/libros/` creada.
- `07-fuentes/indice-fuentes.md` creado: catálogo de libros y lecturas que fundamentan el método.
- README.md actualizado: `07-fuentes/` agregado al mapa de navegación.

## 2026-04-09 (anterior)
- `00-contexto/quien-soy.md` completado: biografía completa extraída del capítulo "Interludio: ¿quién soy?" del libro *Los Seres Musicales*, más dictado directo de Luis sobre su trayectoria con la IA. Estado: `completo`.
- `00-contexto/insights.md` creado: buzón de entrada para ideas y observaciones diarias.
- Carpeta duplicada `Storm Studios — Knowledge Base` eliminada de la raíz.
- README.md actualizado: `insights.md` agregado al mapa de navegación.

## 2026-04-07
- Creación inicial de la estructura del Knowledge Base.
- Todos los archivos creados en estado `borrador`.
