---
titulo: "Elefantito Matemático"
tipo: tecnico
ultima_actualizacion: 2026-05-26
relacionado_con:
  - 01-metodo-pedagogico/filosofia-ensenanza.md
  - 03-apps-herramientas/indice-apps.md
  - 08-sintesis/tecnologia-al-servicio-del-metodo.md
estado: en_progreso
---

# Elefantito Matemático

## Resumen
Juego retro de matemática mental bilingüe (español/inglés), inspirado en Kawashima y en técnicas de *Secrets of Mental Math* de Arthur Benjamin. La versión actual del website ya no es solo el HTML/vanilla JS original: vive integrada en Next.js como app web jugable dentro de la ruta `/apps/matematicas-mentales/jugar`, con tutoriales por nivel, audio narrado, progreso local y mecánica de juego por desbloqueo.

## Propósito Pedagógico
Elefantito Matemático existe porque Luis no entiende la formación musical como entrenamiento de dedos, sino como entrenamiento del sistema nervioso completo. La aritmética mental rápida funciona como un gimnasio del córtex prefrontal: obliga al alumno a sostener atención, manipular información en memoria de trabajo, inhibir impulsos y responder bajo presión temporal.

La conexión con la música no está en que las matemáticas "se parezcan" a la armonía de forma superficial. Está en el tipo de cerebro que ambas actividades exigen. Un estudiante que va a escribir corales, escuchar voces simultáneas, anticipar funciones armónicas y sostener intención consciente antes de tocar necesita un prefrontal fuerte. Por eso Luis puede presentar la app a sus alumnos presenciales con una frase directa: "vas a necesitar un cerebro muy poderoso".

El juego se inspira en la línea de investigación del Dr. Ryuta Kawashima sobre cálculo mental y activación prefrontal. Dentro del método, ese dato se integra con Kahneman: la matemática mental entrena el Sistema 2, el sistema deliberado que permite detener la reacción automática y construir intención.

En clases presenciales, este entrenamiento es obligatorio para alumnos de música. En el website, la app funciona como herramienta opcional para cualquier usuario: desde niños que practican sumas hasta adultos que quieren llevar su velocidad mental al límite.

## Spec del Juego
### Módulo de matemática mental

- Mapa de **6 niveles desbloqueables**.
- Cada nivel tiene pestaña **Tutor** y pestaña **Jugar**.
- El alumno debe completar/aceptar la lección del tutor antes de jugar.
- Progreso guardado en `localStorage` (`unlockedLevels`, `completedLessons`).
- Tiempo ajustable por pregunta: 3 a 25 segundos en la versión Next.js.
- Objetivo de cada partida: llenar la repisa con **20 barriles**.
- Respuesta correcta: el elefantito lanza un barril.
- Error o tiempo agotado: se retira un barril.
- Al completar un nivel, se desbloquea el siguiente.
- Diseño retro/pixel con fuente `Press Start 2P`, scanlines, mapa de niveles, assets de elefantito y barriles.
- Música de fondo y efectos alojados en Cloudflare R2.

### Progresión actual de niveles

| Nivel | Tipos de problema |
|-------|-------------------|
| 1 | Sumas 1 dígito, restas 1 dígito sin negativo, multiplicación 1x1 |
| 2 | Sumas 2 dígitos + 1 dígito, restas 2 dígitos - 1 dígito, divisiones exactas básicas |
| 3 | Sumas de dos números entre 11 y 89 |
| 4 | Sumas de tres dígitos + tres dígitos |
| 5 | Sumas por redondeo/compensación: segundo número cerca de la siguiente centena |
| 6 | Sumas de 4 dígitos + 3 dígitos, sin ceros internos |

### Tutor integrado

La versión nueva incluye tutoriales bilingües por nivel. El nivel 1 explica por qué el cálculo mental pertenece a un curso de música: transposición, memoria de trabajo, procesamiento secuencial, atención, Kawashima, *Brain Age*, Arthur Benjamin y transferencia cognitiva entre música y cálculo. Los niveles posteriores introducen la progresión práctica: números más grandes, resta, división, caminos reversibles, memoria de trabajo y técnicas de descomposición.

Cada tutor tiene audio narrado en español/inglés alojado en Cloudflare R2 y un botón de cierre tipo "Entendido, estoy listo" que marca la lección como completada.

### Módulo de memoria

Elefantito se conecta con una app separada de memoria basada en mnemotecnia clásica de números y letras. No busca entrenar "memoria musical" de forma genérica, sino una capacidad transversal: retener, asociar y recuperar información con velocidad y precisión.

Este módulo enlaza directamente con el principio del método: "Memoria es primero y es todo". La memoria entrenada es el puente entre intención y ejecución; sin una plantilla mental clara, el cuerpo no tiene qué obedecer.

### Relación con el curso musical

Elefantito no reemplaza solfeo, armonía ni entrenamiento auditivo. Prepara el terreno cognitivo para que esos entrenamientos puedan operar mejor. Es una herramienta auxiliar del mismo ecosistema que incluye:

- apps de oído absoluto y relativo;
- Maestro Virtual para validación MIDI;
- Storm Sequencer para composición y entrega de ejercicios;
- curso de armonía SATB y escritura coral.

## Estado Actual
### Versión actual observada en el repo del website

- Repo fuente: `C:\Users\Luis\Documents\claude_code\nuevo-website\storm-studios`
- Ruta Next.js: `app/[locale]/apps/matematicas-mentales/jugar/page.tsx`
- Componentes principales: `components/apps/elefantito-nextjs/`
- Catálogo público: `data/apps/apps-catalog.ts`
- Assets locales: `public/elefantito_piso.png`, `public/elefantito_aire.png`, `public/barril.png`, `public/images/app-matematicas-mentales.png`
- Versión HTML anterior: `public/apps/elefantito.html` conserva una implementación legacy con selector de 8 niveles y récord diario local.

### Por verificar

- Si la versión legacy `public/apps/elefantito.html` sigue enlazada en algún lugar o ya puede considerarse archivo histórico.
- Si la ficha pública del catálogo debe cambiar de "8 niveles" a "6 niveles" para coincidir con la versión Next.js.
- Si las técnicas avanzadas de Arthur Benjamin están planificadas para niveles futuros o quedaron fuera del rediseño actual.

## Tecnología
- Next.js / React para la versión actual integrada al website
- HTML / vanilla JavaScript para la versión legacy
- Estilo visual retro
- Bilingüe: español e inglés
- `localStorage` para progreso
- Cloudflare R2 para audio de tutorial, música y efectos

## Historial de Cambios
- 2026-04-07: Creación inicial (borrador)
- 2026-05-26: Llenado del propósito pedagógico, conexión con el método, módulos cognitivos y pendientes de verificación.
- 2026-05-26: Actualización con la versión real del repo `nuevo-website/storm-studios`: app Next.js con 6 niveles, tutor bilingüe, audio narrado, progreso local y versión HTML legacy identificada.
