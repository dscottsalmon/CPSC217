#Name - David Salmon UCID - 30093320 Tutorial - T04
#this is the final version of my program. The setup is somewhat inspired from the hints given to us.
#everything else was completely on my own or inspired from the slides. The distance function is pretty close to anexact replica from slide 18 of the inclass notes.

import random
import time
import sys

WIDTH = 12
HEIGHT = 9
EMPTY = '.'
ENTERPRISE = 'E'
KLINGON = 'K'
STAR = '*'

num = 4                                         #number of ships, this variable counts down how many ships are remaining
kposition = []                                  #initializing the position list
health = 125                                    #initializing the shields of the Enterprise

def distance(x1,x2,y1,y2):                      #this function is used to determine the Euclidean distance between the enterprise and klingon ships.
        sum = (x2-x1) **2 + (y2-y1) ** 2
        return sum ** 0.5

map= [                                          #map=[y][x] coordinates
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
]

key = {                                         #this maps these commands together so north also gives an 'n' command.
        'north': 'n',
        'west': 'w',
        'east': 'e',
        'south': 's',
        'd': 'destruct',
        'quit': 'q',
}


for i in range (WIDTH):
        map[0].append(EMPTY)                    #this starts the whole map off as blanks
        map[1].append(EMPTY)
        map[2].append(EMPTY)
        map[3].append(EMPTY)
        map[4].append(EMPTY)
        map[5].append(EMPTY)
        map[6].append(EMPTY)
        map[7].append(EMPTY)
        map[8].append(EMPTY)

n = 0
while True:                                     #this big chunk of code is placing my stars, klingons, and the enterprise randomly. n is my count variable
        while True:
                while n < 10:
                        x = random.randint(0,WIDTH-1)
                        y = random.randint(0,HEIGHT-1)
                        if map[y][x] != EMPTY:
                                break
                        if map[y][x] == STAR:   #this one is for stars.
                                break
                        else:
                                map[y][x] = STAR
                                n = n + 1
                if n == 10:
                        break
        n = 0
        while True:
                while n < 4:
                        x = random.randint(0,WIDTH-1)
                        y = random.randint(0,HEIGHT-1)
                        if map[y][x] != EMPTY:
                                break
                        if map[y][x] == STAR or map[y][x] == KLINGON:           #this one is for klingons. Also maps their location to a list.
                                break
                        else:
                                map[y][x] = KLINGON
                                kposition.append(x)             #kposition = [x1,y1,x2,y2,x3,y3,x4,y4], this list describes locations of all 4 klingon ships
                                kposition.append(y)
                                n = n + 1
                if n == 4:
                        break
        n = 0
        while True:
                while n < 1:
                        x = random.randint(0,WIDTH-1)
                        y = random.randint(0,HEIGHT-1)
                        if map[y][x] != EMPTY:
                                break
                        if map[y][x] == STAR or map[y][x] == KLINGON:           #this one is for the enterprise. also maps enterprise location to posx and posy variables.
                                break
                        else:
                                map[y][x] = ENTERPRISE
                                n = n + 1
                                posx = x
                                posy = y
                if n == 1:
                        break
        break

K1loc = [kposition[0], kposition[1]]            #mapping out each ship specifically into individual lists.
K2loc = [kposition[2], kposition[3]]
K3loc = [kposition[4], kposition[5]]
K4loc = [kposition[6], kposition[7]]

K1 = 1                                          #initializing the variables for the kenergy dictionary.
K2 = 2
K3 = 3
K4 = 4

kenergy = {
                K1: 50,
                K2: 50,                         #klingon energy in this dictionary, every one starts at 50.
                K3: 50,
                K4: 50,
}

