"""
Ingresar 10 números enteros. Determinar el máximo y el mínimo.
"""
contador = 0
maximo = 0
minimo = 0
bandera_primer_numero = True

while contador < 4:
    numero = int(input(f"Ingrese el número{contador + 1}: "))
    if bandera_primer_numero == True:
        maximo = numero
        minimo = numero
        bandera_primer_numero = False
    else:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    contador += 1

print(f"El valor mas alto ingresado fue {maximo} y el minimo fue {minimo}")
