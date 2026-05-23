---
titulo: "Decisiones Clave"
tipo: decision
ultima_actualizacion: 2026-05-22
estado: borrador
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

## Historial de Cambios
- **2026-05-22** — Decisión Play Store documentada (en evaluación).
- 2026-04-07: Creación inicial con 2 decisiones documentadas
