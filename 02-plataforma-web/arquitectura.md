---
titulo: "Arquitectura de la Plataforma Web"
tipo: spec
ultima_actualizacion: 2026-04-10
relacionado_con:
  - 00-contexto/stack-tecnologico.md
  - 02-plataforma-web/maestro-virtual.md
estado: en_progreso
---

# Arquitectura de la Plataforma Web

## Resumen
La plataforma web de Storm Studios está concebida principalmente como un sitio educativo y promocional. Su función central es ofrecer gratuitamente contenidos del curso de armonía y entrenamiento auditivo, mientras sirve como embudo para promocionar clases presenciales, talleres y materiales vendidos por Luis, incluyendo libros en Kindle. De manera secundaria, también puede contribuir a aumentar la visibilidad de contenidos en video con miras a una futura monetización en YouTube.

## Propósito de la plataforma
El sitio no está pensado como una aplicación compleja centrada en lógica de cliente o estado interactivo pesado, sino como una plataforma de contenido estructurado, con secciones interactivas puntuales. El objetivo es equilibrar tres funciones:

- **Educación abierta:** ofrecer acceso gratuito a materiales formativos.
- **Promoción profesional:** presentar la propuesta de valor de Luis como maestro y músico.
- **Escalabilidad de contenido:** permitir crecer ordenadamente en páginas, materiales, idiomas y recursos.

## Secciones principales
La plataforma se divide en tres grandes grupos de secciones:

### 1. Secciones interactivas
Son las áreas con mayor valor funcional dentro del sitio.

- **Curso de armonía**
- **Página de apps / herramientas**

### 2. Secciones de promoción
Presentan la identidad profesional y la oferta de valor.

- **Quién soy**
- **Mi Método**
- **Clases / Taller**
- **El Libro**

### 3. Secciones de comunidad
Ayudan a crear relación continua con la audiencia.

- **Blog**
- **Contacto**

## Stack tecnológico
La plataforma está construida con un stack moderno basado en React y Next.js:

- **Framework principal:** Next.js 16 con App Router
- **UI library:** React 19
- **Lenguaje:** TypeScript
- **Estilos:** Tailwind CSS v4
- **Contenido estructurado:** MDX
- **Internacionalización:** next-intl
- **Lógica del servidor / endpoints:** rutas API dentro de `app/api`

En conjunto, se trata de un sitio web moderno orientado a contenido, internacionalización y mantenibilidad.

## Estructura general del proyecto
La arquitectura sigue el modelo de **Next.js App Router**, donde el sistema de rutas define gran parte de la organización del sitio.

### Routing e internacionalización
- La carpeta `app/` contiene la base de la aplicación.
- Existe un segmento dinámico **`[locale]`** para manejar versiones por idioma.
- La internacionalización se organiza alrededor de este segmento, permitiendo mantener una estructura clara por idioma.

### Endpoints del servidor
- La carpeta **`app/api`** contiene endpoints para lógica del lado del servidor.

### Componentes reutilizables
- Los elementos de interfaz reutilizables viven en **`components/`**.
- Esto permite separar presentación y composición visual del contenido y del routing.

### Contenido y datos
- El contenido está desacoplado de la UI y distribuido en carpetas como:
  - `content/`
  - `data/`
  - `messages/`
  - `i18n/`

Esta separación facilita mantener textos, traducciones y contenido editorial sin mezclarlo con la lógica visual.

### Recursos estáticos y SEO técnico
- Los assets estáticos viven en **`public/`**.
- También existen archivos y configuraciones para SEO técnico, como:
  - `sitemap`
  - `robots`
  - redirects
  - compatibilidad con contenido MDX

## Idea arquitectónica central
La plataforma está pensada como una **arquitectura orientada a contenido**, no como una SPA pesada. El principio que guía el diseño es la **separación entre contenido, presentación y routing**.

Las prioridades arquitectónicas son:

- **Internacionalización**
- **SEO**
- **Mantenibilidad**
- **Escalabilidad del contenido**
- **Reutilización de componentes**

En términos prácticos, esto significa:

- el routing resuelve navegación, estructura y versiones por idioma,
- el contenido vive separado en MDX, data y mensajes,
- la presentación se construye con componentes reutilizables,
- y el sistema completo está diseñado para crecer sin volverse caótico.

## Enfoque de diseño
La intención no es construir una aplicación extremadamente compleja en el cliente, sino un sitio sólido, escalable y bien organizado, capaz de soportar:

- más contenido educativo,
- más idiomas,
- nuevas herramientas o secciones,
- mejor posicionamiento SEO,
- y una evolución gradual hacia experiencias más interactivas cuando haga falta.

## Historial de Cambios
- 2026-04-10: Documento ampliado con propósito de la plataforma, secciones principales, stack actual, estructura general del proyecto y principio arquitectónico central.
- 2026-04-07: Creación inicial (borrador)
