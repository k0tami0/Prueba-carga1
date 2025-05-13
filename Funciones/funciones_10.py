"""
Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
"""
def valor_primo (numero: int) -> bool:
    es_primo = True
    if numero < 2:
        es_primo = False
    else:
        for i in range (2, numero):
            if numero % i == 0:
                es_primo = False
                break
    return es_primo

ingreso_usuario = int(input("Ingrese el numero a verificar: ")) 
resultado = valor_primo(ingreso_usuario)
print(resultado)