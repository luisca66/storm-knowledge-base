---
titulo: "Maestro Virtual"
tipo: spec
ultima_actualizacion: 2026-07-09
relacionado_con:
  - 01-metodo-pedagogico/ejercicios/reglas-validacion.md
  - 02-plataforma-web/arquitectura.md
  - 02-plataforma-web/secuenciador.md
  - 08-sintesis/como-enseno-armonia.md
estado: en_progreso
---

# Maestro Virtual

## Resumen
El Maestro Virtual es el validador automático de ejercicios del curso. Recibe un archivo MIDI exportado por el Storm Sequencer, aplica las reglas de validación correspondientes a la lección, y devuelve retroalimentación al alumno. Es la implementación tecnológica del principio pedagógico central: **retroalimentación inmediata como condición de la práctica deliberada**.

**Lo más importante:** el Maestro Virtual no es un validador genérico — es la **codificación completa del Curso Integral de Composición Musical de Hernández Medrano en lógica de software**. Una instancia de Claude está convirtiendo el curso de Medrano en código; el Maestro Virtual ejecuta ese código para revisar los ejercicios de cada alumno. El curso Medrano (disponible en `07-fuentes/libros/curso-medrano.txt`) es la columna vertebral tanto del Maestro Virtual como de la progresión de lecciones.

---

## Por qué existe

En las clases presenciales, Luis valida personalmente el trabajo de cada alumno. El coral perfecto como criterio de avance requiere que alguien — o algo — verifique que los ejercicios cumplen las reglas antes de permitir el avance.

A escala, eso es imposible sin automatización. El Maestro Virtual replica esa función a cualquier hora, sin importar cuántos alumnos haya. Desde la perspectiva de Ericsson/Gladwell: sin retroalimentación inmediata, el alumno puede estar mielinizando el error con perfecta eficiencia.

La plataforma lo describe como "retroalimentación de IA que acompaña al método, no lo sustituye" — la distinción es importante. El Maestro Virtual valida reglas; la comprensión musical la desarrolla el alumno.

## Futuro del Maestro Virtual

Luis ve este proyecto como algo más grande que una herramienta de corrección para alumnos. A largo plazo, el Maestro Virtual puede funcionar como una codificación de sus enseñanzas para que IAs futuras compongan con ese marco y se pueda observar qué hacen con el método. En ese sentido, no solo valida ejercicios: preserva reglas, criterio y estilo pedagógico en una forma computable.

---

## Arquitectura

El sistema vive como una API route dentro de la plataforma Next.js:

- **`midi-parser.ts`** — Parseo del archivo MIDI recibido. Extrae notas, duraciones, voces, y los meta-messages (incluyendo `key_signature`).
- **`scale-validator.ts`** — Módulo de validación para lecciones de escalas. Aplica las reglas de la lección contra el MIDI parseado.
- **API route** (`app/api/...`) — Endpoint que recibe el archivo MIDI del alumno, lo pasa por el parser y el validador, y devuelve el resultado de la validación.

---

## Flujo de Trabajo de Codificación

La traducción del curso (PDF) a código estricto es un proceso iterativo humano-IA:
1. **Asimilación:** Luis utiliza un LLM de frontera (ej. Claude Opus/Fable) capaz de retener el PDF original del curso en contexto.
2. **Traducción paso a paso:** Se avanza lección por lección, extrayendo las reglas musicales y convirtiéndolas en lógica condicional estricta.
3. **Validación aislada:** Antes de tocar el repositorio en Next.js, se prueban las reglas de código en un validador HTML en un entorno de pruebas aislado. Esto garantiza que la lógica musical fue capturada sin alucinaciones.
4. **Integración:** Una vez probada, la regla pasa a formar parte de los módulos de validación (`scale-validator.ts`, etc.) del Maestro Virtual.

---

## El problema enarmónico y la solución

### El problema

