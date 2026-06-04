import shelve
import random

def mostrar_ropa(p):

    print("\nROPA DISPONIBLE\n")

    for prenda in p:
        print(
            prenda["tipo"],
            "-",
            prenda["color"],
            "- usos:",
            prenda["usos"]
        )


def ordena_ropero(p):

    camisas = []
    pantalones = []
    zapatos = []

    for prenda in p:

        if prenda["tipo"] == "camisa":
            camisas.append(prenda["color"])

        elif prenda["tipo"] == "pantalon":
            pantalones.append(prenda["color"])

        elif prenda["tipo"] == "zapatos":
            zapatos.append(prenda["color"])

    return [camisas, pantalones, zapatos]


def elige_combinacion(ropero):

    camisas = ropero[0]
    pantalones = ropero[1]
    zapatos = ropero[2]

    random.shuffle(camisas)
    random.shuffle(pantalones)
    random.shuffle(zapatos)

    combinacion = [
        camisas[0],
        pantalones[0],
        zapatos[0]
    ]

    return combinacion


def verifica_combinacion(combinacion, r):

    for regla in r:

        if combinacion == regla:
            return False

    return True


def incrementa_usos(combinacion, p):

    for prenda in p:

        if (
            prenda["tipo"] == "camisa"
            and prenda["color"] == combinacion[0]
        ):
            prenda["usos"] += 1

        elif (
            prenda["tipo"] == "pantalon"
            and prenda["color"] == combinacion[1]
        ):
            prenda["usos"] += 1

        elif (
            prenda["tipo"] == "zapatos"
            and prenda["color"] == combinacion[2]
        ):
            prenda["usos"] += 1


def selecciona_ropa(ropero, r, p):

    combina = False

    while not combina:

        combinacion = elige_combinacion(ropero)

        print("\nCombinación generada:")
        print("Camisa:", combinacion[0])
        print("Pantalón:", combinacion[1])
        print("Zapatos:", combinacion[2])

        combina = verifica_combinacion(
            combinacion,
            r
        )

        if not combina:
            print("La combinación no es válida.")
        else:
            print("La combinación es válida.")
            incrementa_usos(
                combinacion,
                p
            )


# -----------------------------
# Programa principal
# -----------------------------

config = shelve.open("d.dat")

p = config["p"]
r = config["r"]

ropero = ordena_ropero(p)

selecciona_ropa(
    ropero,
    r,
    p
)

config["p"] = p

config.close()

print("\nUsos actualizados correctamente.")

