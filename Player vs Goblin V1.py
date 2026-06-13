import random
import os
os.system('cls')

# Classes
class Player:
    def __init__(self, hp=10, max_hp=10, lvl=1, xp=0, is_alive=True, name="", dmg_min=1, dmg_max=3):
        self.hp = hp
        self.lvl = lvl
        self.xp = xp
        self.max_hp = max_hp
        self.is_alive = is_alive
        self.name = name
        self.name = input("What is your name?: ")
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
    def get_dmg(self):
        dmg = random.randint(self.dmg_min, self.dmg_max)
        return dmg
    
class Goblin:
    def __init__(self, hp=5, max_hp=5, heal_amt=1, is_alive=True):
        self.hp = hp
        self.max_hp = max_hp
        self.heal_amt = heal_amt
        self.is_alive = is_alive
    def get_dmg(self):
        dmg = random.randint(1, 2)
        return dmg

class Minor_hp_potion:
    def __init__(self, heal_amt=3):
        self.heal_amt = heal_amt

# Objects
player1 = Player(10, 10, 1, 0)

goblin1 = Goblin(5, 5)

# Functions
def take_dmg(entity, name, hp, dmg):
    hp -= dmg
    if hp <= 0:
        print(f"{name} has died!")
        hp = 0
        entity.is_alive = False
    else:
        print(f"{name} took {dmg} damage.")
    return hp

def heal(entity, name, hp, max_hp, heal_amt):
    if hp + heal_amt > max_hp:
        heal_amt = max_hp - hp
    hp += heal_amt
    print(f"{name} healed {heal_amt} HP.")
    return hp

def game():
    escape = 0
    while player1.is_alive and goblin1.is_alive:

        # Player Turn
        player_option = input("\nWhat would you like to do?: \nAttack   Heal   Run Away\n")
        if player_option.lower() in ["attack", "a"]:
            goblin1.hp = take_dmg(goblin1, "Goblin", goblin1.hp, player1.get_dmg())
        elif player_option.lower() in ["heal", "h"]:
             player1.hp = heal(player1, player1.name, player1.hp, player1.max_hp, Minor_hp_potion().heal_amt)
        elif player_option.lower() in ["run away", "ra", "rw", "runaway"]:
            escape = random.randint(1, 2)
            if escape == 1:
                print(f"{player1.name} escaped!")
                break
            else:
                print(f"{player1.name} tripped and fell")
        else:
            print("That is not a valid input")
            continue
        
        # Goblin Turn
        if player1.is_alive and goblin1.is_alive:
            goblin_option = random.randint(1,3)
            if goblin_option == 1:
                player1.hp = take_dmg(player1, player1.name, player1.hp, goblin1.get_dmg())
            elif goblin_option == 2:
                goblin1.hp = heal(goblin1, "Goblin", goblin1.hp, goblin1.max_hp, goblin1.heal_amt)
            else:
                escape = random.randint(1, 2)
                if escape == 1:
                    print("goblin1 ran away!")
                    break
                else:
                    print("goblin1 tripped on itself")

    
    # End Message
    goblin1.__init__()
    if escape == 1:
        print("Game over: Someone chickened out.")
    elif player1.hp > 0:
        player1.xp += 1
        print("You won, and gained 1 XP, Congrats!")
    else:
        print("You lost, better luck next time.")


# Start Loop
play_game = True
while play_game:
    # Level Check
    if player1.xp >= 2:
        player1.xp -= 2 
        player1.lvl += 1
        player1.dmg_max += 1 
        player1.dmg_min += 1
        print(f"You are now level {player1.lvl}!")

    # Start
    play_game = input("Do you want to play Player vs. Goblin V1?: ")

    if play_game.lower() in ["y", "yes"]:
        play_game = True
        game()
    else: 
        print("That's too bad...")
        play_game = False