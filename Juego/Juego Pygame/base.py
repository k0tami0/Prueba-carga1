import pygame
import random

# Inicialización
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los objetos")

# Colores
COLOR_JUGADOR = (255, 0, 0)
COLOR_OBJETO = (0, 255, 0)

# Jugador (rectángulo rojo)
jugador_x, jugador_y = 100, 500
jugador_ancho, jugador_alto = 50, 50
velocidad = 5

# Objeto que cae (rectángulo verde)
objeto_x = random.randint(0, ANCHO - 50)  # Posición aleatoria en X
objeto_y = 0  # Empieza en la parte superior
objeto_ancho, objeto_alto = 50, 50
velocidad_objeto = 5

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Puntaje
puntaje = 0

# Bucle del juego
jugando = True
while jugando:
    clock.tick(60)  # 60 FPS

    # 1. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # 2. Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_ancho:
        jugador_x += velocidad
    if teclas[pygame.K_UP] and jugador_y > 0:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN] and jugador_y < ALTO - jugador_alto:
        jugador_y += velocidad

    # 3. Movimiento del objeto que cae
    objeto_y += velocidad_objeto

    # Si el objeto llega al fondo de la pantalla, lo reiniciamos
    if objeto_y > ALTO:
        objeto_y = 0
        objeto_x = random.randint(0, ANCHO - objeto_ancho)  # Nueva posición aleatoria
        puntaje += 1  # Incrementamos el puntaje

    # 4. Detección de colisión (si el jugador toca el objeto)
    if jugador_x < objeto_x + objeto_ancho and jugador_x + jugador_ancho > objeto_x:
        if jugador_y < objeto_y + objeto_alto and jugador_y + jugador_alto > objeto_y:
            print("¡COLISIÓN! El juego terminó.")
            jugando = False  # Terminamos el juego

    # 5. Dibujar fondo y objetos
    pantalla.fill((0, 0, 0))  # Fondo negro
    pygame.draw.rect(pantalla, COLOR_JUGADOR, (jugador_x, jugador_y, jugador_ancho, jugador_alto))
    pygame.draw.rect(pantalla, COLOR_OBJETO, (objeto_x, objeto_y, objeto_ancho, objeto_alto))

    # 6. Mostrar puntaje
    font = pygame.font.Font(None, 36)
    texto_puntaje = font.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto_puntaje, (10, 10))

    # 7. Actualizar pantalla
    pygame.display.update()

# Salir de pygame
pygame.quit()