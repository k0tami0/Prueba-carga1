def ordenar_array(array_ordenado : list, ascendente = False)-> list:
    for i in range(len(array_ordenado)):
        for j in range(i + 1, len(array_ordenado), 1):
            if ascendente == True:
                if array_ordenado[i] < array_ordenado[j]:
                    auxiliar = array_ordenado[i]
                    array_ordenado[i] = array_ordenado[j]
                    array_ordenado[j] = auxiliar
            else:
                if array_ordenado[i] > array_ordenado[j]:
                    auxiliar = array_ordenado[i]
                    array_ordenado[i] = array_ordenado[j]
                    array_ordenado[j] = auxiliar
    return array_ordenado

array = [9,2,5,95]
array_palabras = ["tal", "que", "buenas", "hola"]
ascendente = True
print(ordenar_array(array))
print(ordenar_array(array, ascendente))