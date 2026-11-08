# Ayuda del proyecto «divisiones»

Referencia técnica: qué hace cada fichero, cada constante y cada función.
Para saber qué es el proyecto, cómo se instala y cómo se usa, mira el
**[README.md](README.md)**.

Reglas de las divisiones en todo el proyecto:

- Cada ficha tiene siempre 6 divisiones, sin repetir ninguna.
- El dividendo tiene tres cifras enteras y dos decimales (de 100,01 a
  999,99) y el divisor, dos cifras enteras y dos decimales (de 10,01 a
  99,99).
- La cifra de las centésimas nunca es 0: 345,60 no vale, porque en realidad
  es 345,6.
- Los números se guardan como enteros en centésimas (34567 = 345,67) para
  evitar los errores de redondeo de los números decimales del ordenador.
  Solo se pasan a texto con coma al escribir el PDF.

## Cómo encajan los ficheros

```
divisiones.py   main(): lee los argumentos, genera las divisiones «en bruto»
        │       y elige la cabecera (rotación guardada en cabeceras_salidas.json)
        │
        ├── cabeceras.py        datos: títulos y textos de las cabeceras
        ├── generacion_pdf.py   dibuja la cabecera y las divisiones y crea el PDF
        │
        └── enviar_email.py     envía el PDF por correo (opción -e)

servidor.py + index.html   página web que ejecuta «divisiones.py -e»
```

---

## `divisiones.py`

Es el programa principal. Solo contiene `main`, la generación de las
divisiones «en bruto» (los números, no el PDF) y la elección de la
cabecera.

### Constantes

| Nombre | Para qué sirve |
|---|---|
| `ASUNTO_EMAIL`, `TEXTO_EMAIL` | Asunto y texto del correo que se envía con `-e`. |
| `NUM_EJERCICIOS` | Número de divisiones de la ficha (6). |
| `DIVIDENDO_MIN`, `DIVIDENDO_MAX` | Límites del dividendo, en centésimas: de `100_00` a `999_99`. |
| `DIVISOR_MIN`, `DIVISOR_MAX` | Límites del divisor, en centésimas: de `10_00` a `99_99`. |
| `FICHERO_CABECERAS_SALIDAS` | Fichero `cabeceras_salidas.json`, donde se apuntan los títulos de las cabeceras que ya han salido. Se crea en la carpeta desde la que se ejecuta el programa, que es la misma de los PDF (en Docker, `/app/pdfs`). |

### Funciones

| Función | Qué hace |
|---|---|
| `numero_con_dos_decimales(minimo, maximo)` | Devuelve un número al azar entre los dos límites, en centésimas, cuya última cifra no sea 0. Así el número siempre tiene dos decimales de verdad. |
| `generar_divisiones(num_ejercicios)` | Crea las parejas `(dividendo, divisor)` de la ficha, en centésimas, por ejemplo `(34567, 1234)` para 345,67 : 12,34. No repite ninguna pareja. |
| `validar_cabeceras()` | Comprueba que no haya dos cabeceras con el mismo título, porque el título es lo que identifica a cada una en `cabeceras_salidas.json`. Si hay alguno repetido, el programa termina con un error que dice cuál. |
| `leer_cabeceras_salidas()` | Lee `cabeceras_salidas.json` y devuelve la lista de títulos que ya han salido en la ronda actual. Si el fichero no existe o está estropeado, devuelve una lista vacía y empieza una ronda nueva. Ignora los títulos que ya no están en `cabeceras.py`. |
| `guardar_cabeceras_salidas(salidas)` | Guarda esa lista en `cabeceras_salidas.json`. |
| `elegir_cabecera()` | Elige al azar la cabecera `(título, texto)` de la ficha, solo entre las que aún no han salido. Cuando han salido todas, empieza una ronda nueva, y la primera cabecera de esa ronda nunca es la última que salió. Devuelve `(cabecera, salidas)`: la cabecera elegida y la lista que hay que guardar. |
| `main(argv=None)` | Función principal. Lee los argumentos (`-o` y `-e`) y comprueba que las direcciones de correo tengan `@`. Si se usó `-e`, comprueba antes de nada los datos del correo con `preparar_envio` (si falta algo, termina sin generar nada). Después comprueba las cabeceras, genera las divisiones, elige la cabecera, crea el PDF con `mostrar_salida` y guarda la cabecera elegida (solo cuando el PDF ya está creado). Si se usó `-e`, al final envía el PDF por correo. |

---

## `generacion_pdf.py`

Convierte los números en texto y dibuja la ficha, con la cabecera que le
pasa `divisiones.py`, en el PDF. Todo lo que tiene que ver con el aspecto de la ficha se cambia con las
constantes del principio del fichero.

### Constantes

