import math

def area_circulo(radio: int|float) -> float:
    """Calcula el area de un círculo

    
    """
    area_circulo = math.pi * math.pow(radio, 2)
    return area_circulo

area= area_circulo(5)
print(f"{area:.2f}")