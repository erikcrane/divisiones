#!/usr/bin/env python3
"""Generador de fichas de divisiones con decimales.

Reglas:
  - Cada ficha tiene siempre NUM_EJERCICIOS (6) divisiones.
  - El dividendo tiene siempre tres cifras enteras y dos decimales
    (de 100,01 a 999,99).
  - El divisor tiene siempre dos cifras enteras y dos decimales
    (de 10,01 a 99,99).
  - "Dos decimales" de verdad: la cifra de las centésimas nunca es 0
    (345,60 no vale, porque en realidad es 345,6).
  - No se repite ninguna división dentro de la misma ficha.
  - La cabecera (título y texto) se elige al azar entre las de
    `cabeceras.py`, sin repetir ninguna hasta que han salido todas (ver
    `elegir_cabecera`).

Los números se guardan como enteros en centésimas (34567 = 345,67) para no
arrastrar errores de redondeo de los float.

Este módulo solo genera las divisiones "en bruto". El PDF se genera en
`generacion_pdf.py`, mediante `mostrar_salida`, para poder cambiar más
adelante el destino sin tocar el resto del programa.
"""

import argparse
import json
import random
from pathlib import Path

from cabeceras import CABECERAS
from enviar_email import enviar_pdf, preparar_envio
from generacion_pdf import mostrar_salida, nombre_pdf_automatico

# Correo que se envía con la opción --email (el PDF va adjunto).
ASUNTO_EMAIL = "¡Nueva misión: ficha de divisiones!"
TEXTO_EMAIL = (
    "¡Hola, jugador!\n\n"
    "El autobús de batalla está a punto de despegar y tu equipo te "
    "necesita. Te envío una nueva ficha con 6 divisiones: resuélvelas para "
    "calcular los materiales de tus construcciones y protegerte de los "
    "enemigos.\n\n"
    "Recuerda: si el divisor tiene decimales, primero corre la coma para "
    "que desaparezca, y corre la del dividendo el mismo número de lugares.\n\n"
    "¡Mucha suerte y a por la victoria magistral!"
)

NUM_EJERCICIOS = 6

# Límites de cada número, en centésimas (ambos incluidos).
DIVIDENDO_MIN, DIVIDENDO_MAX = 100_00, 999_99  # 3 cifras enteras, 2 decimales
DIVISOR_MIN, DIVISOR_MAX = 10_00, 99_99  # 2 cifras enteras, 2 decimales

# Fichero donde se guardan los títulos de las cabeceras que ya han salido en
# la ronda actual. Se crea en la carpeta desde la que se ejecuta (la misma de
# los PDF; en Docker, /app/pdfs). Una cabecera no se repite hasta que han
# salido todas las demás.
FICHERO_CABECERAS_SALIDAS = Path("cabeceras_salidas.json")


def numero_con_dos_decimales(minimo, maximo):
    """Número al azar en centésimas cuya cifra de las centésimas no es 0."""
    while True:
        numero = random.randint(minimo, maximo)
        if numero % 10 != 0:
            return numero


def generar_divisiones(num_ejercicios):
    """Genera las parejas (dividendo, divisor), en centésimas, sin repetir."""
    divisiones = []
    while len(divisiones) < num_ejercicios:
        pareja = (
            numero_con_dos_decimales(DIVIDENDO_MIN, DIVIDENDO_MAX),
            numero_con_dos_decimales(DIVISOR_MIN, DIVISOR_MAX),
        )
        if pareja not in divisiones:
            divisiones.append(pareja)
    return divisiones


def validar_cabeceras():
    """Comprueba que no haya dos cabeceras con el mismo título.

    El título es lo que identifica a cada cabecera en el fichero de las que
    ya han salido, así que no puede repetirse (tampoco puede haber dos con
    el título vacío).
    """
    vistos = set()
    for titulo, _texto in CABECERAS:
        if titulo in vistos:
            raise ValueError(
                f"Hay dos cabeceras con el título {titulo!r} en cabeceras.py: "
                "cada cabecera debe tener un título distinto."
            )
        vistos.add(titulo)


