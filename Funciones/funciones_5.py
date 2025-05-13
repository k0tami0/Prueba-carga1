"""
Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
"""
import math 

def area_circulo (radio : int) -> float:
    area = math.pi * radio**2
    return area

radio_circulo = int(input("Ingrese el radio del circulo: "))
resultado_area = area_circulo(radio_circulo)
print(resultado_area)