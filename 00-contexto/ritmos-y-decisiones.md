---
titulo: "Ritmos Operativos de Luis"
tipo: contexto
ultima_actualizacion: 2026-07-03
relacionado_con:
  - 00-contexto/quien-soy.md
  - 05-operaciones/flujo-trabajo.md
  - 05-operaciones/asesoria-ia.md
estado: en_progreso
---

# Ritmos Operativos de Luis

> Cómo está estructurado el tiempo de Luis en la vida real — bloques fijos, prioridades variables y el sistema que lo mantiene al día con la IA mientras va en bici.

---

## Los bloques fijos

### Mañanas — Esteban Coppel
- **Quién:** Esteban, 33 años, familia Coppel
- **Cuándo:** Diario, 8:00am – 11:30am
- **Traslado:** Bici, 14 km de ida. 50-55 minutos (récord personal: 41:30). Los últimos kilómetros son de subida.
- **Regreso:** ~12:15pm

### Tardes — Adriana y Alejandra (Polanco)
- **Quién:** Dos alumnas, entrenamiento en su gym
- **Cuándo:** Lunes y jueves, 5:30pm – 8:00pm
- **Traslado:** Moto a Polanco

### Otros alumnos fijos
- **Jonás** — viernes en la tarde (alumno nuevo)
- **Bruno** — domingos
- **Asesoría de IA** — martes al mediodía, después de Esteban (reciente)

---

## El sistema de IA en background

Mientras Luis está con Esteban, un proceso automatizado trabaja en su laptop:

1. **Openclaw** — agente que se queda en casa recibiendo links de canales de YouTube que publican noticias de IA y extrae los transcripts uno por uno
2. **Tarea programada de Cowork** — genera un resumen de 55 minutos a partir de esos transcripts, listo para la mañana siguiente

**El resultado:** Luis escucha el resumen de noticias de IA durante el recorrido de bici de 50-55 minutos. Llega a casa de Esteban ya al día. El tiempo de traslado es tiempo de aprendizaje.

> **Convención de registro (desde 2026-07-04):** cada ingesta diaria de ainews se anota en `log.md` en **una sola línea** que apunta al índice mensual — el detalle de temas del día vive únicamente en `07-fuentes/ainews/YYYYMM/indice_general.md`. Es la regla de fuente única aplicada al pipeline: evita que el log duplique el índice y lo mantiene legible para las sesiones reales de trabajo. **Nota para Luis:** si el prompt de la tarea programada de Cowork escribe entradas extensas en el log, hay que ajustarlo para que escriba solo esa línea (ese cambio vive en la configuración de la tarea, fuera del alcance de una sesión normal del KB).

---

## Prioridades variables (según energía disponible)

### 1. Guitarra Clásica
- Repertorio memorizado de ~1.5 horas (que estudiado a fondo se extiende por horas)
- Estudio secuencial: cada sesión continúa donde terminó la anterior
- Enfoque: lento, extra cuidadoso, totalmente concentrado — aplicando su propia metodología
- Meta mínima: una sesión por semana

### 2. Gym — tres rutinas de ~30 minutos cada una
- **Rutina A:** Press militar + press inclinado
- **Rutina B:** Pullups + fondos con aros
- **Rutina C:** Peso muerto, pantorrilla, sentadilla, remo con barra, shrugs
- Meta mínima: cada rutina al menos una vez por semana; a veces puede un día o dos extra
- *Nota de contexto:* Luis fue campeón de fitness a los 52 años en Las Vegas Musclemania. Llegó a cargar 30 toneladas diarias en sus entrenamientos de mayor intensidad.

### 3. Lo demás
Código, website, novia Kari — "como vaya pudiendo." La vida no alcanza.

---

## El principio detrás

Los bloques fijos (clientes, traslados) son inamovibles. Todo lo demás — guitarra, gym, código, website — se inserta en los espacios que quedan, según la energía del día.

El sistema de IA automatizado es un ejemplo de cómo Luis resuelve el problema del tiempo: no consume tiempo extra para mantenerse al día con la IA — convierte el tiempo que ya existe (el traslado en bici) en tiempo de aprendizaje.

---

## Historial de Cambios
- **2026-07-03** — Documentada la convención de registro de ainews a 1 línea (regla de fuente única; Tarea 3 del plan de mejoras).
- **2026-04-17** — Creación del archivo a partir de entrevista a Luis
