# Conceptos No Olvidar

**Para Luis, antes o durante clase.**
Escanea el tema que vas a tocar hoy. Revisa qué ya vio el alumno en su `perfil.md`. Lo que falta, cúbrelo — aunque sea de pasada.

No es un guion. Es un mapa de lo que no puede quedar en el aire.

---

## 1 — Primera victoria con IA
*(Ver: `curso_base/leccion_01_primera_victoria_con_ia.md`)*

- No arrancar con teoría. Primero una tarea real del alumno.
- Tener tres entradas listas: organizar algo, resolver algo, crear algo.
- El diagnóstico sucede *durante* la clase, no antes.
- Mostrar que la respuesta de la IA se revisa — no se acepta automáticamente.
- Cerrar con: qué quería → qué obtuvo → qué lo sorprendió → qué sigue.

**Señal de que ya lo entendió:** puede decir para qué le sirve la IA en algo concreto de su vida o trabajo.

---

## 2 — Prompts: contexto y criterio
*(Ver: `curso_base/leccion_02_prompt_contexto_y_criterio.md`)*

- Contexto > longitud. Un prompt con contexto claro gana siempre al prompt largo y vago.
- La estructura: tarea + contexto + nivel + formato + límites.
- Mostrar el mismo tema con prompt flojo vs. prompt con contexto. Que el alumno vea la diferencia.
- ¿Qué inventó o asumió la IA? Esa pregunta va en cada respuesta.
- No subir información sensible en el prompt.

**Señal de que ya lo entendió:** puede mejorar un prompt propio y explicar por qué el nuevo es mejor.

---

## 3 — Chat vs. agente (la distinción central)
*(Ver: `curso_base/leccion_03_chat_vs_agente.md`)*

- La distinción que no puede faltar: **chat = cerebro estratégico / agente = ejecutor.**
- La pregunta que decide la herramienta: *¿quieres pensar, investigar, estudiar, ejecutar o construir?*
- El mapa básico:
  - Chat → pensar, redactar, planear
  - Deep Research → investigar con fuentes
  - NotebookLM → estudiar lo que ya tienes
  - Agentes → ejecutar tareas
  - Codex / Claude Code → construir proyectos con archivos
- Cada herramienta necesita un tipo distinto de instrucción.

**Señal de que ya lo entendió:** puede clasificar una tarea propia correctamente antes de elegir herramienta.

---

## 4 — Ecosistema base / herramientas gratuitas
*(Ver: `curso_base/leccion_04_ia_gratis_y_ecosistema_base.md`)*

- Verificar antes de clase qué sigue siendo gratuito — cambia con frecuencia.
- No prometer gratis ilimitado. Hay límites de uso.
- Flujo básico sin pagar: ChatGPT/Claude para pensar → Deep Research para investigar → NotebookLM para estudiar → Codex/Antigravity para construir.
- Pagar da más velocidad, privacidad, capacidad y continuidad. No es obligatorio para empezar.
- Distinguir: herramienta gratuita ≠ herramienta suficiente para todo.

**Señal de que ya lo entendió:** puede armar un flujo básico sin pagar y sabe en qué momento pagaría.

---

## 5 — Aprender y documentar con IA
*(Ver: `curso_base/leccion_05_aprender_y_documentar_con_ia.md`)*

- Fuente buena = guía buena. Fuente mala = guía mala. Basura entra, basura sale.
- NotebookLM es para estudiar lo que ya tienes — no para inventar.
- Cerrar con algo usable: una guía de una página, un plan de 3 pasos, algo concreto.
- Conocimiento no es acumular — es poder usar y explicar.
- Verificar que las citas del resumen vengan de las fuentes reales.

**Señal de que ya lo entendió:** puede explicar la guía en sus propias palabras y usarla para hacer algo.

---

## 6 — Flujo Chat→MD→Agente
*(Ver: `curso_base/leccion_06_flujo_chat_md_agente.md` y `01_metodo/flujo_chat_md_agente.md`)*

