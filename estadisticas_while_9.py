"""
Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.
"""

contador = 0
acumulador_numeros =  0

while True:
    numero = int(input("Ingrese un numero (Mínimo 5): "))
    acumulador_numeros += numero
    contador += 1

    if contador == 5:
        pregunta = input("¿Desea seguir ingresando números? si/no: ")
        if pregunta != "si":
            break
        else:
            contador = 4
promedio = acumulador_numeros // contador
print(f"La suma de todos los numeros ingresado es de {acumulador_numeros} y su promedio es {promedio}")