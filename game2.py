import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tavern Adventure")

# Cargar fondo de taberna
background = pygame.image.load(r"C:\Users\CISA\Desktop\PYR\TrainingField\NapOurS.jpg")
background = pygame.transform.scale(background, (width, height))

# Colores
white = (255, 255, 255)

# Personaje
player_width, player_height = 50, 50
player_x, player_y = width // 2 - player_width // 2, height // 2 - player_height // 2
player_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - player_height:
        player_y += player_speed

    screen.blit(background, (0, 0))  # Dibuja el fondo
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
