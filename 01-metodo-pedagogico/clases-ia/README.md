# Clases IA

Sistema profesional para planear, registrar, mejorar y dar seguimiento a clases personalizadas de inteligencia artificial impartidas por Luis.

## Proposito

Este repositorio funciona como memoria permanente del trabajo con alumnos. Sirve para preparar clases, registrar bitacoras, dar seguimiento a tareas, organizar ejercicios, documentar aprendizajes y mejorar el metodo de Luis con el tiempo.

La meta pedagogica central es que cada alumno aprenda a usar IA para aprender, resolver, crear y organizarse con mayor autonomia.

## Para quien es

Para Luis y para agentes de IA que lo apoyen en la preparacion, documentacion y mejora de sus clases. Los reportes estan pensados para uso interno de Luis, no como entregables publicos para alumnos.

## Como usar el repositorio

1. Antes de una clase, abrir `00_instrucciones/antes_de_cada_clase.md`.
2. Revisar la carpeta del alumno en `03_alumnos/`.
3. Preparar un plan flexible con `04_sesiones/plantilla_plan_de_clase.md`.
4. Durante la clase, tomar notas suficientes para reconstruir lo ocurrido.
5. Despues de la clase, llenar `04_sesiones/plantilla_bitacora_sesion.md` dentro de la carpeta del alumno.
6. Actualizar CSVs en `09_base_de_datos/` cuando haya avances, tareas, sesiones o proyectos nuevos.
7. Actualizar `00_instrucciones/ultimo_estado.md` y `00_instrucciones/pendientes.md` si cambia el estado del sistema.

## Flujo recomendado

Antes: revisar perfil, ultima bitacora, tareas y herramientas vistas. Preparar 2 o 3 rutas posibles.

Durante: partir de un problema real del alumno, mantener flexibilidad y registrar descubrimientos.

Despues: documentar bitacora, tarea, proxima clase sugerida, avances y dudas de Luis.

## Registro de alumnos

Cada alumno vive en `03_alumnos/nombre_edad/` con perfil, diagnostico, sesiones, tareas, proyectos, reportes internos y notas privadas. No inventar datos: usar `pendiente` cuando falte informacion.

## Registro de sesiones

Nombrar sesiones como `YYYY-MM-DD_sesion_01.md`. Cada sesion debe tener bitacora. La bitacora es el documento minimo obligatorio despues de cada clase.

## Como pedir ayuda a un agente

Pedir al agente que lea primero `README.md`, `PROJECT_CONTEXT.md`, `AGENTS.md`, `00_instrucciones/ultimo_estado.md` y `00_instrucciones/pendientes.md`. Luego indicar el alumno, el objetivo y si se necesita plan, bitacora, reporte, ejercicio o actualizacion de base de datos.

## Privacidad

Este repositorio puede contener datos personales. Si se registran datos reales de alumnos, mantener el repositorio privado, evitar informacion sensible innecesaria y no subirlo a servicios publicos sin revisar privacidad.

## Estado actual

Version inicial 0.1.0. La estructura base esta creada y lista para completar diagnosticos reales y registrar sesiones.
