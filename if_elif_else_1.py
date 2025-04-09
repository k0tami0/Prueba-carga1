"""
IF - ELSE -ELIF

A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, 
considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
"""
#Entradas
altura_jugador= int(input("Ingrese la altura del jugador (en cm): "))

#Procesos
if altura_jugador >= 200:
    tipo_jugador= "Ala-Pívot"
elif altura_jugador >= 180:
    tipo_jugador= "Alero"
elif altura_jugador >= 160:
    tipo_jugador= "Escolta"
else:
    tipo_jugador="Base"

#Salidas
print(f"{tipo_jugador}")
