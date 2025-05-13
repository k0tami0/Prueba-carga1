
# numero = input("Ingrese un numero: ")
# numero = int(numero)
# es_primo = True

# if numero < 2:
#     es_primo = False
# else:
#     for a in range (2, numero):
#         if numero % a == 0:
#             es_primo = False
    
# print(es_primo)

numero = input("Ingrese un numero: ")
numero = int(numero)
cantidad_primos = 0

for i in range (2, numero+1):
    es_primo = True
    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i)
        cantidad_primos += 1


