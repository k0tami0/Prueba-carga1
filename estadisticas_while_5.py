"""
Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
"""
acumulador = 0
contador = 0

while contador < 5:
    numero = int(input(f"Ingrese el número {contador+1}: "))
    acumulador += numero
    contador += 1

promedio = acumulador / contador

print(f"La suma total es {acumulador} y su promedio es {promedio}")