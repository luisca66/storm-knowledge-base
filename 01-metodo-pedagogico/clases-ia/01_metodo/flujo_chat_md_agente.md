# Flujo Chat→MD→Agente

Metodología core de Luis para enseñar a trabajar con agentes. Separa la planificación (chat) de la ejecución (agente), usando un `.md` como puente entre ambos.

---

## El principio

El chat no es el agente. El agente no planea. Juntarlos sin separación produce caos.

La solución: usar el chat como entrevistador inteligente que extrae toda la información necesaria del humano, la estructura en un documento, y solo entonces se le pasa ese documento al agente para que ejecute.

**El humano no necesita saber programar ni redactar prompts complejos.** Solo necesita saber describir lo que quiere y responder preguntas.

---

## El flujo paso a paso

### Paso 1 — Abrir el chat y hacer el briefing

Entrar al chat y describir:
- **Qué quieres hacer** (la tarea)
- **Cómo se ve el resultado exitoso** (el criterio de éxito)

No hace falta ser preciso. El chat va a hacer las preguntas.

**Modelos recomendados según plan:**
| Plan | Modelo |
|------|--------|
| Pago | Claude 4.7 Extended Thinking |
| Gratuito | Claude 4.6 |
| Alternativa | ChatGPT 5.5 Thinking |
| Alternativa | Gemini 3.1 Pro |

---

### Paso 2 — Pedir la entrevista

Decirle al chat:

> *"Hazme una entrevista sobre este proceso para que cuando tengas toda la información me hagas un `.md` que le voy a dar al agente para que lo ejecute."*

El chat genera un cuestionario. La longitud varía:
- **10 preguntas** → proyectos simples
- **30 preguntas** → proyectos complejos

---

### Paso 3 — Responder el cuestionario

Contestar todas las preguntas con honestidad y detalle. Devolver las respuestas al chat.

No saltarse preguntas. Cada respuesta es información que el agente va a necesitar.

---

### Paso 4 — El chat genera el `.md`

El chat produce un archivo `.md` con el prompt completo, estructurado y listo para el agente. Incluye:
- Contexto del proyecto
- Objetivo y criterio de éxito
- Instrucciones paso a paso para el agente
- Restricciones y consideraciones relevantes

---

### Paso 5 — Guardar el `.md` en el lugar correcto

Estructura de carpetas recomendada:

```
carpeta-del-agente/
└── proyectos/
    └── nombre-del-proyecto/
        └── instrucciones.md   ← este archivo
```

**Luis reitera esto en cada clase:** todos los archivos perfectamente ordenados. La organización no es opcional — es parte del método. Un agente desordenado es un agente que no sirve.

---

### Paso 6 — Ejecutar con el agente

Abrir el agente (Codex, Antigravity, Claude Code o Cowork) y decirle:

> *"Lee el archivo `instrucciones.md` y ejecútalo."*

El agente lee, entiende el contexto completo y ejecuta.

---

### Paso 7 (opcional pero recomendado) — Verificar el output

Abrir un segundo chat dentro del mismo agente (mismo folder) y pedirle que audite si el primer agente hizo bien el trabajo.

El humano revisa el resultado con criterio propio.

**Criterio de Luis:** si verificar tarda más que hacerlo manualmente, el proceso no está maduro para automatización. Ver: *Efecto Santiago*.

---

## Por qué funciona

1. **Separa roles:** el chat piensa, el agente actúa. Cada uno hace lo que sabe hacer.
2. **El humano mantiene el criterio:** no delega el pensamiento, solo la ejecución.
3. **El `.md` es la memoria del proyecto:** cualquier agente futuro puede retomar el trabajo leyendo ese archivo.
4. **Escala:** una vez que el flujo está dominado, se puede reutilizar la estructura para proyectos similares con mínima fricción.

---

## Patrones observados en alumnos

| Alumno | Comportamiento en Paso 6 | Interpretación |
|--------|--------------------------|----------------|
| Karla (30) | Leyó el `.md` completo antes de pasarlo al agente | Disciplina de revisión — perfil financiero/verificador |
| Montse (30) | Ejecutó siguiendo el flujo | Confianza en el proceso |
| Grupo general | Tienden a ir directo al agente sin leer | Normal — el flujo está diseñado para eso |

**Nota de Luis:** *"Karla leyó el plan. Ni yo los leo."*

---

## Conexión con otros principios del método

- **Efecto Santiago:** no saltar el setup correcto. El `.md` bien construido es el metrónomo del agente.
- **Chat = cerebro estratégico / agente = ejecutor:** este flujo operacionaliza esa distinción.
- **Carpeta agéntica:** el `.md` que genera este flujo es el documento fundacional de cualquier carpeta agéntica.

---

## Historial de Cambios
- 2026-05-27: Documento creado a partir de clase 3 del grupo Carmen-Mario-Montse-Karla.
