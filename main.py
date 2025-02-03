import pygame

# Import Other data
from Utils.Chambers_manager import player_shotgun, dealer_shotgun
from Utils.inv_manager import player_items, dealer_items


# Sprites
shotgun = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Shotgun.png")
shotgun_sawed = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Shotgun_sawed.png")

magnifying_glass = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Magnifying_Glass.png")
beer = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Blue_bull.png")
cigarette = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Cigarette.png")
hand_cuffs = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Hand_Cuffs.png")
hand_saw = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Hand_Saw.png")
inverter = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Inverter.png")
adrenaline = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Adrenaline.png")

# Screen
screen = pygame.display.set_mode((800, 600))

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

pygame.quit()