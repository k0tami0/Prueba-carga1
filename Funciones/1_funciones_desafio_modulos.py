"""
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de
la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
"""
def get_string(ingreso: str ,longitud : str = 20) -> int | None:
    mensaje  = ingreso
    largo = 0
    for a in range (len(mensaje)):
        print (a)
        largo += 1
    return largo

mensaje_usuario = input("Ingrese su mensaje ")
resultado = get_string(mensaje_usuario)
print(resultado)

