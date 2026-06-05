---
titulo: "Elefantito Matemático"
tipo: tecnico
ultima_actualizacion: 2026-06-04
relacionado_con:
  - 01-metodo-pedagogico/filosofia-ensenanza.md
  - 03-apps-herramientas/indice-apps.md
  - 08-sintesis/tecnologia-al-servicio-del-metodo.md
estado: completo
---

# Elefantito Matemático

## Resumen

Juego retro de matemática mental bilingüe (español/inglés), inspirado en el Dr. Ryuta Kawashima y en las técnicas de *Secrets of Mental Math* de Arthur Benjamin. Disponible en **web (Next.js)** y **Android (APK)**. Cuenta con 20 niveles progresivos desbloqueables, tutores interactivos bilingües por nivel, mecánica de juego retro con elefante y barriles, y audio narrado alojado en Cloudflare R2.

**Estado actual: terminado y en producción.**

---

## Propósito Pedagógico

Elefantito existe porque Luis no entiende la formación musical como entrenamiento de dedos, sino como entrenamiento del sistema nervioso completo. La aritmética mental rápida funciona como un gimnasio del córtex prefrontal: obliga al alumno a sostener atención, manipular información en memoria de trabajo, inhibir impulsos y responder bajo presión temporal.

La conexión con la música no está en que las matemáticas "se parezcan" a la armonía. Está en el tipo de cerebro que ambas actividades exigen. Un estudiante que va a escribir corales, escuchar voces simultáneas, anticipar funciones armónicas y sostener intención consciente antes de tocar necesita un prefrontal fuerte.

El juego integra dos líneas de investigación:
- **Dr. Ryuta Kawashima**: el cálculo mental rápido activa el córtex prefrontal de forma más intensa que la mayoría de actividades cognitivas (*Brain Age*).
- **Arthur Benjamin**: técnicas de matemática mental que permiten operar números grandes de izquierda a derecha, en voz alta, sin papel. 15+ técnicas implementadas en los 20 niveles.

Integrado con Kahneman: la matemática mental entrena el Sistema 2 — el sistema deliberado que permite detener la reacción automática y construir intención.

En clases presenciales, este entrenamiento es obligatorio para alumnos de música. En el website, la app está disponible para cualquier usuario como herramienta cognitiva.

### El orden: por qué Memoria va antes que Matemáticas

Elefantito no es la primera app cognitiva del camino — es la segunda. El alumno empieza por la **App Memoria – Nemotecnia** (el sistema fonético que asocia dígitos a consonantes, ignorando las vocales, para volver los números palabras memorizables). La razón es secuencial: solo cuando el alumno *retiene números con fluidez* tiene sentido el cálculo mental, porque la matemática mental rápida exige sostener resultados intermedios grandes en memoria de trabajo. Memoria construye la plantilla; Elefantito la ejercita bajo presión. Es el mismo principio "Memoria es primero y es todo" del método.

### El porqué de fondo: gimnasio del cerebro en la era de la IA

Así como quien entra al taller de Luis entra también al gimnasio físico, el alumno arranca por el **desarrollo físico de su cerebro**. En la era de "todo lo hace ChatGPT", mantener el cerebro irrigado y funcionando nunca fue más importante: por un lado para no perderlo por desuso, y por otro para no quedar reducido a consumidor pasivo de las corporaciones que nos necesitan comprando lo que no necesitamos. El entrenamiento cognitivo no es un adorno propedéutico — es la condición para extraer el valor máximo de los estudios y de la vida. Esto enlaza directamente con "no puedes tercerizar tu entendimiento" (Karpathy, ver `clases-ia/00_instrucciones/conceptos_no_olvidar.md`): cuanto más potente la IA, más vale el cerebro que la dirige.

---

## Los 20 Niveles

### Progresión completa

