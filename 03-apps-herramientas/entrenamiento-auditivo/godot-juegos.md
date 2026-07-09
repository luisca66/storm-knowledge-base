---
titulo: "Juegos de Entrenamiento Auditivo — Godot"
tipo: spec
ultima_actualizacion: 2026-07-09
relacionado_con:
  - 03-apps-herramientas/indice-apps.md
  - 03-apps-herramientas/entrenamiento-auditivo/app-android-overview.md
estado: en_progreso
---

# Juegos de Entrenamiento Auditivo — Godot

## Resumen
Juegos de entrenamiento auditivo desarrollados en Godot 4 / GDScript. Son experimentos y semillas del futuro Videojuego Total de Entrenamiento Auditivo: hoy existe al menos un juego por habilidad, y en la visión final todo estará interlazado en un juego de realidad virtual inmersivo.

## Estado general

Luis está intentando mejorar los gráficos, pero aparentemente necesita una tarjeta de video más capaz. El frente está en espera de presupuesto. Aun así, los juegos actuales ya cumplen una función importante: probar mecánicas de entrenamiento auditivo como juego, no como simple quiz.

## Juego de Oído Absoluto

### Concepto
Juego centrado en oído absoluto, con 5 niveles en 5 mundos.

### Niveles
- **Total confirmado:** 5 niveles / 5 mundos
- Personajes/mundos registrados: cocodrilito, personaje esférico, unicornio volador pedido por Kari, nave espacial y otros.

### Mecánica de Entrenamiento Auditivo
El entrenamiento de oído absoluto es la mecánica central, no un adorno de gamificación.

### Estado Actual
Terminado; Luis lo describe como hermoso.

## Juego de Intervalos

### Concepto
Juego centrado en intervalos cantados.

### Mecánica
El enemigo se acerca y produce la nota base pidiendo un intervalo. El alumno canta la nota correcta durante aproximadamente 1.5 segundos para cargar el arma y además la escribe a mano. Cuando ambas respuestas son correctas, se oye la carga y dispara.

### Estado Actual
En desarrollo.

## Pendiente: juegos de todas las apps

Sigue pendiente hacer juegos para todas las apps/habilidades. La visión de Luis es que estos juegos sean semillas separadas de un sistema mayor, no productos aislados sin conexión.

## Decisiones Técnicas
- **Motor:** Godot 4
- **Lenguaje:** GDScript
- **Cuello de botella actual:** gráficos / GPU / presupuesto

## Historial de Cambios
- **2026-07-09** — Ficha llenada desde mapa contextual: juegos como semilla del Videojuego Total, AP terminado, Intervalos en desarrollo, necesidad de GPU/presupuesto y pendiente de juegos para todas las apps.
- 2026-04-07: Creación inicial (borrador)
