## POKEMON CODE DAY PROGRAM
## AMARI TOWNSEND
## 11/11/17

import random

print("Welcome to the Pokemon League! Your goal is to knock out your opponent")
print("within 4 turns. It might sound tough but it's defienelty possible!")

def main():
    
# Getting user and computer input for choosing a Pokemon
    
    userPKMN = input("What Pokemon do you want to use?\n")
    pokemon = ["Pikachu", "Eevee", "Magikarp", "Bulbasaur",
            "Charmander", "Squirtle", "Chikorita", "Cyndaquill", "Totodile",
            "Treecko", "Torchic", "Mudkip", "Turtwig", "Chimchar", "Piplup",
            "Snivy", "Tepig", "Oshawott", "Chespin", "Fennekin", "Froakie",
            "Rowlet", "Litten", "Popplio"]
            
    enemyPKMN = random.choice(pokemon)

    print("Your enemy uses ", enemyPKMN)
    print("It is on like Donkey Kong!")

    battle(userPKMN, enemyPKMN)

def battle(userPKMN, enemyPKMN):

    attacks = [1,2,3,4]
    
#Pokemon HP and battle about to start
    
    pkmn = 100
    comPKMN = 100

    fight = True
    while fight == True:
        print()
        print(userPKMN, " has four attacks: 1. Tackle 2. Cut 3. Splash 4. Skull Bash")
        fight = int(input("Which attack do you choose?(Choose a number. 1, 2, 3, or 4)\n"))
        print()
        if fight == 1:
            comPKMN = comPKMN - 20
            print(userPKMN, "used tackle and did 20 damage")

        elif fight == 2:
            comPKMN = comPKMN - 25
            print(userPKMN, "used cut and did 25 damage")

        elif fight == 3:
            comPKMN = comPKMN - 0
            print(userPKMN, "used splash and did 0 damage LOL!!!")

        else:
            fight == 4
            comPKMN = comPKMN - 30
            print(userPKMN, "used skull bash and did 30 damage!")

        print(enemyPKMN,"now has", comPKMN," health points remaining!")
        print()

#Your turn has ended. It's the cpu's turn
        
    pkmn = 100
    comPKMN = comPKMN

    fight = True
    while fight == True:
        print(enemyPKMN, " has four attacks: 1. Tackle, 2. Cut 3. Splash 4. Skull Bash")
        print()
        fight = random.choice(attacks)

        if fight == 1:
            pkmn = pkmn - 20
            print(enemyPKMN, "used tackle and did 20 damage")

        elif fight == 2:
            pkmn = pkmn -25
            print(enemyPKMN, "used cut and did 25 damage")

        elif fight == 3:
            pkmn = pkmn - 0
            print(enemyPKMN, "used splash and did 0 damage LOL!!!")

        else:
            fight == 4
            pkmn = pkmn - 30
            print(enemyPKMN, "used skull bash and did 30 damage")

        print(userPKMN, "now has", pkmn," health points remaining!")
        print()
        
#cpu's turn ended it is now your turn again

    pkmn = pkmn
    comPKMN = comPKMN

    fight = True
    while fight == True:
        print()
        print(userPKMN, " has four attacks: 1. Tackle 2. Cut 3. Splash 4. Skull Bash")
        fight = int(input("Which attack do you choose?(Choose a number. 1, 2, 3, or 4)\n"))
        print()
        if fight == 1:
            comPKMN = comPKMN - 20
            print(userPKMN, "used tackle and did 20 damage")

        elif fight == 2:
            comPKMN = comPKMN - 25
            print(userPKMN, "used cut and did 25 damage")

        elif fight == 3:
            comPKMN = comPKMN - 0
            print(userPKMN, "used splash and did 0 damage LOL!!!")

        else:
            fight == 4
            comPKMN = comPKMN - 30
            print(userPKMN, "used skull bash and did 30 damage!")

        print(enemyPKMN,"now has", comPKMN," health points remaining!")
        print()

