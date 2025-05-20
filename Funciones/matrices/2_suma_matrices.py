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

def multiplicar_matrices(matriz_a : list,matriz_b : list, matriz_c) -> list: 
    for i in range(len(matriz_c)):
        for j in range(len(matriz_c[0])):
            for k in range(len(matriz_b)):
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_c

matriz_a = [[2,4,6],
            [2,4,6],
            [2,4,6]]

matriz_b = [[4,6,8],
            [4,8,8],
            [4,6,8]]

matriz_c = crear_matriz(len(matriz_a) , len(matriz_b[0]), 0)

resultado_c = multiplicar_matrices(matriz_a, matriz_b, matriz_c)
mostrar_matriz(matriz_c)
