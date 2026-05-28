---
titulo: "La Singularidad Organizacional (EXO 3.0) — Destilado de proyecto"
tipo: destilado
basado_en: "07-fuentes/moonshots-organizational-singularity-peter-diamandis-salim-ismail.md"
fuente_original: "The New Era of Jobs: Organizational Singularity | Moonshots Podcast EP #258"
autores_fuente:
  - Peter Diamandis
  - Salim Ismail
url_fuente: https://youtu.be/I9c8STV7Hnw
proposito: "Base de conocimiento para (1) docencia de IA y (2) asesoría de migración empresarial. Punto de partida para un proyecto con Claude Code."
idioma: es
estado: completo
fecha: 2026-05-28
---

# La Singularidad Organizacional (EXO 3.0)

> Versión reescrita, ordenada y completa de la conversación entre Peter Diamandis y Salim Ismail. No es una transcripción: es un destilado fiel pensado para enseñar y para asesorar. Todo concepto, marco, cifra, nombre y ejemplo del original está aquí, reorganizado por temas en lugar de por el orden del video.

---

## 0. Cómo usar este documento

Este documento tiene dos públicos en mente, que coinciden con tus dos roles:

1. **Como material docente.** Cada sección está escrita para poder convertirse en una clase o módulo. El glosario (§15) y el índice de fuentes (§16) sirven para construir un curso introductorio sobre cómo la IA agéntica reorganiza a las empresas.
2. **Como guía de asesoría.** Las secciones 8 a 12 son, en la práctica, el manual de campo: cómo diagnosticar a un cliente, qué métricas usar, cómo planear la transición y qué advertirle.

La sección final (§17) propone una forma concreta de convertir todo esto en un proyecto de Claude Code.

Una advertencia de honestidad intelectual que conviene transmitir a tus alumnos y clientes: esto es **la tesis de dos autores con una agenda** (venden un programa de transformación y un libro). El marco es valioso y bien razonado, pero está presentado por sus propios creadores. Lo trato aquí como una hipótesis fuerte y útil, no como una ley demostrada. Las cifras (80% de reducción de plantilla, mejoras de 100x, etc.) son sus estimaciones y proyecciones, no datos auditados.

---

## 1. Resumen ejecutivo

Durante casi un siglo, las empresas se organizaron en torno a la **jerarquía**: capas de personas coordinándose entre sí. La tesis central de este marco es que la IA agéntica vuelve obsoleto ese modelo, y que la empresa que sobreviva tendrá que reorganizarse en torno a la **inteligencia**.

Las ideas clave:

- El motivo histórico para que existan las empresas (los costos de coordinación y de ejecución eran más baratos dentro que fuera) **se rompe** cuando los agentes de IA hacen la coordinación y la ejecución casi gratis.
- Por eso fracasan más del 80% de los proyectos de IA en empresas: se está inyectando IA en flujos de trabajo diseñados para humanos. No se puede automatizar un cuello de botella humano; hay que rediseñar el flujo para que sea **nativo de IA**.
- La nueva empresa se organiza alrededor de un **núcleo de inteligencia** de seis capas (sensar, interpretar, decidir, orquestar, aprender, bajo un propósito), envuelto en una capa de **gobernanza y aseguramiento** que evita que los agentes se descarrilen.
- El camino de migración no es arreglar la empresa actual, sino construir un **gemelo digital nativo de IA en el borde** de la organización, migrando flujo por flujo, hasta que ese gemelo se vuelva el nuevo centro de gravedad.
- Estimación de los autores: una empresa promedio podrá operarse con el **20–25% del personal** actual, con mejoras de desempeño de hasta **100x** al año en los flujos automatizados. La transición de la economía tomará **5 a 7 años** ("la transición turbulenta").
- El riesgo no es tu competidor más grande: es el startup nativo de IA de dos o tres personas que ve tu margen jugoso y tu lentitud, y viene a comerte el almuerzo.

---

## 2. El problema: por qué "la IA mató a la empresa moderna"

### 2.1. La teoría de Coase y por qué existen las empresas

En 1937, el economista **Ronald Coase** publicó *The Nature of the Firm* (le valió el Premio Nobel). Su tesis: las grandes empresas crecen porque los **costos de transacción y de coordinación** son más baratos dentro de la organización que fuera de ella. Si tienes a todos en nómina, puedes darles órdenes y coordinar el trabajo mejor que negociando con el mercado abierto. Durante unos 80 años, las organizaciones funcionaron sobre esa lógica.

### 2.2. El linaje de pensadores

El marco se inscribe en una genealogía de pensamiento organizacional:

- **Ronald Coase** — los límites de la empresa los define el costo de coordinar.
- **Herbert Simon** — dónde se traza la frontera de la organización.
- **Clayton Christensen** — el *dilema del innovador*: a medida que creces, empresas más pequeñas entregan productos más baratos y te desplazan.
- **Stanley McChrystal** — cómo lograr coordinación a escala sin perder la conexión emocional con la organización (su trabajo en *Team of Teams*).
- **EXO 1.0** (Exponential Organizations, el libro original de Salim Ismail) — usar **comunidad, multitud (crowd) e IA** para extender el alcance de la empresa "de lado", más allá de sus propios límites.

El ejemplo canónico de EXO 1.0 es **Uber**: su función crítica —emparejar conductor y pasajero— **no ocurre dentro** de la organización, sino "en libertad", afuera. Cuando habilitas esa coordinación externa con tecnología, escalas sin tener todo en nómina. Así se "estiraba" la ley de Coase.

### 2.3. Dónde se rompe todo: la IA agéntica

La conclusión del marco es que **toda esa genealogía se rompe frente a la IA agéntica**. La ley de Coase deja de aplicar.

El razonamiento: dentro de una empresa, hacer algo tan simple como un sitio web exige pasar por capas de reuniones y aprobaciones —marca, privacidad, TI diciendo que no se puede—. Hoy puedes salir de la empresa, usar una herramienta como Vercel/v0 unos minutos, y tenerlo listo casi gratis, con tus lineamientos de marca, tu gusto de diseño, y hasta una docena de versiones probándose en el mercado.

La frase que captura esto (citada por Salim de un tuit cuyo autor no recordaba):

> **"Construir la funcionalidad es más barato que tener la reunión sobre la funcionalidad."**

Es decir: la **coordinación activa** se ha vuelto más cara que la **ejecución**, justo cuando la IA está desplomando el costo de ejecutar. Ese es el vuelco que rompe el modelo.

### 2.4. Por qué fracasa más del 80% de los proyectos de IA

