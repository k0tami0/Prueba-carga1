"""
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
"""

clave_usuario = input("Establezca su clave: ")

clave_ingresada= input("Ingrese su clave: ")

while clave_ingresada != clave_usuario:
    clave_ingresada =input("Contraseña incorrecta, intente nuevamente: ")

print("Acceso permitido")