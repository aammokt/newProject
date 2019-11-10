#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def char_health(self):
        print(self.health)
    def char_power(self):
        print(self.power)

hero = Character(10, 5)
goblin = Character(6, 2)
zombie = Character(10, 2)

def main():
    hero_health = hero.health
    hero_power = hero.power
    goblin_health = goblin.health
    goblin_power = goblin.power
    zombie_health = zombie.health
    zombie_power = zombie.power

    while goblin_health > 0 and hero_health > 0 and zombie_health > 0:
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print("The zombie has {} health and {} power".format(zombie_health, zombie_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight zombie")
        print("3. do nothing")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(hero_power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            print("You do {} damage to the zombie.".format(hero_power))
        elif raw_input == "3":
            pass
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0 and raw_input == "1":
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

        if zombie_health > 0 and raw_input == "2":
            # Zombie attacks hero
            hero_health -= zombie_power
            print("The zombie does {} damage to you.".format(zombie_power))
            if hero_health <= 0:
                print("You are dead.")

main()