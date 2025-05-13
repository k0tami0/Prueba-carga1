"""
Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
"""
def par_impar (numero: int) -> int:
    par = True
    if numero % 2 == 1:
        par = False
    return par

ingreso_usuario = int(input("Ingrese el numero a verificar: ")) 
resultado = par_impar(ingreso_usuario)
if resultado:
    print(f"El numero ingresado {ingreso_usuario} es par.")
else:
    print(f"El numero ingresado {ingreso_usuario} es impar.")