# Juron Townsend
# 11/11/17
# Graphicless RPG



import random



class Hero(object):
    'Creates a hero object.'

    def __init__(self, name:str, HP:int, mgc:int):
        'The constructor.'

        self.name = name
        self.HP = HP # sets the health to a random value
        self.power = 0
        self.heal = 0
        self.mgc = mgc

        print(str(self))
        

    def __str__(self):
        'Displays all the stats of an enemy.'
        
        return ('\n' +
              'Name: ' + self.name + '\n' +
              'HP: ' + str(self.HP) + '\n' +
              'ATK Power: ' + str(self.power) + '\n' +
              'Heal Max: ' + str(self.heal) + '\n' +
              'Magic Counters: ' + str(self.mgc) + '\n')

    # prints everything at once

    def str(self, string):
        'Converts anything to a string.'

        return str(string)


    def attack(self, other): # other is another object, preferably enemy
        'Sets a value to the attack.'

        self.power = random.randrange(10) + 1 # assigns a random value of attack
        chance = random.randrange(20) + 1
        
        if chance == 20:
            self.power *= 2 # chance of multiplying the power by 2
            print('Twice the damage is being dealt!\n')

        other.HP -= self.power

    def healSelf(self):
        'Heals hero a random amount.'

        self.heal = random.randrange(10) + 1
        chance = random.randrange(20) + 1
        
        if chance == 20:
            self.heal *= 2 # chance of multiplying the health gained back by 2
            print('Twice the amount is being healed!\n')

        self.HP += self.heal


class Enemy(object):
    'Creates an enemy object.'

    def __init__(self, name:str, HP:int, mgc:int):
        'The constructor.'

        self.name = name
        self.HP = HP
        self.power = 0
        self.heal = 0
        self.mgc = mgc

        print(str(self))

    def __str__(self):
        'Displays all the stats of an enemy.'
        
        return ('\n' +
              'Name: ' + self.name + '\n' +
              'HP: ' + str(self.HP) + '\n' +
              'ATK Power: ' + str(self.power) + '\n' +
              'Heal Max: ' + str(self.heal) + '\n' +
              'Magic Counters: ' + str(self.mgc) + '\n')


    def str(self, string):
        'Converts anything to a string.'

        return str(string)

        
    # prints everything at once

    def attack(self, other): # other is another object, preferably enemy
        'Sets a value to the attack.'

        self.power = random.randrange(10) + 1
        chance = random.randrange(20) + 1
        
        if chance == 20:
            self.power *= 2 # chance of multiplying the power by 2
            print('Twice the amount of damage is deatl!\n')

        other.HP -= self.power


    def healSelf(self):
        'Heals hero a random amount.'

        self.heal = random.randrange(10) + 1
        chance = random.randrange(20) + 1
        
        if chance == 20:
            self.heal *= 2 # chance of multiplying the health gained back by 2
            print('Twice the amount is being healed!\n')

        self.HP += self.heal
