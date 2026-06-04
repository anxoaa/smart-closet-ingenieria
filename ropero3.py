# -*- coding: utf-8 -*-

import shelve

config = shelve.open("d.dat")

p = config["p"]
r = config["r"]

config.close()

print("===== MI ROPERO =====")
print("1. Ver ropa")
print("2. Seleccionar ropa")
print("3. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("Mostrar ropa")
elif opcion == "2":
    print("Seleccionar ropa")
elif opcion == "3":
    print("Adiós")
else:
    print("Opción incorrecta")
