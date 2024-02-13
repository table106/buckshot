from random import randint as r
from time import sleep as s

from system import clear

from player import *

from shotgun import *

from items import *

def main() -> None:
    print("well hello there! welcome to...")
    s(3)
    print("=====================")
    print("||BUCKSHOT ROULETTE||")
    print("||   (text version)||")
    print("=====================")
    print("version v0.6.3-beta\n")
    print("press enter to start")
    ans = input("or type 'how' for a how-to-play ")
    if ans == "how":
        clear()
        print("alright, so\
              \nthere's a shotgun\
              \nevery time it is empty we load some shells in\
              \nthey can be blank, or live, and will be in a random sequence\
              \nyou only get the numbers though!\
              \nevery turn, you use the shotgun\
              \nyou point it either at yourself, or your enemy\
              \nif you shoot yourself with a blank you get to go again!\
              \n\nITEMS (from round 2 onwards)\
              \n-beer:\
              \nyou eject a round from the shotgun, if its the last one we reload the shotgun\
              \n\n-knife:\
              \nyou saw the shotgun, next shot will deal 2 damage\
              \n\n-magnifying glass:\
              \nyou look into the chamber, revealing the shell inside only to you\
              \n\n-cigarette:\
              \nyou regain a life (not how it works irl)\
              \n\n-cuffs:\
              \nyou cuff your enemy skipping their next turn")
        input("when you finish reading, just press enter")
    clear()
    shotgun = Shotgun()

    player1 = Player(1,input("what does player 1 call themselves? "),2,2)
    player2 = Player(2,input("what about player 2? "),2,2)

    print("good luck.")
    s(2)

    while (player1.lives > 0) and (player2.lives > 0): # round 1
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        s(5)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
            clear()
            player1.turn(shotgun)
            if player1.otherDmg == True:
                player2.takeDmg()
                player1.otherDmg = False
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            clear()
            if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                break
            player2.turn(shotgun)
            if player2.otherDmg == True:
                player1.takeDmg()
                player2.otherDmg = False
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            clear()
        
    if player1.lives == 0:
        print(f"{player2.name} wins.",end=" ")
        player2.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} wins.",end=" ")
        player1.wins += 1
    print("end of round 1.")
    s(5)

    shotgun.content = []
    player1 = Player_R2(1,player1.name,4,4)
    player2 = Player_R2(2,player2.name,4,4)
    clear()
    print("both of you can now have items. (max 8)")
    s(3)

    while (player1.lives > 0) and (player2.lives > 0): # round 2
        player1.getItem(2)
        s(2)
        player2.getItem(2)
        s(2)
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        s(5)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
            clear()
            if player1.cuffed == 2:
                print(f"{player1.name} broke free from cuffs.")
                player1.cuffed = 0
                s(2)
            elif player1.cuffed == 1:
                print(f"{player1.name} is cuffed.")
                player1.cuffed += 1
                s(2)
                player2.turn(shotgun)
                continue
            clear()
            player1.turn(shotgun)
            if player1.otherDmg == True:
                player2.takeDmg(shotgun.dmg)
                player1.otherDmg = False
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            clear()
            if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                break
            if player2.cuffed == 2:
                print(f"{player2.name} broke free from cuffs.")
                player2.cuffed = 0
            elif player2.cuffed == 1:
                print(f"{player2.name} is cuffed.")
                player2.cuffed += 1
                s(2)
                continue
            clear()
            player2.turn(shotgun)
            if player2.otherDmg == True:
                player1.takeDmg(shotgun.dmg)
                player2.otherDmg = False
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            clear()
        clear()

    if player1.lives == 0:
        print(f"{player2.name} wins. end of round 2")
        player2.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} wins. end of round 2")
        player1.wins += 1
    s(5)

    clear()
    print("lets make this a little bit more interesting.")
    s(2)
    print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
    s(5)
    shotgun.content = []
    player1 = Player_R2(1,player1.name,6,6)
    player2 = Player_R2(2,player2.name,6,6)
    clear()
    while (player1.lives > 0) and (player2.lives > 0): # round 3
        player1.getItem(4)
        s(2)
        player2.getItem(4)
        s(2)
        while len(player1.inv) > 8:
            player1.inv.pop()
        while len(player2.inv) > 8:
            player2.inv.pop()
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        s(5)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0): 
            clear()
            if player1.cuffed == 2:
                print(f"{player1.name} broke free from cuffs.")
                player1.cuffed = 0
                s(2)
            elif player1.cuffed == 1:
                print(f"{player1.name} is cuffed.")
                player1.cuffed += 1
                s(2)
                player2.turn(shotgun)
                continue
            clear()
            player1.turn(shotgun)
            if player1.otherDmg == True:
                player2.takeDmg(shotgun.dmg)
                player1.otherDmg = False
            clear()
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            s(2)
            clear()
            if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                break
            if player2.cuffed == 2:
                print(f"{player2.name} broke free from cuffs.")
                player2.cuffed = 0
            elif player2.cuffed == 1:
                print(f"{player2.name} is cuffed.")
                player2.cuffed += 1
                s(2)
                continue
            clear()
            player2.turn(shotgun)
            if player2.otherDmg == True:
                player1.takeDmg(shotgun.dmg)
                player2.otherDmg = False
            s(2)
            clear()
        clear()

    if player1.lives == 0:
        print(f"{player2.name} wins.")
        player2.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} wins.")
        player1.wins += 1
    s(5)

    clear()
    if player1.wins > player2.wins:
        print(f'{player1.name} wins with a score of {player1.wins} to {player2.wins}')
    elif player2.wins > player1.wins:
        print(f'{player2.name} wins with a score of {player2.wins} to {player1.wins}')
    s(5)
    clear()
    print('and this is it!')
    s(2)
    print('hope you enjoyed this thing')
    s(2)
    print('love and kisses, table106') # if youre contributing, add yourself here!
    s(2) # also might want to change the time before end of program

if __name__ == "__main__":
    main()