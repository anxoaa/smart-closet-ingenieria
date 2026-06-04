# -*- coding: utf-8 -*-

import shelve

misprendas = [
    {"tipo": "camisa", "color": "roja", "usos": 2},
    {"tipo": "camisa", "color": "verde", "usos": 0},
    {"tipo": "pantalon", "color": "azul", "usos": 1},
    {"tipo": "pantalon", "color": "negro", "usos": 3},
    {"tipo": "zapatos", "color": "negros", "usos": 5},
    {"tipo": "zapatos", "color": "marrones", "usos": 2}
]

misreglas = [
    ["roja", "azul", "marrones"],
    ["verde", "negro", "negros"]
]

config = shelve.open("miropero.dat")

config["misprendas"] = misprendas
config["misreglas"] = misreglas

config.close()

print("x")
