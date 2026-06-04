import shelve

def mostrar_ropa(misprendas):
    print("\nROPA DISPONIBLE\n")

    for prenda in misprendas:
        print(
            "Tienes",
            prenda["tipo"],
            "de color",
            prenda["color"],
            "con",
            prenda["usos"],
            "usos."
        )

config = shelve.open("miropero.dat")

misprendas = config["misprendas"]

config.close()

mostrar_ropa(misprendas)