| Nombre | Para qué sirve |
|---|---|
| `FUENTE_TITULO`, `FUENTE_TEXTO`, `FUENTE_DIVISIONES` | Fuente del título, del texto de la cabecera y de los números de las divisiones. Cada una puede ser una fuente estándar de PDF (`"Helvetica"`, `"Times-Roman"`, `"Courier"`) o la ruta a un `.ttf` relativa a la carpeta del proyecto. Ahora: Anton para el título y el texto, y Fredoka para las divisiones. |
| `TAMANO_TEXTO` | Tamaño de la letra del texto de la cabecera, en puntos (13,5). El título, los márgenes, las separaciones y las divisiones se calculan a partir de él. |
| `MARGEN_SUPERIOR`, `MARGEN_INFERIOR` | Márgenes de arriba y de abajo de la página. El de arriba es una línea de texto más pequeño que el de abajo (18 mm), para que la cabecera quede más arriba. |
| `SEPARACION_TITULO` | Espacio entre el título y el texto de la cabecera. |
| `SEPARACION_CABECERA` | Espacio entre el texto de la cabecera y la cuadrícula de divisiones. |
| `COLUMNAS`, `FILAS` | Forma de la cuadrícula de divisiones: 2 columnas por 3 filas. |
| `TAMANO_DIVISION` | Tamaño de «toda» la división: es el tamaño de los números, y el grosor de las líneas de la caja se ajusta solo a él. Súbelo o bájalo para dejar más o menos sitio para escribir. |
| `POSICION_CAJA` | Dónde va la línea vertical de la caja, en proporción al ancho de la celda (0,55). A la izquierda queda el dividendo y el sitio para ir restando; a la derecha, el divisor y el cociente. |
| `MARGEN_CELDA` | Margen interior de cada celda de la cuadrícula, en puntos. |
| `COLOR_CUADRICULA` | Color de las líneas que separan las celdas. Con `None` no se dibujan. |
| `COLOR_CAJA` | Color de las líneas de la caja de la división. |
| `PREFIJO_PDF`, `PATRON_NUMERO_PDF` | Prefijo del nombre automático de los PDF (`divisiones`) y el patrón para encontrar el número del último PDF de la carpeta. |

### Funciones

| Función | Qué hace |
|---|---|
| `formatear_numero(centesimas)` | Pasa un número en centésimas a texto con coma decimal: `34567` → `"345,67"`. |
| `mostrar_salida(divisiones, cabecera, ruta_pdf)` | Es el único punto de salida del programa: si algún día cambia el destino, solo hay que tocar este fichero. Pasa los números a texto, llama a `generar_pdf` con la cabecera `(título, texto)` elegida en `divisiones.py` y escribe por consola el PDF generado y la cabecera que ha salido. En Docker, ese mensaje es el que aparece en el log del contenedor. |
| `registrar_fuente(fuente)` | Prepara una fuente para usarla en el PDF y devuelve su nombre. Las estándar las devuelve tal cual. Los `.ttf` los registra, y usa el mismo fichero para la negrita y la cursiva, porque estas fuentes no las tienen. Si no encuentra el fichero, termina con un error. |
| `DivisionCaja` | Dibuja una división con su caja, ocupando todo el ancho de la celda. El dividendo va a la izquierda. La caja tiene forma de «L»: una línea vertical en `POSICION_CAJA`, a la izquierda del divisor, que baja solo hasta la línea horizontal de debajo del divisor, y esa horizontal llega hasta el borde derecho. |
| `DivisionCaja.wrap(ancho, alto)` | Le dice al PDF cuánto sitio ocupa la división: todo el ancho disponible y 1,15 veces `TAMANO_DIVISION` de alto. |
| `DivisionCaja.draw()` | Dibuja los números y las dos líneas de la caja. |
| `cuadricula_divisiones(ejercicios, fuente, ancho, alto)` | Crea la tabla de `COLUMNAS` x `FILAS` con una división en la parte de arriba de cada celda. Todas las celdas tienen el mismo tamaño y entre todas ocupan el ancho y el alto que se le indiquen. |
| `generar_pdf(titulo, texto, ejercicios, ruta_pdf)` | Escribe el PDF: el título (siempre en mayúsculas, al estilo Fortnite), el texto de la cabecera y la cuadrícula de divisiones. Mide lo que ocupa la cabecera y le da a la cuadrícula todo el alto que queda en la página. El título o el texto pueden ser `""` para que no salgan. |
| `nombre_pdf_automatico(carpeta)` | Devuelve el nombre del PDF cuando no se usa `-o`: `divisiones_<día-mes>_<hora>_<año>_<número>.pdf`. El número es uno más que el más alto que ya haya en la carpeta y no se reinicia. |

---

## `cabeceras.py`