- Los 7 pasos en orden. El que más se salta: el paso 2 (pedir la entrevista al chat).
- El `.md` es el puente. Sin `.md`, el agente va ciego.
- Pedir la entrevista con esta frase exacta: *"Hazme una entrevista sobre este proceso para que cuando tengas toda la información me hagas un `.md` que le voy a dar al agente para que lo ejecute."*
- Organización de carpeta = parte del trabajo. No es opcional.
- Verificar con segundo chat dentro del mismo folder.
- ROI: si verificar tarda más que hacerlo manual, el briefing necesita más detalle.
- El Efecto Santiago: sin inversión inicial no hay agente útil.

**Señal de que ya lo entendió:** puede repetir el flujo completo en solitario con una tarea propia.

---

## 7 — Chats de IA: modelos y modalidades
*(Ver: `modulo_chats_ia.md`)*

- La tabla por plan — no olvidar mostrarla:

  | Plan | Modelo |
  |---|---|
  | Pago (Claude) | **Claude 4.8 (Opus)** ← actualizado |
  | Gratuito (Claude) | Claude 4.6 |
  | Alternativa OpenAI | ChatGPT 5.5 Thinking |
  | Alternativa Google | Gemini 3.5 Flash |

- Las 3 modalidades:
  - **Thinking** → problemas complejos, tarda más, no para preguntas rápidas
  - **Deep Research** → busca fuentes reales, el alumno debe verificarlas
  - **Web Search** → datos actuales, no reemplaza investigación profunda
  - **Estándar** → conversación rápida, el 80% de los casos
- Chat ≠ agente. El chat no ejecuta en el mundo real.
- Privacidad: datos de clientes, contraseñas y documentos confidenciales no entran al chat.

**Señal de que ya lo entendió:** puede elegir modelo y modalidad según la tarea, sin preguntar.

---

## 8 — Agentes: flujo, carpeta agéntica, verificación
*(Ver: `modulo_agentes.md`)*

- **Nunca ir directo al agente sin el `.md`.** El agente sin instrucciones claras improvisa.
- Carpeta agéntica: el agente puede crear sus propios `.md` de contexto → la carpeta se autoexplica para sesiones futuras.
- Verificar con segundo chat (mismo folder): *"¿el agente hizo bien el trabajo?"*
- ROI de automatización: tiempo de verificar < tiempo de hacer manual = vale la pena automatizar.
- El Efecto Santiago: la inversión inicial (briefing bien hecho, carpeta organizada) es el precio de un agente que funciona.
- No delegar el pensamiento — solo la ejecución.

**Señal de que ya lo entendió:** toma una tarea propia, genera el `.md`, pasa al agente y evalúa el output. Solo.

---

## 9 — Codex
*(Ver: `modulo_codex.md`)*

- Generar el `.md` de instrucciones **antes** de abrir Codex. Siempre.
- Organización de la carpeta es obligatoria, no un detalle.
- Estructura mínima: `instrucciones.md` + `contexto.md` + archivos del proyecto.
- Los `.md` de contexto que deja el agente son la memoria del proyecto — no borrar.
- Segundo chat para verificar el output antes de usarlo.

**Señal de que ya lo entendió:** crea su carpeta agéntica, ejecuta con Codex y puede volver a esa carpeta en otra sesión sin explicar nada desde cero.

---

## 10 — Pensamiento crítico e IA
*(Ver: `01_metodo/pensamiento_critico_ia.md`)*

- La IA puede alucinar: inventar datos, citar fuentes que no existen, sonar convincente sin tener razón.
- La pregunta que nunca sobra: *¿de dónde vino este dato?*
- No delegar el pensamiento — solo la ejecución. El criterio humano es la capa principal de calidad.
- Privacidad: qué no debe entrar al chat (datos de clientes, información financiera, documentos legales).
- ¿Cuándo derivar a un especialista? Cuando el proyecto necesite arquitectura empresarial, datos sensibles a escala, seguridad formal o cumplimiento legal.
- Usar IA ≠ pensar con IA. El alumno que solo copia respuestas no está aprendiendo.

**Señal de que ya lo entendió:** detecta al menos una debilidad o suposición en una respuesta de la IA sin que Luis lo señale.

