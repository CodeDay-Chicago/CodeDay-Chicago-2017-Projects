##CodeMon

import random
compHealth = 100
userHealth = 100

print('\t\t\t\tWelcome to CodeMon!')
print('\t\t\t   Developed by: Augustus Ryan')
name = input('Whats your name?: ')
print('Hi', name,'! Choose a CodeMon.')
print('1.) Denki a electric type CodeMon')
print()
print('2.) Iwa a earth type CodeMon')
print()
print('3.) Kashi a fire type CodeMon')
print()
print('4.) Mizu a water type CodeMon')
print()
userCM = int(input("Enter your CodeMon's number: "))
compCM = random.randint(1,4)
print("You may come across 4 diffrent CodeMons on your journey. Ippan(A common type CodeMon), Btsurigaki(A psychic type CodeMon), Hagane(A steel type CodeMon), or Kusa(A grass type CodeMon).") 

if userCM == 1:
    print('Your CodeMon is Denki')
    print()
    userCM = 1
elif userCM == 2:
    print('Your CodeMon is Iwa')
    print()
    userCM = 2
elif userCM == 3:
    print('Your CodeMon is Kashi')
    print()
    userCM = 3
elif userCM == 4:
    print('Your CodeMon is Mizu')
    print()
    userCM = 4
else:
    print('Press enter to quit.')

################################################################################################################

while compCM == compCM:
    if userCM == 1:
        if compHealth <= 0:
            print('YOU WIN!!')
            input('Press enter to quit.')
            break
        elif userHealth <= 0:
            print('TAKE THIS L')
            print('Game Over :-(')
            input = ('Press enter to quit.')
        else:
            compdamage = random.randint(5,30)
            userHealth -= compdamage
            print("Butsurigaku did", compdamage, 'damage to your CodeMon!')
            print('Your CodeMon\'s health is at', userHealth)

        usermove = input('Would you like to use Thunder Bolt, Electro Ball, or Hyper Beam?: ')
        if usermove.title() == 'Thunder Bolt':
            damage = random.randint(5,18)
            compHealth -= damage
            print("You did", damage, 'damage to Butsurigaku!')
            print('Your opponnent\'s health is at', compHealth)
        elif usermove.title() == 'Electro Ball':
            damage = random.randint(9,16)
            compHealth -= damage
            print("You did", damage, 'damage to Butsurigaku!')
            print('Your opponnent\'s health is at', compHealth)
        else:
            damage = random.randint(2,27)
            compHealth -= damage
            print("You did", damage, 'damage to Butsurigaku!')
            print('Your opponnent\'s health is at', compHealth)
                    
            
       
    if userCM == 2:
        if compHealth <= 0:
            print('YOU WIN!!')
            input('Press enter to quit.')
            break
        elif userHealth <= 0:
            print('TAKE THIS L')
            print('Game Over :-(')
            input = ('Press enter to quit.')
        else:
            compdamage = random.randint(5,30)
            userHealth -= compdamage
            print("Ippan did", compdamage, 'damage to your CodeMon!')
            print('Your CodeMon\'s health is at', userHealth)
        usermove = input('Would you like to use Earthquake, Rock Blast, or Bulldoze?: ')
        if usermove.title() == 'Earthquake':
            damage = random.randint(4,11)
            compHealth -= damage
            print("You did", damage, 'damage to Ippan!')
            print('Your opponnent\'s health is at', compHealth)
        elif usermove.title() == 'Rock Blast':
            damage = random.randint(9,14)
            compHealth -= damage
            print("You did", damage, 'damage to Ippan!')
            print('Your opponnent\'s health is at', compHealth)
        else:
            damage = random.randint(6,26)
            compHealth -= damage
            print("You did", damage, 'damage to Ippan!')
            print('Your opponnent\'s health is at', compHealth)
            


            

    if userCM == 3:
        if compHealth <= 0:
            print('YOU WIN!!')
            input('Press enter to quit.')
            break
        elif userHealth <= 0:
            print('TAKE THIS L')
            print('Game Over :-(')
            input = ('Press enter to quit.')
        else:
            compdamage = random.randint(5,30)
            userHealth -= compdamage
            print("Hagane did", compdamage, 'damage to your CodeMon!')
            print('Your CodeMon\'s health is at', userHealth)
        usermove = input('Would you like to use Flamethrower, Lava Plume, or Ember?: ')
        if usermove.title() == 'Flamethrower':
            damage = random.randint(8,11)
            compHealth -= damage
            print("You did", damage, 'damage to Hagane!')
            print('Your opponnent\'s health is at', compHealth)
        elif usermove.title() == 'Lava Plume':
            damage = random.randint(6,25)
            compHealth -= damage
            print("You did", damage, 'damage to Hagane!')
            print('Your opponnent\'s health is at', compHealth)
        else:
            damage = random.randint(4,10)
            compHealth -= damage
            print("You did", damage, 'damage to Hagane!')
            print('Your opponnent\'s health is at', compHealth)
 
       
    if userCM == 4:
        if compHealth <= 0:
            print('YOU WIN!!')
            input('Press enter to quit.')
            break
        elif userHealth <= 0:
            print('TAKE THIS L')
            print('Game Over :-(')
            input = ('Press enter to quit.')
        else:
            compdamage = random.randint(5,30)
            userHealth -= compdamage
            print("Kusa did", compdamage, 'damage to your CodeMon!')
            print('Your CodeMon\'s health is at', userHealth)
        usermove = input('Would you like to use Hydro Pump, Aqua Tail, or Waterfall?: ')
        if usermove.title() == 'Hydro Pump':
            damage = random.randint(5,23)
            compHealth -= damage
            print("You did", damage, 'damage to Kusa!')
            print('Kusa\'s health is at', compHealth)
        elif usermove.title() == 'Aqua Tail':
            damage = random.randint(7,10)
            compHealth -= damage
            print("You did", damage, 'damage to Kusa!')
            print('Your opponnent\'s health is at', compHealth)
        else:
            damage = random.randint(11,16)
            compHealth -= damage
            print("You did", damage, 'damage to Kusa!')
            print('Your opponnent\'s health is at', compHealth)
            