Solo contiene datos. `CABECERAS` es la lista de las 100 cabeceras posibles.
Cada una es una pareja `(título, texto)` con una historia de Fortnite: hay
que ayudar a ganar el Battle Royale calculando los materiales de las
construcciones.

Cada vez que se genera un PDF se elige una al azar, pero sin repetir
ninguna hasta que han salido todas, y nunca sale la misma en dos fichas
seguidas (ver `elegir_cabecera` en `divisiones.py`). Las que ya han salido
se apuntan por su título en `cabeceras_salidas.json`, así que **cada
cabecera tiene que tener un título distinto** (se comprueba al arrancar).
Si se cambia el título de una cabecera, cuenta como una nueva.

Para tener más variedad, basta con añadir parejas a la lista: las nuevas
entran en la ronda actual. El texto puede ser `""` para que no salga.
Ningún texto pasa ahora de 7 líneas en el PDF; cuanto más largo es el
texto, menos sitio queda para hacer las divisiones.

`cabeceras.v1.py` es la lista anterior, con las 5 primeras cabeceras. El
programa no la usa.

---

## `enviar_email.py`

Envía el PDF por correo (SMTP de Brevo). Los datos privados (servidor,
puerto, tipo de seguridad, usuario, contraseña, remitente y `DESTINATARIOS`
por defecto) **no están en el código**: se leen de un fichero con el formato
de `.env.ejemplo`, que no se sube a git. Se usa uno solo, el primero que
exista:

1. `/run/secrets/divisiones_env`: en Docker, el secreto `divisiones_env`
   (ver `docker-compose.yml`).
2. El `.env` de la carpeta del proyecto: al ejecutarlo fuera de Docker. En
   un ordenador nuevo hay que copiar el `.env` de otro ordenador, o copiar
   `.env.ejemplo` como `.env` y rellenarlo.

Los datos se leen **solo de ese fichero**: las variables de entorno no se
usan ni se modifican, así que una variable que ya existiera en la terminal
(de otro proyecto o de una prueba antigua) no puede cambiar a quién o desde
dónde se envía el correo. Si no existe ninguno de los dos ficheros, o no se
puede leer, el programa avisa y termina.

El fichero solo se lee cuando se usa `-e`, y se hace al principio, antes de
generar nada: si falta algo, no se crea el PDF. Sin `-e` no hace falta tener
`.env`.

Este fichero es igual que el de multiplicaciones: solo cambia el nombre del
secreto. Si se cambia uno, conviene cambiar también el otro.

| Función | Qué hace |
|---|---|
| `RUTA_SECRETO`, `RUTA_ENV_PROYECTO` | Las dos rutas donde se buscan los datos privados. |
| `SERVIDOR_POR_DEFECTO`, `PUERTO_POR_DEFECTO`, `SEGURIDAD_POR_DEFECTO` | Valores que se usan si el fichero no indica `SERVIDOR_SMTP`, `PUERTO_SMTP` o `SEGURIDAD`. |
| `fichero_env()` | Devuelve la ruta que se usa: el secreto de Docker si existe y, si no, el `.env` del proyecto. |
| `cargar_env(ruta)` | Lee las líneas `CLAVE=valor` del fichero y las devuelve en un diccionario, sin tocar las variables de entorno. Ignora líneas vacías y comentarios y quita las comillas del valor. Si el fichero no existe o no se puede leer, termina con un mensaje claro. |
| `leer_configuracion()` | Carga el fichero y devuelve la configuración del correo (servidor, puerto, seguridad, usuario, contraseña, remitente, nombre del remitente y `DESTINATARIOS`), con los valores por defecto donde falten. Termina con un mensaje claro si el puerto no es un número. |
| `comprobar_configuracion(configuracion, ruta)` | Comprueba que estén rellenos el usuario, la contraseña y el remitente, y que `SEGURIDAD` sea `"tls"` o `"ssl"`. Si falta algo, termina con un mensaje claro. |
| `preparar_envio(direcciones)` | Se llama desde `main` antes de generar el PDF. Lee la configuración y decide los destinatarios: las direcciones de `-e` o, si no hay, los `DESTINATARIOS` del fichero (si tampoco hay, termina). Devuelve `(configuracion, destinatarios)`. |
| `crear_mensaje(configuracion, destinatarios, asunto, texto, ruta_pdf)` | Construye el correo con remitente, destinatarios, asunto y texto, y el PDF adjunto. |
| `enviar_pdf(configuracion, destinatarios, asunto, texto, ruta_pdf)` | Envía el correo con lo que devolvió `preparar_envio`. Se conecta con SSL o STARTTLS según `SEGURIDAD` y avisa si falla la contraseña o la conexión. |

---

## `servidor.py`

Servidor web sencillo, sin dependencias externas. Muestra `index.html`, que
tiene un botón «Generar». Al pulsarlo, se crea la ficha y se envía por
correo.

