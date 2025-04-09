"""
Match

Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.
"""
estacion_elegida= int(input("""Ingrese la estación del año en la que desea viajar 
1_Invierno 
2_Verano 
3_Otoño 
4_Primavera
Su elección: """))
destino_elegido = input("""Ingrese a que destino desea viajar: 
1_Bariloche, 
2_Mar del plata, 
3_Cataratas, 
4_Otros lugares
Su elección: """)


match estacion_elegida:
    case  1:
        if destino_elegido == 1:
            print("Se viaja")
        else:
            print("No se viaja")
    case 2:
        if destino_elegido == 2 or destino_elegido == 3:
            print("Se viaja.")
        else:
            print("No se viaja")
    case 3:
        print("Se viaja.")
    case 4:
        if destino_elegido != 1:
            print("Se viaja")
        else:
            print("No se viaja")