Más del 80% de los proyectos de IA en empresas fracasan, y la causa es estructural: las empresas existentes están cableadas para flujos **humano-a-humano** —aprobaciones, cadenas de cuellos de botella, jerarquías—. Inyectar IA en esa arquitectura es automatizar los cuellos de botella humanos heredados.

La analogía: cuando se inventó la televisión, al principio se puso a los locutores de radio frente a una cámara. No se usaba el medio nuevo en absoluto. Lo mismo pasa al meter IA en organizaciones diseñadas para humanos. Para que funcione, necesitas un **entorno nativo de IA**, no un parche sobre lo viejo.

### 2.5. La cuña fiduciaria: por qué *sí* sigues necesitando una organización

Si la coordinación y la ejecución se abaratan tanto, ¿hace falta una organización? Sí, pero por razones distintas. Lo que sobrevive es la **cuña fiduciaria** (*fiduciary wedge*): la empresa se vuelve sobre todo un **contenedor** —de propósito, legal, de responsabilidad (liability), fiduciario—. Piensa en vehículos legales tipo SPV para inversiones: estructuras que sostienen la responsabilidad legal y fiduciaria.

La cuña fiduciaria es, precisamente, **la brecha entre el juicio y la responsabilidad humanos y lo que la IA puede hacer**. Esa brecha justifica que siga existiendo una entidad legal con personas a cargo. Dentro de ese contenedor habrá activos, propiedad intelectual, agentes y un número reducido de humanos —y agentes haciendo llamadas a APIs, consiguiendo datos, e incluso llamando por teléfono a personas (como el caso de la IA de Alex Finn que llamó a su propio creador).

---

## 3. La Singularidad Organizacional: organizar en torno a la inteligencia

### 3.1. De jerarquía a inteligencia

El nombre del marco —"singularidad organizacional"— apunta al cambio fundamental: en lugar de coordinar y organizar la empresa **alrededor de la jerarquía**, la organizas **alrededor de la inteligencia**. Es uno de los cambios de paradigma más grandes que se pueden pedir.

Otra forma de definir la singularidad organizacional: es el punto en que logras **auto-mejora recursiva a nivel de flujo de trabajo** (*recursive self-improvement at the workflow level*). Cuando un flujo no solo se ejecuta solo, sino que mejora solo en cada iteración, cruzaste el umbral.

El marco completo es la evolución de los libros previos: del *EXO 1.0* original, al *EXO 2.0*, hasta lo que ahora llaman la **Singularidad Organizacional** o **EXO 3.0** (Salim admite que "EXO 3.0" es el mejor nombre que tiene para la organización resultante, y que aceptaría uno mejor).

### 3.2. La arquitectura de tres piezas

El diseño de la nueva organización tiene tres componentes:

1. **MTP (Massive Transformative Purpose / Propósito Masivo Transformador)** — heredado del marco original, pero ahora ya no es un póster en la pared: se convierte en un **protocolo**.
2. **DRIVE** — el andamiaje y el motor de inteligencia (acrónimo cuyos subcomponentes no se detallan en la conversación).
3. **SHAPE** — cómo se da forma a la organización (también un acrónimo de subcomponentes).

### 3.3. El MTP como protocolo (no como póster)

Esta es una de las ideas más finas del marco. El MTP deja de ser un eslogan inspirador y pasa a ser una **guía operativa para agentes** —tanto de IA como humanos— sobre cómo actuar correctamente. Eso implica definir:

- La **arquitectura del MTP**.
- Las **condiciones de frontera**: ¿qué está dentro y qué fuera del propósito?
- Los **bucles de retroalimentación** que indican si estás dentro o fuera del "cono" del MTP.

**Ejemplo (Uber, primeros días):** su MTP —que todos tengan un chofer privado— era excelente. Pero si siempre aceptabas el *surge pricing* (tarifa dinámica), el sistema lo aprendía y te cobraba siempre la tarifa alta; mientras que alguien que nunca acepta surge obtenía el precio bajo, aunque ambos estuvieran parados uno al lado del otro. Eso es **salirse del cono del MTP**: empujar la frontera ética. En el modelo nuevo, ese tipo de comportamiento queda guiado y acotado por la arquitectura del MTP-como-protocolo.

---

## 4. El stack de inteligencia: las seis capas

El corazón de la organización nueva es un **stack de inteligencia** de seis capas. La mejor analogía es el **bucle OODA de John Boyd** (Observe, Orient, Decide, Act — Observar, Orientar, Decidir, Actuar), usado en doctrina militar. Es un volante (*flywheel*) en el centro: una vez que el bucle interno gira, todo lo que metes dentro empieza a generar retroalimentación positiva sobre lo demás. (Es también el núcleo del marco "Solve Everything" de Peter Diamandis y Alex, y de la idea del *inner loop* de aprendizaje rápido.)

### 4.1. Las seis capas

1. **Capa de propósito** — el MTP-como-protocolo que rige todo.
2. **Capa de sensado** — agentes que detectan lo que pasa afuera y traen información nueva.
3. **Capa de interpretación** — qué significa esa información: ¿amenaza una línea de negocio?, ¿varias?, ¿es existencial?
4. **Capa de decisión** — qué hacer al respecto.
5. **Capa de orquestación** — poner en marcha las funciones necesarias para ejecutar la decisión.
6. **Capa de aprendizaje** — el bucle de aprendizaje recursivo. Como dijo Eric Schmidt: *el aprendizaje rápido es la clave del éxito*.

### 4.2. El envoltorio: Govern & Assure (gobernar y asegurar)

Alrededor del stack hay un envoltorio crítico: la capa de **gobernanza y aseguramiento**, que es el **arnés y la supervisión** para que los agentes no se descontrolen. (En las semanas previas a la grabación se habían visto agentes haciendo locuras —por ejemplo, un agente que borró volúmenes enteros de datos de renta de autos—.)

Por "gobernanza" se entiende, en concreto:

- **Arquitectura de evaluación confiable** (*trusted eval*).
- **Registro auditable y buscable** — cada agente debe tener un *searchable log*.
- **Rollback granular** — poder volver a la versión anterior si algo empieza a salirse.
- **Cola de revisión humana** (*human review queue*) — humanos siempre en la supervisión.

El stack de inteligencia más el envoltorio de gobernanza dan un **motor central muy ajustado** que impide que todo se salga de los rieles.

### 4.3. Ejemplo trabajado: el competidor anuncia entrega el mismo día

Imagina una empresa de retail. Un competidor anuncia de repente entrega el mismo día:

