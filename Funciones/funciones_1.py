"""
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
"""

def numero_entero(numero= "Ingrese un numero entero: ", mensaje_error= "ERROR - Debe ingresar un numero válido" ,min = 1, max = 1000 ) -> int:
    while True:
        entrada = input(numero)
        if entrada.isdecimal():
            entrada= int(entrada)
            if min <= entrada <= max:
                return entrada
            else:
                print(f"{mensaje_error}, entre {min} y {max}")
        else:
            print(f"{mensaje_error}, '{entrada}' no es válido")

valor_usuario = numero_entero()
print(f"El numero ingresado fue {valor_usuario}")

    