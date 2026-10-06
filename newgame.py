import pygame
import random
import time
pygame.init()
WIDTH, HEIGHT = 2000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sun set falls")

BG = pygame.transform.scale(pygame.image.load("sun.jpeg"), (WIDTH, HEIGHT))
PLAYER_WIDTH, PLAYER_HEIGHT = 100, 100
player = pygame.Rect(100, HEIGHT - PLAYER_HEIGHT - 100, PLAYER_WIDTH, PLAYER_HEIGHT)
player_image = pygame.image.load("player1.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

Running = True
while Running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - 6 > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x + 5 + player.width < WIDTH:
        player.x += 5
    if keys[pygame.K_UP] and player.y - 5 > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.y + 5 + player.height < HEIGHT:
        player.y += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    WIN.blit(BG, (0, 0))
    WIN.blit(player_image, player)
    pygame.display.update()

pygame.quit()