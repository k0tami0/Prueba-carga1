"""
📌 Desafío: Gestión de Recaudaciones en una Empresa de Colectivos
Una empresa de transporte cuenta con 3 líneas de colectivos, cada una con 5 coches, lo que da un total de 15 unidades en circulación. La empresa emplea 15 choferes, 
cada uno identificado con un legajo único generado aleatoriamente.
Para llevar un control eficiente de la recaudación diaria, se necesita desarrollar un software que permita gestionar y analizar los ingresos obtenidos por cada línea y coche.
🔹 Funcionalidades del Programa
El sistema debe presentar un menú de opciones con las siguientes funciones:
1️⃣ Cargar planilla de recaudación
El chofer debe identificarse ingresando su número de legajo.
Se debe validar que el legajo ingresado exista dentro de la matriz de legajos generada previamente.
Si el chofer existe, podrá ingresar la recaudación indicando la línea y el coche en el que realizó el viaje.
Un chofer puede cargar múltiples recaudaciones por día, en distintas líneas y coches.
Cada coche dentro de cada línea puede acumular varias recaudaciones diarias.
2️⃣ Mostrar la recaudación de cada coche y línea
Presentar una matriz con la recaudación total de cada coche en cada línea.
3️⃣ Calcular y mostrar la recaudación por línea
Sumar y mostrar la recaudación total de cada línea de colectivos.
4️⃣ Calcular y mostrar la recaudación por coche
Permitir al usuario seleccionar un coche y mostrar la suma total de su recaudación.
5️⃣ Calcular y mostrar la recaudación total
Mostrar el total general de todas las recaudaciones registradas.
6️⃣ Salir del programa


🔹 Requisitos del Desarrollo
✔️ Modularización:
El programa debe estar organizado en múltiples funciones, incluyendo:
Ingreso de datos
Validación de líneas y coches
Generación y verificación de existencia de legajo
Cálculos de recaudaciones
✔️ Validaciones:
El legajo ingresado debe existir en la matriz de legajos.
La línea y el coche seleccionados deben ser válidos.
No debe permitirse el ingreso de valores negativos o inválidos en la recaudación.

"""
from funciones_colectivos import *
matriz_generada = False
if matriz_generada == False:
    matriz = crear_matriz(3,5,0)
    matriz_legajos = legajos_aleatorios_en_matriz(matriz)
    mostrar_matriz(matriz_legajos)
    matriz_generada= True
while True:
    menu = menu_colectivos()
    match menu: 
        case 1:
        
            legajo_chofer= int(input("Ingrese su número de legajo, debe tener 4 dígitos: "))
            validar_legajo_ingresado = validar_legajo(legajo_chofer, matriz_legajos)
            while validar_legajo_ingresado == False:
                print(f"\nSu legajo {legajo_chofer}, es incorrecto.")
                legajo_chofer= int(input("Ingrese su número de legajo, debe tener 4 dígitos: "))
                validar_legajo_ingresado = validar_legajo(legajo_chofer, matriz_legajos)
            else:
                print(f"\nSu legajo {legajo_chofer}, es correcto. Ingresando...\n ")
        case 2: 
            mostrar_matriz(matriz_legajos)