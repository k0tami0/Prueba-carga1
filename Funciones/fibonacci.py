"""
Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:
Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
"""

def fibonacci(numero):
    if numero == 0:
        resultado = 0
    elif numero == 1:
        resultado = 1
    else:
        resultado = fibonacci(numero - 1) + fibonacci(numero - 2)
    return resultado


for i in range(18):
    if i == 0:
        print(f"{i} : 0")
    elif i == 1:
        print(f"{i} : 1")
    else:
        a = fibonacci(i - 1)
        b = fibonacci(i - 2)
        print(f"{i} : {a} + {b} = {a + b}")