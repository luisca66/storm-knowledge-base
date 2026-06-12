---
titulo: "Estructura del Curso"
tipo: catalogo
ultima_actualizacion: 2026-06-12
relacionado_con:
  - 01-metodo-pedagogico/filosofia-ensenanza.md
  - 01-metodo-pedagogico/progresion-estudiante.md
  - 02-plataforma-web/maestro-virtual.md
estado: en_progreso
---

# Estructura del Curso — Storm Studios Learning

## Resumen
El curso de armonía de Storm Studios Learning está basado en el método que Luis estudió con el maestro Humberto Hernández Medrano (alumno de Shostakovich), mejorado con 25 años de experiencia profesional en composición y producción. Es un curso totalmente gratuito, progresivo y sin agrupación en módulos — las lecciones son consecutivas. El linaje oficial es **Shostakovich → Hernández Medrano → Cárdenas**.

---

## Vista General

| Componente | Detalle |
|-----------|---------|
| Propedéutico | 4 lecciones (lectura, ritmo, intervalos, secuenciador) |
| Curso de Armonía | ~60 lecciones estimadas; 1 activa en la reconstrucción Next.js |
| Inicio del contenido | Escalas mayores y menores |
| Final del contenido | Armonía cromática y modulación en cuarteto vocal |
| Formato | Video por lección + tarea + Maestro Virtual en tiempo real |
| Acceso | Completamente gratuito |
| Validación | MIDI — el Maestro Virtual valida cada ejercicio en la misma página |

---

## Propedéutico (4 lecciones)

El propedéutico es obligatorio para alumnos sin conocimientos previos. Cubre las herramientas básicas que se usarán en todo el curso.

> **Hito 2026-05-22:** Todos los videos del propedéutico están terminados. Cualquier persona puede llegar al website sin conocimientos previos y comenzar de forma autónoma.

| # | Lección | Tema | Herramienta de práctica |
|---|---------|------|------------------------|
| P01 | Escritura de las Notas Musicales | Lectura y escritura de notas en el pentagrama | App web propia integrada en el website |
| P02 | Escritura de la Rítmica Musical | Lectura y escritura de ritmo | App web propia integrada en el website |
| P03 | Intervalos | Reconocimiento e identificación de intervalos | Dos apps Android indispensables (ver nota) |
| P04 | Uso del Secuenciador | Cómo usar el Storm Sequencer v3.0 integrado en la plataforma | Storm Sequencer v3.0 (integrado en el website) |

> **Nota P03:** Las dos apps de intervalos son el piloto acordado para la estrategia vigente: versión web gratuita y versiones móviles de pago bajo en Google Play / App Store. La distribución directa por APK fue la etapa anterior. Ver `03-apps-herramientas/indice-apps.md` y `00-contexto/decisiones-clave.md`.

---

## Curso de Armonía (~60 lecciones)

Las lecciones son **consecutivas y progresivas** — no hay módulos ni agrupaciones. Cada lección tiene un punto central de aprendizaje; cuando el alumno lo domina, avanza a la siguiente. La validación es en tiempo real a través del Maestro Virtual (MIDI).

### Lecciones en plataforma (Migración Next.js)

Actualmente (junio 2026), el curso de armonía está en **fase de reconstrucción** debido a la migración de la plataforma a Next.js. Los videos son nuevos y toman tiempo en producirse. El número total real de lecciones se definirá sobre la marcha (el estimado de ~60 viene del número de corales que entregó el último alumno presencial que terminó el curso).

| # | Lección (Borrador de secuencia) | Estado / Notas |
|---|---------------------------------|----------------|
| 1 | Escalas Mayores | **Publicada.** (Única activa actualmente) |
| 2 | Modos | *En evaluación:* Intercalar modos antes de menores |
| 3 | Escalas Menores | En planeación |
| 4 | Acordes de 5ª de la Escala Mayor | En planeación |
| 5 | *[Transición / Por definir]* | En planeación |
| 6 | Acordes de 5ª de las Escalas Menores| En planeación |
| 7 | Construcción en Cuarteto Vocal | Primera lección SATB: tesituras, duplicaciones, supresiones, triplicaciones. De aquí en adelante, todo es SATB. |

