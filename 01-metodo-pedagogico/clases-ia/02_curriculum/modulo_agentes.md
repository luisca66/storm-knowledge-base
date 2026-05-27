# Modulo: Agentes

> **Estado:** desarrollado con evidencia de clases reales (clase 3 del grupo martes — Carmen, Mario, Montse, Karla — mayo 2026; y proyecto real de Montse con Codex).

---

## Objetivo

Que el alumno entienda que es un agente, como darle instrucciones utiles y como verificar su output. La metodologia central es el Flujo Chat→MD→Agente.

---

## Distincion central

**Chat = cerebro estratégico. Agente = ejecutor.**

El agente actua en el mundo real: crea archivos, modifica carpetas, ejecuta codigo, accede a fuentes, produce entregables. No planea — ejecuta. Por eso necesita instrucciones claras antes de empezar.

---

## La metodologia: Flujo Chat→MD→Agente

Este es el flujo que Luis enseña para trabajar con agentes. Separa la planificacion (chat) de la ejecucion (agente), usando un `.md` como puente entre ambos.

### Los 7 pasos

**Paso 1 — Briefing al chat**
Describir al chat: que se quiere hacer y como se ve el resultado exitoso.

**Paso 2 — Pedir la entrevista**
Decirle al chat:
> "Hazme una entrevista sobre este proceso para que cuando tengas toda la informacion me hagas un `.md` que le voy a dar al agente para que lo ejecute."

El chat genera un cuestionario de 10 a 30 preguntas segun la complejidad.

**Paso 3 — Responder el cuestionario**
Contestar todas las preguntas. No saltarse ninguna.

**Paso 4 — El chat genera el `.md`**
El chat produce instrucciones completas para el agente: contexto, objetivo, pasos, restricciones.

**Paso 5 — Guardar el `.md` en la carpeta correcta**
```
carpeta-del-agente/
└── proyectos/
    └── nombre-del-proyecto/
        └── instrucciones.md
```

**Paso 6 — Ejecutar con el agente**
Abrir el agente y decirle: "Lee el archivo `instrucciones.md` y ejecutalo."

**Paso 7 — Verificar con segundo chat**
Abrir un segundo chat dentro del mismo agente (mismo folder) para auditar si el trabajo esta correcto.

Documento completo: `01_metodo/flujo_chat_md_agente.md`

---

## La carpeta agéntica

Cuando un agente trabaja en una carpeta, puede crear sus propios archivos `.md` de contexto: quien soy, que hago, como funciono, cuales son mis restricciones. Esos archivos quedan en la carpeta. La proxima vez que el agente (o cualquier otro agente) entre a la carpeta, lee esos archivos y retoma el trabajo sin que Luis tenga que explicar nada de nuevo.

Esto es lo que hace que una carpeta se vuelva "agéntica": se autoexplica.

---

## ROI de la automatizacion

Criterio para decidir si vale la pena automatizar un proceso:

> Si el tiempo de verificar el output del agente es mayor que el tiempo de hacer el proceso manualmente, el flujo no esta maduro para automatizacion.

Esto no significa que el agente no sirva — significa que el briefing necesita mas detalle, o que el proceso necesita mas estandarizacion antes de delegarse.

La inversion inicial (El Efecto Santiago) siempre se requiere: aprender a hacer un buen briefing, a responder la entrevista bien, a organizar la carpeta. Quien no hace esa inversion obtiene outputs inutiles del agente.

---

## Agentes disponibles en el curso

| Agente | Para que | Nivel requerido |
|---|---|---|
| **Codex** (OpenAI) | Proyectos, carpetas, archivos, scripts | Intermedio |
| **Claude Code** | Codigo y documentacion en repositorios | Intermedio-avanzado |
| **Cowork** | Organizacion y ejecucion guiada | Intermedio |
| **Antigravity** | Prototipos y proyectos asistidos | Intermedio |

---

## Herramientas de planificacion (para el Paso 1-4)

