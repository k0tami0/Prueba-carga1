"""
Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
"""
def par_impar (numero: int) -> bool:
    par = True
    if numero % 2 == 1:
        par = False
    return par

ingreso_usuario = int(input("Ingrese el numero a verificar: ")) 
resultado = par_impar(ingreso_usuario)

print(resultado)

