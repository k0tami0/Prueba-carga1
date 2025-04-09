"""
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
"""

clave_usuario = input("Establezca su clave: ")

clave_ingresada= input("Ingrese su clave: ")
contador = 3

while clave_ingresada != clave_usuario and contador > 0:
    print(f"Contraseña incorrecta le quedan {contador} intentos: ")
    clave_ingresada =input(f"Intente nuevamente: ")
    contador -=1


if clave_ingresada == clave_usuario:
    print("Acceso permitido.")
else:
    print("Cuenta bloqueada.")


