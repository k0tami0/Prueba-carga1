"""
Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
"""

def numero_decimal(mensaje= "Ingrese un numero decimal: " ) -> float:
    valor = float(input(mensaje))
    return valor

ingreso_usuario = numero_decimal()

print(f"{ingreso_usuario:.2f}")