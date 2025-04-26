
jugador_nombre = "Juan"
jugador_vida = 100
jugador_daño = 50
enemigo_nombre = "Goblin"
enemigo_vida = 80
enemigo_daño = 10
defenderse = False

while True:
    accion_juan = int(input("Que hace juan?: 1- Atacar, 2- Defenderse: "))
    if accion_juan == 1:
        enemigo_vida -= jugador_daño
        print(f"Juan lanza un potente ataque a {enemigo_nombre} y le quita {jugador_daño} puntos de vida: ")
        if enemigo_vida > 0:
            print(f"La vida actual de {enemigo_nombre} es {enemigo_vida}")
        else:
            print(f"¡{enemigo_nombre} Derrotado!")
    elif accion_juan == 2:
        defenderse = True

    if enemigo_vida <= 0:
        break    

    accion_enemigo = int(input("Que hace el enemigo?: 1- Atacar: "))
    if accion_enemigo == 1:
        if defenderse == True:
            print(f"El {enemigo_nombre} atacó pero {jugador_nombre} se defendió con su escudo!")
            defenderse = False
        else:
            print(f"El {enemigo_nombre} lanza un potente ataque a {jugador_nombre} y le quita {enemigo_daño} puntos de vida")
            jugador_vida -= enemigo_daño
            print(f"La vida actual de{jugador_nombre} es {jugador_vida}")

print(f"{jugador_nombre} venció a {enemigo_nombre}")
    