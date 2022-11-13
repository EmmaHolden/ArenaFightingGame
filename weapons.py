import random

class Weapons:
    def __init__(self, name, fatigue, mindam, maxdam):
        self.name = name
        self.fatigue = fatigue
        self.mindam = mindam
        self.maxdam = maxdam


sword = Weapons(name = "sword", fatigue = 20, mindam = 7, maxdam = 18)
spear = Weapons(name = "spear", fatigue = 30, mindam = 15, maxdam = 20)
pistol = Weapons(name = "pistol", fatigue = 10, mindam = 1, maxdam = 20)
bow = Weapons(name = "bow", fatigue = 30, mindam = 10, maxdam = 25)
mace = Weapons(name = "mace", fatigue = 20, mindam = 5, maxdam = 20)
sling = Weapons(name = "sling", fatigue = 15, mindam = 5, maxdam = 15)
whip= Weapons(name = "whip", fatigue = 10, mindam = 8, maxdam = 12)
dagger = Weapons(name = "dagger", fatigue = 15, mindam = 12, maxdam = 18)
club = Weapons(name = "club", fatigue = 20, mindam = 10, maxdam = 15)
staff = Weapons(name = "staff", fatigue = 25, mindam = 12, maxdam = 18)

weapons_list = []
weapons_list.extend([sword, spear, pistol, bow, mace, sling, whip, dagger, club, staff])