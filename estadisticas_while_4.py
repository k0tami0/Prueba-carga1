acumulador = 0
contador = 0

while contador < 11:
    if contador % 2 == 0:
        acumulador += contador
    contador +=1

print(acumulador)