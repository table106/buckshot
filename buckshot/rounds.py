from random import randint as r

from player import *

from system import trySleep, printAndLogInfo

def round1(player1: Player, player2: Player, shotgun: Shotgun, testmode: bool=False):
    while (player1.lives > 0) and (player2.lives > 0):
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        trySleep(5, testmode)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
            clear()
            printAndLogInfo(player1, player2, shotgun)
            player1.turn(shotgun)
            if player1.otherDmg == True:
                player2.takeDmg()
                player1.otherDmg = False
            if testmode:
                print(player1.lives, player2.lives, shotgun)
            clear()
            if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                break
            printAndLogInfo(player1, player2, shotgun)
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
    trySleep(5, testmode)

def round2(player1: Player_R2, player2: Player_R2, shotgun: Shotgun, testmode: bool=False):
    while (player1.lives > 0) and (player2.lives > 0):
        player1.getItem(1)
        trySleep(2, testmode)
        player2.getItem(1)
        trySleep(2, testmode)
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        trySleep(5, testmode)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
            clear()
            if player1.cuffed == 2:
                print(f"{player1.name} broke free from cuffs.")
                player1.cuffed = 0
                trySleep(2, testmode)
            elif player1.cuffed == 1:
                print(f"{player1.name} is cuffed.")
                player1.cuffed += 1
                trySleep(2, testmode)
                player2.turn(shotgun)
                continue
            clear()
            printAndLogInfo(player1, player2, shotgun)
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
                trySleep(2, testmode)
            elif player2.cuffed == 1:
                print(f"{player2.name} is cuffed.")
                player2.cuffed += 1
                trySleep(2, testmode)
                continue
            clear()
            printAndLogInfo(player1, player2, shotgun)
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
    trySleep(5, testmode)

def round3(player1: Player_R2, player2: Player_R2, shotgun: Shotgun, testmode: bool=False):
    while (player1.lives > 0) and (player2.lives > 0): # round 3
        player1.getItem(2)
        trySleep(2, testmode)
        player2.getItem(2)
        trySleep(2, testmode)
        while len(player1.inv) > 8:
            player1.inv.pop()
        while len(player2.inv) > 8:
            player2.inv.pop()
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        trySleep(5, testmode)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0): 
            clear()
            if player1.cuffed == 2:
                print(f"{player1.name} broke free from cuffs.")
                player1.cuffed = 0
                trySleep(2, testmode)
            elif player1.cuffed == 1:
                print(f"{player1.name} is cuffed.")
                player1.cuffed += 1
                trySleep(2, testmode)
                player2.turn(shotgun)
                continue
            clear()
            printAndLogInfo(player1, player2, shotgun)
            player1.turn(shotgun)
            if player1.otherDmg == True:
                player2.takeDmg(shotgun.dmg)
                player1.otherDmg = False
            clear()
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            trySleep(2, testmode)
            clear()
            if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                break
            if player2.cuffed == 2:
                print(f"{player2.name} broke free from cuffs.")
                player2.cuffed = 0
                trySleep(2, testmode)
            elif player2.cuffed == 1:
                print(f"{player2.name} is cuffed.")
                player2.cuffed += 1
                trySleep(2, testmode)
                continue
            clear()
            printAndLogInfo(player1, player2, shotgun)
            player2.turn(shotgun)
            if player2.otherDmg == True:
                player1.takeDmg(shotgun.dmg)
                player2.otherDmg = False
            trySleep(2, testmode)
            clear()
        clear()
    if player1.lives == 0:
        print(f"{player2.name} wins.")
        player2.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} wins.")
        player1.wins += 1
    trySleep(5, testmode)