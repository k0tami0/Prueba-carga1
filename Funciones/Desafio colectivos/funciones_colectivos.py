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
import random

def menu_colectivos():
    eleccion_usuario = int(input("""Bienvenido al programa de recaudación de colectivos, a continuación, seleccione uno de los menús ingresado el numero correspondiente
    1- Cargar planilla de recaudación.
    2- Mostrar la recaudación por coche en cada línea.
    3- Mostrar la recaudación total por línea.
    4- Mostar la recaudación total de un coche.
    5- Mostar la recaudación total de todas las líneas.
    6- Salir del programa
    Su elección: """))
    return eleccion_usuario

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
             print(f"{matriz[i][j]}", end= " ")
        print(" ")

def legajos_aleatorios_en_matriz(matriz : list )-> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(1000,9999)
    return matriz

def validar_legajo(legajo : int, matriz_legajos : list) -> bool:
    validacion = False
    for i in range(len(matriz_legajos)):
        for j in range(len(matriz_legajos[i])):
            if matriz_legajos[i][j] == legajo:
                validacion = True
    
    return validacion
