vector = [1,50,2,23,1]

acumulador = 0
contador_pares = 0
for i in range(len(vector)):
    if vector[i] % 2 == 0:
        acumulador += vector[i]
        contador_pares += 1

promedio = acumulador / contador_pares
print(promedio)