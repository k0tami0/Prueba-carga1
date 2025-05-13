"""
Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
"""
def mayor_de_tres(numero_1:int, numero_2:int, numero_3:int) -> int:
    mayor= numero_1
    if numero_2 > numero_1 and numero_2 > numero_3:
        mayor = numero_2
    else: 
        mayor = numero_3
    return mayor

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
tercer_numero = int(input("Ingrese el tercer numero: "))
mayor = mayor_de_tres(primer_numero,segundo_numero,tercer_numero)
print(mayor)