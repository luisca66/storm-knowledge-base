# Leccion 06 — Flujo Chat→MD→Agente

## Origen de la leccion

Esta leccion nace de la clase 3 del grupo del martes (Carmen, Mario, Montse, Karla — mayo 2026). Luis necesitaba una metodologia estructurada para enseñar a trabajar con agentes sin que el alumno tuviera que saber programar ni redactar prompts complejos. El flujo Chat→MD→Agente resolvio ese problema.

## Objetivo

Que el alumno sepa planear un proyecto con el chat, convertirlo en un `.md` y pasarselo al agente para que lo ejecute — separando claramente la fase de pensamiento de la fase de ejecucion.

## Para quien sirve

Para cualquier alumno que ya distingue chat de agente (leccion 03) y quiere dar el siguiente paso: usar un agente para una tarea real. Especialmente util para perfiles administrativos, financieros o de produccion que necesitan automatizar procesos concretos.

## Duracion sugerida

90 a 120 minutos.

## Herramientas

- **Chat de planificacion:** Claude 4.7 Extended Thinking (plan pago) o Claude 4.6 (gratuito). Alternativas: ChatGPT 5.5 Thinking, Gemini 3.1 Pro.
- **Agente de ejecucion:** Codex, Claude Code, Cowork o Antigravity segun el proyecto.
- **Archivo puente:** un `.md` generado por el chat y guardado en la carpeta del agente.

## Conceptos clave

- Separacion de roles: chat piensa, agente actua.
- Briefing.
- Entrevista del chat.
- Archivo `.md` como puente.
- Carpeta agéntica.
- Verificacion con segundo chat.

## Filosofia silenciosa

Division de trabajo inteligente: el humano no delega el pensamiento, solo la ejecucion. El `.md` es la memoria del proyecto — cualquier agente futuro puede retomar el trabajo desde ese archivo.

## Preparacion de Luis

Tener un proyecto real del alumno listo para usar como ejemplo. Debe ser algo concreto: una tarea administrativa, un proceso repetitivo, una organizacion de archivos, un documento de planificacion.

Saber de antemano que agente va a usar el alumno y tener la carpeta lista.

## Apertura

Preguntar:

- Que tarea haces en el trabajo que podrias delegar si alguien supiera exactamente como hacerla?
- Si le escribieras instrucciones perfectas a un asistente nuevo, como empezarias?

Esas respuestas son el briefing inicial.

## Actividad guiada: los 7 pasos

### Paso 1 — Briefing al chat

Abrir el chat y describir:
- Que se quiere hacer.
- Como se ve el resultado exitoso.

No hace falta ser preciso. El chat hara las preguntas.

### Paso 2 — Pedir la entrevista

Decirle al chat exactamente:

> "Hazme una entrevista sobre este proceso para que cuando tengas toda la informacion me hagas un `.md` que le voy a dar al agente para que lo ejecute."

El chat genera un cuestionario. Rango tipico:
- 10 preguntas → proyectos simples
- 30 preguntas → proyectos complejos

### Paso 3 — Responder el cuestionario

Contestar todas las preguntas con honestidad y detalle. No saltarse ninguna. Cada respuesta es informacion que el agente va a necesitar.

### Paso 4 — El chat genera el `.md`

El chat produce un archivo `.md` con:
- Contexto del proyecto.
- Objetivo y criterio de exito.
- Instrucciones paso a paso para el agente.
- Restricciones y consideraciones.

### Paso 5 — Guardar el `.md` en el lugar correcto

Estructura recomendada:
```
carpeta-del-agente/
└── proyectos/
    └── nombre-del-proyecto/
        └── instrucciones.md
```

Luis reitera en cada clase: todos los archivos perfectamente ordenados. La organizacion no es opcional.

### Paso 6 — Ejecutar con el agente

Abrir el agente y decirle:

> "Lee el archivo `instrucciones.md` y ejecutalo."

El agente lee, entiende el contexto completo y ejecuta.

### Paso 7 (recomendado) — Verificar con segundo chat

