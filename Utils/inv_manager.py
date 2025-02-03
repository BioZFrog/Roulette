import random
import pygame

inv = 8 # Items capacity in inventory

sprite_images= {"Beer":pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Blue_bull.png"), "Magnifying Glass": pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Magnifying_Glass.png"), "Cigarette": pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Cigarette.png"), "Hand Cuffs" :pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Hand_Cuffs.png"), "Hand Saw": pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Hand_Saw.png"), "Inverter" : pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Inverter.png"), "Adrenaline":pygame.image.load(r"D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Adrenaline.png"), "Expired Medicine" : "D:\ALL VSC WORK\Roulette\Assets\Sprites\Items\Expired_Medicine.png" }

items = list(sprite_images.keys())

player_items = random.choices(items, k=9)

inventory_positions = [(220 + (i % 4) * 100, 400 + (i // 4) * 100) for i in range(8)]

