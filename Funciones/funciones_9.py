"""
Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
"""
def calculo_potencia(base : int, exponente : int) -> int:
    potencia = base ** exponente
    return potencia

base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))
resultado = calculo_potencia(base, potencia)
print(resultado)