1. **Sensado:** agentes detectan el anuncio y lo traen al sistema.
2. **Interpretación:** ¿esto amenaza una línea de negocio?, ¿varias?, ¿es existencial?, ¿qué tan grave es?
3. **Decisión:** ¿ofrecemos también entrega el mismo día?, ¿compramos un startup que ya lo hace?, ¿lo ignoramos porque creemos que no funcionará?
4. **Orquestación:** si la decisión es comprar un startup, se activan funciones para buscar candidatos, analizar cuáles están listos para M&A, avisar al equipo de desarrollo corporativo, preparar a los abogados y a los agentes legales.
5. **Aprendizaje:** ¿compramos otra empresa antes?, ¿funcionó?, ¿qué aprendimos?
6. Todo, envuelto en la gobernanza.

El punto clave: lo que antes hacían el director de estrategia, el de marketing y otros reunidos durante **meses** para evaluar alternativas competitivas, ahora ocurre en **horas o días**. En cada capa, un humano puede actuar como **válvula de aprobación**: en la capa de interpretación, por ejemplo, revisa, aprueba con un botón y deja pasar al siguiente nivel; gente senior puede estar viendo a los agentes evaluar seis opciones estratégicas distintas en paralelo.

### 4.4. El *impedance mismatch* (desajuste de impedancia)

Aquí aparece un concepto útil para tus clientes: el **desajuste de impedancia** entre velocidades. Históricamente existía entre una empresa Fortune 500 y un startup: la Fortune 500 tiene tanto que perder que se paraliza al decidir; el startup dice "qué más da, probemos todo". Como lo formula Robert Goldberg: en una empresa grande, **uno de cada veinte que diga "no" mata la idea**; en cambio, el startup va con 20 inversionistas y basta que uno diga "sí" para arrancar.

### 4.5. Auto-mejora recursiva a nivel de flujo de trabajo

El verdadero corazón del marco. Toma el **procesamiento de facturas**: hoy tiene puntos de control humanos (¿llegaron los bienes?, ¿existe el proveedor en el sistema?, ¿hay contrato legal?). Quizá un ERP automatizó una o dos capas. En el modelo nuevo, todo el flujo se ejecuta solo **y** un agente se pregunta, en cada bucle, "¿cómo lo hago mejor la próxima vez?" y mejora continuamente. Cuando llegas a ese nivel, puedes recostarte: el sistema se auto-mejora.

---

## 5. Gobernanza de agentes: el "pasaporte" del agente

Los agentes harán cosas inesperadas, así que necesitan barreras. El marco toma una idea de los *smart contracts* de Web3 más algo de arquitectura web antigua: **cada agente recibe un "pasaporte"** con metadata sobre qué tiene permitido hacer y qué no.

Componentes:

- **APIs controladas por política** (*policy-controlled APIs*).
- **Metadata por objeto de datos** — define a qué puede o no exponerse cada dato.
- **Marco de responsabilidad** (*liability framework*) — para que los agentes no hagan cosas ilegales. (Los abogados enloquecen ante agentes operando fuera de la organización sin control.)
- **Restricciones y supervisión** — otros agentes en el bucle de gobernanza vigilando. En cuanto algo se sale, se notifica a un humano, se detiene al agente, se hace rollback, se revisa y se reintenta.

### ¿Por qué es viable? La analogía cuántica

En computación cuántica necesitas como mil qubits físicos para lograr uno lógico fiable —mucha redundancia—. Con agentes pasa algo parecido, pero **los agentes son baratos**: puedes tener muchos agentes haciendo trabajo y muchos otros supervisándolos, y aun así el costo total te deja con todos los beneficios del stack.

---

## 6. Defensibilidad: los cinco fosos (*moats*)

Pregunta de diagnóstico que todo CEO y miembro del C-suite debería hacerse:

> **¿Hay una línea de tu negocio, de alto margen, que dos personas con herramientas de agentes autónomos (tipo Open Claw o Hermes) podrían replicar en 60 a 90 días?**

Si la respuesta es sí, estás en temporada de caza. "Cualquiera con un margen jugoso está expuesto." Garantizan que ahora mismo hay dos personas con esas herramientas disrumpiendo a empresas como Dropbox.

Frente a esto, hay (al menos) cinco fosos defensivos:

1. **Datos propietarios** — datos clave que no se pueden replicar en otro lado.
2. **Captura regulatoria** — como en salud. Puede erosionarse con el tiempo, pero sirve por ahora.
3. **Foso de inteligencia (el más importante)** — si **aprendes más rápido que todos**, nadie te alcanza. Por eso los bucles de aprendizaje de Claude y GPT van más adelante que los de Manus o Grok; una vez que tomas esa delantera, es muy difícil alcanzarte.
4. **Compromiso profundo con el propósito** — no desviarte de él; nada te sacude.
5. **Relación con el cliente y marca** — la relación dedicada con el cliente alimenta los datos propietarios; la marca vive junto al MTP, es la conexión emocional con el usuario. Una marca fuerte, reforzada con todas las capacidades de agentes nuevas, es difícil de desbancar.

(Todos los fosos pueden erosionarse, pero sirven como protección durante la transición.)

---

## 7. Qué le pasa a la gente: las tres capas de la organización

Tomando la organización clásica —**C-suite, mando medio (middle management) y línea de frente (coalface)**—, esto le pasa a cada capa:

### 7.1. C-suite (alta dirección)

Se vuelve sobre todo **responsabilidad (accountability), supervisión vía dashboards, evaluación y validación** —no ejecución—. No harás la evaluación estratégica: el agente la hace; tú aplicas tu juicio y experiencia para decidir si la acción del agente está alineada (apruebas o no). La alta dirección guía, sostiene la rendición de cuentas y observa lo que hacen los agentes.

### 7.2. Mando medio (el mayor cambio)

Aquí ocurre el mayor impacto. El mando medio en las empresas actuales hace casi pura **coordinación**: toma datos de la línea de frente, los reempaqueta para que el C-suite los absorba. **Esa función cae cerca del 90%.** A las personas de esta capa hay que "elevarlas" a manejo de excepciones, resolución de problemas, etc. —de lo cual hay muchísimo por hacer, pero hoy no se hace por falta de tiempo—.

### 7.3. Línea de frente (coalface)

El 20% de abajo hace trabajo **mucho más potenciado**: sus agentes hacen casi todo, y ellos hacen supervisión y vigilancia.

### 7.4. La magnitud de la reducción de plantilla

Estimación de los autores: podrás operar una empresa promedio con cerca del **20–25% de la fuerza laboral** que tenías (una reducción del ~80%). Más afinado por sector:

- Empresa de marketing: hasta **10%** de humanos.
- Empresa físico-intensiva o muy regulada (p. ej., construir un data center): hasta **25%**.

**De dónde sale el 80% de reducción:** ~60% del mando medio, ~20% de abajo, ~20% de arriba. La compresión está en todas partes, pero sobre todo en el mando medio —no hay forma de superar a un agente recopilando y agregando reportes de ventas—.

