import random

chambers = 6 # Shells Capacity in shotgun


def generater_shoutgun_chambers(chambers):
    rounds = ["Live Round", "Blank"]
    return random.choices(rounds, k=chambers)

player_shotgun = generater_shoutgun_chambers(chambers)
dealer_shotgun = generater_shoutgun_chambers(chambers)