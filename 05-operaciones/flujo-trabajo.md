---
titulo: "Flujo de Trabajo"
tipo: contexto
ultima_actualizacion: 2026-07-08
relacionado_con:
  - 00-contexto/stack-tecnologico.md
  - 00-contexto/decisiones-clave.md
  - 05-operaciones/infraestructura.md
  - 01-metodo-pedagogico/ejercicios/reglas-validacion.md
estado: en_progreso
---

# Flujo de Trabajo

## Resumen
Cómo trabaja Luis día a día: herramientas, procesos, y patrones. Esto ayuda a la IA a entender el contexto operativo real.

## Qué significa este archivo en el ecosistema

Este archivo no convierte al KB en el lugar desde donde se operan los proyectos. Luis trabaja cada website, app, cliente o experimento en su propio repo, carpeta, herramienta y momento. El KB registra el contexto para que, cuando Luis pida ayuda, la IA entienda qué existe, qué se ha intentado, qué decisiones están vigentes y qué conexiones estratégicas importan.

El objetivo no es que una IA futura "opere desde el KB". El objetivo es que lea el KB y pueda:

1. **Orientarse:** entender propósito, estado y prioridades sin pedir que Luis repita toda su historia.
2. **Dar criterio:** proponer ideas, detectar contradicciones, recordar decisiones y sugerir estrategias.
3. **Conectar:** relacionar website, clases, apps, Migración Empresas, método pedagógico y fuentes.
4. **Acompañar ejecución externa:** cuando Luis abra un proyecto específico, usar el contexto del KB para ayudar mejor en ese entorno.
5. **Aprender:** registrar al final lo descubierto para que la siguiente colaboración sea más inteligente.

La decisión vigente sigue siendo **no imponer límites a priori a la colaboración con IA**, pero el KB no centraliza la operación. Las fronteras prácticas viven en cada proyecto y se documentan aquí solo cuando generan conocimiento útil para el ecosistema.

## Diagnóstico al 2026-07-08

| Capa | Estado | Evidencia |
|------|--------|-----------|
| Orientación | Fuerte | Schema único, índice, decisiones, síntesis y contexto de las tres líneas |
| Registro de proyectos | Parcial | Hay stack, arquitectura y catálogos, pero falta una vista clara de proyectos vivos, repos, estado, decisiones y próximos hitos |
| Estrategia | Fuerte | Las páginas de síntesis permiten cruzar método, tecnología, negocio, IA y fuentes |
| Ejecución | Externa al KB | Cada proyecto se trabaja por separado, en su propio repo/contexto, según la necesidad que aparezca |
| Aprendizaje | Fuerte en el KB, manual | Log, historial y síntesis funcionan; falta capturar con más constancia lo aprendido en proyectos externos |

**Conclusión:** la continuidad intelectual está resuelta. Lo que falta no es convertir el KB en un panel de control, sino registrar mejor los proyectos y sus desarrollos para que la IA tenga memoria contextual cuando Luis pida ayuda.

## Lo que falta construir

### 1. Mapa contextual de proyectos

Por cada proyecto importante:
- nombre y URL del repo;
- ruta local habitual;
- propósito;
- estado actual;
- decisiones vigentes;
- hitos ya logrados;
- siguientes preguntas o caminos posibles;
- comandos o datos técnicos útiles solo si ayudan a orientar una colaboración futura;
- ambientes y servicios conectados;
- ubicación general de credenciales/activos críticos, sin guardar secretos en el KB.

### 2. Memoria de decisiones por proyecto

Cada proyecto necesita dejar claro:
- qué se decidió;
- por qué se decidió;
- qué alternativas se descartaron;
- qué sigue abierto;
- qué aprendizaje debería recordar una IA futura.

Los primeros candidatos son website/Storm Studios Learning, Maestro Virtual, Storm Sequencer, apps auditivas, apps de paga, Migración Empresas y clases particulares.

### 3. Registro de desarrollos

Cuando un proyecto avance fuera del KB, traer de vuelta lo importante:
- qué se construyó;
- qué cambió;
- qué problema resolvió;
- qué quedó pendiente;
- qué decisión nueva apareció;
- qué debería saber una IA antes de volver a tocar ese tema.

