"""
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de
la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
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

def get_string(ingreso: str = "Ingrese el mensaje: " ,longitud : int = 20) -> str | None:
    largo_mensaje = len(ingreso)
    if largo_mensaje > longitud:
        return print(f"El mensaje {ingreso} tiene {largo_mensaje} dígitos, que superan los permitidos ({longitud})")
    else:
        return print(f"El mensaje {ingreso} tiene {largo_mensaje} dígitos")



mensaje = input("Ingrese su mensaje: ")
resultado = get_string(mensaje, 1)