---

## 11 — NotebookLM
*(Ver: `modulo_notebooklm.md` — pendiente de desarrollar con clase real)*

- Primero las fuentes. Sin fuentes buenas no hay estudio bueno.
- Generar preguntas de repaso, no solo resumen.
- Verificar que las respuestas vengan de las fuentes cargadas — no de conocimiento general.
- NotebookLM estudia lo que le das. No investiga, no navega, no inventa.

**Señal de que ya lo entendió:** puede generar una guía de estudio propia y hacerse preguntas de repaso sobre ella.

---

## 12 — GitHub
*(Ver: `modulo_github.md` — pendiente de desarrollar con clase real)*

- Repositorio = carpeta con memoria e historial. No es solo almacenamiento.
- Commit = guardar con una explicación del cambio. Cada commit cuenta la historia del proyecto.
- No publicar datos privados en repositorios públicos.
- Es el prerrequisito para usar Claude Code con fluidez.

**Señal de que ya lo entendió:** hace su primer commit y entiende que puede volver a cualquier versión anterior.

---

## 13 — Antigravity
*(Ver: `modulo_antigravity.md` — pendiente)*

- Útil para prototipos rápidos y estructuras de proyectos asistidos.
- Opción gratuita para construir antes de necesitar Codex.
- El alumno no debe asumir magia — mostrar qué hace exactamente.

---

## 14 — Cowork
*(Ver: `modulo_cowork.md` — pendiente)*

- Organización y ejecución guiada con agente.
- Útil para flujos de trabajo con múltiples pasos o tareas recurrentes.
- Revisar siempre permisos antes de conectar herramientas externas.

---

## 15 — Claude Code
*(Ver: `modulo_claude_code.md` — pendiente)*

- Opera sobre repositorios → necesita GitHub como base.
- Especializado en explicar errores, editar archivos y documentar código.
- No ejecutar cambios sin revisar primero.

---

## 16 — Las 4 categorías del trabajo frente a la IA

Este marco ayuda al alumno a clasificar su propio trabajo sin entrar en pánico. Úsalo cuando el tema del desplazamiento laboral aparezca — para dar estructura en lugar de alarma.

| Categoría | Descripción | Futuro |
|---|---|---|
| **Theater** | Trabajo que aparenta valor pero no lo tiene | Desaparece primero |
| **Commoditized** | Tareas rutinarias automatizables | Desaparece a mediano plazo |
| **In-the-line** | Operativo esencial | Se comprime |
| **Durable** | Estratégico, creativo, relacional | Permanece y se valoriza |

- Pedir al alumno que clasifique 3 tareas de su trabajo real.
- La pregunta útil: *¿qué parte de tu trabajo requiere criterio, relación o creatividad que la IA no puede replicar?*
- No usarlo para asustar — usarlo para enfocar el aprendizaje en lo Durable.

**Señal de que ya lo entendió:** puede clasificar sus propias tareas y nombrar al menos una que es Durable y por qué.

---

## 17 — El Sándwich Humano

Este concepto responde la pregunta más frecuente en clase: *"¿la IA no nos va a quitar el trabajo?"* Úsalo antes de que el alumno entre en pánico o en negación.

**El principio**: cuando algo que era caro de producir (código, diseño, texto, análisis) se vuelve barato, la gente no consume menos — consume más. El volumen total explota. Lo que cambia es dónde está el cuello de botella: ya no en la ejecución, sino en el **juicio, el criterio y el buen gusto** — en quien puede distinguir cuál de diez versiones generadas es la mejor.

**La estructura del trabajo nuevo:**

| Momento | Quién | Qué hace |
|---|---|---|
| Inicio | Humano | Encuadra: contexto, criterios, qué importa |
| Medio | IA | Ejecuta: genera en minutos lo que tomaría días |
| Final | Humano | Juzga: ¿cuál versión es mejor? ¿logró el objetivo? ¿qué sigue? |

