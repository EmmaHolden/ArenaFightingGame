from weapons import Weapons, weapons_list
from fighter import Fighter
from battle import Battle
from utilities import clear
import random

fighters = []

num_fighters_chosen = False
while not num_fighters_chosen:
    raw_num_fighters = (input("How many combatants should there be?: "))
    if raw_num_fighters.isdigit():
        num_fighters = int(raw_num_fighters)
        num_fighters_chosen = True

for x in range(1, num_fighters + 1):
    name = input(f"What is the name of fighter {x}?: ")
    new_character = Fighter(name, weapons_list)
    fighters.append(new_character)

print("Okay, so your fighters are:")
for f in fighters:
    print(f.name)
bet = input("Who do you think will win?: ").lower()
clear()
battle_is_on = True
while battle_is_on:
    if len(fighters) == 1:
        winner = fighters[0].name
        print(f"\nThe game is over! {winner} is the winner!")
        battle_is_on = False
        if bet == winner.lower():
            print("Your guess was correct!")
        else:
            print("Your guess was wrong!")
    else:
        if input("\nPress enter for the next turn") == "":
            battle = Battle(fighters)