Abrir un segundo chat dentro del mismo agente (mismo folder) y pedirle que audite si el primer agente hizo bien el trabajo. El alumno revisa el resultado con criterio propio.

**Criterio de Luis:** si verificar tarda mas que hacerlo manualmente, el proceso no esta maduro para automatizacion. Ese es el ROI de la IA en flujos de trabajo.

## Ejercicio practico

El alumno elige una tarea real de su trabajo y ejecuta los 7 pasos completos. Al final debe tener:
- Un `.md` generado por el chat.
- Un output producido por el agente.
- Una evaluacion propia: el agente lo hizo bien?

## Preguntas de criterio

- El `.md` que genero el chat es lo que querías comunicarle al agente?
- El agente siguio las instrucciones o improviso?
- Que parte del output revisarias antes de usarlo?
- Si lo hicieras manualmente, cuanto tardarias? Cuanto tardaste en el flujo completo?
- Que mejorarias en el briefing para la proxima vez?

## Variantes por perfil

| Alumno/perfil | Proyecto sugerido |
|---|---|
| Karla (financiero/administrativo) | Proceso financiero recurrente: categorizar gastos, generar reporte mensual, organizar documentos |
| Montse (asistente de produccion) | Calendario de eventos, agenda de reuniones, organizacion de archivos de proyecto |
| Carmen (productora) | Flujo de cotizacion, organizacion de carpetas de proyecto audiovisual |
| Mario (director) | Investigacion de referentes, mapa de herramientas para un proyecto |
| Julio (financiero con poca paciencia) | Tarea corta, resultado inmediato — briefing rapido de 5 preguntas |
| Jonas (adolescente) | Proyecto de app o juego — el chat genera las especificaciones, el agente empieza a construir |
| Bruno (adolescente creativo) | Plan de entrenamiento o app personal — el agente organiza el proyecto |

## Errores comunes

- Saltarse la entrevista del chat e ir directo al agente con instrucciones vagas.
- No guardar el `.md` en la carpeta correcta del agente.
- No verificar el output del agente antes de usarlo.
- Asumir que si el agente termino, termino bien.
- Querer automatizar un proceso que todavia no se entiende bien manualmente.

## Señal de avance

El alumno puede tomar una tarea propia, convertirla en un `.md` usando el chat, y pasarsela al agente sin ayuda de Luis. Ademas puede evaluar si el output es correcto.

## El Efecto Santiago en esta leccion

Este flujo requiere inversion inicial: aprender a hacer el briefing, aprender a responder la entrevista, aprender a organizar la carpeta. Quien no hace esa inversion (el Santiago de los agentes) termina dando instrucciones vagas al agente y obteniendo resultados inutiles. La diferencia entre un agente util y uno que no sirve es casi siempre el `.md` que lo precede.

Ver: `filosofia-ensenanza.md` → seccion El Efecto Santiago.

## Cierre

Guardar el `.md` generado. Definir una tarea real para hacer en solitario antes de la siguiente clase.

## Tarea opcional

Usar el flujo Chat→MD→Agente para una tarea real de trabajo durante la semana. Traer el resultado a la siguiente clase para revisarlo juntos.

## Siguiente leccion sugerida

Depende del perfil:
- Proyecto propio de largo aliento → avanzar en la carpeta agéntica del alumno.
- Interes en privacidad y permisos → leccion de privacidad y limites.
- Interes en construir algo → modulo Codex o Claude Code.

## Que registrar en bitacora

- Tarea elegida por el alumno.
- Calidad del briefing inicial.
- Numero de preguntas que genero el chat.
- Si el alumno leyo el `.md` antes de pasarlo al agente (como Karla).
- Calidad del output del agente.
- Tiempo de verificacion vs. tiempo de ejecucion manual.
- Si el alumno puede repetir el flujo solo.

## Referencia metodologica

Documento completo del flujo: `01-metodo-pedagogico/clases-ia/01_metodo/flujo_chat_md_agente.md`
