from random import randint as r
from time import sleep as s

from player import *

def round1(player1: Player, player2: Player, shotgun: Shotgun, testmode: bool=False):
    while (player1.lives > 0) and (player2.lives > 0):
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
            if testmode:
                print(player1.lives, player2.lives, shotgun)
            clear()
            if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                break
            player2.turn(shotgun)
            if player2.otherDmg == True:
                player1.takeDmg()
                player2.otherDmg = False
            if testmode:
                print(player1.lives, player2.lives, shotgun)
            clear()
    if player1.lives == 0:
        print(f"{player2.name} wins.",end=" ")
        player2.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} wins.",end=" ")
        player1.wins += 1
    print("end of round 1.")
    s(5)

def round2(player1: Player_R2, player2: Player_R2, shotgun: Shotgun, testmode: bool=False):
    while (player1.lives > 0) and (player2.lives > 0):
        player1.getItem(1)
        s(2)
        player2.getItem(1)
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
            if testmode:
                print(player1.lives, player2.lives, shotgun, player1.cuffed, player2.cuffed)
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
            if testmode:
                print(player1.lives, player2.lives, shotgun, player1.cuffed, player2.cuffed)
            clear()
        clear()

    if player1.lives == 0:
        print(f"{player2.name} wins. end of round 2")
        player2.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} wins. end of round 2")
        player1.wins += 1
    s(5)

def round3(player1: Player_R2, player2: Player_R2, shotgun: Shotgun, testmode: bool=False):
    while (player1.lives > 0) and (player2.lives > 0): # round 3
        player1.getItem(2)
        s(2)
        player2.getItem(2)
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