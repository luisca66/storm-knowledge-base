---
titulo: "Funcionalidades y Estado Actual"
tipo: catalogo
ultima_actualizacion: 2026-07-09
relacionado_con:
  - 02-plataforma-web/arquitectura.md
  - 02-plataforma-web/maestro-virtual.md
  - 02-plataforma-web/secuenciador.md
  - 03-apps-herramientas/indice-apps.md
estado: en_progreso
---

# Funcionalidades y Estado Actual

## Resumen
Qué existe hoy en [stormstudios.com.mx](https://www.stormstudios.com.mx) — funcionalidades implementadas, contenido disponible y lo que está pendiente. Snapshot actualizado 2026-07-09 con el mapa contextual de proyectos.

---

## Páginas activas

| Ruta | Descripción | Estado |
|------|-------------|--------|
| `/es` | Página de inicio | ✅ Activa |
| `/es/quien-soy` | Biografía y trayectoria de Luis | ✅ Activa |
| `/es/mi-metodo` | El Camino de la Señal, filosofía pedagógica | ✅ Activa |
| `/es/clases-taller` | Modalidades de estudio (presencial / distancia / digital) | ✅ Activa |
| `/es/curso-armonia` | Curso de Armonía Tradicional con lecciones | ✅ Activa |
| `/es/apps` | Catálogo de las 11 webapps + Sequencer | ✅ Activa |
| `/es/el-libro` | Página del libro *Los Seres Musicales* | ✅ Activa |
| `/es/blog` | Blog de contenidos | ✅ Activa |
| `/es/contacto` | Formulario / datos de contacto | ✅ Activa |
| `/es/privacidad` | Política de privacidad | ✅ Activa |
| `/es/recursos/` | Guías temáticas (armonía, auditivo, intervalos, teoría) | ✅ Activa |

El sitio está disponible en **español e inglés** via internacionalización (`/es/` y `/en/`).

---

## Curso de Armonía — contenido implementado

El curso tiene capacidad para ~60 lecciones. Al 2026-05-02 están publicadas:

| Sección | Lecciones | Estado |
|---------|-----------|--------|
| Introducción | 1 lección introductoria | ✅ Publicada |
| Propedéutico | P01 Escritura de notas, P02 Escritura rítmica, P03 Intervalos, P04 Uso del secuenciador | ✅ Terminado |
| Lecciones principales | Lecciones 1 a 3 | ✅ Terminadas |
| Lección actual | Lección 4 | En producción |
| Lecciones pendientes | Lecciones posteriores | En desarrollo progresivo |

Todo el contenido publicado del curso vive en **dos idiomas**.

---

## Herramientas integradas

### Storm Sequencer v3.0
Secuenciador MIDI en el navegador, construido en HTML/vanilla JS. Permite al alumno escribir ejercicios del curso y exportarlos como archivo MIDI para enviarlo al Maestro Virtual. Ver `secuenciador.md` para detalles técnicos y pedagógicos.

### Maestro Virtual
Validador automático de ejercicios. El alumno sube el archivo MIDI exportado del Sequencer y recibe retroalimentación. La plataforma describe esto como "retroalimentación de IA que acompaña al método, no lo sustituye." Ver `maestro-virtual.md` para arquitectura y estado por lección.

---

## Webapps — catálogo completo (gratuitas)

| App | Categoría | Función |
|-----|-----------|---------|
| Elefantito Matemático | Cognitiva | Aritmética mental cronometrada |
| App Memoria – Nemotecnia | Cognitiva | Memorizar números 0–99 con juego de parejas |
| Desglose | Auditiva | Aislar e identificar notas individuales dentro de acordes |
| Intervalos – Reconocimiento | Auditiva | Identificar distancias relativas entre notas |
| Intervalos – Cantados | Auditiva | Producción vocal precisa de intervalos |
| Reconocimiento de Acordes | Auditiva | Identificar acordes (tríadas hasta acordes con 13ª) |
| Cantar Acordes | Auditiva | Cantar las notas de acordes de dificultad progresiva |
| Grados Escala Mayor | Auditiva | Reconocer grados diatónicos y cromáticos en tonalidades mayores |
| Grados Escala Menor | Auditiva | Reconocer grados diatónicos y cromáticos en tonalidades menores |
| Oído Absoluto Multi-tímbrico | Auditiva | Reconocimiento de notas sin referencia, 5 timbres |
| Oído Absoluto Guitarra Clásica | Auditiva | Versión especializada para guitarristas |

---

## Modalidades de estudio ofrecidas

| Modalidad | Descripción |
|-----------|-------------|
| **Taller presencial** (CDMX) | Estudio-gimnasio en Ciudad de México. Armonía + entrenamiento auditivo + trabajo corporal. Modalidad más completa. |
| **Estudio guiado a distancia** | Combinación del curso gratuito, apps, blog y guías de estudio. Permite trabajo serio desde cualquier lugar. |
| **Recursos digitales** | Acceso libre al curso, apps, blog y guías. Sin acompañamiento directo. |

**Precios:** No publicados en el sitio. El contacto es por teléfono (55 5103 1758) o email (info@stormstudios.com.mx).

---

## Recursos adicionales

- **Guías temáticas:** 4 guías en `/es/recursos/` (curso de armonía, entrenamiento auditivo, intervalos, fundamentos)
- **Blog:** Artículos sobre el método, neurociencia aplicada, pedagogía musical
- **Libro *Los Seres Musicales*:** Disponible en formato digital — contiene los principios del método

---

## Pendientes identificados

- [ ] Lección 4 del curso de armonía (en producción)
- [ ] Lecciones posteriores del curso de armonía (publicar progresivamente)
- [ ] Precios publicados en el sitio (actualmente solo por contacto)
- [ ] Sección de asesorías de IA (línea de negocio nueva — ver `vision-proyecto.md`)

---

## Historial de Cambios
- **2026-04-07** — Creación inicial (borrador)
- **2026-05-02** — Archivo llenado a partir de scraping del sitio stormstudios.com.mx. Estado actualizado de borrador a en_progreso.
- **2026-07-09** — Estado actualizado por entrevista: propedéutico terminado, lecciones 1-3 terminadas, Lección 4 en producción, todo en dos idiomas; apps reencuadradas como webapps gratuitas.
