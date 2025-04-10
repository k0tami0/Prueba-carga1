"""
Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.
"""
contador = 0
acumulador_numeros =  0

while True:
    numero = int(input(f"Ingrese el {contador +1}° numero: "))
    acumulador_numeros += numero
    contador += 1

    if contador == 5:
        pregunta = input("Ya ingresó 5 numeros, ¿Desea seguir ingresando más? (Maximo 10) si/no: ")
        if pregunta != "si":
            break
    elif contador == 10:
        break
promedio = acumulador_numeros / contador
print(f"La suma de todos los numeros ingresado es de {acumulador_numeros} y su promedio es {promedio:.2f}")