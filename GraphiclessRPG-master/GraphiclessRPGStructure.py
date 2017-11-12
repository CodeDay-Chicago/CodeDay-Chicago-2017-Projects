# Juron Townsend
# 11/11/17
# Graphicless RPG



import random
from GraphiclessRPGClasses import *



name = input('What is your name? ')
hero = Hero(name, random.randrange(51) + 50, 10)
adire = Enemy('Adire', random.randrange(51) + 50, 10)



def heroOption():
    'Decides what the hero will do.'

    while True:
        choice = int(input('It is your turn. You can press the respective buttons to\n' +
                           '1: attack\n' +
                           '2: heal\n\n'))

        if choice == 1:
            hero.attack(adire)
            print('You dealt ' + str(hero.power) + ' points of damage to ' + adire.name + '\n\n')
            print(str(adire))
            break
        
        elif choice == 2:
            hero.healSelf()
            print('You healed ' + str(hero.heal) + ' points of HP.\n\n')
            print(str(hero))
            break

def enemyOption():
    'Decides automatically what the enemy does.'

    choice = random.randrange(2) + 1

    if choice == 1:
        adire.attack(hero)
        print(adire.name + ' dealt ' + str(adire.power) + ' points of damage to ' + hero.name + '\n\n')
        print(str(hero))
        
    elif choice == 2:
        adire.healSelf()
        print(adire.name + ' healed ' + str(adire.heal) + ' points of HP.\n\n')
        print(str(adire))

    input('\nPress Enter to continue.\n')

        
def winner():
    'Determines the winner.'

    if hero.HP <= 0:
        print('\n\nYou lost the game.\n')
    elif adire.HP <= 0:
        print('\n\nYou won the game!.\n')

    print(str(hero))
    print(str(adire))

    print('\n\n\nYou played a total of ' + str(turnNumber) + ' turns.')

def main():
    'The structure of the game.'

    global turnNumber

    print(str(hero))
    print(str(adire)) # reprints stats every round
    turnNumber = 0 # keeps track of how many turns were played
    turn = 0 # keeps track of whose turn it is    

    while (hero.HP or adire.HP) > 0:

        if turn == 0:
            heroOption()
            turn = 1

        if turn == 1:
            enemyOption()
            turn = 0

        turnNumber += 1

    winner()


main()