**Ejemplo concreto:** trabajando con Fermi America, estimaron que una planta de energía que hoy opera con **800 personas** podría operarse con cerca de **80** (~10%).

**Ratios de gestión:** la proporción gerente : "contribuidor individual de alto impacto" (HIC, término de Jack Dorsey) pasaría de 1:5 o 1:3 a **1:20 o más**. Jack Dorsey lo llevó al extremo (todos conectados al CEO), lo cual solo es posible usando IA para todo.

### 7.5. El problema de alineación / aprendizaje (y la solución: el modelo de gremio)

Surge un problema serio: si ya no hay gente de nivel inicial haciendo el trabajo duro (armando hojas de cálculo, sudando los detalles), **¿de dónde sale el conocimiento institucional?**, ¿de dónde saldrá la futura alta dirección si desaparecen los niveles de entrada e intermedios?

La solución propuesta: **programas de aprendizaje (apprenticeship) muy activos y agresivos** —una vuelta al modelo de **gremio (guild)**—. Un mando medio desplazado, en lugar de irse, se asocia con el CFO para trabajar en alternativas: aprende mucho más y se divierte más.

### 7.6. La visión optimista: la explosión cámbrica

Se puede leer la reducción de plantilla por el lado negativo ("75% de desempleo") o por el lado *moonshot*: si cada empresa necesita 20% del personal, surgirán **cinco veces más empresas**. Es la **explosión cámbrica de startups**, que ya se observa —incluso con la contratación de nivel inicial subiendo ahora mismo—.

---

## 8. Cómo llegar: la estrategia del borde y el gemelo digital

Esta es la parte de mayor experiencia práctica de los autores, porque cuando construyeron el modelo EXO ya habían tenido que resolver el problema del **sistema inmune** organizacional: cuando intentas algo disruptivo en una empresa grande, los anticuerpos te atacan.

### 8.1. No puedes arreglar la empresa existente

La regla más enfática de todo el marco: **no puedes cambiar, arreglar ni transformar la empresa existente**. Se remonta a **Buckminster Fuller**: no arregles el sistema viejo; construye uno nuevo en el borde y deja que se vuelva el nuevo centro de gravedad. **John Hagel y John Seely Brown** (Center for the Edge) identificaron que lo disruptivo ocurre **en el borde**.

Casos:

- **Nestlé / Nespresso (1976):** durante 10 años intentaron correrlo como línea de negocio dentro de la nave nodriza. No encajaba —otra marca, otra cadena de suministro, otra entrega, otra propuesta al cliente—. Cuando finalmente lo pusieron aparte, en otro edificio, despegó. Hoy Nespresso es una de sus líneas de mayor desempeño (hay una en cada habitación de hotel del mundo).
- **Apple / Mac:** Steve Jobs tomó un equipo pequeño, lo puso en el borde, en secreto, y le dijo "ve a disrumpir una industria distinta".
- **AWS:** Amazon Web Services no se hizo dentro del servicio central. Simplemente no encajaba.
- **Richard Branson / número de Dunbar:** cada vez que una empresa llegaba a ~150 personas (el número de Dunbar), la escindía en otra para romper ese límite. (Salim lo lleva más al extremo: spin-off cada vez que pasa algo.)

El obstáculo de fondo es el **ego humano**: el resultado exitoso protegiéndose de su propia disrupción. Salim cuenta que, incluso siendo un individuo persuasivo, no logró transformar internamente a una de sus empresas de 100 personas; tuvo que arrancarla como organización separada, y lo ha repetido varias veces.

> Salim afirma haber visto el proceso de innovación en detalle en unas **250 de las Fortune 500**, y **nunca** vio funcionar otro método que el de hacer lo disruptivo en el borde, apuntando a espacios adyacentes de una forma distinta.

### 8.2. Dos reglas de gobierno para la iniciativa del borde

1. **La organización del borde debe reportar directamente al CEO**, en la cúspide.
2. **El consejo (board) debe dar respaldo total al CEO.** Si vas a disrumpir tu propia organización sin apoyo del consejo, estás perdido.

### 8.3. Construir el gemelo digital nativo de IA

El procedimiento (esto es, en esencia, el plan de migración que venderías a un cliente):

1. **No toques la organización existente.** Es tu motor de ingresos, tu vaca lechera. Meter IA "a presión" en ella es justo lo que está fallando hoy.
2. En el **borde**, crea una **entidad separada**: el gemelo digital nativo de IA.
3. Toma **tres a cinco de tus jóvenes audaces**.
4. **Asóciate con un *builder*, no con una consultora.** Consigue *forward deployed engineers* (ingenieros desplegados, el término de moda en software).
5. **Elige un flujo de trabajo** estandarizado y bien entendido —por ejemplo, procesamiento de facturas—.
6. **Cópialo, no lo muevas, al sistema nuevo.** (El marco incluye una metodología para descomponer y puntuar cada tarea del flujo.)
7. **Forkea los datos** necesarios para correrlo.
8. **Córrelo en paralelo** hasta alcanzar el bucle de auto-mejora recursiva. Cuando veas que los bucles de mejora aquí van mucho más rápido que en la empresa vieja, ya casi estás —pero dale unas semanas más y un control de calidad—.
9. **Deprecia lentamente lo viejo** y pasa al siguiente flujo (confirmación de recibos, luego previsión de demanda, etc.). Poco a poco, el gemelo digital crece en el borde.

Has **desriesgado** la operación: si algo sale terriblemente mal, no arriesgas la nave nodriza.

### 8.4. La promesa de desempeño y el efecto adyacente

Estimación de los autores: una vez que el gemelo digital corre bien, la mejora de desempeño es de **100x o más al año**. Si hoy procesas una factura, deberías procesar 100; si algo tomaba 100 días, debería tomar uno.

El efecto secundario emocionante: una vez que el gemelo corre solo, tu gran equipo emprendedor —antes limitado porque no querías quemar a la gente— queda libre para **construir productos y servicios adyacentes** y escindir nuevas empresas.

### 8.5. Sectores que ya completaron el ciclo

Dos sectores ya recorrieron el ciclo completo (humano → asistido por IA → nativo de IA):

- **Contact centers / atención al cliente:** de BPO humano, a chatbots asistidos, a atención nativa de IA (caso Klarna). Peter cuenta su experiencia con el soporte de Starlink, todo basado en Grok.
- **Marketing y generación de contenido:** de pesado en agencias, a asistido por IA, a nativo de IA.

(Como anécdota del propio proceso: el primer libro tomó tres años; el segundo, dos años y medio; **el tercero, tres meses**, porque cada colaborador podía usar IA para aportar datos, ayuda y metodología.)

