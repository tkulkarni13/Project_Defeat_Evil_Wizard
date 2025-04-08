import random
from Character import Character

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=25)
    
    def special_ability(self, opponent):
        print("\n--- Special Abilities ---")
        print("1. Deadly Slash - Deals 10 damage to opponent and prevents healing")
        print("2. Battle Rage - Increase attack power by 5")

        choice = input("Choose your special ability: ")
        if choice == '1':
            self.deadly_slash(opponent)
        elif choice == '2':
            self.battle_rage()
        else:
            print("Invalid choice. No special ability used.")
    
    def deadly_slash(self, opponent):
        attack_damage = 10
        opponent.health -= attack_damage
        opponent.anti_heal = True
        print(f"{self.name} uses special ability Deadly Slash! Deals {attack_damage} damage!")

    def battle_rage(self):
        self.attack_power += 5
        print(f"{self.name} uses special ability Battle Rage! Gain 5 attack power.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def special_ability(self, opponent):
        print("\n--- Special Abilities ---")
        print("1. Fireball - Deals 20 - 45 damage to opponent")
        print("2. Ice Blast - Deals 25 damage to opponent")

        choice = input("Choose your special ability: ")
        if choice == '1':
            self.fireball(opponent)
        elif choice == '2':
            self.ice_blast(opponent)
        else:
            print("Invalid choice. No special ability used.")

    def fireball(self, opponent):
        attack_damage = random.randint(self.attack_power - 15, self.attack_power + 10)
        opponent.health -= attack_damage
        print(f"{self.name} uses special ability Fireball! Deals {attack_damage} damage!")
    
    def ice_blast(self, opponent):
        attack_damage = 25
        opponent.health -= attack_damage
        print(f"{self.name} uses special ability Ice Blast! Deals {attack_damage} damage!")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=20)
    
    def special_ability(self, opponent):
        print("\n--- Special Abilities ---")
        print("1. Double Shot - Shoot two arrows at once")
        print("2. Evade - Dodge the next attack")

        choice = input("Choose your special ability: ")
        if choice == '1':
            self.double_shot(opponent)
        elif choice == '2':
            self.evade()
        else:
            print("Invalid choice. No special ability used.")
    
    def double_shot(self, opponent):
        new_attack_power = self.attack_power * 2
        attack_damage = random.randint(new_attack_power - 5, new_attack_power + 5)
        opponent.health -= attack_damage
        print(f"{self.name} uses special ability Double Shot! Deals {attack_damage} damage!")
    
    def evade(self):
        self.block=True
        print(f"{self.name} uses special ability Evade! Dodge next attack!")

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=30)
    
    def special_ability(self, opponent):
        print("\n--- Special Abilities ---")
        print("1. Holy Strike - Deals 20 - 40 damage to opponent")
        print("2. Divine Shield - Block the next attack")

        choice = input("Choose your special ability: ")
        if choice == '1':
            self.holy_strike(opponent)
        elif choice == '2':
            self.divine_shield()
        else:
            print("Invalid choice. No special ability used.")

    def divine_shield(self):
        self.block=True
        print(f"{self.name} uses special ability Divine Shield! Block next attack!")
    
    def holy_strike(self, opponent):
        attack_damage = random.randint(self.attack_power - 10, self.attack_power + 10)
        opponent.health -= attack_damage
        print(f"{self.name} uses special ability Holy Strike! Deals {attack_damage} damage!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        if (self.anti_heal):
            print(f"{self.name} attempted to heal but was prevented!")
            self.anti_heal = False
        else:
            self.health += 5
            print(f"{self.name} regenerates 5 health! Current health: {self.health}")