### 4. Vista de prioridades

El KB debe poder responder con claridad:
- qué proyectos están vivos;
- cuáles están en pausa;
- cuáles son históricos;
- cuáles generan dinero hoy;
- cuáles son legado/reputación;
- cuáles tienen bloqueo por decisión de Luis;
- cuáles tienen bloqueo técnico.

## Orden recomendado

1. **Mapa contextual de proyectos:** lista viva de proyectos, repos, estado, propósito y siguiente pregunta estratégica.
2. **Registro de desarrollos recientes:** capturar avances importantes hechos fuera del KB para que no se pierdan.
3. **Prioridades por línea:** clases particulares, Storm Studios Learning y Migración Empresas, separadas pero conectadas.
4. **Decisiones pendientes:** precios, apps de paga, toolchain iOS, taller de audio, localStorage y propagación a clases-ia.
5. **Síntesis estratégica:** usar el mapa para detectar qué conviene avanzar, no para operar todos los repos desde aquí.

No conviene documentar todos los comandos de todos los repos antes de saber qué contexto estratégico falta. Primero hay que registrar qué proyectos existen, qué papel cumplen y qué necesita recordar la IA sobre cada uno.

## Lectura de avance — 2026-07-08

La revisión de salud del KB confirma que el sistema está mecánicamente sano: `herramientas/lint_kb.py` reporta referencias, enlaces y frontmatter sin roturas. Luis aclara una distinción central: el KB no existe para operar proyectos desde aquí, sino para registrar lo hecho y dar contexto profundo a la IA que ayude en cada proyecto por separado.

Orden práctico para las próximas sesiones:

1. **Mapa contextual de proyectos** — registrar proyectos vivos, históricos y en pausa; propósito, estado, repo/ruta si aplica, próximos hitos y decisiones vigentes.
2. **Documentar la vaca lechera** — cerrar la entrevista de clases particulares: tipos de clase, tarifa vigente, relación con la tarifa previa de $1,250 y el Taller de Ingeniería de Audio y Producción Musical.
3. **Propagación a clases-ia** — pasar la tabla de modelos de `ai-radar.md` a `conceptos_no_olvidar.md` y `leccion_01`, leyendo antes `INSTRUCCIONES_CLASES_IA.md`.
4. **Apps de paga** — documentar toolchain iOS, piloto P03 y migración de Intervalos Cantados completa.
5. **Lección 1 + Maestro Virtual** — no como "circuito autónomo del KB", sino como documentación de criterio pedagógico y validación para futuras conversaciones técnicas.

Las ingestas de contenido largo, como `Shadows of Forgotten Ancestors`, siguen siendo valiosas, pero hoy no son el cuello de botella principal.

## Herramientas Diarias
[LLENAR: ¿Con qué herramientas trabajas cada día? Claude.ai, Cowork, Claude Code, VS Code, etc.]

## Patrón de Trabajo Típico
[LLENAR: ¿Cómo es un día típico? ¿Cuándo programas? ¿Cuándo das clases? ¿Cuándo trabajas en el proyecto?]

## Cómo Trabajas con IA
[LLENAR: Tu flujo de vibe coding. ¿Cómo distribuyes tareas entre Claude.ai (estrategia), Cowork (archivos), y Claude Code (implementación)?]

## Limitaciones de Tiempo
[LLENAR: Esto es importante — una IA que entiende que tu tiempo es limitado puede priorizar mejor sus sugerencias.]

## Historial de Cambios
- **2026-07-08 (2)** — Reencuadrado el archivo: el KB no es centro operativo; registra contexto, historia, decisiones y desarrollos para que la IA ayude mejor en proyectos separados.
- **2026-07-08** — Añadida lectura de avance tras lint sano: prioridades prácticas para convertir continuidad intelectual en autonomía operativa.
- **2026-06-12** — Definido el modelo de autonomía operativa, diagnóstico por capas y orden de implementación. Estado: `borrador` → `en_progreso`.
- **2026-04-07** — Creación inicial (borrador).