---

## 9. La metodología REWRITE, paso a paso

Llaman **REWRITE** a la metodología de reconstrucción. Los pasos:

### Paso 1 — *Backcasting* (retro-proyección)

El *backcasting* es una técnica de estudios de futuro: defines cómo se ve la visión y trabajas hacia atrás. Si Elon quiere llegar a Marte en siete años, pregunta: ¿dónde tengo que estar en 5 años?, ¿en 3?— y así obtienes el mapa de ruta. Si partes del presente diciendo "quiero ir a Marte", no tienes idea de cómo llegar.

Aplicado: toma tu empresa (la de transporte o retail del ejemplo) y pregunta: en ese mundo futuro, **¿cómo se ve esta empresa cumpliendo su MTP de forma nativa de IA?** Es lo más difícil para la gente —soltar cómo lo han hecho siempre— y, a la vez, una de las cosas más fáciles de hacer **conversando con un modelo de lenguaje**.

### Paso 2 — Puntuar la empresa (scoring)

Se evalúa a la organización en **siete dimensiones** (siete preguntas, autoevaluación del 1 al 7, disponible gratis en su sitio). Dos ejemplos de métricas:

- **Arrastre organizacional (organizational drag), 1 a 10:** ¿cuántos bucles de decisión y aprobaciones hay para lograr algo? ¿Va por cinco o seis aprobaciones, o —como en Nvidia— vas directo al fundador y te dice sí o no (o te lo dice una IA)?
- **IA como ciudadano de primera clase, 1 a 10:** si la IA es una herramienta inyectada, estás en la parte baja; si tienes un *Chief AI Officer* y ya construyes capacidad nativa de IA, estás alto.

> El antecedente público de este paso es la **encuesta ExQ (Exponential Quotient)** que OpenExO ofrece gratis en su sitio: autoevaluación de ~10 minutos que arroja un puntaje, un mapa de transformación y recomendaciones de qué atributos implementar primero. Es la versión 2.0 del diagnóstico; el *rewrite score* del programa nuevo es su evolución. Útil como modelo para tu propia herramienta de diagnóstico (ver §17 y Apéndice B).

### Paso 3 — Mapear y documentar los flujos prescriptivos

Toma tus flujos más prescriptivos y mapéalos y documéntalos para tener conocimiento claro. **Gran problema: el conocimiento tácito (*tacit knowledge*).** Un productor de video, por ejemplo, hace pasos que no son obvios desde afuera ni están documentados en ningún lado; si pierdes a esa persona y la IA aún no los hace, te quedas sin esa capacidad.

### Paso 4 — Romper el sistema inmune (hackear la cultura)

Hay un fenómeno de resistencia: las empresas intentan "destilar" (shatter) el conocimiento de la gente con un agente, y la gente se defiende. Dato citado: **el 44% de los trabajadores de la Gen Z estaría saboteando a la IA**, dándole mala información para que no pueda quitarles el empleo después. Es el sistema inmune en acción: intentas hacer algo y la cultura te mata por dentro.

Los autores dicen haber creado un **proceso de 10 semanas para romper el sistema inmune y "hackear la cultura a escala"**, aplicado ya unas **100 veces** en empresas grandes.

> Ese proceso tiene nombre comercial: el **ExO Sprint** (un servicio de OpenExO; ver Apéndice B). Lo confirma un testimonio de Tony Saldanha (ex-VP de Global Business Services en P&G) en el sitio: viene a decir que solo el 10% del reto son las ideas y el 90% es lograr que la empresa entera avance, y que el equipo de Salim fue quien logró "descongelar" esa resistencia. Es exactamente el problema del sistema inmune.

### Paso 5 — Cortar el arrastre organizacional

Empieza a eliminar niveles de aprobación: reduce el flujo hasta el punto de casi romperlo y observa qué pasa. Regla práctica que dan a los clientes: si un proceso toma 10 pasos, fuérzalo a **tres pasos o menos**; cuando esté en tres o menos, estás listo para empezar a moverlo al gemelo digital.

### Paso 6 — Construir el gemelo y migrar flujos uno por uno

(Como en §8.3.) En paralelo, montar el marco legal del gemelo digital y obtener la aprobación del consejo.

### Paso 7 — Recablear los sistemas

Recableas cada vez más para que todo apunte al gemelo nuevo y no al viejo.

---

## 10. La nueva arquitectura tecnológica (stack viejo vs. nuevo)

### 10.1. Cómo operan hoy la mayoría de las empresas (arquitectura vieja)

De abajo hacia arriba:

1. Proveedor de nube / redes / conectividad.
2. Sistemas ERP (Oracle Financials, SAP, etc.), con **todos los datos atrapados dentro** —esos proveedores no quieren que extraigas tus datos fácilmente—.
3. Capa de aplicaciones.
4. La gente intentando **poner IA encima** de esa arquitectura horrible que llevamos 50 años cargando y que no se puede desenredar fácilmente.

### 10.2. La nueva arquitectura

De abajo hacia arriba:

1. Conectividad y proveedor de nube.
2. Un **data lake** con todos tus datos accesibles en un solo lugar, **con niveles de aprobación adjuntos a cada objeto de dato**.
3. Una **capa de aplicaciones hecha a la medida** para ti (porque la IA puede construirla) y los flujos.
4. La IA.
5. Los **agentes** encima.

Es un stack completamente distinto, **que posees por completo**. La velocidad es la clave: pregúntale a cualquiera que haya implementado un ERP cuánto sufrió, y cómo termina mapeando el flujo de la organización al ERP —en vez de al revés—. Ahora puedes tener software construido a tu medida.

### 10.3. Por qué los proveedores de SaaS están aterrados

Ese modelo nuevo es **incompatible** con el de los SaaS. Hoy intentan defender su lugar porque están **cableados al sistema límbico de la organización heredada**. Pero si construyes el stack propio, tienes plena agencia y control a un costo mucho menor.

---

## 11. Horizonte temporal y magnitud del cambio