n = 0
while True:                                     #game loop, this is what gets repeated.
        while True:
                for _ in range(WIDTH):
                        print(map[n][_], end=' ')
                print(' ')
                n = n + 1
                if n == 9:
                        break
        print(' ')
        n = 0
        oldposy = posy
        oldposx = posx
                                                #everything above this in the game loop involves printing the map each turn, and assigning the old variables incase
                                                #the enterprise cannot move to the new location

        p = input('COMMAND: ')                  #this is actual input. it turns all imput into lowercase, then checks the key dictionary.
        p = p.lower()
        if p in key:
                p = key[p]

        if p == 'q':                            #these are the quit/destruct commands
                print("GAME OVER")
                break
        elif p == 'destruct':
                print('Self destruct sequence activated. Detonation in T-minus:')
                time.sleep(1)
                print('5...')
                time.sleep(1)
                print('4...')
                time.sleep(1)
                print('3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                print("The Enterprise has Self Destructed.")
                time.sleep(1)
                print('GAME OVER')
                break



        elif p == 'n':                  #these are the movement commands, and what happens if you run into an edge of the map
                if posy > 0:
                        posy = posy - 1
                else:
                        print("You can't go there! You have to fight the Klingons!")
        elif p == 's':
                if posy < HEIGHT-1:
                        posy = posy + 1
                else:
                        print("You can't go there! Earth needs you to fight the Klingons!")
        elif p == 'w':
                if posx > 0:
                        posx = posx - 1
                else:
                        print("You can't go there! The Klingons are the other way!")
        elif p == 'e':
                if posx < WIDTH-1:
                        posx = posx + 1
                else:
                        print("You can't go there! Don't be a coward, go back to the fight!")
        else:
                print('That is an unknown command.')

        if  map[posy][posx] == STAR:            #this stops you from running into stars
                print("You can't go there! There is a star in the way!")
                posy = oldposy
                posx = oldposx

        elif map[posy][posx] == KLINGON:        #this whole chunk of code is what happens when you run into a klingon ship.
                if [posx, posy] == K1loc:
                        print('BOOP! The Enterprise attacked the Klingon Ship!')
                        oldenergy = kenergy[K1]
                        i = random.randint(23,28)
                        if i > oldenergy or i == oldenergy:     #if the damage taken by the klingon ship is greater than or equal to its old health then it is destroyed. The
                                num = num - 1
                                if num == 3 or num == 2:
                                        print("The Klingon ship has been destroyed!",num,"more ships left to go!")
                                if num == 1:
                                        print('The Klingon ship has been destroyed! Just',num,'more left to go!')
                                kenergy[K1] = 0                        
                        else:
                                kenergy[K1] = oldenergy - i
                                posy = oldposy
                                posx = oldposx
                                print("The Klingon shields have taken",i,"damage!")
                if [posx,posy] == K2loc:
                        print('BOOP! The Enterprise attacked the Klingon Ship!')
                        oldenergy = kenergy[K2]                         #code is virtually the same for all four ships.
                        i = random.randint(23,28)
                        if i > oldenergy or i == oldenergy:
                                num = num - 1
                                if num == 3 or num == 2:
                                        print("The Klingon ship has been destroyed!",num,"more ships left to go!")
                                if num == 1:
                                        print('The Klingon ship has been destroyed! Just',num,'more left to go!')
                                kenergy[K2] = 0
                        else:
                                kenergy[K2] = oldenergy - i
                                posy = oldposy
                                posx = oldposx
                                print("The Klingon shields have taken",i,"damage!")
                if [posx, posy] == K3loc:
                        print('BOOP! The Enterprise attacked the Klingon Ship!')
                        oldenergy = kenergy[K3]
                        i = random.randint(23,28)
                        if i > oldenergy or i == oldenergy:
                                num = num - 1
                                if num == 3 or num == 2:
                                        print("The Klingon ship has been destroyed!",num,"more ships left to go!")
                                if num == 1:
                                        print('The Klingon ship has been destroyed! Just',num,'more left to go!')
                                kenergy[K3] = 0
                        else:
                                kenergy[K3] = oldenergy - i
                                posy = oldposy
                                posx = oldposx
                                print("The Klingon shields have taken",i,"damage")            
                if [posx,posy] == K4loc:
                        print('BOOP! The Enterprise attacked the Klingon Ship!')
                        oldenergy = kenergy[K4]
                        i = random.randint(23,28)
                        if i > oldenergy or i == oldenergy:
                                num = num - 1
                                if num == 3 or num == 2:
                                        print("The Klingon ship has been destroyed!",num,"more ships left to go!")
                                if num == 1:
                                        print('The Klingon ship has been destroyed! Just',num,'more left to go!')
                                kenergy[K4] = 0
                        else:
                                kenergy[K4] = oldenergy - i
                                posy = oldposy
                                posx = oldposx
                                print("The Klingon shields have taken",i,"damage!")

        if distance(posx,kposition[0],posy,kposition[1]) < 3:
                if kenergy[K1] == 0:                    #this chunk of code determines what happens if the distance between the Klingons and Enterprise is less than 3.
                        pass                            #if the eucladean distance is less then 3 then the Klingons fire upon the enterprise.
                else:
                        i = random.randint(0,100)
                        if i > 42:
                                print('The Klingon at',K1loc,'fired and missed.')
                                pass
                        else:
                                damage = random.randint(5,10)
                                print("The Klingon at",K1loc,"fired on the Enterprise! The shields have taken",damage,"damage")
                                health = health - damage
        if distance(posx,kposition[2],posy,kposition[3]) < 3:           #again, this code is virtually the same for all 4 klingon ships.
                if kenergy[K2] == 0:
                        pass
                else:
                        i = random.randint(0,100)
                        if i > 42:
                                print('The Klingon at',K2loc,'fired and missed.')
                                pass
                        else:
                                damage = random.randint(5,10)
                                print("The Klingon at",K2loc,"fired on the Enterprise! The shields have taken",damage,"damage")
                                health = health - damage
        if distance(posx,kposition[4],posy,kposition[5]) < 3:
                if kenergy[K3] == 0:
                        pass                
                else:
                        i = random.randint(0,100)
                        if i > 42:
                                print('The Klingon at',K3loc,'fired and missed.')
                                pass
                        else:
                                damage = random.randint(5,10)
                                print("The Klingon at",K3loc,"fired on the Enterprise! The shields have taken",damage,"damage")
                                health = health - damage
        if distance(posx,kposition[6],posy,kposition[7]) < 3:
                if kenergy[K4] == 0:
                        pass
                else:
                        i = random.randint(0,100)
                        if i > 42:
                                print('The Klingon at',K4loc,'fired and missed.')
                                pass
                        else:
                                damage = random.randint(5,10)
                                print("The Klingon at",K4loc,"fired on the Enterprise! The shields have taken",damage,"damage")
                                health = health - damage


        map[oldposy][oldposx] = EMPTY           #this is drawing the actual movement of the enterprise. The reason its in this order
                                                #down here is so old spot is turned into an empty, and if the enterprise doesn't move it is then
        map[posy][posx] = ENTERPRISE            #relabeled as enterprise.

        if kenergy[K1] == 0 and kenergy[K2] == 0 and kenergy[K3] == 0 and kenergy[K4] == 0:             #this is checking for the win condition every turn.
                print('The Final Klingon Ship has been destroyed!!')
                print('YOU WIN')
                print('GAME OVER')
                sys.exit()
        if health < 0 or health == 0:
                print('The Enterprise was destroyed in a fiery explosion.')             #this is checking for the lose condition every turn.
                print('(even though this is in space...)')
                print('YOU LOSE')
                print('GAME OVER')
                sys.exit()

        print("The Enterprise's shields are at",health)         #this prints the enterpise's shields every turn, unless a win/lose condition is met.
