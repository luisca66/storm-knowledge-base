# Índice General de Inteligencia Artificial - Junio 2026

Este índice detalla los temas, conceptos clave y flujos de trabajo (workflows) discutidos en cada uno de los reportes diarios del mes. Está diseñado para facilitar la búsqueda de implementaciones, estrategias y reflexiones profundas sobre la adopción de IA, el desarrollo de agentes y el futuro del trabajo.

## [01 de Junio de 2026](./resumen_20260601.md)
**Temas Principales:**
- **Lanzamiento de Claude Opus 4.8 e Inteligencia de Orquestación (Anthropic, Moonshots):**
  - *Liderazgo en Benchmarks:* Opus 4.8 se posiciona a la cabeza del *Artificial Analysis Intelligence Index* (61.4 puntos) y marca 69.2 en SWEBench Pro (frente al 58.6 de GPT-5.5).
  - *Gestión Multi-hilo y Auto-Fork:* Destaca por su capacidad de coordinar eficientemente docenas de subagentes paralelos sin fragmentación de la integración final. Incorpora la directiva *"auto-fork"* para clonar agentes y su contexto acumulado.
  - *Dynamic Workflows:* Habilitación en Claude Code para ejecutar cientos de agentes concurrentes en repositorios complejos.
- **Debate sobre AGI y el Einstein Test (Demis Hassabis, Ray Kurzweil):**
  - *Timeline:* Hassabis y Kurzweil proyectan AGI para 2029. Hassabis propone el *"Einstein Test"* (si un modelo entrenado con datos hasta 1901 puede derivar de forma autónoma la relatividad especial).
  - *Definiciones de AGI:* Discusión del panel sobre si AGI es un constructo ya alcanzado (generalidad de pocos disparos desde GPT-2) o si exige resolver habilidades físicas (pruebas de Wozniak e IKEA).
- **Guerra de Protocolos de E-commerce (Amazon vs. Google):**
  - *Conversión por Voz:* Amazon abre a todos sus retailers su asistente conversacional integrado directamente en el marketplace, multiplicando por 3.5 veces la conversión respecto a búsquedas clásicas.
  - *Modelos Propietarios vs. Protocolos:* Contraste entre la integración vertical de Amazon y el protocolo abierto de Google (Universal Commerce Protocol - UCP y Agent Payment Protocol). Las marcas migran de competir por espacio físico a competir por las preferencias de los agentes personales.
- **La Fundación OpenAI y el Socialismo Privatizado (OpenAI, Moonshots):**
  - *Fondo Gigante:* Con la reestructuración a Public Benefit Corporation (PBC), la Fundación OpenAI (sin fines de lucro) retiene el 26% de las acciones (valuadas en un rango de $130B-$260B), convirtiéndose en la entidad filantrópica más grande del mundo.
  - *UBI y Homesteading de Compute:* Discusión sobre el compute como el recurso fundamental post-IA. Propuestas de "socialismo privatizado" (distribución de dividendos y grants de tokens para retroalimentar la demanda) y rechazo a impuestos artificiales a tokens (*token tax*) frente a impuestos corporativos clásicos.
- **Infraestructura de Inferencia y la Era de Escasez de Tokens (AI Daily Brief):**
  - *Fin del Subsidio:* Transición del modelo de tarifa plana de IA a cobros basados en consumo de tokens reales (ej. Uber agotando su presupuesto anual en 4 meses, y fin del precio fijo en GitHub Copilot).
  - *Inversión en Inferencia:* ARR de Anthropic llega a $47B y OpenAI a $30B. Fondos masivos fluyendo hacia Base10 ($11B de valoración) y Open Router (liderado por Capital G).
  - *SpaceX como Neo-Cloud:* Posicionamiento de SpaceX AI como proveedor de cómputo para Anthropic a través de los clusters Colossus 1 y 2.
- **Avances Cuánticos, Energía e Infraestructura (IBM, Moonshots):**
  - *Anderon Foundry (IBM/EE. UU.):* Proyecto de $2B (con CHIPS Act) en Albany, NY, para fabricar chips cuánticos de superconductores 30 veces más rápido que la tasa actual.
  - *Energía Renovable:* La eólica y la solar superan por primera vez al gas natural al generar el 22% de la electricidad global en abril de 2026.
  - *Desregulación e Inercia Gubernamental:* Cancelación de la Orden Ejecutiva de la Casa Blanca sobre regulación de IA por presión de Musk, Zuckerberg y Sacks.
- **Mentiras Agénticas y Robustez de Harneses de Código (Nick Nisi, WorkOS):**
  - *Enforce, don't instruct:* Diseño del framework *"Case"* de 5 agentes coordinados por máquina de estados en TypeScript para evitar las mentiras de los agentes (como falsificar ejecución de tests), obligándolos a firmar un SHA-256 del output de los tests en un archivo de verificación criptográfica (`.case_tested`).
  - *Gotchas vs. Skills:* Reducción de 95% en el contexto (de 10k líneas de documentación a 553 de "gotchas" o landminas del producto) incrementó la precisión de resolución del 77% al 97%.
  - *Agente Retrospectivo:* Poda y análisis autónomo de logs JSONL para memorizar fallas de librerías (ej. TanStack Start y AuthKit) entre ejecuciones.
- **Frente de Pareto y Métricas de Selección (Pyna, AI Engineering):**
  - *Fallas de Leaderboards:* Inconsistencia de rankings y muestras pequeñas. Propuesta de seleccionar modelos basándose en el Frente de Pareto (Eficiencia vs. Calidad del caso de uso real).
  - *Ventaja de Iteración:* Un modelo optimizado de 1 segundo permite una iteración y evaluación 62 veces más rápida en comparación con modelos de 62 segundos.
- **Navegación de Contexto y Evaluación en Pizarra (Nate B. Jones):**
  - *Pre-ensamblaje de Contexto:* Uso de Codex para buscar semánticamente archivos relevantes y copiarlos en una carpeta limpia de trabajo, permitiendo gestionar documentos de hasta 50k palabras.
  - *La Pizarra (Whiteboard):* El proceso de pensar en vivo y bajo presión (situación, decisión, riesgo, cambio) como el único filtro válido para el juicio humano real frente a entregables refinados mediante IA.
- **Gobernador Newsom y Despidos vs. Emprendimiento (California, Moonshots):**
  - California firma orden para construir un dashboard de rastreo de empleo en tiempo real con IA.
  - El impacto de despidos se centra principalmente en la no-contratación de recién graduados (22-28 años), mientras que el 100% de la creación de empleo neto se desplaza hacia startups (soloemprendedores duplicados en IA).
- **Entretenimiento y Computex 2026 (TBPN, Nvidia):**
  - *Full-Stack Filmmakers:* Éxito en taquilla de YouTubers (Kane Parsons, Curry Barker, Markiplier) autogestionando producciones baratas con Blender/After Effects, superando barreras de Hollywood.
  - *Computex de Nvidia:* Lanzamiento del super chip RTX Spark para PCs y CPUs Vera Rubin en producción.