| Nivel | Técnica | Tipo de Problema |
|-------|---------|-----------------|
| 1 | Suma básica (1 dígito) | 1–9 |
| 2 | Suma/resta básica (1 dígito) | 1–9 |
| 3 | Suma dos cifras | 11–99 |
| 4 | Suma tres cifras | 100–999 |
| 5 | Suma 4d + 3d (sin ceros) | 1,000–9,999 + 100–999 |
| 6 | Suma dos cifras avanzada | 11–99, sin unidades ≠ 0 |
| 7 | Suma tres cifras (sin ceros) | 100–999 |
| 8 | Redondeo y compensación | 3d + número que termina en 91–99 |
| 9 | Suma compleja 4d + 3d | 1,000–9,999 + 100–999 |
| 10 | **Complementos a 100** | Técnica digit-by-digit (Benjamin) |
| 11 | **Complementos a 1,000** | Extensión de complementos |
| 12 | Resta sin préstamo (2d) | 30–99 |
| 13 | Resta sin préstamo (3d) | 100–999 |
| 14 | **Redondeo y compensación en resta** | Números que terminan en 7–9 |
| 15 | **Resta con complemento (3d)** | 200–999 con análisis de redondeo |
| 16 | **Tablas de multiplicación** | 2×2 a 12×12 |
| 17 | **Tablas de 11 y 12** | Multiplicación especializada |
| 18 | **Factorización (11 ó 12)** | 2d × múltiplos de 11/12 |
| 19 | **Multiplicación 2d×1d (distributiva)** | 12–99 × 2–9 |
| 20 | **Multiplicación 3d×1d (distributiva extendida)** | 100–999 × 2–9 |

*(Además, el catálogo interno documenta tipos de problema hasta el 24, incluyendo división exacta 2d/3d y fracciones decimales cíclicas — extensibles como niveles futuros.)*

### Técnicas de Arthur Benjamin implementadas

Las siguientes técnicas de *Secrets of Mental Math* tienen tutores interactivos completos:

- Complementos a 100 y 1,000 (niveles 10–11)
- Propiedad distributiva izquierda-a-derecha (niveles 19–20)
- Factorización por 11 y 12 (nivel 18)
- Redondeo y compensación en suma y resta (niveles 8, 14–15)
- Tablas multiplicativas extendidas (niveles 16–17)
- División izquierda-a-derecha (planificada)
- Fracciones decimales cíclicas — 1/7 = 142857, 1/11 = 09–90 (planificada)

---

## Mecánica de Juego

- **Objetivo**: llenar la repisa con 20 barriles
- **Respuesta correcta**: el elefantito lanza un barril
- **Error o tiempo agotado**: se retira un barril
- **Tiempo por pregunta**: configurable (default 10s, rango 3–25s)
- **Progresión bloqueada**: hay que completar el tutor del nivel actual para jugar; hay que completar el juego para desbloquear el siguiente
- **Estética**: pixel art retro, fuente `Press Start 2P`, scanlines, colores neon verde/cian
- **Audio**: 24 tracks de música aleatoria desde Cloudflare R2; efectos de sonido por acción

---

## Tutor Bilingüe por Nivel

Cada nivel tiene un componente `TutorLevel[N].jsx` dedicado (20 archivos, 7–16 KB cada uno). Cada tutor:

1. Explica la técnica mental del nivel (bilingüe español/inglés)
2. Practica paso a paso con el alumno antes de soltarlo al juego cronometrado
3. Tiene sistema de pistas y rastreo de errores
4. Incluye audio narrado en ambos idiomas alojado en Cloudflare R2
5. Termina con botón "Entendido, estoy listo" que desbloquea el juego

El tutor del Nivel 1 explica por qué el cálculo mental pertenece a un curso de música: transposición, memoria de trabajo, procesamiento secuencial, atención, Kawashima, *Brain Age*, Arthur Benjamin y transferencia cognitiva entre música y cálculo.

---

## Plataformas

### Web (Next.js)

- **Rutas**: `/es/apps/matematicas-mentales/jugar` y `/en/apps/matematicas-mentales/jugar`
- **Componente principal**: `components/apps/elefantito-nextjs/ElefantitoApp.jsx`
- **27 archivos JSX** (~8,000–10,000 líneas de código)
- **Progreso**: `localStorage` con versionado (`"locked-v1"`)
- **Estado global**: React Context API (`GameProvider`, `LanguageProvider`)
- **Localización**: `next-intl`, archivos `es.json` y `en.json`
- **Assets**: `public/elefantito_piso.png`, `public/elefantito_aire.png`, `public/barril.png`

