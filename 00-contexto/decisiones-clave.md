---
titulo: "Decisiones Clave"
tipo: decision
ultima_actualizacion: 2026-06-11
estado: en_progreso
---

# Decisiones Clave

## Resumen
Registro de decisiones importantes del proyecto y su razonamiento. Esto es crítico para que una IA entienda POR QUÉ las cosas son como son y no proponga cambios que ya fueron considerados y descartados.

## Formato de Registro

Cada decisión sigue este formato:

```
### [Título de la decisión]
**Fecha:** YYYY-MM-DD
**Contexto:** Por qué surgió esta decisión.
**Decisión:** Qué se decidió.
**Razonamiento:** Por qué se eligió esta opción.
**Alternativas consideradas:** Qué otras opciones había.
**Consecuencias:** Qué implica esta decisión.
```

---

### Estudiantes deben usar el secuenciador Storm Studios (no DAWs comerciales)
**Fecha:** [LLENAR]
**Contexto:** Los estudiantes necesitan una herramienta para completar ejercicios MIDI.
**Decisión:** El secuenciador propio de Storm Studios es la herramienta obligatoria.
**Razonamiento:** Los archivos MIDI estándar no distinguen equivalentes enarmónicos (F# vs Gb). El secuenciador de Storm Studios exporta mensajes meta de key_signature que permiten la validación correcta. Además, enmarcado como decisión pedagógica.
**Alternativas consideradas:** DAWs comerciales (Logic, Ableton, etc.) — descartados por la limitación enarmónica del MIDI estándar.
**Consecuencias:** Dependencia del secuenciador propio; necesidad de mantenerlo y documentarlo.

### Migración de hosting a Vercel
**Fecha:** [LLENAR]
**Contexto:** [LLENAR]
**Decisión:** Cancelar Dreamhost y Mediafire, consolidar en Vercel Hobby + Zoho Mail + Google Drive.
**Razonamiento:** [LLENAR]
**Alternativas consideradas:** [LLENAR]
**Consecuencias:** Pendiente migración de audio assets con URLs hardcodeadas.

### Distribución de apps P03 — Play Store vs. descarga directa
**Fecha:** 2026-05-22
**Contexto:** Los videos del propedéutico están terminados (hito). P03 (Intervalos) requiere dos apps Android que actualmente se distribuyen como descarga gratuita desde el website. Con el propedéutico completo, cualquier persona puede llegar al website sin saber nada — pero las apps de P03 presentan fricción: el usuario debe encontrar la sección de descargas, bajar el APK y habilitarlo manualmente en Android.
**Decisión:** En evaluación. No se ha decidido aún.
**Opciones en análisis:**
- **Play Store** — menos fricción para el usuario, mayor alcance, proceso de publicación requerido ($25 USD, cuenta developer, AAB, keystore, assets de tienda, política de privacidad). Una vez publicado, las actualizaciones son sencillas.
- **Descarga directa desde website** — sin costo, control total, pero el usuario debe habilitar "fuentes desconocidas" en Android — fricción considerable para alumnos no técnicos.
**Consecuencias si se va a Play Store:** Necesidad de keystore firmado (archivo crítico — su pérdida impide actualizar la app para siempre). Proceso de revisión de Google (puede tomar días). Requiere política de privacidad aunque la app no recolecte datos.
**Próximo paso:** Confirmar qué apps son exactamente las dos de P03 (se asume Intervalos – Reconocimiento e Intervalos – Cantados) y decidir si se publican ambas o solo una como piloto.

### CLAUDE.md como fuente única del schema; AGENTS.md reducido a stub
**Fecha:** 2026-06-11
**Contexto:** El KB mantenía dos schemas maestros paralelos (CLAUDE.md para Claude, AGENTS.md para Codex) sincronizados a mano. Varios lints (al menos 4) señalaron el riesgo de divergencia, y el 2026-06-11 se confirmó divergencia real: cada copia tenía contenido que la otra no (la regla del doble reglamento de clases-ia y el pendiente de localStorage solo existían en AGENTS.md). Además, tres archivos competían por declararse "leer primero" (CLAUDE.md, README.md, index.md), e index.md describía a AGENTS.md como maestro y a CLAUDE.md como "histórico" — jerarquía invertida respecto a lo que CLAUDE.md decía de sí mismo.
**Decisión:** CLAUDE.md es la única fuente de verdad del schema, redactado de forma agnóstica de agente ("la IA" en vez de "Claude"/"Codex") para servir a cualquier IA presente o futura. AGENTS.md queda como stub de redirección. Roles claros: README = portada del repo privado, index = catálogo, log = historial. Ningún otro archivo se declara "leer primero".
**Razonamiento:** Claude Cowork carga CLAUDE.md automáticamente y completo en cada sesión — cero fricción para el colaborador de mayor volumen. Codex puede seguir el stub con un solo salto. Una fuente única elimina la sincronización manual, que ya había fallado en la práctica. La redacción agnóstica es coherente con el propósito del KB: que *cualquier* IA futura pueda operarlo.
**Alternativas consideradas:** (a) AGENTS.md como maestro — es el estándar multi-agente emergente, pero Claude (el colaborador principal) no lo carga automáticamente, mientras que Codex sí puede seguir un stub; (b) symlink — frágil en Windows y en checkouts de git; (c) seguir sincronizando a mano — descartado por evidencia: ya divergieron.
**Consecuencias:** Al editar el schema solo se toca CLAUDE.md. Si algún agente reconstruye AGENTS.md con contenido propio, hay que revertirlo y restaurar el stub. La unificación del propósito (dos niveles: continuidad hoy, autonomía mañana) y del alcance (tres líneas de negocio) quedó plasmada en CLAUDE.md §2.

## Historial de Cambios
- **2026-06-11** — Decisión de fuente única del schema documentada (CLAUDE.md maestro, AGENTS.md stub). Estado: borrador → en_progreso.
- **2026-05-22** — Decisión Play Store documentada (en evaluación).
- 2026-04-07: Creación inicial con 2 decisiones documentadas
