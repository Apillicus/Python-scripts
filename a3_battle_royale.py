
import random

# we use a fixed seed for testing purposes
# remember that the EXACT NUMBER OF RANDOM CALLS MUST ALSO MATCH THE SPECIFICATIONS
#   for random to behave consistently with the example
random.seed(31337)

def main():
    # create four Fighter instances pre-equipped with Weapons and Armor,
    #   add them to a list
    the_fighters = list()
    the_fighters.append(initialize_mario())
    the_fighters.append(initialize_megaman())
    the_fighters.append(initialize_link())
    the_fighters.append(initialize_samus())
    
    round = 1
    
    while len(the_fighters) > 1:
    
        print(f"*****ROUND {round}*****")
    
        # select a random attacker and defender from the remaining Fighters
        att_i = random.randrange(0,len(the_fighters))
        def_i = random.randrange(0,len(the_fighters)-1)
        if def_i >= att_i:
            def_i += 1
            
        # have the attack performed, and check to see if the defender is eliminated
        elim = the_fighters[att_i].attack(the_fighters[def_i])
        
        # if the defender is eliminated, print a message saying so, have the attacker
        #   "loot" all the items from the defeated defender, and remove the defender
        #   from the list of Fighters
        if elim:
            print(f"{the_fighters[att_i].get_name()} eliminated {the_fighters[def_i].get_name()}!")
            the_fighters[att_i].loot(the_fighters[def_i])
            the_fighters.pop(def_i)
        
        # print a status update at the end of each round
        print("*****STATUS*****")
        for fighter in the_fighters:
            print(fighter.status())
        print()
        
        round += 1
    
    print(f"{the_fighters[0].get_name()} is the winner!")

class Fighter:
    
    def __init__(self,name,health,min_dam,max_dam):
        self.name = name
        self.health = health
        self.initial_health = health
        self.min_dam = min_dam
        self.max_dam = max_dam

        self.weapon = []
        self.armor = []
        
        
    
    def status(self):
        output = f"{self.name}: {self.health}/{self.initial_health} HP"
        output += f", {self.min_dam}-{self.max_dam} dam"
        output += f", Weapons: [{', '.join([w.status() for w in self.weapon])}]"
        output += f", Armor: [{', '.join([a.status() for a in self.armor])}]"
        return output
    
    def add_weapon(self,weapon):
        #TODO: Implement method
        self.weapon.append(weapon)
        
    
    def add_armor(self,armor):
        #TODO: Implement method
        self.armor.append(armor)
        
    
    def get_name(self):
        return self.name
    
    def attack(self,other):
        # TODO: Implement method
        attack_bonus = 0
        damage = 0
        # Call this and use random.randint to call the min and max damage
        if len(self.weapon) == 0:
            attack_bonus = 0
        else:
            attack_bonus = self.weapon[0].get_damage_buff()
        damage = random.randint(self.min_dam,self.max_dam) + attack_bonus

        if len(self.weapon) > 0:
            print(f'{self.name} attacks {other.name} with {self.weapon[0].name} for {damage} damage')
        else:
            print(f'{self.name} attacks {other.name} for {damage} damage')
        
        print(attack_bonus)
        if len (self.weapon) > 0:
            if self.weapon[0].check_break():
                print(f'{self.weapon[0].name} breaks!')
                self.weapon.pop(0)
                if len (self.weapon) > 0:
                    print(f'{self.name} equips {self.weapon[0].name}')
                else:
                    print(f'{self.name} is out of weapons!')
        
        return other.take_damage(damage)
            
        # Return boolean from damage (Elimination?)
        pass
    
    def take_damage(self,amount):
        # TODO: Implement method
        damage_reduction = 0
        damage = 0
        if len(self.armor) > 0:
            damage_reduction = self.armor[0].get_damage_reduction()
        damage = max(0,amount - damage_reduction)
        self.health -= damage

        
        if len(self.armor) > 0:
            print(f'{self.name} blocks with {self.armor[0].name} and takes {damage} damage. {self.name} now has {self.health} health.')
        else:
            print(f'{self.name} takes {damage} damage. {self.name} now has {self.health} health.')
        
        print(damage_reduction)
        if len (self.armor) > 0:
            if self.armor[0].check_break():
                print(f'{self.armor[0].name} breaks!')
                self.armor.pop(0)
                if len (self.armor) > 0:
                    print(f'{self.name} equips {self.armor[0].name}')
                else:
                    print(f'{self.name} is out of armor!')
            
        return self.health <= 0
        
    
    def loot(self,other):
        # TODO: Implement method
        while len(other.weapon) > 0:
            get_weapon = other.weapon.pop(0)
            self.weapon.append(get_weapon)
            print(f'{self.name} takes {get_weapon.name} from {other.name}' )
        while len(other.armor) > 0:
            get_armor = other.armor.pop(0)
            self.armor.append(get_armor)
            print(f'{self.name} takes {get_armor.name} from {other.name}' )
        pass

class Weapon:
    
    def __init__(self,name,damage_buff,durability):
        # TODO: Implement constructor
        self.name = name
        self.damage_buff = damage_buff
        self.durability = durability
        self.initial_durability = durability
        pass
    
    def status(self):
        return f"{self.name} (+{self.damage_buff} dam, {self.durability}/{self.initial_durability} dur)"
    
    def get_name(self):
        # TODO: Implement method
        self.name = name()
        pass
    
    def get_damage_buff(self):
        # TODO: Implement method
        return self.damage_buff
        pass
    
    def check_break(self):
        # TODO: Implement method
        
        self.durability -= 1
        
        return self.durability <= 0

        pass

class Armor:
    
    def __init__(self,name,damage_reduction,durability):
        # TODO: Implement constructor
        self.name = name
        self.damage_reduction = damage_reduction
        self.durability = durability
        self.initial_durability = durability
        pass
    
    def status(self):
        return f"{self.name} (-{self.damage_reduction} dam, {self.durability}/{self.initial_durability} dur)"
    
    def get_name(self):
        # TODO: Implement method
        self.get_name = name()
        pass
    
    def get_damage_reduction(self):
        #TODO: Implement method
        return self.damage_reduction
        pass
    
    def check_break(self):
        # TODO: Implement method
        self.durability -= 1
        return self.durability <= 0

        pass

def initialize_mario():
    mario = Fighter("Mario",12,1,5)
    mario.add_weapon(Weapon("Fire Flower",1,5))
    mario.add_armor(Armor("Super Star",100,1))
    return mario

def initialize_megaman():
    megaman = Fighter("Mega Man",20,1,1)
    megaman.add_weapon(Weapon("Crash Bomber",2,4))
    megaman.add_weapon(Weapon("Atomic Fire",2,2))
    megaman.add_weapon(Weapon("Metal Blade",1,8))
    megaman.add_armor(Armor("Leaf Shield",1,4))
    return megaman

def initialize_link():
    link = Fighter("Link",15,0,2)
    link.add_weapon(Weapon("Master Sword",3,5))
    link.add_armor(Armor("Hylian Shield",3,5))
    return link

def initialize_samus():
    samus = Fighter("Samus",15,0,1)
    samus.add_weapon(Weapon("Super Missile",5,1))
    samus.add_weapon(Weapon("Arm Cannon",2,10))
    samus.add_armor(Armor("Power Suit",2,5))
    samus.add_armor(Armor("Zero Suit",1,5))
    return samus
    
if __name__ == "__main__":
    main()
