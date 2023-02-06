########
#import modules
#######
def checkhealth():
    if health == 0:
        print("You died")

########
#define functions
#######
def start():
    print("Welcome!\nThe goal is to find the backrooms and escape without dying.")
    townhall()

def townhall():
    print("You are in townhall")
    move = input("\nWhere would you like to go? Say one of these choices:\n\thallwayb\n\thallwayd\n\tstairs\n")
    if move.lower() == "hallwayb":
        hallwayB()
    elif move.lower() == "hallwayd":
        hallwayD()
    elif move.lower() == "stairs":
        stairs()
    else:
        #TODO: what should happen if they type something else?
        pass
def stairs():
    print(''' 
     __  _.-"` `'-.
    /||\\'._ __{}_(
    ||||  |'--.__\\
    |  L.(   ^_^|
    \ .-' |   _ |
    | |   )\___/
    |  \-'`:._]
    \__/;      '-.
    ''')
    print("\nsomeone wearing a black shirt that says 'security' is standing in the staircase. They say you need to stay on the first floor.")
    input("\nPress enter to go back.")
    townhall()

def hallwayB():
    print("You are in hallwayb")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttownhall\n\thallwayd\n\tcafateria\n")
    if move.lower() == "townhall":
        townhall()
    elif move.lower() == "hallwayd":
        hallwayD()
    elif move.lower() == "cafateria":
        cafateria()
    else:
        #TODO: what should happen if they type something else?
        pass
def cafateria():
    print("You are in the cafateria and see favio eating.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tkeep going\n\thallwayb\n\teat with favio\n\ttownhall\n")
    if move.lower() == "townhall":
        townhall()
    elif move.lower() == "hallwayb":
        hallwayB()
    elif move.lower() == "eat with favio":
        print("You ate with favio.")
        input("\nPress enter to go back.")
        hallwayb()
    elif move.lower() == "keep going":
        keepgoing()
    else:

        #TODO: what should happen if they type something else?
        pass
def hallwayD():
    print("You are in hallwayd")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttownhall\n\thallwayb\n\tlibrary\n")
    if move.lower() == "hallwayb":
        hallwayB()
    elif move.lower() == "townhall":
        townhall()
    elif move.lower() == "library":
        library()
    else:
        #TODO: what should happen if they type something else?
        pass
def library():
    global health
    print("You are in the library and see mr jones fighting over the last cup of coffee.")
    move = input("\nWhat do you do? Say one of these choices:\n\thallwayd\n\tsnitch\n\thelp mr jones\n")
    if move.lower() == "hallwayd":
        hallwayD()
    elif move.lower() == "snitch":
        print("You decided to snitch but snitches get stitches")
        health = health - 100
        checkhealth()
    elif move.lower() == "help mr jones":
        print("You helped mr jones and he thanked you and said he will give you free A's.")
        hallwayD()
    else:
        #TODO: what should happen if they type something else?
        pass
def keepgoing():
    print("You fell into the backrooms and are confused.")
    move = input("\nWhere do you go now? Say one of these choices:\n\tforward\n\tright\n\tleft\n")
    if move.lower() == "forward":
        forward()
    elif move.lower() == "left":
        print("You went left and saw a monster.")
        health = health - 100
        checkhealth()
    elif move.lower() == "right":
        rint("You went right and saw a monster.")
        health = health - 100
        checkhealth()
    else:
        #TODO: what should happen if they type something else?
        pass
def forward():
    print("You go forward and see another student.")
    move = input("\nwhat do you do? Say one of these choices:\n\thelp\n\trun\n")
    if move.lower() == "help":
        help()
    elif move.lower() == "run":
        rint("You ran and saw a monster.")
        health = health - 100
        checkhealth()
    else:
        #TODO: what should happen if they type something else?
        pass
def help():
    print("You helped and he said he knew a way out.")
    move = input("\nwhat do you do? Say one of these choices:\n\ttrust\n\tdont trust\n")
    if move.lower() == "trust":
        print("You trusted him and you found a way out\n You won!")
    elif move.lower() == "run":
        rint("You ran and ran right into a monster.")
        health = health - 100
        checkhealth()
 
########
#main
#######
#TODO: Add some global variables
health = 100
start()