- **La transición turbulenta:** la transición completa de la mayoría de las empresas (no de una sola) tomará unos **5 a 7 años**. Pasado ese periodo, una empresa o está muerta o ya hizo la transición. Esto coincide con la conversación más amplia sobre el "periodo turbulento" que Peter sitúa en **2 a 8 años**, que hay que arquitectar con cuidado a nivel social.
- **Personal:** entre 10% y 25% del actual, según el sector (ver §7.4).
- **Es una carrera.** Si alguien en tu industria corre este proceso y tiene un gemelo digital que mejora de forma recursiva, y tú no, estás cocinado. Ejemplo: si Procter & Gamble automatiza todo, Unilever no podrá competir (o al revés).
- **Caso real:** Cognition Labs hizo crecer su ARR **73 veces** al volverse plenamente nativa de IA. No es especulación: son señales tempranas, y cada dato recogido apunta a esa trayectoria.
- **100x y desmonetización:** veremos una clase de empresas entregando 100x respecto a lo anterior, con la rentabilidad por las nubes. Pero la rentabilidad se acotará: al ver esos márgenes, otras empresas mandarán sus agentes a competir, los precios bajan, las cosas se **desmonetizan**, y eso empuja hacia el **ingreso universal alto (UHI), el ingreso básico universal (UBI) y los servicios básicos universales**, porque el costo de todo se desploma.
- **Combustible de crecimiento:** los autores enmarcan esto como "combustible de cohete" para las visiones de crecimiento del PIB de triple dígito (mencionan a Elon como "amigo del podcast").

---

## 12. Qué sobrevive y qué muere (antes / después)

### Lo que sobrevive y prospera

- El **MTP codificado como protocolo** en la empresa.
- La **carcasa de rendición de cuentas** (accountability shell): entidad legal, contenedor fiduciario y de responsabilidad.
- La **inteligencia propietaria** dentro del stack (crítica).
- Los **protocolos de coordinación** (se vuelven decisivos).
- El **juicio curatorial / el gusto** (curatorial judgment / taste): cuando la ejecución es casi gratis, el juicio y el gusto se vuelven lo importante.

### Lo que muere

- El **organigrama** tal como lo construimos. (David Rose: la estructura que te dio éxito en el siglo XX te hará fracasar en el XXI.) La organización misma **se vuelve un protocolo**, y la estructura pasa a ser **dinámica, cambiante, como una ameba**.
- El **plan a cinco años** y toda **planeación estática**: en medio de la singularidad no puedes saber cómo se verá el mundo en un año. Todo son **bucles de aprendizaje constante**. (Tradicionalmente el organigrama solo cambiaba con eventos mayores —M&A, nueva línea de negocio, reemplazo del equipo directivo—; ahora cambia continuamente.)
- El **mando medio como capa de coordinación**.
- Las **revisiones trimestrales** como unidad de toma de decisiones.
- La **planeación anual**.
- Los **fosos de inercia** ("los clientes no cambian porque cambiar es molesto").
- Los **activos que se vuelven obsoletos** (wasting assets) en la economía.

---

## 13. Aplicaciones más allá de la empresa

- **Gobiernos.** Aplica por completo: casi todos los procesos de gobierno son prescriptivos y bien entendidos (renovar una licencia de conducir es frustrante pero perfectamente conocido). Esa fricción puede eliminarse. Sheikh Mohammed (EAU) habría dicho que quiere correr el **50% del gobierno emiratí** sobre este modelo; ya procesan visas doradas y de residente en **5 horas** (antes inaudito).
- **Organizaciones sin fines de lucro.** También aplica.
- **Colapso de dominios.** El marco propone diseñar organizaciones que detonen un "colapso de dominio" sector por sector (salud, educación), montando una estructura donde el *inner loop* de aprendizaje empiece a moverse.
- **Universidades** (una de las mayores categorías que se acercan a ellos). Ven la disrupción venir y piden ayuda. El cambio: de **enseñar contenido** a **enseñar ejecución**, volviéndose hubs emprendedores. El título de ingeniería del futuro no será "estudié ingeniería cuatro años", sino "construí un montón de cosas, fueron lo bastante interesantes y me certificaron": **hacer en lugar de aprender**.
- **Emprendedores.** Si vas a fundar una empresa, ya tienes plataforma y *playbook* para empezar de forma nativa de IA desde el día uno. Como dice William Gibson (parafraseado): *el futuro ya está aquí, solo que no está distribuido de forma uniforme*. La singularidad organizacional ya llegó; un startup de cinco personas ya se está construyendo así.

---

## 14. El libro como IA viva y cómo participar

- **El libro se publica como una IA, no como texto estático.** Un libro impreso queda obsoleto el día que se publica; cada dos o tres días algo cambia el juego. Por eso lo lanzan como un **Claude skill** que se actualiza en tiempo real (con conectores a herramientas como QuickBooks). La idea: no te certificas en algo de hace cinco años; la propia IA se mantiene actualizada.
- **La comunidad EXO** cuenta con ~**50,000 personas en 150 países**, en proceso de reentrenamiento para este modelo.
- **Cómo entrar al programa:** seleccionan CEOs, los puntúan con el *rewrite score*; iban por ~**4 empresas** al momento de grabar, en **lotes de 10 a 20**. Es un **proceso de 90 días** para arrancar y dejar correr unos flujos en el modelo nuevo. Si una empresa tiene demasiado arrastre organizacional, primero le piden arreglar eso.
  - Contacto mencionado: **Kevin Allen** (jefe de comunidad), *kevin@openexo.com*; sitios **openexo.com** y **organizationalsingularity.com**.
- **Transición social incorporada:** un miembro de la comunidad (Patrick Sandina) propuso usar el proceso para **reentrenar a las personas en riesgo** dentro del nuevo modelo, resolviendo el contrato social por el camino. (Nota legal: en Alemania, los consejos de trabajadores —*workers councils*— deciden cuántos empleados puede o no tener la empresa grande, lo cual limita la flexibilidad.)

**Mensaje de cierre de los autores:** si eres empleado y quieres que tu empresa prospere, envía esto a tu CEO y a tu consejo. Si eres el CEO: ya está ocurriendo, a ritmo acelerado, y la disrupción **no viene de tu competidor más grande**, sino del startup nativo de IA que ve lo lento que eres y lo mucho que ganas, y viene a comerte el almuerzo.

---

## Apéndice A — El modelo ExO base (2.0): MTP + SCALE + IDEAS

> El podcast da por sabido el modelo ExO original. Conviene tenerlo aquí porque es el cimiento del que parte EXO 3.0, y porque es excelente material introductorio para tus clases. La fórmula es: **MTP + SCALE + IDEAS**, con 11 atributos alrededor del propósito.

En el centro está el **MTP (Massive Transformative Purpose)**: la aspiración de la organización, el cambio que quiere lograr en el mundo. Alrededor hay dos grupos de cinco atributos.

**S.C.A.L.E.** — cinco atributos *externos*, para conectar con la abundancia de afuera y aprovecharla:

- **Staff on Demand** — personal bajo demanda; talento global y flexible en lugar de plantilla fija.
- **Community & Crowd** — comunidad y multitud; el motor para generar ideas, financiamiento y difusión.
- **AI & Algorithms** — IA y algoritmos; usar datos y aprendizaje automático para decidir mejor.
- **Leveraged Assets** — activos apalancados; rentar y compartir en lugar de poseer, para operar ligero.
- **Engagement** — enganche; gamificación y mecánicas para atraer y retener.

