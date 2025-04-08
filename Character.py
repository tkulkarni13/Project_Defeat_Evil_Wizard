import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.block = False
        self.anti_heal = False
    
    # Basic attack
    def attack(self, opponent):
        if (opponent.block):
            print(f"{opponent.name} felt no damage!")
            opponent.block = False
        else:
            attack_damage_range = 5 
            attack_damage = random.randint(self.attack_power - attack_damage_range, self.attack_power + attack_damage_range)
            opponent.health -= attack_damage
            print(f"{self.name} attacks {opponent.name} for {attack_damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        if (not self.anti_heal):
            heal_amount = random.randint(10,20)
            self.health += heal_amount
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")
        else:
            print(f"{self.name} attempted to heal but was prevented!")
            self.anti_heal = False

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")