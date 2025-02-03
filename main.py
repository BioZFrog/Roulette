import pygame
import random

# Import Other data
from Utils.Chambers_manager import player_shotgun, dealer_shotgun
from Utils.inv_manager import player_items, inventory_positions, items, sprite_images



# Sprites
shotgun = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Shotgun.png")
shotgun_sawed = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Shotgun_sawed.png")



# Screen
screen = pygame.display.set_mode((800, 600))

pygame.init()

running = True
while running:
    screen.fill((255, 255, 255))  #

    # Render inventory items
    for item, pos in zip(player_items, inventory_positions):
        if item in player_items:
            screen.blit( sprite_images[item], pos)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Update display

pygame.quit()