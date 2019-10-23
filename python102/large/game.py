#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
    def status(self):
        print(f'The {self.name} have {self.health} health and {self.power} power.')
    def attack(self, other_char):
        other_char.health -= self.power
        print(f'The {self.name} do {self.power} damage to the {other_char.name}.')
        if other_char.health <= 0:
            print(f'The {other_char.name} is dead.')

class Hero(Character):
    pass

class Goblin(Character):
    pass

hero = Hero("Hero", 10, 5)
goblin = Goblin("Goblin", 6, 2)

def main():

    while goblin.alive() and hero.alive():
        hero.status()
        goblin.status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            goblin.attack(hero)

main()