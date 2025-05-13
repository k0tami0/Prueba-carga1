"""
Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
1- Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
2- Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
3- Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
"""
def validar_entero(numero= "Ingrese un numero entero: ", mensaje_error= "ERROR - Debe ingresar un numero válido" ,min = 1, max = 1000 ) -> int:
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
print(validar_entero())

def validar_decimal(numero= "Ingrese un numero decimal: ", mensaje_error= "ERROR - Debe ingresar un numero válido" ,min = 1, max = 1000 ) -> float:
    while True:
        entrada = input(numero)
        try:
            entrada= float(entrada)
            if min <= entrada <= max:
                return entrada
            else:
                print(f"{mensaje_error}, entre {min} y {max}")
        except ValueError:
            print(f"{mensaje_error}, '{entrada}' no es válido")
print(validar_decimal())

def validar_cadena(mensaje= "Ingrese su mensaje: ") -> str:
    entrada = input(mensaje)
    return entrada
print(validar_cadena())