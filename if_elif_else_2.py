"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...
"""
import random 

nota = random.randint(1,10)

if nota >= 6:
    mensaje = "Promoción directa"
elif nota >= 4:
    mensaje = "Aprobado"
else:
    mensaje ="Desaprobado"

print(f"{mensaje}, la nota es {nota}")

