---
titulo: "Stack Tecnológico"
tipo: contexto
ultima_actualizacion: 2026-07-03
relacionado_con:
  - 02-plataforma-web/arquitectura.md
  - 05-operaciones/infraestructura.md
  - 03-apps-herramientas/indice-apps.md
estado: en_progreso
---

# Stack Tecnológico — Storm Studios Learning

## Resumen
Todas las herramientas, plataformas y tecnologías que usa Storm Studios Learning. Luis opera como "vibe coder" — construye con IA sin formación formal en programación. El stack es moderno, económico y deliberadamente sin dependencias innecesarias.

---

## Plataforma Web

| Tecnología | Detalle |
|-----------|---------|
| **Framework** | Next.js 16 con App Router |
| **UI Library** | React 19 |
| **Lenguaje** | TypeScript |
| **Estilos** | Tailwind CSS v4 |
| **Contenido** | MDX |
| **Internacionalización** | next-intl |
| **Hosting** | Vercel (plan Hobby — gratuito) |
| **Dominio** | stormstudios.com.mx |

---

## Apps móviles (Android / iOS)

| Tecnología | Detalle |
|-----------|---------|
| **Desarrollo Android** | Android Studio |
| **Desarrollo iOS** | En curso (entrevista 2026-06-11) — toolchain por documentar (¿Mac/Xcode? ¿wrapper?) |
| **Lenguaje original** | Python → APK (proceso inicial de Luis) |
| **Estado actual** | Carpetas de proyecto entregadas a Claude Code / Codex / Antigravity para desarrollo. En paralelo se construyen las web apps gratuitas y sus versiones móviles de paga (Android e iOS) — estrategia en decisiones-clave.md 2026-06-11 |
| **Apps publicadas** | **11 webapps gratuitas** en stormstudios.com.mx (verificado 2026-07-03; catálogo en `indice-apps.md`). Versiones Android/iOS en preparación para venta a precio bajo en Play Store / App Store. **Sin descarga directa de APKs** — eliminada del modelo (contradicción resuelta por Luis, 2026-07-03) |

---

## Herramientas Web Propias

| Herramienta | Tecnología | Descripción |
|-------------|-----------|-------------|
| **Storm Sequencer v3.0** | HTML/vanilla JS | Secuenciador musical online con exportación MIDI |
| **Maestro Virtual** | API Next.js + validación MIDI | Validador en tiempo real de ejercicios del curso |

---

## Juegos Educativos

| Herramienta | Tecnología |
|-------------|-----------|
| Juegos de entrenamiento auditivo | Godot 4 / GDScript |

---

## Email y Comunicación

| Servicio | Detalle |
|---------|---------|
| **Email profesional** | Zoho Mail Standard |
| **Contacto público** | info@stormstudios.com.mx |
| **Teléfono** | 55 5103 1758 (Ciudad de México) |

---

## Almacenamiento y Datos

| Servicio | Uso |
|---------|-----|
| **Google Drive** | Archivos generales (vía suscripción Gemini Pro) |
| **Firebase** | Base de datos en JSON para la plataforma |
| **Audio assets** | [LLENAR: estado actual de migración desde Dreamhost] |

---

## Herramientas de Desarrollo

| Herramienta | Uso |
|------------|-----|
| **Claude (Cowork, Claude Code)** | IA principal para desarrollo, documentación y KB |
| **ChatGPT** | IA secundaria — especialmente para desarrollo Android en fases iniciales |
| **Gemini** | IA secundaria — usado en fases iniciales de compilación Android |
| **Codex / Antigravity** | Desarrollo de apps entregando carpeta de proyecto |
| **Sistema operativo** | Windows (PowerShell) |
| **Equipos** | PC de escritorio + laptop |

---

## Flujo de Trabajo con IA

Luis no escribe código manualmente. Su flujo es:
1. Define la funcionalidad o el cambio que necesita (en lenguaje natural)
2. Entrega el folder del proyecto a la IA (Claude Code, Codex o Antigravity)
3. La IA implementa el cambio completo
4. Luis prueba y valida el resultado

Para el KB y la documentación, trabaja en sesiones de dictado con Claude (Cowork).

**Convicción estratégica:** "El futuro está en mis datos, no en mis habilidades para usar la IA." La calidad del trabajo de la IA depende de la calidad de los datos que Luis ha acumulado en 35 años — no de sus habilidades técnicas de prompting.

---

## Pendientes

- Estado actual de la migración de audio assets desde Dreamhost
- Detalles del flujo de trabajo específico con cada herramienta de IA

---

## Historial de Cambios
- 2026-04-07: Creación inicial (borrador)
- 2026-04-16: Llenado sustancial con stack completo extraído del sitio, memoria de sesiones anteriores y dictado de Luis. Estado: `en_progreso`.
- 2026-06-11: Sección "Apps Android" → "Apps móviles (Android / iOS)" — iOS en desarrollo activo confirmado por entrevista; toolchain iOS por documentar; señalada la contradicción "10 apps en Google Play" vs decisión Play Store del 05-22.
- 2026-07-03: **Contradicción resuelta por Luis:** la descarga directa de APKs (el mecanismo que describía la documentación de mayo) queda eliminada del modelo hacia adelante; el dato "10 apps en Google Play" era incorrecto. Estado real: 11 webapps gratuitas publicadas en el website; versiones móviles de paga en preparación para las tiendas. Toolchain iOS sigue pendiente de documentar.
