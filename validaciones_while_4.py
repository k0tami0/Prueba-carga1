"""
Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.
"""

colores_permitidos = ["Rojo", "Verde", "Azul"]
color_ingresado = input("Ingrese un color primario (Rojo, Verde, Azul): ")

while color_ingresado not in colores_permitidos:
    print(f"El color ingresado {color_ingresado} no es un color primario.")
    color_ingresado = input("Intente nuevamente: ")

print(f"El color {color_ingresado} es primario.")
