---
titulo: "Storm Studios Learning — Base de Conocimiento"
tipo: indice
ultima_actualizacion: 2026-06-10
estado: en_progreso
---

# Storm Studios Learning — Base de Conocimiento

## Quién es Luis

Soy Luis Cárdenas, músico profesional con 35 años de carrera y maestro de música con 30 años de experiencia. Me formé en guitarra y teoría musical bajo el linaje **Shostakovich → Hernández Medrano → Cárdenas**, y pasé 15 años como compositor y productor en la industria publicitaria de la Ciudad de México. En 2018 gané el Campeonato Mundial de Men's Physique de Musclemania en Las Vegas. Desde 2025 construyo software educativo como "vibe coder" — usando IA para desarrollar todas las herramientas de la plataforma sin formación formal en programación. Storm Studios Learning es mi proyecto de vida: un curso de armonía gratuito, 10 apps de entrenamiento auditivo, y un método pedagógico propio llamado "Los Seres Musicales" que integra neurociencia, fisiología y filosofía yóguica para transformar a cualquier estudiante en un músico consciente y completo.

## Qué es este Knowledge Base

Este repositorio contiene la información necesaria para que una IA colabore activamente con Luis en Storm Studios Learning, sus clases y asesorías de IA, y Migración Empresas.

**Objetivo principal:** Que cualquier IA pueda leer estos archivos y continuar el desarrollo del proyecto sin necesidad de que Luis explique todo desde cero cada vez.

## Mapa de Navegación

| Carpeta | Contenido | Prioridad |
|---------|-----------|-----------|
| `00-contexto/` | Bio, visión, stack técnico, decisiones clave | Alta — leer primero |
| `00-contexto/insights.md` | Buzón de entrada para ideas y observaciones diarias — procesar y distribuir al archivo que corresponda | Media — consultar frecuentemente |
| `01-metodo-pedagogico/` | Filosofía, estructura del curso, lecciones, ejercicios | Alta — el corazón del proyecto |
| `02-plataforma-web/` | Arquitectura Next.js, Maestro Virtual, secuenciador | Alta — la implementación |
| `03-apps-herramientas/` | Catálogo de apps Android, Godot, HTML | Media |
| `04-contenido-musical/` | Repertorio, MIDIs, audio assets | Media |
| `05-operaciones/` | Infraestructura, migraciones, flujo de trabajo | Baja — consultar según necesidad |
| `06-diario-proyecto/` | Registro cronológico mensual | Referencia — contexto temporal |
| `07-fuentes/` | Libros y lecturas que fundamentan el método, con índice de impacto por área. | Media — referencia para decisiones pedagógicas |
| `08-sintesis/` | Síntesis de nivel 2 que integran fuentes, entrevistas y pensamiento de Luis | Alta — conocimiento acumulado |
| `09-migracion-empresas/` | Nueva línea empresarial de IA; visión, cartera y método transversal | Alta — negocio activo |

## Convenciones

### Metadatos (frontmatter YAML)

Cada archivo abre con un bloque YAML entre `---`. Los campos son:

- **titulo**: Nombre descriptivo del documento.
- **tipo**: `contexto` | `leccion` | `spec` | `decision` | `diario` | `catalogo`
- **ultima_actualizacion**: Fecha en formato YYYY-MM-DD.
- **relacionado_con**: Lista de rutas a otros documentos relevantes.
- **estado**: `borrador` | `en_progreso` | `completo` | `requiere_revision`

### Estados

- **borrador**: Archivo creado con estructura pero sin contenido real.
- **en_progreso**: Tiene contenido parcial, falta completar.
- **completo**: Documentación completa y revisada.
- **requiere_revision**: Contenido desactualizado o con errores conocidos.

## Instrucciones para la IA

1. **Siempre lee este README primero.**
2. Antes de trabajar en algo, revisa el archivo correspondiente y su campo `estado`.
3. Después de hacer cambios en cualquier archivo, actualiza `ultima_actualizacion` y el `Historial de Cambios` al final.
4. Luis trabaja como "vibe coder" — no sabe código formalmente pero construye con IA. Adapta tus explicaciones a ese contexto.
5. El idioma de trabajo es español. El código y nombres técnicos pueden estar en inglés.
6. Luis usa tú (nunca voseo argentino).
7. Cuando no estés seguro de algo, pregunta. No inventes información sobre el método pedagógico ni sobre las decisiones técnicas — están documentadas aquí por una razón.

---
## Historial de Cambios
- **2026-06-10** — Mapa ampliado para incluir Migración Empresas como nueva línea activa del ecosistema de Luis.