def leer_cabeceras_salidas():
    """Devuelve la lista de títulos de cabeceras que ya han salido en la ronda.

    Si el fichero no existe o está estropeado, se empieza una ronda nueva.
    Los títulos que ya no están en `cabeceras.py` (porque se han quitado o
    cambiado) se ignoran.
    """
    try:
        datos = json.loads(FICHERO_CABECERAS_SALIDAS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    if not isinstance(datos, list):
        return []
    titulos = {titulo for titulo, _texto in CABECERAS}
    return [titulo for titulo in datos if titulo in titulos]


def guardar_cabeceras_salidas(salidas):
    FICHERO_CABECERAS_SALIDAS.write_text(
        json.dumps(salidas, ensure_ascii=False, indent=1), encoding="utf-8"
    )


def elegir_cabecera():
    """Elige al azar la cabecera (título, texto) de la ficha.

    Solo se elige entre las que aún no han salido en la ronda. Cuando ya han
    salido todas, empieza una ronda nueva, pero sin repetir la última que
    salió (así nunca hay dos fichas seguidas con la misma cabecera).

    Devuelve (cabecera, salidas): `salidas` es la lista que hay que guardar
    con `guardar_cabeceras_salidas` una vez generado el PDF.
    """
    salidas = leer_cabeceras_salidas()
    pendientes = [cabecera for cabecera in CABECERAS if cabecera[0] not in salidas]

    if not pendientes:
        ultima = salidas[-1]
        pendientes = [cabecera for cabecera in CABECERAS if cabecera[0] != ultima]
        salidas = []

    # Si solo hubiera una cabecera, no queda otra que repetirla.
    cabecera = random.choice(pendientes or CABECERAS)
    return cabecera, salidas + [cabecera[0]]


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="divisiones.py",
        description=(
            f"Genera una ficha PDF con {NUM_EJERCICIOS} divisiones con decimales."
        ),
        epilog=(
            "Ejemplos:\n"
            "  python3 divisiones.py\n"
            "  python3 divisiones.py -o ficha.pdf\n"
            "  python3 divisiones.py --email alguien@gmail.com\n"
            "  python3 divisiones.py -e"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-o",
        "--salida",
        metavar="PDF",
        help=(
            "ruta del PDF de salida (por defecto: "
            "divisiones_<día-mes>_<hora>_<año>_<número>.pdf)"
        ),
    )
    parser.add_argument(
        "-e",
        "--email",
        action="append",
        nargs="?",
        const="",
        metavar="DIRECCION",
        help=(
            "envía el PDF por correo a esta dirección (se puede repetir); "
            "sin dirección, a los DESTINATARIOS del fichero .env"
        ),
    )
    args = parser.parse_args(argv)

    direcciones = [d for d in args.email or [] if d]
    for direccion in direcciones:
        if "@" not in direccion:
            parser.error(f"'{direccion}' no parece una dirección de correo.")

    # Con -e, los datos del correo se comprueban antes de generar nada: si
    # falta el .env o algún dato, el programa se corta sin crear el PDF.
    envio = preparar_envio(direcciones) if args.email is not None else None

    try:
        validar_cabeceras()
    except ValueError as error:
        parser.error(str(error))

    divisiones = generar_divisiones(NUM_EJERCICIOS)
    cabecera, salidas = elegir_cabecera()
    ruta_pdf = args.salida or nombre_pdf_automatico()
    mostrar_salida(divisiones, cabecera, ruta_pdf)
    guardar_cabeceras_salidas(salidas)

    if envio is not None:
        enviar_pdf(*envio, ASUNTO_EMAIL, TEXTO_EMAIL, ruta_pdf)


if __name__ == "__main__":
    main()
