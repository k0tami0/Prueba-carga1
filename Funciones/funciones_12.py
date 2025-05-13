"""
Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro.
La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
Por defecto es del 1 al 10.
"""

def tabla_de_multiplicar(numero = "Ingrese el numero a multiplicar: ", error="Error, no se ingresó un numero, pruebe nuevamente: ", minimo = 1, maximo = 10 ) -> int:
    numero = input(numero)
    while not numero.isdigit():
        numero = input(error)
    numero = int(numero)
    minimo = int(input("Defina el valor minimo a multiplicar: "))
    maximo = int(input("Defina el valor maximo a multiplicar: "))
    for i in range (minimo, maximo + 1):
        tabla = numero * i
        print(f"{numero} * {i} = {tabla}")

tabla_de_multiplicar()

