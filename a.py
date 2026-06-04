# -*- coding: utf-8 -*-
# El código está optimizado a lo máximo posible para que no consuma tanto

import shelve

p = [
    {"tipo": "camisa", "color": "roja", "usos": 2},
    {"tipo": "camisa", "color": "verde", "usos": 0},
    {"tipo": "pantalon", "color": "azul", "usos": 1},
    {"tipo": "pantalon", "color": "negro", "usos": 3},
    {"tipo": "zapatos", "color": "negros", "usos": 5},
    {"tipo": "zapatos", "color": "marrones", "usos": 2}
]

r = [
    ["roja", "azul", "marrones"],
    ["verde", "negro", "negros"]
]

config = shelve.open("d.dat")

config["p"] = p
config["r"] = r

config.close()

print("Datos guardados correctamente.")
