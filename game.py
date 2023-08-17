import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge the Falling Objects")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Personaje
player_width, player_height = 50, 50
player_x, player_y = width // 2 - player_width // 2, height - player_height - 10
player_speed = 5
player_lives = 3

# Vidas
heart_image = pygame.image.load("C:\Users\CISA\Desktop\PYR\TrainingField\knhnfd.png.")  # Agrega tu propia imagen de corazón
heart_width, heart_height = 30, 30
heart_spacing = 40
hearts = [pygame.Rect(10 + i * heart_spacing, 10, heart_width, heart_height) for i in range(player_lives)]

# Objetos que caen
object_width, object_height = 30, 30
object_speed = 3
objects = []

clock = pygame.time.Clock()

def create_object():
    x = random.randint(0, width - object_width)
    y = -object_height
    objects.append((x, y))

def check_collision():
    global player_lives
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for i, (x, y) in enumerate(objects):
        object_rect = pygame.Rect(x, y, object_width, object_height)
        if player_rect.colliderect(object_rect):
            player_lives -= 1
            del objects[i]
            create_object()

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

    if len(objects) < 5:
        create_object()

    check_collision()

    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

    for i, (x, y) in enumerate(objects):
        pygame.draw.rect(screen, red, (x, y, object_width, object_height))
        objects[i] = (x, y + object_speed)

    for heart_rect in hearts:
        screen.blit(heart_image, heart_rect)

    pygame.display.flip()
    clock.tick(60)

    if player_lives <= 0:
        running = False

pygame.quit()
sys.exit()