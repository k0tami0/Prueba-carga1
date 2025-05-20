"""
Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
Una lista de nombres (lista_nombres).
Un nombre a buscar en la lista (nombre_antiguo).
Un nombre de reemplazo (nombre_nuevo).
La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.

"""
def promedio_enteros(lista : list) -> int:
    acumulador = 0
    for i in range (len(lista)):
        acumulador += lista[i]
    promedio = acumulador // len(lista)
    return promedio

def promedio_enteros_positivos(lista : list) -> int:
    acumulador = 0
    for i in range (len(lista)):
        if lista[i] > 0:
            acumulador += lista[i]
    promedio = acumulador // len(lista)
    return promedio

def producto_enteros(lista : list) -> int:
    acumulador = 0
    for i in range (len(lista)):
        if i == 0:
            acumulador = lista[i]
        else:   
            acumulador *= lista[i]
    return acumulador

def mayor_en_lista ( lista: list) -> int:
    mayor = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def encontrar_mayor(lista: list) ->int :
    mayor = 0
    for i in range(len(lista)):
        if i == 0: 
            mayor = lista[i]
        elif lista[i] > mayor:
            mayor = lista[i]
            posicion = i
    print(f"El valor mas alto es {mayor} y se encuentra en la posicion {posicion}")
    return mayor

def mostrar_lista(lista: list) :
    for i in range(len(lista)):
        print(lista[i], end= " ")
    print("")

def reemplazar_nombres (lista : list, nombre_a_buscar : str, nuevo_nombre : str ) -> list:
    contador = 0
    for i in range(len(lista)):
        if lista[i] == nombre_a_buscar:
            lista[i] = nuevo_nombre
            contador += 1
    print(f"La cantidad de cambios fue {contador}")
    return lista

lista_nombres = ["pancho","mastrangelo","pablo","mesi","nombre_antiguo" ]
lista_a = [2,4,20,30,10,5] 
reemplazo_a = reemplazar_nombres(lista_nombres, "mesi", "Hola")
promedio_a = promedio_enteros (lista_a)
mayor_a = mayor_en_lista(lista_a)

producto_a = producto_enteros(lista_a)
posicion_mayor_a = encontrar_mayor(lista_a)

mostrar_lista(reemplazo_a)
print (posicion_mayor_a)
print(promedio_a)
print (mayor_a)
print(producto_a)
mostrar_lista(lista_a)
print (posicion_mayor_a)