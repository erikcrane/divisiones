"""Encabezados de la ficha, con temática de Fortnite.

Solo datos, sin lógica. Cada vez que se genera un PDF se elige uno al azar
(ver `mostrar_salida` en `generacion_pdf.py`).

Cada encabezado es una pareja (título, texto). Cualquiera de los dos puede
ser "" para que esa parte no salga. Para añadir variedad basta con añadir
más parejas a la lista. Conviene que los textos tengan una longitud
parecida (unas 7 líneas): cuanto más largo es el texto, menos sitio queda
para hacer las divisiones.
"""

CABECERAS = [
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
]
