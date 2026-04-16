---
titulo: "Migraciones Pendientes"
tipo: catalogo
ultima_actualizacion: 2026-04-07
relacionado_con:
  - 05-operaciones/infraestructura.md
  - 04-contenido-musical/audio-assets.md
estado: borrador
---

# Migraciones Pendientes

## Resumen
Tareas de migración que están pendientes de completar.

## Migración de Audio Assets (Dreamhost → Google Drive)

**Estado:** Pendiente
**Descripción:** Los archivos de audio estaban en Dreamhost (cancelado). Las URLs están hardcodeadas en el codebase de Next.js. Necesitan moverse a Google Drive y actualizar todas las referencias.

### Pasos
1. [ ] Inventariar todos los archivos de audio referenciados en el código
2. [ ] Verificar cuáles archivos aún son accesibles / cuáles se tienen respaldados
3. [ ] Subir a Google Drive
4. [ ] Generar URLs públicas de Google Drive
5. [ ] Buscar y reemplazar todas las URLs hardcodeadas en el codebase
6. [ ] Probar que todo funcione
7. [ ] Deploy

### Notas
[LLENAR: Cualquier contexto adicional]

## Otras Migraciones
[LLENAR si hay más]

## Historial de Cambios
- 2026-04-07: Creación inicial (borrador)
