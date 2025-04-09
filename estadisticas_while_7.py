"""
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
"""

acumulador_positivos = 0
acumulador_negativos = 1
seguir = "si"
while seguir == "si":
    numeros= int(input("Ingrese un número: "))
    if numeros > 0 :
        acumulador_positivos += numeros
    else:
        acumulador_negativos *= numeros
    seguir =input("¿Desea seguir? si/no: ")
print(f"La suma de los numeros positivos es {acumulador_positivos} y el producto de los negativos es {acumulador_negativos}")

