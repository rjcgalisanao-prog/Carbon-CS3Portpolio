import random
import time

class hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def defend(self):
        print(f"{self.name} is defending and will take reduced damage next turn!")

    def display_hp(self):
        print(f"{self.name} has {self.health} HP remaining.")

hero1 = hero("Warrior", 100, 20)
hero2 = hero("Mage", 80, 25)

input("Press Enter to start the battle...")
choice = input("Choose your hero: 1 for Warrior, 2 for Mage: ")

if choice == "1":
    current_hero = hero1
elif choice == "2":
    current_hero = hero2
else:
    print("Invalid choice. Defaulting to Warrior.")
    current_hero = hero1

action = input(f"Action: ")
if action.lower() == "attack":
    current_hero.attack(hero2 if current_hero == hero1 else hero1)
elif action.lower() == "defend":
    current_hero.defend()

hero1.display_hp()
hero2.display_hp()