#Your turn has ended. It's the cpu's turn now

    pkmn = pkmn
    comPKMN = comPKMN

    fight = True
    while fight == True:
        print(enemyPKMN, " has four attacks: 1. Tackle, 2. Cut 3. Splash 4. Skull Bash")
        print()
        fight = random.choice(attacks)

        if fight == 1:
            pkmn = pkmn - 20
            print(enemyPKMN, "used tackle and did 20 damage")

        elif fight == 2:
            pkmn = pkmn -25
            print(enemyPKMN, "used cut and did 25 damage")

        elif fight == 3:
            pkmn = pkmn - 0
            print(enemyPKMN, "used splash and did 0 damage LOL!!!")

        else:
            fight == 4
            pkmn = pkmn - 30
            print(enemyPKMN, "used skull bash and did 30 damage")

        print(userPKMN, "now has", pkmn," health points remaining!")
        print()

#CPU's turn ended. You are now up.

    pkmn = pkmn
    comPKMN = comPKMN

    fight = True
    while fight == True:
        print()
        print(userPKMN, " has four attacks: 1. Tackle 2. Cut 3. Splash 4. Skull Bash")
        fight = int(input("Which attack do you choose?(Choose a number. 1, 2, 3, or 4)\n"))
        print()
        if fight == 1:
            comPKMN = comPKMN - 20
            print(userPKMN, "used tackle and did 20 damage")

        elif fight == 2:
            comPKMN = comPKMN - 25
            print(userPKMN, "used cut and did 25 damage")

        elif fight == 3:
            comPKMN = comPKMN - 0
            print(userPKMN, "used splash and did 0 damage LOL!!!")

        else:
            fight == 4
            comPKMN = comPKMN - 30
            print(userPKMN, "used skull bash and did 30 damage!")

        print(enemyPKMN,"now has", comPKMN," health points remaining!")
        print()

#Your turn ended. It is now the CPU's turn

    pkmn = pkmn
    comPKMN = comPKMN

    fight = True
    while fight == True:
        print(enemyPKMN, " has four attacks: 1. Tackle, 2. Cut 3. Splash 4. Skull Bash")
        print()
        fight = random.choice(attacks)

        if fight == 1:
            pkmn = pkmn - 20
            print(enemyPKMN, "used tackle and did 20 damage")

        elif fight == 2:
            pkmn = pkmn -25
            print(enemyPKMN, "used cut and did 25 damage")

        elif fight == 3:
            pkmn = pkmn - 0
            print(enemyPKMN, "used splash and did 0 damage LOL!!!")

        else:
            fight == 4
            pkmn = pkmn - 30
            print(enemyPKMN, "used skull bash and did 30 damage")

        print(userPKMN, "now has", pkmn," health points remaining!")
        print()

#The CPU's turn ended it is now your turn.

    pkmn = pkmn
    comPKMN = comPKMN

    fight = True
    while fight == True:
        print()
        print(userPKMN, " has four attacks: 1. Tackle 2. Cut 3. Splash 4. Skull Bash")
        fight = int(input("Which attack do you choose?(Choose a number. 1, 2, 3, or 4)\n"))
        print()
        if fight == 1:
            comPKMN = comPKMN - 20
            print(userPKMN, "used tackle and did 20 damage")

        elif fight == 2:
            comPKMN = comPKMN - 25
            print(userPKMN, "used cut and did 25 damage")

        elif fight == 3:
            comPKMN = comPKMN - 0
            print(userPKMN, "used splash and did 0 damage LOL!!!")

        else:
            fight == 4
            comPKMN = comPKMN - 30
            print(userPKMN, "used skull bash and did 30 damage!")

        print(enemyPKMN,"now has", comPKMN," health points remaining!")
        print()

    pkmn = pkmn
    comPKMN = comPKMN

    if comPKMN <= 0:
        print("You won your Pokemon Battle!")
    else:
        pkmn <=0
        print("You lost your Pokemon battle.")

    input("Press enter to quit\n")
    
        
    


    
        


    

    

    

    

        


    


    

            


    


    

    



        









main()
