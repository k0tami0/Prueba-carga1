"""
📌 Desafío: Verificación de un Cuadrado Mágico
Un cuadrado mágico es una matriz cuadrada de n × n en la que la suma de los números en cada fila, cada columna y cada diagonal principal es la misma. 
Esta suma se conoce como constante mágica (M), y se calcula con la siguiente fórmula:

M= n(n**2+1) / 2 

Formalmente, un cuadrado mágico de orden n contiene los números enteros del 1 al n², organizados de manera que cumplen la condición de igualdad en las sumas.
🔹 Objetivo
Desarrollar un programa en Python que permita ingresar una matriz cuadrada de orden n y determine si es un cuadrado mágico.
🔹 Requisitos del Programa
✔️ Ingreso de datos:
Permitir que el usuario ingrese la matriz manualmente o, de manera opcional, generar una aleatoria.
Validar que los valores ingresados sean números enteros en el rango de 1 a n² y que no se repitan.
Asegurar que la matriz ingresada tenga un tamaño válido (n × n).

✔️ Verificación del cuadrado mágico:
Calcular la constante mágica según la fórmula.
Comparar la suma de:
Cada fila
Cada columna
Las dos diagonales principales
Determinar si todas las sumas son iguales a la constante mágica.
✔️ Salida de resultados:
Mostrar la matriz ingresada de forma clara y organizada.
Indicar si la matriz es un cuadrado mágico o no.

📌 Extras opcionales:
 ✅ Permitir que el usuario ingrese matrices de distintos tamaños (por ejemplo, 3×3, 4×4, etc.).
 ✅ Mostrar mensajes de error en caso de ingreso inválido.
 ✅ Implementar una opción para generar un cuadrado mágico válido automáticamente.
"""
import random

def cuadrado_magico():
    pass

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def crear_matriz_cuadrada(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list | None:
    if cantidad_filas == cantidad_columnas:
        matriz = []
        for i in range(cantidad_filas):
            fila = [valor_inicial] * cantidad_columnas
            matriz += [fila]
    else: 
        matriz = print(f"La matriz ingresada de {cantidad_filas} x {cantidad_columnas} no se puede crear ya que no es cuadrada")
    return matriz

def cargar_matriz(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
             matriz[i][j] = int(input(f"Ingrese un valor para la posición {i} {j}: "))

def cargar_matriz_enteros(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Ingrese un valor para la posición {i}{j}: "))
    return matriz

def repetidos_en_matriz(matriz : list, lista: list):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == (len(lista[i])):
                pass

def mostrar_matriz(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
             print(f"{matriz[i][j]}", end= " ")
        print(" ") 

# M= n(n**2+1) / 2 

def cuadrado_magico_dos(matriz: list):
    largo_matriz = len(matriz)
    formula_magica = largo_matriz * (largo_matriz ** 2 + 1) / 2
    cuadrado_magico = True

    for i in range(len(matriz)):
        suma_fila = 0
        for j in range(len(matriz)):
            suma_fila += matriz[i][j]
        if suma_fila != formula_magica:
            cuadrado_magico = False
            
    for i in range(len(matriz)):
        suma_columna = 0
        for j in range(len(matriz)):
            suma_columna += matriz[j][i]
        if suma_columna != formula_magica:
            cuadrado_magico = False

    suma_diagonal = 0
    for i in range(len(matriz)):
        suma_diagonal += matriz[i][i]
    if suma_diagonal != formula_magica:
        cuadrado_magico = False

# #fila + 1 : columna - 1
    suma_diagonal_invertida = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)-1, 0, -1):
            suma_diagonal_invertida += matriz[i][j-i]
            break
    if suma_diagonal_invertida != formula_magica:
        cuadrado_magico = False

    return cuadrado_magico

matriz_magica = [[2,7,6],
                 [9,5,1],
                 [4,3,8]]

es_magico = cuadrado_magico_dos(matriz_magica)
mostrar_matriz(matriz_magica)
print(es_magico)

