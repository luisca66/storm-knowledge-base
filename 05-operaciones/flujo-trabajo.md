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

## Qué significa autonomía en este ecosistema

La autonomía no significa que una IA "sepa mucho" sobre Luis ni que tenga permiso abstracto para hacer cualquier cosa. Significa que, ante un objetivo concreto, pueda completar el ciclo:

1. **Orientarse:** entender propósito, estado y prioridades sin pedir que Luis repita el contexto.
2. **Ejecutar:** localizar el proyecto correcto, hacer el cambio y usar sus herramientas.
3. **Verificar:** demostrar que el resultado cumple criterios musicales, técnicos o comerciales explícitos.
4. **Recuperarse:** detectar fallas, revertir o restaurar el sistema y dejar trazabilidad.
5. **Aprender:** incorporar al KB lo descubierto para que la siguiente ejecución sea mejor.

La decisión vigente sigue siendo **no imponer límites a priori a la autonomía de la IA**. Las fronteras se descubrirán en la práctica y se documentarán cuando aparezcan. El obstáculo actual no es de permiso: es de información operativa, acceso, criterios de aceptación e integración.

## Diagnóstico al 2026-06-12

| Capa | Estado | Evidencia |
|------|--------|-----------|
| Orientación | Fuerte | Schema único, índice, decisiones, síntesis y contexto de las tres líneas |
| Ejecución | Parcial | Hay stack y arquitectura, pero no un mapa completo de repos, rutas, comandos, ambientes y despliegues |
| Verificación | Débil | Faltan reglas de validación MIDI, fichas completas de lecciones, inventarios de assets y criterios de aceptación por producto |
| Recuperación | Débil | No están documentados rollback, restauración, incidentes, respaldo externo ni activos críticos como keystores |
| Aprendizaje | Fuerte en el KB, manual | Log, historial y síntesis funcionan; la captura nocturna y propagación entre repos aún no son automáticas |

**Conclusión:** la continuidad intelectual está resuelta. La autonomía operativa todavía depende demasiado de que Luis recuerde dónde está cada cosa, pruebe personalmente el resultado y explique qué cuenta como "correcto".

## Lo que falta construir

### 1. Mapa operativo de proyectos

Por cada línea y repositorio:
- nombre y URL del repo;
- ruta local habitual;
- propósito y responsable;
- comandos de instalación, desarrollo, pruebas, build y deploy;
- ambientes y servicios conectados;
- ubicación de credenciales, sin guardar secretos en el KB;
- estado actual y siguiente hito verificable.

### 2. Contratos de resultado

Cada tarea repetible necesita una definición de terminado:
- qué entrada recibe;
- qué salida debe producir;
- reglas que nunca puede violar;
- pruebas automáticas y revisión humana necesarias;
- evidencia que debe dejar.

Los primeros contratos prioritarios son Lección 1, Maestro Virtual, publicación de una app P03 y preparación/registro de una clase de IA.

### 3. Runbooks

Documentar procedimientos ejecutables para:
- publicar y revertir el website;
- agregar o modificar una lección;
- validar e integrar una regla del Maestro Virtual;
- publicar una app móvil;
- preparar una clase y actualizar expedientes;
- respaldar y restaurar el KB;
- responder a una falla de producción.

### 4. Integración y automatización

La escena objetivo del "martes cualquiera" requiere:
- lectura automática de agenda, alumnos, radar y pendientes;
- preparación matutina de clases y prioridades;
- captura nocturna de avances, decisiones y tareas;
- sincronización controlada entre el KB y los repos operativos;
- alertas cuando el estado documentado contradiga el código o la producción.

## Orden recomendado

1. **Inventario operativo:** repos, rutas, comandos, ambientes, servicios y activos críticos.
2. **Primer circuito autónomo completo:** Lección 1 + Maestro Virtual, desde cambio hasta prueba y deploy.
3. **Seguridad operativa:** respaldo externo del KB, restauración y rollback.
4. **Segundo circuito:** piloto P03, desde código hasta tienda y medición.
5. **Automatización diaria:** preparación matutina y cierre nocturno de clases.

No conviene documentar las ~60 lecciones ni portar las 10 apps antes de cerrar un circuito completo. La autonomía se demuestra con una tarea repetible de punta a punta; después se replica el patrón.

## Lectura de avance — 2026-07-08

La revisión de salud del KB confirma que el sistema está mecánicamente sano: `herramientas/lint_kb.py` reporta referencias, enlaces y frontmatter sin roturas. El cuello de botella ya no es ordenar el KB, sino convertir su continuidad intelectual en ejecución verificable.

Orden práctico para las próximas sesiones:

1. **Mapa operativo de proyectos** — documentar rutas locales, repos, comandos, ambientes, despliegues y activos críticos. Es el avance con más retorno porque desbloquea trabajo autónomo en website, apps y Migración Empresas.
2. **Circuito Lección 1 + Maestro Virtual** — convertir `leccion-01-escalas-mayores.md`, `tipos-de-ejercicio.md` y `reglas-validacion.md` de borradores a contrato ejecutable mínimo: qué produce el alumno, cómo se valida y cómo se prueba.
3. **Propagación a clases-ia** — pasar la tabla de modelos de `ai-radar.md` a `conceptos_no_olvidar.md` y `leccion_01`, leyendo antes `INSTRUCCIONES_CLASES_IA.md`. Es una tarea acotada, pero toca el subsistema con doble reglamento.
4. **Documentar la vaca lechera** — cerrar la entrevista de clases particulares: tipos de clase, tarifa vigente, relación con la tarifa previa de $1,250 y el Taller de Ingeniería de Audio y Producción Musical.
5. **Apps de paga** — documentar toolchain iOS y preparar el piloto P03. Debe venir después del inventario operativo para no depender de memoria oral.

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
- **2026-07-08** — Añadida lectura de avance tras lint sano: prioridades prácticas para convertir continuidad intelectual en autonomía operativa.
- **2026-06-12** — Definido el modelo de autonomía operativa, diagnóstico por capas y orden de implementación. Estado: `borrador` → `en_progreso`.
- **2026-04-07** — Creación inicial (borrador).
