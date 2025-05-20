def llenar_primer_columna_de_Cada_fila(matriz):
    for i in range(len(matriz)):
        matriz[i][0] = input(f"Ingrese el numero de línea {i +1}: ")
    return matriz

def mostar_matriz(matriz : list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end= " ")
        print(" ") 


matriz_a =  [[0,0,0],
             [0,0,0],
             [0,0,0]]

matriz_a_completa = llenar_primer_columna_de_Cada_fila(matriz_a)
mostar_matriz(matriz_a_completa)

def cuadrado_magico(matriz: list) -> bool:
#M= n(n**2+1) / 2 
    es_magico = True
    n = len(matriz)
    constante_magica = n * (n**2 +1) // 2

#compara la suma de cada fila
    for i in range(len(matriz)):
        acumulador_filas = 0
        for j in range(len(matriz[i])):
            acumulador_filas += matriz[i][j]
        if acumulador_filas != constante_magica:
            es_magico = False

#compara la suma de cada columna
    for i in range(len(matriz)):
        acumulador_columnas = 0
        for j in range(len(matriz[i])):
            acumulador_columnas += matriz[j][i]
        if acumulador_columnas != constante_magica:
            es_magico = False

#compara la suma de la diagonal principal (para sumar la diagonal principal cada valor debe ser el mismo)
    acumulador_diagonal_principal = 0
    for i in range(len(matriz)):
        acumulador_diagonal_principal += matriz[i][i]
    if acumulador_diagonal_principal != constante_magica:
        es_magico = False

#compara la suma de la diagonal principal inversa
    acumulador_diagonal_inversa = 0
    for i in range(len(matriz)):
        acumulador_diagonal_inversa += matriz[i][len(matriz) - 1 - i]
    if acumulador_diagonal_inversa != constante_magica:
        es_magico = False
#retorna un booleano True | False
    return es_magico


matriz_a =  [[8,1,6],
             [3,5,7],
             [4,9,2]]

matriz_a_magica = cuadrado_magico(matriz_a)
print(matriz_a_magica)