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

filas= int(input("Ingrese la cantidad de filas para la matriz: "))
columnas= int(input("Ingrese la cantidad de columnas para la matriz: "))

matriz = crear_matriz(filas,columnas, 0)
mostrar_matriz(matriz)