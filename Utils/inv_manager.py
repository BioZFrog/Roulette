import random

inv = 8 # Inventory Items Capacity

items = ["Beer", "Magnifying Glass", "Adrenaline", "Hand Cuffs", "Hand Saw", "Expired Medicine", "Cigarette", "Inverter"]

player_items = random.choices(items, k=inv)
dealer_items = random.choices(items, k=inv)