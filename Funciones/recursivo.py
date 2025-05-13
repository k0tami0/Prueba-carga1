numero = int(input("Ingrese un número: "))
#Utilizo un acumulador inicianizandolo en el valor que toma la variable numero.
acumulador = numero

#Itero desde el numero dado {numero - 1} menos uno porque el valor ingresado por el usuario ya lo tengo en el acumulador
for i in range(numero - 1, 0, -1 ):
#El acumulador va cambiando su valor a medida que se lo multiplica por {i}, calculando efectivamente el factorial del numero ingresado por el usuario
    acumulador = acumulador * i

print(acumulador)
