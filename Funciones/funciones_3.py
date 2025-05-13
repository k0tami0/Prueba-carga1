"""
Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
"""
def texto (ingreso = "Ingrese un mensaje: ")-> str:
    mensaje_usuario = input(ingreso)
    return mensaje_usuario

ingreso_usuario= texto()
print(ingreso_usuario)