**I.D.E.A.S.** — cinco atributos *internos*, para gestionar esa abundancia y crecer:

- **Interfaces** — procesos que filtran y conectan lo externo con lo interno de forma simple.
- **Dashboards** — tableros con datos en tiempo real para dirigir la organización.
- **Experimentation** — cultura de experimentación y aprendizaje continuo.
- **Autonomy** — equipos autónomos y autoridad descentralizada.
- **Social** — tecnologías sociales para acelerar conversaciones y decisiones.

La conexión con EXO 3.0 es directa: el **MTP** pasa de "norte estratégico" a **protocolo operativo**; el atributo **AI & Algorithms** deja de ser un atributo más para volverse el **núcleo** (el stack de inteligencia de seis capas, §4); y atributos como **Dashboards, Autonomy y Experimentation** se reencarnan en la supervisión vía tableros, los equipos pequeños en el borde y la auto-mejora recursiva.

---

## Apéndice B — El ecosistema y la oferta comercial de OpenExO

> Esto es lo que encontré al revisar el sitio. Sirve para dos cosas: como inteligencia de mercado (cómo empaqueta y cobra el referente del sector) y como inventario de herramientas que puedes usar o tomar como modelo para tu propia práctica.

### Un punto estratégico que conviene notar

El embudo público de OpenExO (la página *begin-your-transformation*) **todavía vende el modelo 2.0**: la encuesta ExQ, el taller "10x Shift", el modelo MTP + SCALE + IDEAS. El marco nuevo del podcast —la Singularidad Organizacional / EXO 3.0— **aún no está en ese embudo**; vive aparte, en *organizationalsingularity.com*, y se ofrece de forma selectiva (lotes de 10–20 empresas). En otras palabras: la maquinaria comercial existente (assessment → taller → sprint → certificación) es el andamiaje sobre el que enchufarán el 3.0. Para ti es una ventana de oportunidad: el espacio de "traducir el 3.0 a clientes hispanohablantes" está prácticamente vacío.

### Herramientas y productos (útiles como modelo o para usar)

- **Encuesta ExQ** — diagnóstico gratuito de ~10 min; puntaje + mapa de transformación + recomendaciones. Modelo directo para tu herramienta de autodiagnóstico.
- **ExO Chat Bot** — "compañero de IA" entrenado en ExO 2.0; el precursor de la idea de "el libro como IA / Claude skill" del podcast.
- **Taller 10x Shift** — sesión de 2 h en vivo con Salim Ismail (~USD 100). Incluye guía de crecimiento de ~30 páginas, redacción del MTP y el lienzo ExO en el taller, acceso al chatbot, el reporte de desempeño y el curso ExO Foundations (valor declarado ~USD 299).
- **ExO Sprint** — el servicio de implementación; es, con alta probabilidad, el "proceso de 10 semanas para romper el sistema inmune" del podcast.
- **ExO Canvas** — lienzo tipo *business model canvas* adaptado al modelo ExO.
- **ExO Toolkit / Resource Hub / Exponential Transformation Guide** — plantillas y frameworks descargables.

### Cifras de desempeño que publican (con cautela)

OpenExO cita un estudio de benchmark de 8 años según el cual las organizaciones que aplican la fórmula habrían logrado: **~40x** mayores retornos al accionista, **~2.6x** mejor crecimiento de ingresos, **~6.8x** mayor rentabilidad y **~11.7x** mejor rotación de activos. Trátalas como **cifras de marketing autoreportadas**, no auditadas; útiles para ilustrar la promesa, no para garantizar resultados a un cliente.

### Lo más relevante para ti: la ruta de consultor

OpenExO tiene una **ruta de certificación** (ExO Certification Journey) y un modelo explícito de **oportunidades de consultoría**: capacitan a personas para volverse consultores ExO y los conectan con organizaciones vía sus "servicios de emparejamiento de mercado" (*market matching*). Dado que tu meta es asesorar migraciones, esta es una vía concreta: te certificas, usas su andamiaje y su comunidad (50,000 personas en 150 países), y te posicionas como el puente al mercado de habla hispana. Vale la pena revisar a fondo *learn.openexo.com*, *openexo.com/certifications* y los planes en *exopass.openexo.com/plans* antes de decidir si te apoyas en su ecosistema o construyes el tuyo de forma independiente.

### Propuesta de valor que usan (para inspirar la tuya)

Un testimonio de Accenture en el sitio resume bien el ángulo de venta: afirman haber recibido en pocas horas el valor que una consultoría tradicional entregaría tras seis meses y medio millón de dólares. El encuadre —velocidad y costo radicalmente menores frente a la consultoría clásica— es justo el que tú puedes adoptar al ofrecer migraciones asistidas por IA.

---

- **Singularidad organizacional / EXO 3.0** — modelo de empresa organizada en torno a la inteligencia (no a la jerarquía); el punto en que hay auto-mejora recursiva a nivel de flujo de trabajo.
- **MTP (Massive Transformative Purpose)** — Propósito Masivo Transformador; en este marco, un **protocolo** operativo, no un eslogan.
- **DRIVE / SHAPE** — acrónimos de los subcomponentes del andamiaje de inteligencia y de la forma organizacional (sin detallar en la fuente).
- **Cuña fiduciaria (fiduciary wedge)** — la brecha entre el juicio/responsabilidad humanos y lo que la IA puede hacer; justifica mantener una entidad legal como contenedor.
- **Stack de inteligencia** — las seis capas: propósito, sensado, interpretación, decisión, orquestación, aprendizaje.
- **Bucle OODA (Boyd)** — Observar, Orientar, Decidir, Actuar; el volante de aprendizaje en el centro del stack.
- **Govern & Assure** — capa de gobernanza: evaluación confiable, registro buscable, rollback granular, cola de revisión humana.
- **Pasaporte del agente** — metadata que define qué puede/ no puede hacer un agente (APIs por política, metadata por objeto, marco de responsabilidad).
- **Auto-mejora recursiva a nivel de workflow** — un flujo que no solo se ejecuta solo, sino que mejora solo en cada iteración.
- **Gemelo digital nativo de IA** — réplica de la empresa construida en el borde, en una entidad separada, que se vuelve el nuevo centro de gravedad.
- **Forward deployed engineers** — ingenieros desplegados; perfil de *builder* (no consultor) que implementa en sitio.
- **Backcasting** — planear desde la visión futura hacia atrás hasta el presente.
- **Arrastre organizacional (organizational drag)** — fricción de aprobaciones y bucles de decisión (métrica 1–10).
- **Sistema inmune organizacional** — la resistencia cultural que ataca lo disruptivo (anticuerpos).
- **Conocimiento tácito (tacit knowledge)** — saber-hacer no documentado, difícil de transferir a la IA.
- **Desajuste de impedancia (impedance mismatch)** — diferencia de velocidad de decisión entre actores (Fortune 500 vs. startup; humano vs. agente).
- **Fosos / moats** — datos propietarios, regulación, inteligencia (aprender más rápido), propósito, relación con el cliente/marca.
- **HIC (high-impact individual contributor)** — contribuidor individual de alto impacto (término de Jack Dorsey); ratio gerente:HIC de 1:20+.
- **Coalface** — la línea de frente operativa de la empresa.
- **Transición turbulenta** — el periodo de 5–7 años (o 2–8) de migración de la economía.
- **Desmonetización** — caída del costo de bienes y servicios que empuja hacia UBI/UHI/servicios básicos universales.
- **Colapso de dominio** — automatización acelerada de un sector entero (salud, educación) vía el inner loop.

