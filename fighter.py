import random

class Fighter:
    def __init__(self, name, weaponslist):
        self.health = 50
        self.stamina = 50
        self.name = name
        self.choose_weapon(weaponslist)

    def choose_weapon(self, weaponslist):
        choice = random.sample(weaponslist, 3)
        weapon_chosen = False
        while not weapon_chosen:
            chosen_weapon = input(f"Would you like {self.name} to use the {choice[0].name}, the {choice[1].name}, or "
                                  f"the {choice[2].name}?: ").lower()
            for x in choice:
                if chosen_weapon == x.name:
                    self.weapon = x
                    weapon_chosen = True