En música occidental, F# (Fa sostenido) y Gb (Sol bemol) son **enarmónicos**: suenan exactamente igual en afinación temperada. Un archivo MIDI estándar solo registra el número de nota MIDI (0–127) y la velocidad — no sabe si la nota es F# o Gb. Ambas producen el mismo número.

Para el Maestro Virtual esto es un problema crítico. Una escala de Fa# mayor tiene un nombre específico para cada nota (Fa#, Sol#, La#, Si, Do#, Re#, Mi#). Si el alumno escribe Sol# cuando debería ser La♭, suenan igual pero son armónicamente distintas. Sin esa información, el validador no puede determinar si el ejercicio es correcto.

### La solución: `key_signature` meta-messages

Los DAWs comerciales (incluido Cubase) exportan MIDI sin `key_signature` meta-messages por defecto — solo guardan las notas como números. Para resolver el problema enarmónico, Luis construyó el **Storm Sequencer** como herramienta propia que sí exporta estos meta-messages.

El `key_signature` meta-message indica la armadura de clave: cuántos sostenidos o bemoles, y si es mayor o menor. Con esa información, el Maestro Virtual puede resolver la enarmónica de cada nota y validar correctamente.

**Esto es la razón de existir del Sequencer propio** — no es comodidad ni ahorro de licencias. Es la única forma de producir el MIDI que el validador requiere.

---

## Estado de las lecciones

El Maestro Virtual vive dentro del website y, según estimación de Luis (2026-07-09), está listo aproximadamente hasta la **Lección 6**. Avanzará conforme se vaya necesitando en las lecciones, no como un proyecto aislado separado del curso.

**El número de lecciones es aproximado.** El último alumno que terminó el curso presencial con Luis escribió aproximadamente **60 corales**, pero ese número puede variar al adaptar el material a la plataforma en línea.

La progresión de lecciones sigue la estructura del Curso Medrano (5 niveles: propedéutico → armonía diatónica → séptimas/novenas → modulación → figuración melódica + cromatismo). Ver `01-metodo-pedagogico/estructura-curso.md` para el mapa completo.

| Etapa | Contenido | Estado documentado |
|-------|-----------|--------------------|
| Propedéutico (P01–P04) | Notas, ritmo, intervalos, secuenciador | Terminado en el website; no depende del validador armónico completo |
| Lecciones 1-3 | Primeras lecciones del curso | Terminadas en el website |
| Lección 4 | Lección actual | En producción |
| Lecciones hasta aprox. 6 | Reglas iniciales del Maestro Virtual | Listas según estimación de Luis; avanzarán conforme se necesiten |
| SATB | Tesituras, duplicaciones, enlaces, cadencias | Será la etapa técnicamente más compleja |
| Séptimas, modulación y cromatismo | V7–V9, parentescos, figuración, 6ª napolitana | Pendiente |

**Nota:** La validación de corales SATB requiere verificar simultáneamente: tesituras de las 4 voces, duplicaciones permitidas/prohibidas, movimientos paralelos (quintas y octavas), enlaces entre acordes, y estados/inversiones. Es el desarrollo técnico más complejo del proyecto.

---

## Pendientes críticos

- [ ] Mantener alineado el avance del Maestro Virtual con las lecciones reales del website
- [ ] Definir arquitectura del validador SATB para las lecciones de armonía (Lecciones 6+)
- [ ] Especificar reglas de validación por lección en `ejercicios/reglas-validacion.md`

---

## Historial de Cambios
- **2026-04-07** — Creación inicial (borrador)
- **2026-05-02** — Archivo sustancialmente expandido: propósito pedagógico, arquitectura, el problema enarmónico y su solución, estado por lección. Estado: en_progreso.
- **2026-06-12** — Documentado el flujo humano-IA para traducir Medrano a código y reconciliado el estado post-migración: Lección 1 activa, resto en planeación y validación de producción pendiente de verificar en el repo.
- **2026-07-09** — Reconciliado con mapa contextual: Maestro Virtual vive dentro del website, listo aproximadamente hasta Lección 6 y con futuro como codificación del método para IAs futuras.
