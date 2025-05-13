#Se pasa el valor ingresado por usuario, en este caso 5
def recursiva(numero: int) -> int:
#el programa pregunta, 5 es igual a 0? En este caso no por lo que pasa al else
    if numero == 0:
        numero = 1
        return numero
#aca se acumula la recursiva, por lo que seria numero(5) = numero(5) * recursiva(numero - 1) (4)
#para resolver esa multiplicación antes se necesita resolver la recursiva(numero - 1), asi que el programa continua hasta que encuentre el valor base
#en este caso es el 0, al numero ser 0 se le asiga el valor 1 y la cuenta queda numero(1) = numero(1) * recursiva(numero - 1) == 1
    else:    
        numero = numero * recursiva(numero - 1)
#El programa retorna el valor de numero para que las anteriores funciones se resuelva en el orden de ultima a primera
        return numero
    
print(recursiva(5))

#Realizar una función recursiva que calcule la suma de los primeros números naturales:

def suma_recursiva (numero: int) -> int:
    if numero == 0:
        return 0
    else:
        numero = numero + suma_recursiva (numero - 1)
        return numero
print(suma_recursiva(5))

def calcular_potencia(base : int, exponente: int) -> int:
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
    return resultado

print (calcular_potencia(2,3))

def sumar_digitos(numero:int) -> int:
    if numero < 10:
        suma = numero
    else:
        suma = numero % 10  + sumar_digitos(numero // 10)
    return suma

print(sumar_digitos(123))

"""
Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:
Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
"""

def fibonacci(numero):
    if numero < 0:
        suma = numero
    else:
        suma = numero + 1 + fibonacci(numero - 2)
    return suma

print(fibonacci(9))