### El Maestro Virtual (El Curso en Código)
El Maestro Virtual no es solo un feature técnico. Es un **documento vivo que contiene todo el curso de Luis traducido a código**. Este documento crece y evoluciona a la par de la producción de los videos.
Su objetivo inmediato es permitir que el alumno revise sus tareas en línea gratis. 
Su objetivo a largo plazo (el "experimento de vida" de Luis) es **hacer que una IA componga música estando obligada a obedecer estrictamente este set de reglas**, para ver los resultados de la ingeniería neural pura aplicada al arte.

### Mapa completo del curso (basado en el Curso Medrano)

Las ~60 lecciones siguen la arquitectura del Curso Integral de Composición Musical de Hernández Medrano. La progresión es:

**Bloque 1 — Elementos y fundamentos** (cubierto en propedéutico + lecciones 1-2)
- Armónicos naturales, temperamento igual, escalas heptáfonas, grados, modos
- Intervalos: clasificación, inversión, compuestos
- Escalas básicas: mayor natural, menor natural, menor armónica, menor melódica

**Bloque 2 — Armonía diatónica en SATB** (lecciones ~3-30)
- Funciones de los grados (tonales, modales, atractivos)
- 4 tipos de acordes de 5ª y sus regiones tonales
- Cuarteto vocal (SATB): tesituras, extensiones máximas
- Duplicaciones, estados e inversiones
- Movimientos melódicos permitidos y prohibidos
- Movimientos armónicos: quintas/octavas paralelas
- Material armónico bachiano + tabla de enlaces
- Cadencias (auténtica, plagal, rota, ampliada) y semicadencias
- Acordes de paso (V 6/4, VII 6/3, I 6/4)
- Armonización de tetracordes (fórmulas por modo y dirección)

**Bloque 3 — Acordes con séptima y novena** (lecciones ~31-45)
- V7 e inversiones
- VII7 e inversiones (con homónimo)
- II7 e inversiones
- V9 e inversiones (solo 3ª inversión en clásicos)
- IV7 y VI7 (casos excepcionales en Bach)

**Bloque 4 — Modulación** (lecciones ~46-55)
- Modulación diatónica a tonos vecinos (1er grado de parentesco, 12 casos)
- Modulación cromática (por nuevo VII, VI o IV grado)
- Modulación en 2do grado de parentesco (2-5 alteraciones, con tonalidad de paso)
- Modulación en 3er grado de parentesco (6-7 alteraciones)
- Modulación sin tonalidad de paso
- Modulación por enarmonia (VII7 e inversiones)
- Corte libre

**Bloque 5 — Figuración melódica y armonía cromática** (lecciones ~56-60)
- Notas extrañas: anticipos, apoyaturas, retardos, bordados, escapadas, pasos
- Ornamentación doble, triple, cuádruple
- V-5 y VII-3
- 6ª napolitana
- Acordes del homónimo (préstamo modal)

El formato SATB (Soprano, Alto, Tenor, Bajo) es el cuarteto vocal estándar de la armonía clásica — el mismo formato en que Medrano enseñaba y en que la tradición Shostakovich está escrita.

---

## Cursos Avanzados (de pago, con Luis)

Estos cursos no están en la plataforma gratuita. Son el siguiente paso para alumnos que terminan el curso de armonía y quieren convertirse en Seres Musicales completos.

1. **Contrapunto** — [LLENAR: descripción]
2. **Análisis** — [LLENAR: descripción]
3. **Film Scoring** — [LLENAR: descripción]

---

## Pendientes de Documentar

- Títulos y temas de lecciones 3 a 60
- Contenido específico de cada lección publicada (objetivos, contenido teórico, ejercicios, notas pedagógicas)
- Descripción de los tres cursos avanzados de pago

---

## Historial de Cambios
- **2026-06-12** — Estado post-migración Next.js reconciliado: una lección activa, secuencia inicial en evaluación y Maestro Virtual entendido como el curso traducido a código. Nota P03 actualizada a la estrategia web-gratis/móvil-de-paga.
- **2026-05-22** — Hito: videos del propedéutico terminados. Documentada la arquitectura de herramientas: P01/P02 con apps web propias, P03 con dos apps Android, P04 con Storm Sequencer. Decisión Play Store en evaluación.
- 2026-04-07: Creación inicial (borrador)
- 2026-04-16: Llenado con propedéutico completo (4 lecciones), estructura general y progresión del curso extraídos del sitio web. Estado: `en_progreso`.
- 2026-04-16: Mapa completo del curso (5 bloques, ~60 lecciones) derivado del Curso Integral de Composición Musical de Hernández Medrano. Pendiente: títulos de lecciones individuales 3-60 y descripción de cursos avanzados.
