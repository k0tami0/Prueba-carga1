def mostrar_matriz(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
             print(f"{matriz[i][j]}", end= " ")
        print(" ")

def cuadrado_magico_dos(matriz: list):
    largo_matriz = len(matriz)
    formula_magica = largo_matriz * (largo_matriz ** 2 + 1) / 2
    cuadrado_magico = True
    suma_diagonal_invertida = 0

    for i in range(len(matriz)):
            suma_diagonal_invertida += matriz[i][largo_matriz - 1 - i]
    if suma_diagonal_invertida != formula_magica:
        cuadrado_magico = False
    return cuadrado_magico


matriz_magica = [[2,7,6],
                 [9,5,1],
                 [4,3,8]]

es_magico = cuadrado_magico_dos(matriz_magica)
mostrar_matriz(matriz_magica)
print(es_magico)