### Android

- **APK en español**: `https://pub-2de970e8bf224791a9ab6d06fa62ce19.r2.dev/APKs/elefantito-matematico.apk`
- **APK en inglés**: `https://pub-2de970e8bf224791a9ab6d06fa62ce19.r2.dev/APKs/little-elephant-math.apk`
- **Distribución**: descarga directa desde el catálogo del website
- **Código fuente**: `D:\Android Studio\Utility apps\elefantitomatematico` (repositorio separado)
- **Tecnología**: Kotlin nativo con Jetpack Compose — **no es un WebView ni wrapper**. App completamente nativa con arquitectura MVVM.
- **Target SDK**: Android 36 (última versión). Min SDK 24 (Android 7.0+)
- **Offline total**: los 28 archivos MP3 van empaquetados localmente (24 pistas de música + 2 de tutor + efectos). No necesita conexión a internet.
- **Progreso**: `SharedPreferences` (equivalente al `localStorage` de la web)
- **20 niveles idénticos** a la web, misma mecánica de 20 barriles, tutores bilingües
- **Audio de tutor**: solo los niveles 1 y 2 tienen narración de voz — igual en web y Android. Los niveles 3–20 tienen tutores interactivos paso a paso que no la necesitan.
- **Teclado numérico propio** en pantalla (no el del sistema)
- **Retrato fijo** (portrait locked)

### HTML Legacy

- **Estado**: archivado en `/archive/apps/elefantito-legacy.html`
- **No enlazado** desde ninguna parte de la aplicación actual
- **Propósito**: referencia histórica — tenía 8 niveles y récord diario local

---

## Integración en el Ecosistema

Elefantito no reemplaza solfeo, armonía ni entrenamiento auditivo. Prepara el terreno cognitivo para que esos entrenamientos operen mejor. Es una herramienta auxiliar del mismo ecosistema:

- Apps de oído absoluto y relativo
- Maestro Virtual para validación MIDI en tiempo real
- Storm Sequencer para composición y entrega de ejercicios
- Curso de armonía SATB y escritura coral

**En el catálogo público** (`data/apps/apps-catalog.ts`):
- Slug: `matematicas-mentales`
- Categoría: `cognitive`
- Features declaradas: 20 niveles progresivos, tutores bilingües, técnicas reales de matemática mental, progresión bloqueada, web + APK Android

**Blog post de lanzamiento**: `content/blog/es/2026-05-27-propedeutico-listo-apps-matematicas-memoria.mdx` — "El propedéutico ya está listo, y las primeras apps cognitivas también"

---

## Stack Técnico

| Capa | Tecnología |
|------|-----------|
| Framework | Next.js 14+ (React Server + Client Components) |
| Estado | React Context API |
| Localización | next-intl |
| Estilos | Tailwind CSS |
| Fuente | Press Start 2P (Google Fonts) |
| Almacenamiento | localStorage |
| Audio | Web Audio API + MP3 en Cloudflare R2 |
| Android | Kotlin/Jetpack Compose nativo. Audio empaquetado localmente. Offline total. |
| TypeScript | Sí (componentes principales .tsx) |

---

## Historial de Cambios

- **2026-04-07** — Creación inicial (borrador)
- **2026-05-26** — Llenado del propósito pedagógico y versión con 6 niveles documentada
- **2026-05-29** — Reescritura completa. Luis terminó el proyecto en web y Android. Actualización a 20 niveles, 25 tipos de problema, 15+ técnicas de Arthur Benjamin implementadas, APK en Cloudflare R2, HTML legacy archivado. Estado cambiado a `completo`.
- **2026-06-04** — Entrevista a Luis: añadido el orden cognitivo (Memoria antes que Matemáticas y por qué) y el argumento de fondo "gimnasio del cerebro en la era de la IA" (no perder el cerebro por desuso; no caer en consumidor pasivo). Conexión con Karpathy "no puedes tercerizar tu entendimiento".
