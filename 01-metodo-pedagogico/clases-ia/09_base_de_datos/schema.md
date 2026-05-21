# Schema de base de datos ligera

## alumnos.csv
Registra datos generales del alumno. `id_alumno` debe coincidir con la carpeta en `03_alumnos`.

## sesiones.csv
Registra cada clase. `archivo_bitacora` apunta al Markdown de la sesion.

## herramientas.csv
Lista herramientas del curriculum con categoria, nivel, uso principal, riesgos y notas.

## avances.csv
Registra cambios de nivel o evidencias claras de autonomia.

## tareas.csv
Registra tareas asignadas y su revision.

## proyectos.csv
Registra proyectos personales o de clase por alumno.

## fuentes.csv
Indexa fuentes internas o externas usadas para mejorar clases.

## bitacora_global.csv
Registra cambios importantes del sistema, ideas y acciones siguientes.

## Reglas de uso

- Usar `pendiente` si falta informacion.
- No guardar datos sensibles innecesarios.
- No borrar filas historicas; agregar nuevas filas o marcar estado.
- Mantener consistencia entre CSVs y archivos Markdown.
