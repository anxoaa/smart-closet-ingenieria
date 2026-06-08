import shelve

def mostrar_ropa(p):
    print("\nROPA DISPONIBLE\n")

    for prenda in p:
        print(
            "Tienes",
            prenda["tipo"],
            "de color",
            prenda["color"],
            "con",
            prenda["usos"],
            "usos."
        )

config = shelve.open("d.dat")

p = config["p"]

config.close()

mostrar_ropa(p)
