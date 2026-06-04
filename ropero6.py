import shelve

def ordena_ropero(p):

    miscamisas = []
    mispantalones = []
    miszapatos = []

    for prenda in p:

        if prenda["tipo"] == "camisa":
            miscamisas.append(prenda["color"])

        if prenda["tipo"] == "pantalon":
            mispantalones.append(prenda["color"])

        if prenda["tipo"] == "zapatos":
            miszapatos.append(prenda["color"])

    ropero = []

    ropero.append(miscamisas)
    ropero.append(mispantalones)
    ropero.append(miszapatos)

    return ropero


def selecciona_ropa(ropero):

    print("Camisas:", ropero[0])
    print("Pantalones:", ropero[1])
    print("Zapatos:", ropero[2])


config = shelve.open("d.dat")

p = config["p"]

config.close()

ropero = ordena_ropero(p)

selecciona_ropa(ropero)
