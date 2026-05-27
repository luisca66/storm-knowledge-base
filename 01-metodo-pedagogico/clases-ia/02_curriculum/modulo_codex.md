# Modulo: Codex

> **Estado:** desarrollado con evidencia de clases reales (clase 3 del grupo martes — Montse, mayo 2026; proyecto real de calendario PDF).

---

## Objetivo

Que el alumno sepa usar Codex para ejecutar proyectos con archivos y carpetas, entienda el concepto de carpeta agéntica y pueda verificar el trabajo del agente con un segundo chat.

---

## Que es Codex

Codex es el agente de OpenAI para trabajo con repositorios, archivos y proyectos. Puede leer carpetas, crear documentos, modificar archivos existentes, ejecutar scripts y producir entregables concretos a partir de instrucciones en lenguaje natural.

A diferencia del chat, Codex actua: no solo responde.

---

## Concepto central: la carpeta agéntica

Una carpeta agéntica es una carpeta que se autoexplica. Contiene:
- El proyecto o los archivos del trabajo.
- Archivos `.md` de contexto creados por el agente: quien soy, que hago, cuales son mis restricciones, como funciono.

Cuando el agente entra a esa carpeta la proxima vez — o cuando entra un agente diferente — lee esos `.md` y retoma el trabajo sin que Luis ni el alumno tengan que explicar nada.

**Una carpeta agéntica bien construida es un proyecto que puede continuar sin supervision constante.**

---

## Estructura recomendada de carpeta

```
nombre-del-proyecto/
├── instrucciones.md        ← el .md generado por el chat (Flujo Chat→MD→Agente)
├── contexto.md             ← que es este proyecto, quien lo usa, como funciona
├── [archivos del proyecto]
└── proyectos/
    └── nombre-subproyecto/
        └── instrucciones.md
```

Luis reitera en cada clase: todos los archivos perfectamente ordenados. La organizacion no es opcional — es parte del metodo. Un agente desordenado es un agente que no sirve.

---

## Flujo de trabajo con Codex

El flujo correcto es el Flujo Chat→MD→Agente (ver `leccion_06`):

1. Abrir el chat y hacer el briefing.
2. Pedir la entrevista al chat.
3. Responder el cuestionario.
4. El chat genera el `.md`.
5. Guardar el `.md` en la carpeta de Codex.
6. Decirle a Codex: "Lee el archivo `instrucciones.md` y ejecutalo."
7. Verificar el output con un segundo chat dentro del mismo proyecto.

---

## Verificacion con segundo chat

Una vez que Codex termina, abrir un **segundo chat dentro del mismo agente** (mismo folder) y pedirle que audite si el primer agente hizo bien el trabajo.

Este segundo chat lee el contexto del folder, entiende que se pidio y evalua si el resultado es correcto. El alumno revisa el resultado con criterio propio.

---

## Herramientas

- **Codex** (OpenAI) — el agente principal.
- **Chat de planificacion** — para generar el `.md` de instrucciones antes de entrar a Codex.

---

## Conceptos clave

- Agente vs. chat.
- Instrucciones estructuradas (el `.md`).
- Carpeta agéntica.
- Verificacion con segundo chat.
- Organizacion de archivos.
- ROI de automatizacion.

---

## Filosofia silenciosa

Un agente desordenado es un agente que no sirve. La carpeta no es solo el lugar donde viven los archivos — es la memoria del proyecto. Organizarla bien desde el inicio es parte del trabajo, no un detalle secundario.

---

## Preparacion de Luis

Tener una carpeta de ejemplo organizada para mostrar. Saber el proyecto que va a trabajar el alumno. Tener acceso a Codex activo.

---

## Actividad guiada

1. Mostrar una carpeta agéntica ya construida: explicar cada archivo `.md` de contexto.
2. Ejecutar un proyecto real del alumno usando el Flujo Chat→MD→Agente.
3. Mostrar como Codex lee el `.md` y ejecuta.
4. Abrir el segundo chat para verificar el output.

---

## Ejercicio practico

El alumno crea su primera carpeta agéntica:
- Nombre del proyecto.
- El `.md` de instrucciones generado por el chat.
- Un archivo de contexto basico.
- Ejecuta con Codex.
- Verifica con segundo chat.
- Decide: el agente lo hizo bien?

---

## Variantes por perfil

| Alumno/perfil | Proyecto real usado en clase |
|---|---|
| Montse (asistente de Mario) | Calendario de conferencias en PDF — el agente buscó días y horarios para optimizar la agenda de Mario |
| Carmen (productora) | Organizacion de carpeta de proyecto audiovisual |
| Mario (director) | Investigacion de referentes para un proyecto |
| Jonas (adolescente) | Estructura inicial de una app o proyecto de juego |
| Karla (finanzas) | Organizacion de documentos financieros recurrentes |

---

## Errores comunes

- Abrir Codex sin haber generado el `.md` de instrucciones.
- Dar instrucciones directamente en el chat de Codex sin contexto estructurado.
- No organizar la carpeta antes de ejecutar.
- No verificar el output con el segundo chat.
- Modificar archivos del proyecto manualmente sin que el agente sepa.
- No crear el archivo de contexto — la proxima sesion el agente no sabe que hizo antes.

---

## Señal de avance

El alumno puede crear una carpeta agéntica, ejecutar un proyecto con Codex usando el flujo correcto y verificar el resultado. Puede regresar a esa carpeta en otra sesion y el agente retoma sin que Luis tenga que explicar nada.

---

## Conexion con el curriculo

- Requiere haber visto: `leccion_03` (chat vs. agente), `leccion_06` (Flujo Chat→MD→Agente)
- Modulo relacionado: `modulo_agentes.md`, `modulo_github.md`
- Documento metodologico: `01_metodo/flujo_chat_md_agente.md`

---

## Historial de evidencia

- 2026-05-26: enseñado en clase 3 del grupo martes. Montse ejecuto el flujo completo con un proyecto real de calendario PDF para Mario. El agente buscó días disponibles y organizo la agenda. Verificacion con segundo chat: el agente lo hizo correctamente.
