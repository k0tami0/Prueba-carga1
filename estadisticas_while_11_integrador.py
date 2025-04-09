"""
Integrador While
Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
"""
acumulador_positivos = 0
acumulador_negativos = 0
contador_negativos = 0 
contador_positivos = 0
positivo_mayor = 0
bandera_primer_numero = True

while True:
    numero = input("Ingrese un numero o presione * para finalizar: ")
    if numero == "*":
        break
    else: 
        numero = int(numero)
        if numero > 0:
            acumulador_positivos += numero
            contador_positivos += 1
            if bandera_primer_numero == True:
                positivo_mayor = numero
                bandera_primer_numero = False
            elif numero > positivo_mayor:
                positivo_mayor = numero
        else:
            acumulador_negativos += numero
            contador_negativos += 1

promedio_positivos = acumulador_positivos / contador_positivos 
total_ingresados= contador_positivos + contador_negativos
porcentaje_negativos = contador_negativos / total_ingresados * 100
#salidas
print(f"""La suma acumulada de los numeros positivos es de {acumulador_positivos}, y la de los negativos es {acumulador_negativos}
se ingresaron {contador_negativos} numeros negativos
el promedio de los numeros positivos es de {promedio_positivos}
el numero positivo mas grande es {positivo_mayor}
el porcentaje de numeros negativos respecto al total de ingresos es de {porcentaje_negativos}%""")