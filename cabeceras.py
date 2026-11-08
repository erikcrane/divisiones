"""Encabezados de la ficha, con temática de Fortnite (100 cabeceras).

Solo datos, sin lógica. Cada encabezado es una pareja (título, texto), y el
texto puede ser "" para que no salga. Cada vez que se genera un PDF se elige
una al azar, sin repetir ninguna hasta que han salido todas (ver
`elegir_cabecera` en `divisiones.py`). Las que ya han salido se apuntan, por
su título, en `cabeceras_salidas.json`.

Cada cabecera tiene que tener un título distinto, porque el título es lo que
la identifica en ese fichero (se comprueba al arrancar). Si se cambia el
título de una, cuenta como una cabecera nueva. Para dar más variedad basta
con añadir parejas a la lista.

Ningún texto pasa de 7 líneas en el PDF (con Anton a 13,5 puntos; la
mayoría ocupan 5) y todos los títulos caben en una línea. Si se cambia la
fuente o el tamaño del texto de la cabecera, conviene volver a comprobarlo:
cuanto más largo es el texto, menos sitio queda para hacer las divisiones.
"""

CABECERAS = [
    # --- 1 a 10: el comienzo de la partida -----------------------------------
    (
        "¡Necesitamos tu ayuda para ganar la partida!",
        "El autobús de batalla ya ha despegado y la tormenta se está cerrando. "
        "Para conseguir la victoria magistral tenemos que sobrevivir hasta el "
        "final, y para eso hay que construir muy rápido muros, rampas y "
        "torres que nos protejan de los enemigos. Pero cada construcción "
        "necesita la cantidad justa de materiales: si nos equivocamos en los "
        "cálculos, nos quedaremos sin madera, piedra o metal en el peor "
        "momento. ¿Nos ayudas a resolver estas divisiones para que nuestras "
        "construcciones aguanten y ganemos la partida?",
    ),
    (
        "¡Saltamos del autobús!",
        "Acabamos de saltar del autobús de batalla y bajamos planeando hacia "
        "la isla. Abajo ya vemos a otros jugadores que van a aterrizar justo "
        "en el mismo sitio que nosotros. En cuanto toquemos el suelo habrá "
        "que levantar muros a toda velocidad para no quedar al descubierto, y "
        "para eso necesitamos saber cuántos materiales gastar en cada uno. "
        "Resuelve estas divisiones y ayúdanos a sobrevivir al aterrizaje "
        "para seguir en la partida.",
    ),
    (
        "¡Aterrizaje caliente!",
        "Hemos aterrizado en la zona más peligrosa del mapa y hay enemigos "
        "por todas partes. Solo tenemos el pico y unos pocos materiales, así "
        "que cada pared que construyamos tiene que estar bien calculada. Si "
        "gastamos demasiado en una, no nos quedará nada para la siguiente y "
        "nos eliminarán enseguida. ¡Tú eres quien lleva las cuentas del "
        "equipo! Resuelve estas divisiones para que podamos protegernos y "
        "salir con vida de este aterrizaje.",
    ),
    (
        "¡A por los materiales!",
        "La partida acaba de empezar y lo primero es conseguir materiales. "
        "Hemos talado árboles, roto coches y derribado paredes con el pico, "
        "y ahora tenemos que repartir todo lo recogido entre las "
        "construcciones que vamos a necesitar más adelante. Si lo repartimos "
        "mal, nos quedaremos sin defensa cuando lleguen los enemigos. "
        "¿Nos ayudas con las cuentas? Resuelve estas divisiones para "
        "aprovechar cada trozo de madera, piedra y metal.",
    ),
    (
        "¡El primer cofre!",
        "Hemos encontrado el primer cofre de la partida y dentro había armas "
        "y un buen montón de materiales. Pero a lo lejos se oyen pasos: otro "
        "equipo viene a por nosotros. Tenemos el tiempo justo para levantar "
        "un pequeño fuerte, y cada pieza necesita la cantidad exacta de "
        "materiales para que no se venga abajo. Resuelve estas divisiones y "
        "ayúdanos a construir nuestra defensa antes de que lleguen los "
        "enemigos.",
    ),
    (
        "¡La partida empieza ahora!",
        "Cien jugadores en la isla y solo uno puede ganar. Para ser nosotros "
        "tenemos que planificarlo todo desde el principio: cuántos "
        "materiales recoger, cuántos muros levantar y cuántas rampas "
        "necesitaremos para llegar a lo alto. Cada construcción es una cuenta "
        "que hay que hacer bien, porque un error nos puede costar la "
        "partida. ¿Te unes a nuestro equipo? Resuelve estas divisiones y "
        "empecemos con buen pie el Battle Royale.",
    ),
    (
        "¡Planeando hacia la victoria!",
        "Bajamos con el ala delta y desde el aire vemos toda la isla. Hay "
        "una casa perfecta para hacernos fuertes, pero tendremos que "
        "reforzarla con muros y techos antes de que lleguen los demás "
        "jugadores. Los materiales que llevamos son pocos y hay que "
        "repartirlos con cuidado entre todas las paredes. Resuelve estas "
        "divisiones para calcular cuánto usar en cada una y convertir esa "
        "casa en el mejor refugio de la isla.",
    ),
    (
        "¡Primer encuentro con el enemigo!",
        "Acabamos de ver al primer rival de la partida y él también nos ha "
        "visto a nosotros. Empieza el tiroteo y lo único que puede salvarnos "
        "es construir más rápido que él. Pero no basta con ser rápido: hay "
        "que saber cuántos materiales poner en cada muro para que aguante "
        "los disparos. ¡Necesitamos tus cálculos ya! Resuelve estas "
        "divisiones para ganar este primer combate y seguir avanzando hacia "
        "la victoria.",
    ),
    (
        "¡Mochila llena, cuentas pendientes!",
        "Llevamos la mochila llena de madera, piedra y metal, pero no "
        "sabemos cuánto podemos gastar en cada construcción sin quedarnos "
        "cortos al final de la partida. Los mejores jugadores siempre "
        "calculan antes de construir, y por eso te necesitamos a ti. Cada "
        "división que resuelvas nos dirá cuántos materiales usar en un muro, "
        "una rampa o un suelo. ¡Ayúdanos a planificar bien para llegar al "
        "último círculo con todo lo necesario!",
    ),
    (
        "¡Ruta hacia la zona segura!",
        "El primer círculo de la tormenta acaba de aparecer y estamos justo "
        "en el borde. Tenemos que cruzar un campo abierto donde cualquier "
        "francotirador nos puede ver, así que iremos poniendo muros para "
        "cubrirnos a cada paso. Para no quedarnos sin materiales a mitad de "
        "camino, hay que calcular cuántos usar en cada tramo. Resuelve estas "
        "divisiones y ayúdanos a llegar sanos y salvos a la zona segura.",
    ),
    # --- 11 a 20: la tormenta -------------------------------------------------
    (
        "¡Cuidado, que viene la tormenta!",
        "La tormenta avanza muy deprisa y tenemos que cruzar medio mapa "
        "para llegar a la zona segura. Por el camino nos esperan enemigos "
        "escondidos en las colinas, así que tendremos que construir rampas "
        "para subir y muros para cubrirnos mientras corremos. Cada metro "
        "de construcción gasta materiales y no podemos permitirnos fallar "
        "ni una cuenta. ¿Te atreves a ayudarnos? Resuelve estas divisiones "
        "y calcula lo que necesitamos para sobrevivir a la tormenta y ganar "
        "la partida.",
    ),
    (
        "¡La tormenta se cierra!",
        "El círculo es cada vez más pequeño y la tormenta nos pisa los "
        "talones. Los jugadores que quedan se están amontonando en la zona "
        "segura y todos quieren el mejor sitio. Nosotros vamos a construir "
        "una torre alta para ver venir a los enemigos, pero cada piso "
        "necesita su ración exacta de materiales. Resuelve estas divisiones "
        "para que nuestra torre llegue bien alto y podamos ganar la partida "
        "desde arriba.",
    ),
    (
        "¡Atrapados en la tormenta!",
        "Nos hemos entretenido abriendo un cofre y la tormenta nos ha "
        "alcanzado. Perdemos vida a cada segundo y tenemos que salir "
        "corriendo hacia el círculo. Para avanzar más rápido construiremos "
        "rampas que nos lleven por encima de las colinas, y cada rampa gasta "
        "materiales. Si calculamos mal, nos quedaremos sin nada en medio de "
        "la tormenta. ¡Rápido, resuelve estas divisiones y sácanos de aquí "
        "antes de que sea tarde!",
    ),
    (
        "¡Cambio de zona!",
        "La zona segura acaba de moverse al otro lado del río y tenemos que "
        "cruzarlo cuanto antes. No hay ningún puente cerca, así que vamos a "
        "construir uno con nuestros materiales. Necesitamos saber cuántas "
        "piezas caben con lo que llevamos y cuánto gastar en cada una para "
        "llegar hasta la otra orilla. Resuelve estas divisiones y ayúdanos a "
        "construir el puente antes de que la tormenta nos alcance.",
    ),
    (
        "¡Carrera contra la tormenta!",
        "Quedan treinta segundos para que la tormenta se cierre y estamos "
        "muy lejos del círculo. La única forma de llegar a tiempo es "
        "construir una larga fila de rampas y correr por encima de ellas. "
        "Cada rampa necesita sus materiales, y si nos faltan a mitad de "
        "camino caeremos en plena tormenta. ¿Nos echas una mano? Resuelve "
        "estas divisiones para calcular cuántas rampas podemos hacer y ganar "
        "la carrera.",
    ),
    (
        "¡Ojo con el borde de la tormenta!",
        "Hemos decidido quedarnos en el borde de la tormenta para que nadie "
        "nos ataque por la espalda. Es una buena estrategia, pero los "
        "enemigos que entren en el círculo pasarán justo por delante de "
        "nosotros. Hay que levantar una pared larga y resistente, y repartir "
        "bien los materiales entre todos sus trozos. Resuelve estas "
        "divisiones para que nuestra defensa aguante y sigamos vivos hasta "
        "el final.",
    ),
    (
        "¡El círculo se mueve!",
        "En esta partida el último círculo no se queda quieto, sino que se "
        "va moviendo por el mapa. Cada vez que se desplaza tenemos que "
        "abandonar nuestro fuerte y construir otro nuevo un poco más allá. "
        "Eso significa que los materiales deben durar para varios fuertes, "
        "y hay que repartirlos con mucho cuidado. Resuelve estas divisiones "
        "y ayúdanos a planificar cada fuerte para llegar hasta el final.",
    ),
    (
        "¡Tormenta a la vista!",
        "Desde lo alto de la montaña vemos cómo la tormenta morada avanza "
        "hacia nosotros. Tenemos un minuto para bajar, cruzar el valle y "
        "llegar al círculo, y abajo nos espera otro equipo escondido. "
        "Vamos a necesitar muros para cubrirnos y rampas para escapar si "
        "las cosas se complican. Resuelve estas divisiones para calcular los "
        "materiales de cada construcción y ganar esta carrera contra la "
        "tormenta.",
    ),
    (
        "¡La última zona!",
        "Solo queda un círculo pequeñísimo y todos los jugadores estamos "
        "dentro. No hay árboles ni casas, solo lo que cada uno sea capaz de "
        "construir. Quien tenga mejor organizados sus materiales podrá "
        "levantar más muros y aguantar más tiempo. ¡Ese tienes que ser tú! "
        "Resuelve estas divisiones para repartir cada material en el sitio "
        "justo y conseguir que nuestro equipo sea el último en pie.",
    ),
    (
        "¡Sobrevivir a la tormenta!",
        "La tormenta ha dejado la isla casi vacía y solo quedan unos pocos "
        "jugadores escondidos en sus fuertes. Para ganar tendremos que "
        "acercarnos a ellos sin que nos vean, construyendo paredes y techos "
        "por el camino. Cada construcción es una cuenta, y una sola cuenta "
        "mal hecha puede dejarnos al descubierto. ¿Nos ayudas? Resuelve "
        "estas divisiones y llévanos hasta la victoria magistral.",
    ),
    # --- 21 a 30: el último círculo y el duelo final -------------------------
    (
        "¡Último círculo: solo quedamos tres!",
        "Hemos llegado a la zona final y quedan solo dos rivales, uno a cada "
        "lado. Estamos rodeados y no hay sitio donde esconderse, así que la "
        "única forma de salir vivos es levantar un fuerte bien alto antes "
        "de que nos disparen. Tenemos que repartir los materiales entre "
        "todas las paredes y rampas sin malgastar ni uno solo, y para eso "
        "hay que hacer bien las cuentas. ¡Eres nuestra última esperanza! "
        "Resuelve estas divisiones y ayúdanos a conseguir la victoria.",
    ),
    (
        "¡Uno contra uno!",
        "Solo quedamos nosotros y un último rival. Es el momento más "
        "importante de la partida y cada decisión cuenta. Él está "
        "construyendo una torre enorme, así que nosotros tenemos que "
        "construir una aún más alta y resistente. Para conseguirlo hay que "
        "saber exactamente cuántos materiales poner en cada piso. ¡Toda la "
        "partida depende de tus cálculos! Resuelve estas divisiones y "
        "llévanos a la victoria magistral.",
    ),
    (
        "¡A un paso de la victoria!",
        "Hemos sobrevivido a toda la partida y solo nos separa un rival de "
        "la victoria magistral. Nos quedan pocos materiales y no podemos "
        "malgastar ni uno: cada muro, cada rampa y cada techo tiene que estar "
        "perfectamente calculado. Si lo hacemos bien, aguantaremos sus "
        "disparos y le ganaremos. Resuelve estas divisiones y ayúdanos a dar "
        "el último paso hacia la victoria.",
    ),
    (
        "¡Los cinco últimos!",
        "Quedamos cinco jugadores en la isla y todos estamos dentro de un "
        "círculo muy pequeño. Los demás ya han empezado a construir sus "
        "torres y se disparan entre ellos. Nosotros vamos a esperar "
        "escondidos en un fuerte bien protegido, pero para eso necesitamos "
        "calcular cuántos materiales poner en cada pared. Resuelve estas "
        "divisiones para que nuestro fuerte aguante mientras los demás se "
        "eliminan entre sí.",
    ),
    (
        "¡Duelo en lo alto!",
        "El último rival está en lo alto de una torre y nos dispara desde "
        "arriba. Para tener una oportunidad tenemos que subir más alto que "
        "él, construyendo rampas y muros a la vez. Cada rampa que ponemos "
        "gasta materiales, y si nos quedamos sin ellos a mitad de camino, "
        "caeremos al suelo. ¿Nos ayudas con las cuentas? Resuelve estas "
        "divisiones y ganemos juntos este duelo en las alturas.",
    ),
    (
        "¡La victoria magistral está cerca!",
        "Nunca habíamos llegado tan lejos en una partida. Quedan solo dos "
        "equipos y el nuestro tiene más materiales, pero el otro tiene "
        "mejores armas. Nuestra ventaja será construir mejor que ellos: "
        "muros más resistentes, rampas más altas y fuertes bien cerrados. "
        "Para eso hay que calcular con precisión cuánto gastar en cada "
        "pieza. Resuelve estas divisiones y llévanos a la victoria "
        "magistral.",
    ),
    (
        "¡El duelo final!",
        "Estamos frente a frente con el último enemigo y los dos tenemos "
        "poca vida. Quien construya mejor ganará la partida. Él usa mucha "
        "madera porque es rápida de poner; nosotros preferimos el metal, "
        "que aguanta más, pero hay que calcular bien cuánto tenemos para "
        "cada muro. Resuelve estas divisiones para que nuestras "
        "construcciones resistan sus disparos y ganemos el duelo final.",
    ),
    (
        "¡Sin materiales no hay victoria!",
        "Hemos llegado al último círculo con muy pocos materiales, y eso es "
        "un problema: sin ellos no podemos construir nada para protegernos. "
        "Tendremos que aprovechar al máximo cada trozo de madera, piedra y "
        "metal que nos queda, repartiéndolo con mucho cuidado entre los "
        "muros y las rampas. Resuelve estas divisiones para que no se "
        "desperdicie ni una pieza y podamos ganar la partida.",
    ),
    (
        "¡Todo o nada!",
        "Es la última pelea de la partida y nos lo jugamos todo. El rival "
        "acaba de romper nuestro fuerte y tenemos que reconstruirlo en "
        "segundos. Sabemos cuántos materiales nos quedan, pero no cuántos "
        "usar en cada pared para que el nuevo fuerte sea igual de "
        "resistente. ¡Ahí entras tú! Resuelve estas divisiones lo más rápido "
        "que puedas y ayúdanos a ganar esta pelea de todo o nada.",
    ),
    (
        "¡El trono de la isla!",
        "Quien gane esta partida será el rey de la isla, y queremos que "
        "seas tú. Ya hemos eliminado a casi todos los rivales, pero los que "
        "quedan son los mejores constructores del servidor. Para superarlos "
        "tenemos que construir más rápido y mejor que ellos, sin desperdiciar "
        "ni un material. Resuelve estas divisiones y ayúdanos a calcular "
        "cada construcción para subir al trono de la isla.",
    ),
    # --- 31 a 40: el equipo ----------------------------------------------------
    (
        "¡El escuadrón te necesita!",
        "Nuestro escuadrón ha aterrizado en el centro del mapa y ya se oyen "
        "disparos por todas partes. Hemos recogido montones de materiales, "
        "pero ahora hay que repartirlos bien entre los cuatro compañeros "
        "para que cada uno pueda construir su defensa. Si alguien se queda "
        "corto, los enemigos lo eliminarán y perderemos la partida. Tú eres "
        "el encargado de los cálculos del equipo: resuelve estas divisiones "
        "para que todos tengamos lo necesario y lleguemos juntos al final "
        "del Battle Royale.",
    ),
    (
        "¡Partida en dúo!",
        "Hoy jugamos en dúo y tú eres nuestro compañero. Mientras uno "
        "dispara, el otro tiene que construir para protegernos a los dos, "
        "así que es muy importante saber cuántos materiales usar en cada "
        "muro. Si nos equivocamos, nos quedaremos sin nada cuando más lo "
        "necesitemos. Resuelve estas divisiones para que nuestras "
        "construcciones aguanten y podamos ganar juntos esta partida en "
        "dúo.",
    ),
    (
        "¡Compañero caído!",
        "Un enemigo ha derribado a nuestro compañero y tenemos que "
        "reanimarlo antes de que lo eliminen. Para hacerlo sin que nos "
        "disparen, hay que construir una caja de muros a su alrededor y "
        "quedarnos dentro unos segundos. Cada muro necesita sus materiales y "
        "no podemos fallar ni uno. ¡Rápido, resuelve estas divisiones! Así "
        "sabremos cuánto gastar en cada pared y salvaremos a nuestro "
        "compañero.",
    ),
    (
        "¡Trío en apuros!",
        "Jugamos en trío y estamos rodeados por dos equipos a la vez. La "
        "única forma de salir de aquí es que cada uno construya su parte del "
        "fuerte: uno los muros, otro las rampas y otro los techos. Para que "
        "nadie se quede sin materiales hay que repartirlos con mucho "
        "cuidado entre los tres. Resuelve estas divisiones y ayúdanos a "
        "organizar el equipo para escapar del cerco.",
    ),
    (
        "¡Repartiendo el botín!",
        "Acabamos de eliminar a un escuadrón entero y han dejado en el suelo "
        "un montón de materiales y armas. Ahora toca repartir el botín entre "
        "los cuatro miembros del equipo de forma justa, para que todos "
        "puedan construir lo que necesiten en la siguiente pelea. ¿Nos "
        "ayudas a hacer el reparto? Resuelve estas divisiones para que nadie "
        "se quede con menos de lo que le toca y sigamos ganando.",
    ),
    (
        "¡Trabajo en equipo!",
        "En Fortnite gana el equipo que mejor se organiza, no el que tiene "
        "las mejores armas. Nuestro escuadrón ha decidido construir un "
        "fuerte gigante entre los cuatro, y cada uno se encargará de un lado. "
        "Para que el fuerte quede bien cerrado, todos tenemos que gastar los "
        "materiales en la medida justa. Resuelve estas divisiones y ayúdanos "
        "a coordinar las construcciones del equipo.",
    ),
    (
        "¡El nuevo del equipo!",
        "Hoy te unes a nuestro escuadrón y te hemos dado el trabajo más "
        "importante: llevar las cuentas de los materiales. Nosotros "
        "recogeremos madera, piedra y metal, y tú nos dirás cuánto gastar en "
        "cada muro, rampa o torre para protegernos de los enemigos. Si las "
        "cuentas salen bien, llegaremos al final de la partida. ¡Demuestra "
        "lo que vales y resuelve estas divisiones!",
    ),
    (
        "¡Nos cubrimos las espaldas!",
        "Nuestro compañero está disparando desde lo alto de una colina y "
        "necesita que alguien le proteja por detrás. Ese alguien somos "
        "nosotros: tenemos que construir una pared de muros a su espalda "
        "para que nadie le sorprenda. Pero la pared es larga y los "
        "materiales escasos, así que hay que calcular bien cuánto poner en "
        "cada tramo. Resuelve estas divisiones y protejamos juntos a nuestro "
        "compañero.",
    ),
    (
        "¡Estrategia de escuadrón!",
        "Antes de la pelea final, nuestro escuadrón se ha reunido para "
        "planear la estrategia. Tenemos una cantidad de materiales y hay que "
        "decidir cuánto dar a cada compañero y cuánto gastar en cada "
        "construcción. Un buen plan puede darnos la victoria, y uno malo nos "
        "dejará sin defensa. ¡Tú eres el estratega del equipo! Resuelve estas "
        "divisiones y prepara el mejor plan para ganar.",
    ),
    (
        "¡Somos el último escuadrón!",
        "De todos los escuadrones que empezaron la partida solo quedamos "
        "dos, y el nuestro está completo. Tenemos ventaja, pero el otro "
        "equipo se ha hecho fuerte en una torre enorme. Para asaltarla "
        "tendremos que construir rampas por los cuatro lados a la vez, y "
        "cada compañero necesita sus materiales. Resuelve estas divisiones "
        "para repartirlos bien y conseguir juntos la victoria magistral.",
    ),
    # --- 41 a 50: las batallas de construcción -------------------------------
    (
        "¡Batalla de construcción!",
        "Un rival nos ha encontrado y ha empezado a construir a toda "
        "velocidad para ganarnos la altura. Quien tenga el fuerte más alto "
        "y resistente se llevará la victoria, así que tenemos que poner "
        "muros, rampas, suelos y techos más rápido que él. Pero los "
        "materiales se acaban enseguida, y para que no se nos derrumbe "
        "nada hay que calcular exactamente cuánto usar en cada pieza. "
        "¡Necesitamos tu ayuda! Resuelve estas divisiones para ganar la "
        "batalla de construcción y quedarnos con la victoria magistral.",
    ),
    (
        "¡Guerra de rampas!",
        "Un enemigo está subiendo con rampas hacia nosotros y tenemos que "
        "impedir que nos gane la altura. La única forma es construir "
        "nuestras propias rampas más rápido que él, una encima de otra. "
        "Cada rampa gasta materiales, y si se nos acaban, él llegará arriba "
        "primero. ¿Nos ayudas con los cálculos? Resuelve estas divisiones "
        "para saber cuántas rampas podemos construir y ganar esta guerra.",
    ),
    (
        "¡Torre de noventa grados!",
        "Vamos a construir la famosa torre de noventa grados, la que sube "
        "en espiral girando sin parar. Es la mejor forma de ganar altura muy "
        "deprisa, pero gasta muchísimos materiales: en cada vuelta hay que "
        "poner un muro, una rampa y un suelo. Para no quedarnos a medias "
        "tenemos que calcular cuántas vueltas podemos dar. Resuelve estas "
        "divisiones y ayúdanos a subir hasta lo más alto.",
    ),
    (
        "¡Encerrados en una caja!",
        "Estamos dentro de una caja de cuatro muros, un suelo y un techo, y "
        "el enemigo está fuera intentando romperla. Cada vez que destroza una "
        "pared tenemos que reconstruirla al momento. Para aguantar todo el "
        "combate necesitamos saber cuántos materiales podemos gastar en cada "
        "reparación. Resuelve estas divisiones y ayúdanos a mantener la caja "
        "cerrada hasta que el enemigo se rinda.",
    ),
    (
        "¡Edición rápida!",
        "Los mejores jugadores no solo construyen: también editan sus "
        "muros para abrir ventanas y puertas por las que disparar. Nosotros "
        "queremos aprender a hacerlo, pero cada muro que editamos y volvemos "
        "a cerrar gasta materiales. Para practicar sin quedarnos sin nada "
        "tenemos que llevar bien las cuentas. Resuelve estas divisiones para "
        "calcular los materiales y convertirnos en expertos de la edición.",
    ),
    (
        "¡Fuerte de metal!",
        "Hemos decidido construir un fuerte entero de metal, el material más "
        "resistente del juego. El problema es que el metal tarda en "
        "construirse y es el que menos abunda, así que no podemos "
        "desperdiciar ni una pieza. Tenemos que repartir el metal entre "
        "todas las paredes y techos para que el fuerte quede completo. "
        "Resuelve estas divisiones y ayúdanos a levantar el fuerte más duro "
        "de la isla.",
    ),
    (
        "¡Madera, piedra y metal!",
        "Tenemos los tres materiales del juego y cada uno sirve para algo. "
        "La madera se construye rápido, la piedra aguanta un poco más y el "
        "metal es el más resistente. Para ganar la próxima pelea hay que "
        "decidir cuánto usar de cada uno en nuestras construcciones. ¡Esa "
        "decisión es tuya! Resuelve estas divisiones para repartir bien los "
        "materiales y construir la defensa perfecta.",
    ),
    (
        "¡Muros que no caen!",
        "El enemigo tiene un arma muy potente que rompe los muros de un par "
        "de disparos. Para aguantar tendremos que poner varias capas de muros "
        "una detrás de otra, y eso gasta muchos materiales. Hay que calcular "
        "cuántas capas podemos permitirnos con lo que llevamos en la "
        "mochila. Resuelve estas divisiones y ayúdanos a levantar unos muros "
        "que el enemigo no pueda derribar.",
    ),
    (
        "¡El campeón de la construcción!",
        "Hoy se celebra un torneo de construcción en la isla y queremos "
        "ganarlo. Gana el jugador que levante el fuerte más grande con los "
        "materiales que le dan al empezar. No hay que ser el más rápido, "
        "sino el que mejor aproveche cada pieza. ¡Necesitamos tu cabeza para "
        "los números! Resuelve estas divisiones para repartir los "
        "materiales y convertirnos en campeones de la construcción.",
    ),
    (
        "¡Construcción a toda velocidad!",
        "Un equipo entero viene corriendo hacia nosotros y tenemos muy pocos "
        "segundos para protegernos. Hay que construir lo más rápido posible, "
        "pero sin equivocarnos, porque cada error nos hace perder materiales "
        "y tiempo. Por eso los cálculos tienen que estar hechos antes de "
        "empezar a construir. Resuelve estas divisiones para que sepamos "
        "cuánto poner en cada pieza y aguantemos el ataque.",
    ),
    # --- 51 a 60: objetos y botín --------------------------------------------
    (
        "¡Una llama de suministros!",
        "Hemos encontrado una llama de suministros, una de las cosas más "
        "valiosas de la isla. Al romperla nos ha dado munición, vendas y "
        "cientos de materiales. Ahora hay que decidir cómo repartirlos entre "
        "las construcciones que haremos en el resto de la partida. Si lo "
        "hacemos bien, tendremos defensa hasta el final. Resuelve estas "
        "divisiones y ayúdanos a aprovechar este tesoro.",
    ),
    (
        "¡Lanzamiento de suministros!",
        "Un globo con una caja de suministros está bajando del cielo justo "
        "delante de nosotros. Dentro hay armas legendarias, pero otros "
        "equipos también lo han visto y vienen a por él. Para llegar primero "
        "y abrir la caja sin que nos disparen, hay que construir muros "
        "alrededor. ¿Nos ayudas con los materiales? Resuelve estas "
        "divisiones y consigamos el botín antes que nadie.",
    ),
    (
        "¡El cofre dorado!",
        "Detrás de esa pared brilla un cofre dorado, pero está en medio de "
        "un campo abierto lleno de enemigos. Para llegar a él sin que nos "
        "eliminen vamos a construir un pasillo de muros desde nuestra "
        "posición hasta el cofre. Hay que calcular cuántos muros caben con "
        "los materiales que tenemos. Resuelve estas divisiones y ayúdanos a "
        "abrir el cofre sin recibir ni un disparo.",
    ),
    (
        "¡Escudos para todos!",
        "Hemos encontrado varias pociones de escudo y tenemos que "
        "repartirlas entre los miembros del escuadrón. Mientras nos las "
        "bebemos, alguien tiene que proteger al grupo construyendo muros a "
        "nuestro alrededor. Para que nadie se quede sin escudo ni sin "
        "protección hay que hacer bien las cuentas. Resuelve estas "
        "divisiones y ayúdanos a prepararnos para la siguiente pelea.",
    ),
    (
        "¡Botiquín en peligro!",
        "Tenemos poca vida y necesitamos usar un botiquín, que tarda unos "
        "segundos en curarnos. Durante ese tiempo no podemos movernos, así "
        "que hay que construir una caja de muros a nuestro alrededor para "
        "que nadie nos ataque. Cada muro necesita sus materiales y no hay "
        "margen para fallar. Resuelve estas divisiones para calcular la caja "
        "perfecta y curarnos sin peligro.",
    ),
    (
        "¡El arma legendaria!",
        "Por fin hemos conseguido un arma legendaria, la más potente de la "
        "partida. Pero con ella no basta para ganar: los rivales se "
        "esconderán detrás de sus construcciones y nosotros tendremos que "
        "construir más rápido que ellos para acercarnos. Para eso hay que "
        "saber cuántos materiales usar en cada rampa y en cada muro. "
        "Resuelve estas divisiones y saquemos todo el partido a nuestra "
        "nueva arma.",
    ),
    (
        "¡Máquina expendedora!",
        "Hemos encontrado una máquina que cambia materiales por objetos "
        "muy útiles. El problema es que, si gastamos demasiado en la "
        "máquina, no nos quedará suficiente para construir nuestras "
        "defensas. Hay que calcular muy bien cuánto podemos gastar en "
        "objetos y cuánto guardar para muros y rampas. Resuelve estas "
        "divisiones y ayúdanos a hacer el mejor intercambio de la partida.",
    ),
    (
        "¡Caja de munición!",
        "Hemos abierto una caja de munición y ahora tenemos balas para "
        "rato. Pero de nada sirven si los enemigos nos disparan sin que "
        "tengamos dónde cubrirnos. Antes de atacar, vamos a preparar una "
        "buena defensa con los materiales que llevamos, repartidos entre "
        "varios muros y una torre. Resuelve estas divisiones para calcular "
        "cada construcción y lanzarnos al ataque bien protegidos.",
    ),
    (
        "¡Tesoro enterrado!",
        "Hemos encontrado un mapa del tesoro que marca un sitio en la playa. "
        "Allí hay enterrado un arma especial, pero la playa está totalmente "
        "despejada y cualquiera nos verá mientras cavamos. Tendremos que "
        "construir un pequeño fuerte para protegernos mientras sacamos el "
        "tesoro. Resuelve estas divisiones y ayúdanos a calcular los "
        "materiales del fuerte para conseguir el arma.",
    ),
    (
        "¡Pescando en el lago!",
        "Estamos pescando en el lago porque algunos peces nos curan la vida "
        "y nos dan escudo. Mientras pescamos estamos muy expuestos, así que "
        "hay que construir muros en la orilla para que nadie nos dispare "
        "desde los árboles. Los materiales no sobran y hay que repartirlos "
        "bien entre todos los muros. Resuelve estas divisiones y ayúdanos a "
        "pescar tranquilos para ganar la partida.",
    ),
    # --- 61 a 70: lugares de la isla ------------------------------------------
    (
        "¡Pelea en la ciudad!",
        "Hemos llegado a una ciudad llena de edificios altos y en cada "
        "ventana puede haber un enemigo. Para movernos de un edificio a "
        "otro sin que nos vean, construiremos puentes y paredes entre los "
        "tejados. Cada puente necesita su cantidad exacta de materiales, "
        "porque si se queda corto nos caeremos a la calle. Resuelve estas "
        "divisiones y ayúdanos a cruzar la ciudad de tejado en tejado.",
    ),
    (
        "¡En lo alto de la montaña!",
        "Hemos subido a la montaña más alta de la isla y desde aquí "
        "dominamos todo el mapa. Es el mejor sitio para defenderse, pero "
        "también el más buscado por los demás jugadores. Vamos a construir "
        "un fuerte en la cima para que nadie pueda echarnos, y hay que "
        "repartir bien los materiales entre todas sus paredes. Resuelve estas "
        "divisiones y ayúdanos a convertir la montaña en nuestro castillo.",
    ),
    (
        "¡Emboscada en el bosque!",
        "Caminamos por el bosque y, de repente, nos disparan desde detrás de "
        "los árboles. ¡Es una emboscada! Tenemos que construir muros a toda "
        "prisa para cubrirnos y averiguar desde dónde nos atacan. Por suerte, "
        "aquí hay mucha madera, pero hay que calcular cuánta gastar en cada "
        "muro para no quedarnos sin nada. Resuelve estas divisiones y "
        "ayúdanos a salir del bosque con vida.",
    ),
    (
        "¡Cruzando el desierto!",
        "Tenemos que atravesar el desierto para llegar a la zona segura, y "
        "en el desierto no hay dónde esconderse. Ni árboles, ni rocas, ni "
        "casas: solo arena y algún cactus. Toda nuestra protección tendrá que "
        "salir de los materiales que llevamos en la mochila. Resuelve estas "
        "divisiones para calcular cuántos muros podemos construir por el "
        "camino y cruzar el desierto sin que nos eliminen.",
    ),
    (
        "¡Batalla en la nieve!",
        "Estamos en la zona nevada de la isla y el suelo resbala muchísimo. "
        "Los enemigos se deslizan por las colinas a toda velocidad y nos "
        "disparan desde cualquier lado. Para protegernos vamos a construir "
        "un iglú de muros y techos, y hay que calcular bien cuántos "
        "materiales usar en cada pieza para que no se derrumbe. Resuelve "
        "estas divisiones y ganemos la batalla en la nieve.",
    ),
    (
        "¡Defensa en la granja!",
        "Nos hemos refugiado en una vieja granja, con su granero, su "
        "molino y un montón de balas de paja. Es un buen escondite, pero sus "
        "paredes son de madera y se rompen enseguida. Hay que reforzarlas con "
        "nuestras propias construcciones antes de que lleguen los enemigos. "
        "Resuelve estas divisiones para calcular los materiales de cada "
        "refuerzo y defender la granja hasta el final.",
    ),
    (
        "¡Pelea en el castillo!",
        "Hemos llegado a un castillo en ruinas en lo alto de una colina. "
        "Tiene torres y murallas, pero muchas están rotas y llenas de "
        "agujeros. Vamos a tapar cada hueco con nuestras construcciones para "
        "que nadie pueda entrar, y para eso necesitamos saber cuántos "
        "materiales poner en cada agujero. Resuelve estas divisiones y "
        "ayúdanos a convertir este castillo en una fortaleza.",
    ),
    (
        "¡La isla del lago!",
        "En medio del gran lago hay una pequeña isla y queremos llegar a "
        "ella para escondernos. No tenemos barca, así que construiremos un "
        "puente de suelos desde la orilla. Después levantaremos un fuerte en "
        "la isla para defendernos. Hay que repartir los materiales entre el "
        "puente y el fuerte para que lleguen para todo. Resuelve estas "
        "divisiones y ayúdanos a conquistar la isla del lago.",
    ),
    (
        "¡Bajo tierra!",
        "Hemos descubierto unos túneles secretos debajo de la isla. Son un "
        "escondite perfecto, pero tienen varias entradas y por cualquiera "
        "de ellas puede aparecer un enemigo. Vamos a bloquearlas todas con "
        "muros, menos una que vigilaremos nosotros. Hay que calcular cuántos "
        "materiales gastar en cada entrada. Resuelve estas divisiones y "
        "ayúdanos a convertir los túneles en nuestra base secreta.",
    ),
    (
        "¡En el puerto!",
        "Estamos en el puerto, rodeados de contenedores, grúas y barcos. "
        "Los contenedores son un buen escondite, pero los enemigos pueden "
        "subirse encima y dispararnos desde arriba. Para evitarlo vamos a "
        "construir techos y muros entre los contenedores, y hay que repartir "
        "bien los materiales. Resuelve estas divisiones y ayúdanos a "
        "defender el puerto hasta que llegue la tormenta.",
    ),
    # --- 71 a 80: vehículos, noche y situaciones especiales ------------------
    (
        "¡Al volante!",
        "Hemos encontrado un coche y vamos a usarlo para llegar a la zona "
        "segura a toda velocidad. Pero al bajarnos estaremos rodeados de "
        "enemigos que habrán oído el motor. En cuanto paremos tendremos que "
        "construir muros alrededor del coche para protegernos. Resuelve estas "
        "divisiones para tener los cálculos preparados y que, al llegar, "
        "levantemos la defensa en un abrir y cerrar de ojos.",
    ),
    (
        "¡Partida nocturna!",
        "Se ha hecho de noche en la isla y apenas se ve nada. Los enemigos "
        "aprovechan la oscuridad para acercarse sin que los veamos, así que "
        "es mejor estar bien protegidos. Vamos a construir un fuerte cerrado "
        "por todos los lados y esperar dentro a que amanezca. Resuelve estas "
        "divisiones para calcular los materiales de cada pared y pasar la "
        "noche a salvo.",
    ),
    (
        "¡Francotirador a la vista!",
        "Un francotirador nos está disparando desde muy lejos y no sabemos "
        "exactamente dónde está. Cada vez que asomamos la cabeza, ¡pum!, "
        "perdemos vida. Necesitamos construir una línea de muros para "
        "avanzar hacia él sin que nos vea. Hay que calcular cuántos muros "
        "podemos poner con los materiales que nos quedan. Resuelve estas "
        "divisiones y ayúdanos a llegar hasta el francotirador.",
    ),
    (
        "¡Nos atacan por sorpresa!",
        "Estábamos tranquilamente recogiendo materiales cuando un equipo nos "
        "ha atacado por sorpresa. No hay tiempo para pensar: hay que "
        "construir ya. Por suerte, tú puedes hacer los cálculos mientras "
        "nosotros ponemos los muros. Necesitamos saber cuántos materiales "
        "usar en cada pieza para que la defensa aguante el ataque. ¡Rápido, "
        "resuelve estas divisiones y sálvanos!",
    ),
    (
        "¡Saltando con la plataforma!",
        "Hemos encontrado una plataforma de salto que nos lanza muy alto. "
        "Desde arriba podremos planear hasta la zona segura, pero al "
        "aterrizar estaremos solos y a la vista de todos. Habrá que "
        "construir una defensa nada más tocar el suelo, con los materiales "
        "justos para cada pared. Resuelve estas divisiones para tener las "
        "cuentas hechas antes de saltar.",
    ),
    (
        "¡El gran asalto!",
        "Un equipo se ha encerrado en una torre gigante y no hay forma de "
        "sacarlos de ahí. Vamos a lanzar un gran asalto construyendo rampas "
        "por los cuatro lados al mismo tiempo. Para que todas las rampas "
        "lleguen hasta arriba hay que repartir los materiales con mucha "
        "precisión. ¿Nos ayudas a preparar el asalto? Resuelve estas "
        "divisiones y conquistemos la torre enemiga.",
    ),
    (
        "¡Retirada estratégica!",
        "Hemos perdido mucha vida en la última pelea y lo más inteligente es "
        "retirarse a un lugar seguro para recuperarnos. Mientras huimos, "
        "iremos dejando muros detrás de nosotros para frenar a los "
        "enemigos que nos persiguen. Hay que calcular cuántos muros podemos "
        "poner por el camino sin quedarnos sin materiales. Resuelve estas "
        "divisiones y ayúdanos a escapar.",
    ),
    (
        "¡Escondidos en un arbusto!",
        "Nos hemos disfrazado de arbusto para pasar desapercibidos, pero un "
        "enemigo está a punto de descubrirnos. En cuanto nos vea, tendremos "
        "que construir una caja de muros a toda velocidad. Para estar "
        "preparados, ya queremos saber cuántos materiales gastar en cada "
        "muro. Resuelve estas divisiones mientras seguimos escondidos y "
        "estaremos listos para cuando empiece la pelea.",
    ),
    (
        "¡Rescate en el tejado!",
        "Nuestro compañero se ha quedado atrapado en el tejado de un edificio "
        "y abajo le esperan varios enemigos. Para rescatarlo vamos a "
        "construir una rampa desde el edificio de al lado y un pasillo de "
        "muros para que pueda escapar. Todo eso necesita materiales bien "
        "repartidos. Resuelve estas divisiones y ayúdanos a rescatar a "
        "nuestro compañero antes de que sea tarde.",
    ),
    (
        "¡La trampa perfecta!",
        "Vamos a preparar una trampa para los enemigos: un fuerte que parece "
        "vacío, pero dentro estaremos esperando nosotros. Para que el "
        "engaño funcione, el fuerte tiene que ser grande y resistente, y eso "
        "gasta muchos materiales. Hay que calcular muy bien cuánto poner en "
        "cada pared. Resuelve estas divisiones y ayúdanos a construir la "
        "trampa perfecta para ganar la partida.",
    ),
    # --- 81 a 90: entrenamientos y retos ---------------------------------------
    (
        "¡Entrenamiento de constructor!",
        "Antes de la gran partida del fin de semana vamos a entrenar en el "
        "modo creativo. Queremos practicar la construcción de torres, cajas "
        "y rampas, y cada ejercicio usa una cantidad diferente de materiales. "
        "Para aprovechar bien el entrenamiento necesitamos tener todas las "
        "cuentas hechas. Resuelve estas divisiones y ayúdanos a convertirnos "
        "en los mejores constructores de la isla.",
    ),
    (
        "¡Reto semanal!",
        "Esta semana el juego nos ha propuesto un reto: construir doscientas "
        "piezas en una sola partida. Si lo conseguimos, ganaremos un montón "
        "de experiencia para subir de nivel. Pero para construir tanto hay "
        "que organizar muy bien los materiales y saber cuánto usar en cada "
        "pieza. Resuelve estas divisiones y ayúdanos a completar el reto "
        "semanal.",
    ),
    (
        "¡Torneo de la isla!",
        "Hoy jugamos el torneo más importante del año y los mejores "
        "jugadores del mundo están en la isla. Para ganarles no basta con "
        "disparar bien: hay que construir mejor que nadie y no desperdiciar "
        "ni un material. Cada partida del torneo es un examen de cálculo. "
        "¿Estás preparado? Resuelve estas divisiones y ayúdanos a ganar el "
        "torneo de la isla.",
    ),
    (
        "¡Subiendo de nivel!",
        "Nos falta muy poco para subir al siguiente nivel del pase de "
        "batalla y conseguir una skin nueva. Para lograrlo tenemos que "
        "quedar entre los diez primeros en esta partida, y eso significa "
        "sobrevivir hasta el último círculo. Las construcciones serán clave "
        "para protegernos de los enemigos. Resuelve estas divisiones para "
        "calcular los materiales y subir de nivel.",
    ),
    (
        "¡Partida igualada!",
        "Esta partida está muy igualada: todos los jugadores que quedan "
        "tienen buenas armas y mucha experiencia. La diferencia la marcará "
        "quien mejor administre sus materiales. Nosotros queremos ser los "
        "más listos y calcular cada construcción antes de hacerla. Resuelve "
        "estas divisiones para que nuestras defensas sean las más eficaces "
        "y ganemos esta partida tan reñida.",
    ),
    (
        "¡Récord de victorias!",
        "Llevamos tres victorias seguidas y queremos conseguir la cuarta "
        "para batir nuestro récord. Los rivales ya nos conocen y vienen a "
        "por nosotros desde el principio de la partida. Tendremos que "
        "construir más y mejor que nunca, sin malgastar ni un material. "
        "Resuelve estas divisiones y ayúdanos a calcular cada construcción "
        "para batir el récord de victorias.",
    ),
    (
        "¡Solo con el pico!",
        "Esta vez nos hemos propuesto un reto difícil: ganar la partida "
        "construyendo con los materiales que consigamos solo con el pico. "
        "Eso significa recoger poco a poco y aprovechar al máximo cada trozo "
        "de madera, piedra y metal. Hay que repartirlos con mucho cuidado "
        "entre los muros y las rampas. Resuelve estas divisiones y ayúdanos "
        "a superar este reto.",
    ),
    (
        "¡Partida de práctica!",
        "Estamos en una partida de práctica con amigos para mejorar nuestras "
        "construcciones. Cada uno tiene la misma cantidad de materiales y "
        "gana quien levante el fuerte más alto sin que se caiga. El secreto "
        "está en calcular bien cuántos materiales poner en cada piso. "
        "Resuelve estas divisiones y ayúdanos a ganar esta partida de "
        "práctica contra nuestros amigos.",
    ),
    (
        "¡Misión diaria!",
        "La misión de hoy consiste en construir diez torres en diferentes "
        "lugares de la isla sin que nos eliminen. Cada torre necesita la "
        "misma cantidad de materiales, así que hay que repartir todo lo que "
        "llevamos entre las diez. Si calculamos mal, no podremos terminar la "
        "última. Resuelve estas divisiones y ayúdanos a completar la misión "
        "diaria.",
    ),
    (
        "¡El mejor constructor!",
        "Dicen que en esta isla hay un jugador que construye más rápido que "
        "nadie, y hoy queremos ganarle. Sabemos que su secreto es tener "
        "siempre los materiales bien organizados. Nosotros vamos a hacer lo "
        "mismo, pero con tu ayuda: tú harás los cálculos y nosotros "
        "construiremos. Resuelve estas divisiones y demostremos quién es el "
        "mejor constructor de la isla.",
    ),
    # --- 91 a 100: misiones y finales ------------------------------------------
    (
        "¡Misión: defender la base!",
        "Nuestro escuadrón ha montado una base en el centro del mapa y los "
        "demás equipos quieren quitárnosla. La base tiene muchas paredes y "
        "todas necesitan refuerzos antes del próximo ataque. Hay que "
        "repartir los materiales entre todas ellas, sin dejar ninguna "
        "débil. Resuelve estas divisiones y ayúdanos a defender la base "
        "hasta el final de la partida.",
    ),
    (
        "¡Misión: proteger al compañero!",
        "Nuestro compañero lleva el arma más potente del equipo y tenemos "
        "que protegerlo a toda costa. Mientras él dispara, nosotros "
        "construiremos muros a su alrededor para que ningún enemigo le "
        "alcance. Hay que calcular bien cuántos materiales usar en cada muro "
        "para que la protección dure toda la pelea. Resuelve estas "
        "divisiones y cumplamos juntos la misión.",
    ),
    (
        "¡Misión: llegar al centro!",
        "El último círculo se va a cerrar justo en el centro del mapa, y "
        "queremos ser los primeros en llegar para escoger el mejor sitio. "
        "El camino es largo y está lleno de enemigos, así que iremos "
        "construyendo muros y rampas por el camino. Resuelve estas "
        "divisiones para repartir los materiales entre todo el trayecto y "
        "llegar al centro antes que nadie.",
    ),
    (
        "¡Misión: sobrevivir diez minutos!",
        "El reto de hoy es aguantar vivos diez minutos en la zona más "
        "peligrosa de la isla. No hace falta eliminar a nadie, solo resistir. "
        "Para lograrlo vamos a construir un fuerte enorme y reforzarlo cada "
        "vez que lo ataquen. Hay que calcular cuántos materiales gastar en "
        "cada refuerzo para que lleguen hasta el final. Resuelve estas "
        "divisiones y ayúdanos a sobrevivir.",
    ),
    (
        "¡Misión: la torre más alta!",
        "Queremos construir la torre más alta que se haya visto nunca en la "
        "isla, tan alta que desde arriba se vea todo el mapa. Pero cuanto "
        "más alta es la torre, más materiales gasta, y no podemos quedarnos "
        "a medias. Hay que calcular cuántos pisos podemos construir con lo "
        "que tenemos. Resuelve estas divisiones y ayúdanos a tocar el cielo "
        "con nuestra torre.",
    ),
    (
        "¡Misión: escapar del cerco!",
        "Tres equipos nos han rodeado y nos disparan desde todos los lados. "
        "La única salida es construir un túnel de muros y techos que nos "
        "permita escapar sin que nos vean. Cada tramo del túnel gasta "
        "materiales y no podemos quedarnos sin ellos en mitad de la huida. "
        "Resuelve estas divisiones para calcular cuánto usar en cada tramo y "
        "escapar del cerco.",
    ),
    (
        "¡Misión: recuperar la corona!",
        "En la última partida ganamos la corona de la victoria, pero un "
        "rival nos la quiere quitar. Si nos elimina, se la quedará él. "
        "Tenemos que protegernos mejor que nunca, con muros, techos y "
        "rampas bien construidos y sin malgastar materiales. Resuelve estas "
        "divisiones y ayúdanos a calcular cada construcción para conservar "
        "la corona una partida más.",
    ),
    (
        "¡Misión: el último refugio!",
        "La tormenta ha cubierto casi toda la isla y solo queda un pequeño "
        "trozo de tierra a salvo. Todos los jugadores que quedan se dirigen "
        "hacia allí. Nosotros queremos llegar primero y construir el último "
        "refugio de la partida, uno tan resistente que nadie pueda "
        "romperlo. Resuelve estas divisiones para calcular sus materiales y "
        "ganar desde dentro.",
    ),
    (
        "¡Misión: victoria magistral!",
        "Esta es la misión más importante de todas: conseguir la victoria "
        "magistral. Para lograrlo habrá que sobrevivir a la tormenta, ganar "
        "las batallas de construcción y quedar como el último jugador en "
        "pie. Todo eso depende de tener los materiales bien calculados en "
        "cada momento. Resuelve estas divisiones y ayúdanos a cumplir la "
        "misión que todos los jugadores sueñan con completar.",
    ),
    (
        "¡Celebramos la victoria!",
        "¡Lo hemos conseguido! Gracias a tus cálculos ganamos la última "
        "partida y ahora todo el servidor quiere jugar contra nosotros. En "
        "la próxima partida vendrán a por nuestro equipo desde el primer "
        "minuto, así que tenemos que estar preparados. Resuelve estas "
        "divisiones para tener listos los materiales de nuestras "
        "construcciones y volver a ganar.",
    ),
]
