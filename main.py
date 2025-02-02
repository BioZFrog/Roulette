import pygame

# Sprites
shotgun = pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Shotgun.png")


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