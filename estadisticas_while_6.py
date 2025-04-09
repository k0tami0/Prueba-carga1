"""
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
"""

suma_total = 0
contador = 0
pregunta = "si"
while pregunta == "si":
    numero = int(input(f"Ingrese un número: "))
    suma_total += numero
    contador += 1
    pregunta=input("¿Desea seguir ingresando numeros? si/no : ")

promedio = suma_total / contador

print(f"La suma total es {suma_total} y su promedio es {promedio}")