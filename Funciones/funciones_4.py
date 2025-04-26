"""
Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retornar el área. 
"""
def area_rectangulo (base: int, altura: int ) -> int:
    area = base * altura
    return area

base_rectangulo= int(input("Ingrese la base del rectángulo: "))
altura_rectangulo= int(input("Ingrese la altura del rectángulo: "))
resultado = area_rectangulo(base_rectangulo, altura_rectangulo)
print(resultado)
