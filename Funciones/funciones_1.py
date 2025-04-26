"""
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
"""

def numero_entero(mensaje= "Ingrese un numero entero: " ) -> int:
    valor = int(input(mensaje))
    return valor

ingreso_usuario = numero_entero()

print(ingreso_usuario)

    