Lo que escribe `divisiones.py` por consola (el PDF generado, la cabecera
que ha salido, el resultado del correo o el error) solo se muestra en la
consola del servidor, que en Docker es el log del contenedor. La página web
solo dice si ha ido bien o mal.

| Nombre | Qué hace |
|---|---|
| `CARPETA_PDFS` | Carpeta donde se guardan los PDF y `cabeceras_salidas.json`. Se puede cambiar con la variable de entorno `CARPETA_PDFS`; por defecto es la carpeta del proyecto. En Docker es `/app/pdfs`. |
| `ESPERA_SEGUNDOS` | Segundos que hay que esperar entre una ficha y la siguiente (20), para no mandar muchos correos por error. |
| `segundos_restantes()` | Devuelve los segundos que faltan para poder generar otra ficha (0 si ya se puede). |
| `Manejador` | Clase que atiende las peticiones de la web. |
| `Manejador._responder(codigo, tipo, cuerpo)` | Envía una respuesta HTTP con su código, su tipo de contenido y su cuerpo. |
| `Manejador._responder_json(codigo, mensaje)` | Responde con un JSON que lleva el mensaje y `espera`, los segundos que faltan. La página usa `espera` para la cuenta atrás del botón. |
| `Manejador.do_GET()` | Devuelve la página `index.html`, o un 404 si se pide otra dirección. |
| `Manejador.do_POST()` | Atiende `/generar`. Si ya se está generando una ficha, responde 409. Si aún no ha pasado la espera, responde 429. Si no, ejecuta `divisiones.py -e` en `CARPETA_PDFS`, con un límite de 120 s. Pasa la salida del script a la consola del servidor e informa a la página de si ha ido bien. La espera empieza a contar al terminar, haya ido bien o mal. |
| `main()` | Lee el puerto (`-p`, por defecto 80, el que se usa en Docker) y arranca el servidor para toda la red local. Fuera de Docker, un usuario normal no puede usar el 80, así que hay que indicar otro, por ejemplo `-p 8000`. Se para con Ctrl+C. |

---

## Otros ficheros

| Fichero | Qué es |
|---|---|
| `index.html` | La página web con el botón «Generar» y la cuenta atrás. |
| `Dockerfile`, `docker-compose.yml` | Sirven para ejecutar el servidor en Docker (`docker compose up -d --build`). El servidor escucha en el puerto 80 del contenedor, pero no se publica ningún puerto en el host: Nginx Proxy Manager está en la misma red de Docker y apunta a `divisiones`, puerto 80. Para unir el contenedor a la red de NPM hay un bloque `networks` comentado en `docker-compose.yml`. Los PDF y `cabeceras_salidas.json` se guardan en `/app/pdfs`, que es el volumen de Docker `divisiones_pdfs`: se conservan al recrear o actualizar el contenedor, y solo se borran con `docker compose down -v` o desde Portainer. Los PDF se acumulan y nada los borra. La contraseña no va en la imagen: `docker-compose.yml` monta el `.env` como secreto de Docker (`divisiones_env`) al arrancar. |
| `fonts/` | Fuentes `Anton-Regular.ttf` y `Fredoka-SemiBold.ttf`, con sus licencias `OFL-Anton.txt` y `OFL-Fredoka.txt`. Las dos son libres (SIL Open Font License), así que se pueden subir a git y redistribuir siempre que vayan acompañadas de su licencia. Anton es la alternativa libre más parecida a la letra de Fortnite (Burbank Big Condensed, que es de pago). |
| `cabeceras_salidas.json` | Se crea solo. Guarda los títulos de las cabeceras que ya han salido en la ronda actual. Si lo borras, empieza una ronda nueva. No se sube a git. En Docker está en `/app/pdfs`, dentro del volumen `divisiones_pdfs`, así que se conserva al recrear el contenedor. |
| `.env` | Datos privados del correo, incluida la contraseña. **No se sube a git**: hay que copiarlo a mano a cada ordenador. |
| `.env.ejemplo` | Plantilla del `.env`, sin datos reales. Sí se sube a git. |
| `.gitignore` | Lo que git no sincroniza: `.env`, `.venv/`, `__pycache__/`, los PDF, `cabeceras_salidas.json` y los ficheros del entorno de desarrollo creados con `uv init` (`src/`, `pyproject.toml`, `.python-version`, `uv.lock`). |
| `.dockerignore` | Lo que no se envía a Docker al construir la imagen. |
| `README.md` | Portada del repositorio: qué es, instalación, uso y licencias. |
| `AYUDA.md` | Este fichero. |
| `docs/ejemplo.png` | Captura de una ficha de ejemplo que aparece en el README. Hay que regenerarla a mano si cambia mucho el aspecto de la ficha. |
| `CLAUDE.md` | Notas técnicas del proyecto para Claude Code. |