| Plan | Chat recomendado |
|---|---|
| Pago | Claude 4.7 Extended Thinking |
| Gratuito | Claude 4.6 |
| Alternativa | ChatGPT 5.5 Thinking / Gemini 3.1 Pro |

---

## Conceptos clave

- Agente.
- Briefing.
- Instrucciones estructuradas.
- Archivo `.md` como puente.
- Carpeta agéntica.
- Verificacion.
- ROI de automatizacion.
- El Efecto Santiago aplicado a agentes.

---

## Filosofia silenciosa

El humano no delega el pensamiento — solo la ejecucion. El `.md` es la prueba de que el humano penso antes de actuar. Un agente sin un `.md` bien construido es un ejecutor sin criterio.

---

## Preparacion de Luis

Tener una tarea real del alumno lista para usar como proyecto. La tarea debe ser:
- Concreta (no vaga).
- Repetible (vale la pena automatizar).
- Con resultado verificable (el alumno puede saber si esta bien o mal).

---

## Actividad guiada

Ejecutar los 7 pasos del Flujo Chat→MD→Agente con una tarea real del alumno. Luis modela el Paso 1 (briefing) y el Paso 2 (pedir la entrevista). El alumno ejecuta los pasos 3 a 7.

---

## Ejercicio practico

El alumno:
1. Elige una tarea de su trabajo que repite con frecuencia.
2. Completa el flujo completo (briefing → `.md` → agente → verificacion).
3. Mide: cuanto tardaria hacerlo manualmente vs. cuanto tardó el flujo completo.
4. Decide: vale la pena automatizarlo?

---

## Variantes por perfil

| Alumno/perfil | Proyecto sugerido |
|---|---|
| Karla (finanzas) | Proceso financiero recurrente: categorizar gastos, reporte mensual |
| Montse (asistente) | Calendario de eventos, organizacion de archivos, agenda de reuniones |
| Carmen (productora) | Flujo de cotizacion, organizacion de carpeta de proyecto |
| Mario (director) | Investigacion de referentes, mapa de herramientas |
| Julio (financiero) | Briefing corto (5 preguntas), resultado inmediato |
| Jonas (adolescente) | Especificaciones de una app o juego que quiere construir |

---

## Errores comunes

- Ir directo al agente sin hacer el briefing ni el `.md`.
- Dar instrucciones vagas ("haz algo sobre marketing").
- No verificar el output antes de usarlo.
- Asumir que si el agente termino, lo hizo correctamente.
- Querer automatizar un proceso que el alumno mismo no entiende bien.
- Delegar el pensamiento junto con la ejecucion.

---

## Señal de avance

El alumno puede tomar una tarea propia, generar el `.md` sin ayuda de Luis, pasarselo al agente y evaluar si el output es correcto. Puede repetir el flujo en solitario.

---

## Patrones observados en alumnos

| Alumno | Comportamiento | Interpretacion |
|---|---|---|
| Karla (30) | Leyo el `.md` completo antes de pasarlo al agente | Disciplina de revision — perfil financiero/verificador |
| Montse (30) | Ejecuto siguiendo el flujo, verifico con segundo chat | Confianza en el proceso, disciplina de cierre |
| Grupo general | Tendencia a ir directo al agente sin leer el `.md` | Normal — el flujo esta diseñado para eso |

---

## Conexion con el curriculo

- Requiere haber visto: `leccion_03` (chat vs. agente), `leccion_05` (documentar con IA)
- Leccion correspondiente: `leccion_06` (Flujo Chat→MD→Agente)
- Documento metodologico: `01_metodo/flujo_chat_md_agente.md`
- Herramienta relacionada: `modulo_codex.md`, `modulo_claude_code.md`, `modulo_cowork.md`

---

## Historial de evidencia

- 2026-05-26: enseñado en clase 3 del grupo martes (Carmen, Mario, Montse, Karla). Flujo completo ejecutado. Distincion clave: Karla leyo el plan antes de pasarlo al agente.
- Proyecto real de Montse: calendario de conferencias PDF para Mario — ejecutado con Codex, verificado con segundo chat.
