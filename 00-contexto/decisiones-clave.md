---
titulo: "Decisiones Clave"
tipo: decision
ultima_actualizacion: 2026-07-03
estado: en_progreso
---

# Decisiones Clave

## Resumen
Registro de decisiones importantes del proyecto y su razonamiento. Esto es crítico para que una IA entienda POR QUÉ las cosas son como son y no proponga cambios que ya fueron considerados y descartados.

## Formato de Registro

Cada decisión sigue este formato:

```
### [Título de la decisión]
**Fecha:** YYYY-MM-DD
**Contexto:** Por qué surgió esta decisión.
**Decisión:** Qué se decidió.
**Razonamiento:** Por qué se eligió esta opción.
**Alternativas consideradas:** Qué otras opciones había.
**Consecuencias:** Qué implica esta decisión.
```

---

### Estudiantes deben usar el secuenciador Storm Studios (no DAWs comerciales)
**Fecha:** [LLENAR]
**Contexto:** Los estudiantes necesitan una herramienta para completar ejercicios MIDI.
**Decisión:** El secuenciador propio de Storm Studios es la herramienta obligatoria.
**Razonamiento:** Los archivos MIDI estándar no distinguen equivalentes enarmónicos (F# vs Gb). El secuenciador de Storm Studios exporta mensajes meta de key_signature que permiten la validación correcta. Además, enmarcado como decisión pedagógica.
**Alternativas consideradas:** DAWs comerciales (Logic, Ableton, etc.) — descartados por la limitación enarmónica del MIDI estándar.
**Consecuencias:** Dependencia del secuenciador propio; necesidad de mantenerlo y documentarlo.

### Migración de hosting a Vercel
**Fecha:** [LLENAR]
**Contexto:** [LLENAR]
**Decisión:** Cancelar Dreamhost y Mediafire, consolidar en Vercel Hobby + Zoho Mail + Google Drive.
**Razonamiento:** [LLENAR]
**Alternativas consideradas:** [LLENAR]
**Consecuencias:** Pendiente migración de audio assets con URLs hardcodeadas.

### Distribución de apps P03 — Play Store vs. descarga directa
**Fecha:** 2026-05-22
**Contexto:** Los videos del propedéutico están terminados (hito). P03 (Intervalos) requiere dos apps Android que actualmente se distribuyen como descarga gratuita desde el website. Con el propedéutico completo, cualquier persona puede llegar al website sin saber nada — pero las apps de P03 presentan fricción: el usuario debe encontrar la sección de descargas, bajar el APK y habilitarlo manualmente en Android.
**Decisión:** En evaluación. No se ha decidido aún.
**Opciones en análisis:**
- **Play Store** — menos fricción para el usuario, mayor alcance, proceso de publicación requerido ($25 USD, cuenta developer, AAB, keystore, assets de tienda, política de privacidad). Una vez publicado, las actualizaciones son sencillas.
- **Descarga directa desde website** — sin costo, control total, pero el usuario debe habilitar "fuentes desconocidas" en Android — fricción considerable para alumnos no técnicos.
**Consecuencias si se va a Play Store:** Necesidad de keystore firmado (archivo crítico — su pérdida impide actualizar la app para siempre). Proceso de revisión de Google (puede tomar días). Requiere política de privacidad aunque la app no recolecte datos.
**Próximo paso:** Confirmar qué apps son exactamente las dos de P03 (se asume Intervalos – Reconocimiento e Intervalos – Cantados) y decidir si se publican ambas o solo una como piloto.
**Actualización 2026-06-11:** Superada por la decisión "Apps: versiones web gratuitas + versiones móviles de paga". La pregunta ya no es *si* publicar en tiendas, sino *cuáles primero y a qué precio* — las 2 apps de P03 quedan como piloto recomendado.

### Apps: versiones web gratuitas + versiones móviles de paga (Android e iOS)
**Fecha:** 2026-06-11 (pensada unas semanas antes; documentada y evaluada hoy)
**Contexto:** El modelo original era apps gratuitas. Las apps quedaron "hermosas" y Luis identificó disposición real a pagar por tenerlas en el celular. Hoy se programan en paralelo, según el tiempo lo permite, las web apps gratuitas y sus versiones Android e iOS.
**Decisión:** Todas las apps viven en versión web gratuita (el filtro freemium queda intacto). Las versiones móviles se venden a precio bajo en las tiendas (Google Play / App Store), buscando volumen y visibilidad.
**Razonamiento:** No se cobra el contenido — se cobra la conveniencia (celular, offline, pantalla de inicio). La web gratis ES el demo. Las herramientas de práctica diaria se usan en momentos muertos (transporte, esperas, gym), donde el navegador es torpe y la app nativa gana. Además las tiendas son un canal de descubrimiento que el website no tiene: cada app es un anzuelo hacia el embudo. Resuelve de paso la fricción del APK señalada en la decisión del 2026-05-22.
**Alternativas consideradas:** (a) Todo gratis con descarga directa — fricción de "fuentes desconocidas" y cero presencia en tiendas; (b) cobrar también la web — rompería el filtro freemium; (c) suscripción — descartada: a estos precios genera resentimiento y choca con la marca de generosidad del método.
**Consecuencias:** Mantenimiento multiplicado (10+ apps × 3 plataformas) para un solo desarrollador; cuotas de tienda (Google $25 único, Apple ~$99 USD/año) y comisiones del 15-30%; el keystore de Android se vuelve activo crítico. **La métrica correcta es tráfico calificado al ecosistema, no el ingreso directo** — a ~$2.99 menos comisión se necesitan cientos de ventas para igualar la colegiatura mensual de un solo alumno particular. **Acordado:** piloto con las 2 apps de P03 de punta a punta (publicar, poner precio, medir ventas y tráfico un par de meses) antes de portar el catálogo completo; pago único, nunca suscripción.
**Actualización 2026-07-03 (Luis):** la decisión se consolida y **la descarga directa de APKs queda eliminada del modelo** — la contradicción señalada en `stack-tecnologico.md` queda resuelta: la distribución es únicamente webapps gratuitas en el website + versiones móviles de paga en Play Store / App Store. Estado real: **las 11 webapps ya están publicadas** en stormstudios.com.mx (9 de oído + 2 cognitivas; se sumó *Cantar Acordes* al catálogo). La única inconclusa es **Intervalos – Cantados** (4 de 12 niveles en vivo; la versión completa ya está terminada en otro folder y solo falta migrarla — se da por resuelta).

### Sin límites a priori para la autonomía de la IA
**Fecha:** 2026-06-11
**Contexto:** En la entrevista de propósito del KB se le preguntó a Luis qué decidió que la IA nunca haga sin él, por más capaz que sea.
**Decisión:** No definir fronteras por adelantado. "No tengo ninguna idea y ningún prejuicio — iré viendo conforme el proyecto vaya creciendo, y las IAs también."
**Razonamiento:** Los límites correctos solo pueden descubrirse en la práctica, no postularse en abstracto. Definirlos hoy sería congelar prejuicios sobre capacidades que cambian cada mes. Mientras tanto: "me fascina trabajar con ustedes".
**Alternativas consideradas:** Listas de acciones prohibidas o de aprobación obligatoria — descartadas por prematuras.
**Consecuencias:** La frontera de autonomía es un descubrimiento continuo, no una política fija. Cuando aparezca el primer límite real en la práctica, documentarlo aquí.

### CLAUDE.md como fuente única del schema; AGENTS.md reducido a stub
**Fecha:** 2026-06-11
**Contexto:** El KB mantenía dos schemas maestros paralelos (CLAUDE.md para Claude, AGENTS.md para Codex) sincronizados a mano. Varios lints (al menos 4) señalaron el riesgo de divergencia, y el 2026-06-11 se confirmó divergencia real: cada copia tenía contenido que la otra no (la regla del doble reglamento de clases-ia y el pendiente de localStorage solo existían en AGENTS.md). Además, tres archivos competían por declararse "leer primero" (CLAUDE.md, README.md, index.md), e index.md describía a AGENTS.md como maestro y a CLAUDE.md como "histórico" — jerarquía invertida respecto a lo que CLAUDE.md decía de sí mismo.
**Decisión:** CLAUDE.md es la única fuente de verdad del schema, redactado de forma agnóstica de agente ("la IA" en vez de "Claude"/"Codex") para servir a cualquier IA presente o futura. AGENTS.md queda como stub de redirección. Roles claros: README = portada del repo privado, index = catálogo, log = historial. Ningún otro archivo se declara "leer primero".
**Razonamiento:** Claude Cowork carga CLAUDE.md automáticamente y completo en cada sesión — cero fricción para el colaborador de mayor volumen. Codex puede seguir el stub con un solo salto. Una fuente única elimina la sincronización manual, que ya había fallado en la práctica. La redacción agnóstica es coherente con el propósito del KB: que *cualquier* IA futura pueda operarlo.
**Alternativas consideradas:** (a) AGENTS.md como maestro — es el estándar multi-agente emergente, pero Claude (el colaborador principal) no lo carga automáticamente, mientras que Codex sí puede seguir un stub; (b) symlink — frágil en Windows y en checkouts de git; (c) seguir sincronizando a mano — descartado por evidencia: ya divergieron.
**Consecuencias:** Al editar el schema solo se toca CLAUDE.md. Si algún agente reconstruye AGENTS.md con contenido propio, hay que revertirlo y restaurar el stub. La unificación del propósito (dos niveles: continuidad hoy, autonomía mañana) y del alcance (tres líneas de negocio) quedó plasmada en CLAUDE.md §2.

### Los libros serán obras de consulta — legado y reputación, no línea de ingreso principal
**Fecha:** 2026-07-03
**Contexto:** El radar de IA registró la caída del 57% en ventas de libros de no ficción (Tim Ferriss, junio 2026): los libros de consulta y tutoriales están siendo sustituidos por chatbots, y el valor de mercado migra hacia la narración y el entretenimiento. La IA planteó a Luis si su plan de libros Kindle debía pivotar hacia lo narrativo.
**Decisión:** No pivotar. *Los Seres Musicales* y los libros que vengan **serán libros de consulta**, con plena conciencia de la señal del mercado.
**Razonamiento:** Los libros no juegan en la categoría "ingreso" — juegan en la categoría **respeto y legado**. Ganándose el respeto de la comunidad musical, Luis espera que se conviertan en parte de su legado. El dinero, mientras tanto, llega por la vaca lechera (las clases particulares, $1,500 MXN por sesión) y por lo que se pueda extraer de la plataforma y de los videos de YouTube. Un libro de consulta serio construye autoridad ante la comunidad de un modo que un libro "narrativo para vender" no lograría — y la autoridad alimenta el embudo completo.
**Alternativas consideradas:** Reorientar los libros hacia narrativa/historia personal (la categoría que sobrevive comercialmente según el radar) — descartado: optimizaría el ingreso del peldaño equivocado de la escalera.
**Consecuencias:** Cero presión de monetización sobre los libros; los manuales Kindle de las apps siguen en la escalera como artículos de precio bajo; la métrica de éxito de los libros es reputación y permanencia, no ventas. Coherente con el rol del website ($0 por diseño): las piezas de legado no se miden en dinero.

## Historial de Cambios
- **2026-07-03** — Decisión nueva: libros como obras de consulta (legado/reputación, no ingreso). Decisión de apps actualizada: descarga directa eliminada del modelo, 11 webapps publicadas, contradicción de distribución resuelta.
- **2026-06-11** — Entrevista de propósito: 2 decisiones nuevas (apps web-gratis/móvil-de-paga con piloto P03; sin límites a priori a la autonomía de la IA). Decisión Play Store del 05-22 marcada como superada.
- **2026-06-11** — Decisión de fuente única del schema documentada (CLAUDE.md maestro, AGENTS.md stub). Estado: borrador → en_progreso.
- **2026-05-22** — Decisión Play Store documentada (en evaluación).
- 2026-04-07: Creación inicial con 2 decisiones documentadas