---

## 16. Índice de personas, empresas y obras citadas

**Personas:** Ronald Coase, Herbert Simon, Clayton Christensen, Stanley McChrystal, Jack Dorsey, John Boyd, Eric Schmidt, Robert Goldberg, Buckminster Fuller, John Hagel, John Seely Brown, Richard Branson, Steve Jobs, David Rose, William Gibson, Alex Finn, Kevin Allen, Patrick Sandina, Sheikh Mohammed (EAU), Elon Musk; los anfitriones Peter Diamandis y Salim Ismail, y "Alex" (coautor del marco *Solve Everything*).

**Empresas / herramientas:** Uber, Vercel/v0, Cloudflare, Oracle (Financials), SAP, AWS, Nestlé/Nespresso, Apple/Mac, IBM, Procter & Gamble, Unilever, Siemens Energy, Black & Decker, HP, Dropbox, Nvidia, Klarna, Starlink, Grok (xAI), Claude, GPT, Manus, Cognition Labs, Fermi America, Block, Accenture, Rassini, TD Ameritrade; herramientas de agentes autónomos: Open Claw, Hermes. Productos/servicios de OpenExO: encuesta ExQ, ExO Chat Bot, taller 10x Shift, ExO Sprint, ExO Canvas, ExO Toolkit, ExO Foundations, ruta de certificación ExO.

**Obras / marcos:** *The Nature of the Firm* (Coase, 1937), *Exponential Organizations* (EXO 1.0 y 2.0), *Team of Teams* (McChrystal), el dilema del innovador (Christensen), el bucle OODA (Boyd), el número de Dunbar, el marco *Solve Everything*, el libro/Claude skill *Organizational Singularity* (EXO 3.0).

**Conceptos numéricos para tener a la mano:** Coase 1937 (~80 años de vigencia del modelo); >80% de proyectos de IA fracasan; 60–90 días para replicar una línea de alto margen; 6 capas del stack; reducción a 10–25% del personal (80% de recorte: 60% mando medio, 20% base, 20% cúpula); Fermi America 800→80; ratio 1:20+; 100x/año; Cognition Labs 73x ARR; 44% de Gen Z saboteando IA; proceso de 10 semanas para el sistema inmune (≈100 veces aplicado); 90 días para arrancar; lotes de 10–20; comunidad de 50,000 en 150 países; transición de 5–7 (o 2–8) años; visas en 5 horas (EAU); ~250 de las Fortune 500 observadas; Nespresso desde 1976.

---

## 17. Cómo convertir esto en un proyecto con Claude Code

Como tu objetivo doble es **enseñar IA** y **asesorar migraciones**, te propongo estructurar el repositorio del proyecto así. Es una sugerencia de andamiaje; ajústala a tu vault y a tu forma de trabajar.

```
singularidad-organizacional/
├── CLAUDE.md                      # Contexto e instrucciones para Claude Code
├── 00-fuente/
│   └── transcript-original.md     # El transcript crudo (referencia)
├── 01-marco/
│   └── singularidad-organizacional-exo-3.0.md   # Este documento
├── 02-docencia/
│   ├── modulo-1-por-que-se-rompe-coase.md
│   ├── modulo-2-stack-de-inteligencia.md
│   ├── modulo-3-gobernanza-de-agentes.md
│   ├── modulo-4-estrategia-del-borde.md
│   └── ejercicios-y-casos.md
└── 03-asesoria/
    ├── diagnostico-cliente.md     # Las 7 dimensiones + drag + fosos (modelo: ExQ)
    ├── plan-de-migracion-90-dias.md
    ├── ecosistema-openexo.md      # Apéndice B: oferta, herramientas, certificación
    └── plantillas/                # Backcasting, scoring, mapa de flujos
```

**Para el `CLAUDE.md`**, dale a Claude Code el contexto esencial: que eres profesor de IA y asesor de migración empresarial; que este marco es la base conceptual; tu preferencia de español neutro (tú, sin voseo) y tono serio-cálido; y que distinga siempre entre los hechos del marco y las proyecciones de sus autores.

**Tres entregables concretos que Claude Code puede ayudarte a construir desde aquí:**

1. **Una herramienta de autodiagnóstico para clientes** (las 7 dimensiones, el arrastre organizacional 1–10, la presencia de IA como ciudadano de primera clase 1–10, y los cinco fosos), que produzca un *rewrite score* y una recomendación inicial.
2. **Un generador de plan de migración de 90 días**: dado un sector y un flujo de trabajo, propone el backcasting, identifica el conocimiento tácito en riesgo, y bosqueja el gemelo digital del borde.
3. **Un currículo modular para tus clases**, con la genealogía de pensadores, los ejemplos (Uber, Nespresso, Klarna, Fermi America) y ejercicios de "¿qué línea de tu negocio replicarían dos personas en 90 días?".
4. **Un módulo de posicionamiento como consultor**: comparar tu oferta con la de OpenExO (Apéndice B), decidir si te certificas en su ruta o construyes una propia, y adaptar la encuesta ExQ como base de tu autodiagnóstico en español.

Si quieres, en una próxima sesión puedo redactar el `CLAUDE.md` y el primer módulo docente, o construir el cuestionario de diagnóstico como artefacto interactivo.

---

## Historial de cambios

- **2026-05-28** — Destilado inicial a partir del transcript de Moonshots EP #258.
- **2026-05-28** — Añadidos Apéndice A (modelo ExO base: MTP + SCALE + IDEAS) y Apéndice B (ecosistema y oferta comercial de OpenExO) tras revisar openexo.com; conexiones del ExQ y el ExO Sprint con la metodología REWRITE; cuarto entregable de consultoría en §17.
