"""
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
"""

def pedir_entero(mensaje : str, mensaje_error : str = "ERROR - Debe ingresar un numero válido" ,min : int = 1, max : int = 1000, intentos : int = 3) -> int | None:
    """
    Args:
        mensaje (str): Se pide el ingreso de un número.
        mensaje_error (str, optional): El mensaje que se mostrara por pantalla en caso de que lo ingresado no sea válido. por default es: "ERROR - Debe ingresar un numero válido".
        min (int, optional): El valor mínimo que el usuario puede ingresar. Por defecto es 1.
        max (int, optional): El valor mínimo que el usuario puede ingresar. Por defecto es 1000.
        intentos (int, optional): La cantidad de intentos que tiene el usuario. Por defecto es 3.

    Returns:
        int | None : Retorna el numero entero si cumple las condiciones o None en caso de no cumplirlas.
    """
    numero = None
    contador = intentos
    for i in range(intentos + 1):
        if i == 0:
            entrada = input(mensaje)
        else:
            entrada = input(f"{mensaje_error}, {mensaje}, tiene {contador} intento(s): ")
            contador -= 1
        if entrada.isdigit():
            entrada = int(entrada)
            if min <= entrada <= max:
                numero = entrada
                break
    return numero

legajo_alumno = pedir_entero("Ingrese el N° de Legajo: ", "No se ingresó un legajo válido", 1000, 2000, 2 )#1000 - #2000

edad_alumno = pedir_entero ("Ingrese la edad del alumno: ", "No se ingresó una edad válida", 18,25 , 2)#18 #25

nota_alumno =pedir_entero ("Ingrese la nota del alumno: ", "No se ingresó una nota válida", 1, 10, 2)

print(f"El alumno con legajo {legajo_alumno}, de {edad_alumno}, tiene una calificación de: {nota_alumno}")
