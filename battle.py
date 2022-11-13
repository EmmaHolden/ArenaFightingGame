import random
from utilities import clear


class Battle:
    def __init__(self, fighters):
        clear()
        for x in fighters:
            if x.stamina > x.weapon.fatigue:
                self.attack(x, fighters)
            else:
                print(f"\n{x.name} is too fatigued to fight. Skipping their turn...\n")
            x.stamina += (random.randint(0, 10))

    def attack(self, x, fighters):
        targets = [l for l in fighters if l != x]
        x.target = random.choice(targets)
        x.damage = random.randint(x.weapon.mindam, x.weapon.maxdam)
        print(f"\n{x.name} does {x.damage} damage to {x.target.name} with their {x.weapon.name}\n")
        x.target.health -= x.damage
        if x.target.health <= 0:
            print(f"\n{x.target.name} has died!\n")
            fighters.remove(x.target)
        if x.weapon.fatigue < x.stamina:
            x.stamina -= x.weapon.fatigue
        else:
            x.stamina = 0