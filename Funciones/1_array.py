"""
Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
"""
def array_numeros(cantidad : int) -> int|None:
    array = [None] * cantidad

    for i in range (len(array)):
        array[i] = int(input(f"Que numero desea colocar en la posición {i}?: "))

    return array

cantidad_elementos= int(input("Elija la cantidad de elementos que desea que tenga la lista: "))

lista = array_numeros(cantidad_elementos)

print(lista)

