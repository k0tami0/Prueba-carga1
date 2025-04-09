"""
Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
"""
nota_ingresada = int(input("Ingrese una nota: "))

while nota_ingresada < 1 or nota_ingresada > 10:
    print(f"La nota {nota_ingresada} no es válida, debe ser un número entre 1 y 10")
    nota_ingresada = int(input("Ingrese una nota: "))

print(f"La nota ingresada fue {nota_ingresada}")
