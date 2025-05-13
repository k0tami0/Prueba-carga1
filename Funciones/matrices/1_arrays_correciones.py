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



matriz_a = [[9,8],
            [6,5],
            [3,2]]

matriz_b = [[1,2,3,4],
            [1,2,3,4]]

# Crear matriz resultado con ceros
matriz_c = crear_matriz(len(matriz_a), len(matriz_b[0]), 0)

# Multiplicación de matrices
for i in range(len(matriz_c)):
        for j in range(len(matriz_c[0])):
            for k in range(len(matriz_b)):
                 matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]


# Mostrar resultado
for fila in matriz_c:
    print(fila)