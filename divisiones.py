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

Los números se guardan como enteros en centésimas (34567 = 345,67) para no
arrastrar errores de redondeo de los float.

Este módulo solo genera las divisiones "en bruto". El PDF se genera en
`generacion_pdf.py`, mediante `mostrar_salida`, para poder cambiar más
adelante el destino sin tocar el resto del programa.
"""

import argparse
import random

from enviar_email import enviar_pdf
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

    divisiones = generar_divisiones(NUM_EJERCICIOS)
    ruta_pdf = args.salida or nombre_pdf_automatico()
    mostrar_salida(divisiones, ruta_pdf)

    if args.email is not None:
        enviar_pdf(direcciones, ASUNTO_EMAIL, TEXTO_EMAIL, ruta_pdf)


if __name__ == "__main__":
    main()