- El humano sigue siendo indispensable en los dos extremos.
- La experiencia de dominio (música, negocios, comunicación) es el encuadre — y eso no se automatiza.
- Quien tiene criterio más fino gana más, no menos, cuando la ejecución se vuelve barata.

**Señal de que ya lo entendió:** puede identificar, en una tarea propia, cuál parte es su encuadre único y cuál es ejecución que puede delegar a la IA.

---

## 18 — El problema aguas arriba
*(Ver: `modulo_agentes.md` — sección "El problema aguas arriba")*

- El error más común con agentes no ocurre durante la ejecución — ocurre *antes* de empezar.
- El síntoma: el alumno instala el agente y pregunta *"¿y ahora qué le digo?"*.
- La causa raíz: ausencia de claridad de intención aguas arriba.
- La solución: antes de abrir el agente, definir en lenguaje verificable: ¿qué hace?, ¿con qué archivos?, ¿qué produce?, ¿cuáles son sus límites?
- Cuatro archivos que dan identidad a un agente persistente: `soul.md` / `identity.md` / `user.md` / `heartbeat.md`
- Los setups que fallan no fallaron por el agente — fallaron por falta de claridad upstream.

**Señal de que ya lo entendió:** puede describir el propósito de un agente en dos oraciones verificables (se puede comprobar si el agente lo cumplió o no).

---

## Conceptos transversales — estos van en cualquier clase

Estos no tienen tema propio pero se cuelan en todo. Si no aparecen solos, menciónalos:

| Concepto | Cuándo mencionarlo |
|---|---|
| **Privacidad** | Antes de conectar cualquier herramienta o subir cualquier archivo |
| **Verificación** | Cada vez que el alumno acepta una respuesta sin leerla |
| **El Efecto Santiago** | Cuando el alumno quiere saltarse el setup para ir directo a ejecutar |
| **ROI de automatización** | Cuando el alumno pregunta si vale la pena automatizar algo |
| **Criterio humano** | Cuando el alumno empieza a confiar demasiado en el output de la IA |
| **Organización de archivos** | Siempre que se abra un agente o se cree una carpeta de proyecto |
| **La Bifurcación** | En la primera clase, o cuando el alumno no entiende para qué sirve aprender esto. Dos caminos: consumidor pasivo vs. creador agéntico. La brecha crece cada mes. |
| **"No puedes tercerizar tu entendimiento"** (Karpathy) | Cuando el alumno empieza a copiar respuestas sin leerlas, o pregunta si la IA puede hacer "todo". Mientras más potente el modelo, más vale lo que TÚ sabes de tu dominio. |
| **El Sándwich Humano** | Cuando el alumno pregunta si la IA lo va a reemplazar, o cuando quiere "automatizar todo". Su criterio de dominio es el encuadre y el juicio — los dos extremos que la IA no puede ocupar. |
| **El problema aguas arriba** | Cuando el alumno instala un agente y no sabe qué pedirle, o cuando los outputs son genéricos sin importar cuántas veces lo intente. El problema no es el agente — es la falta de claridad upstream. |

---

## Cómo usar este documento

**Antes de clase:**
1. Abrir el `perfil.md` del alumno → ver qué ya está marcado como visto.
2. Abrir este archivo → escanear los temas del día.
3. Identificar qué conceptos de esos temas aún no han aparecido en clase.
4. No hace falta cubrirlos todos de golpe — pero sí que ninguno quede en cero por siempre.

**Durante clase:**
- Si el alumno hace algo sin entender el concepto detrás → parar, nombrarlo, seguir.
- La señal de avance al final de cada sección dice cuándo puedes darlo por cubierto.

---

## Historial de Cambios
- 2026-05-27: Documento creado. Cubre 15 temas + conceptos transversales.
- 2026-05-28: Sección 16 (4 categorías del trabajo). Conceptos transversales: La Bifurcación y Karpathy.
- 2026-05-29: Tabla de modelos actualizada (Opus 4.8). Sección 17 (El Sándwich Humano). Concepto transversal: El Sándwich Humano.
- 2026-06-01: Sección 18 (El problema aguas arriba). Concepto transversal: El problema aguas arriba.
