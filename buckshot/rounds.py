from random import randint as r

from player import *

from system import testmodeLog

def round1(shotgun: Shotgun, testmode: bool=False, *players):
    player1: Player = players[0]
    player2: Player = players[1]
    if len(players) > 2:
        player3: Player = players[2]
        while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0):
            liveshells = r(1,4)
            blankshells = r(1,4)
            shotgun.insertShells(liveshells, blankshells)
            clear()
            print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
            sleep(5)
            clear()
            while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0) and (len(shotgun.content) > 0):
                clear()
                testmodeLog(shotgun, testmode, *players)
                print()
                player1.turn(shotgun)
                clear()
                if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                    break
                testmodeLog(shotgun, testmode, *players)
                print()
                player2.turn(shotgun)
                clear()
                if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                    break
                testmodeLog(shotgun, testmode, *players)
                print()
                player3.turn(shotgun)
                clear()
        if player1.lives == 0:
            print(f"{player2.name} and {player3.name} both get a win. end of round 1")
            player2.wins += 1
            player3.wins += 1
        elif player2.lives == 0:
            print(f"{player1.name} and {player3.name} both get a win. end of round 1")
            player1.wins += 1
            player3.wins += 1
        elif player3.lives == 0:
            print(f"{player1.name} and {player2.name} both get a win. end of round 1")
            player1.wins += 1
            player2.wins += 1
    else:
        while (player1.lives > 0) and (player2.lives > 0):
            liveshells = r(1,4)
            blankshells = r(1,4)
            shotgun.insertShells(liveshells, blankshells)
            clear()
            print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
            sleep(5)
            clear()
            while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
                clear()
                testmodeLog(player1, player2, shotgun, testmode)
                print()
                player1.turn(shotgun)
                clear()
                if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                    break
                testmodeLog(player1, player2, shotgun, testmode)
                print()
                player2.turn(shotgun)
                clear()
        if player1.lives == 0:
            print(f"{player2.name} wins.",end=" ")
            player2.wins += 1
        elif player2.lives == 0:
            print(f"{player1.name} wins.",end=" ")
            player1.wins += 1
        print("end of round 1.")
    sleep(5)

def round2(shotgun: Shotgun, testmode: bool=False, *players):
    player1: Player_R2 = players[0]
    player2: Player_R2 = players[1]
    if len(players) > 2:
        player3: Player_R2 = players[2]
        while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0):
                liveshells = r(1,4)
                blankshells = r(1,4)
                shotgun.insertShells(liveshells, blankshells)
                clear()
                print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
                sleep(5)
                clear()
                while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0) and (len(shotgun.content) > 0):
                    clear()
                    testmodeLog(shotgun, testmode, *players)
                    print()
                    player1.turn(shotgun)
                    clear()
                    if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                        break
                    testmodeLog(shotgun, testmode, *players)
                    print()
                    player2.turn(shotgun)
                    clear()
                    if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                        break
                    testmodeLog(shotgun, testmode, *players)
                    print()
                    player3.turn(shotgun)
                    clear()
        if player1.lives == 0:
            print(f"{player2.name} and {player3.name} both get a win. end of round 2")
            player2.wins += 1
            player3.wins += 1
        elif player2.lives == 0:
            print(f"{player1.name} and {player3.name} both get a win. end of round 2")
            player1.wins += 1
            player3.wins += 1
        elif player3.lives == 0:
            print(f"{player1.name} and {player2.name} both get a win. end of round 2")
            player1.wins += 1
            player2.wins += 1
    else:
        while (player1.lives > 0) and (player2.lives > 0):
            liveshells = r(1,4)
            blankshells = r(1,4)
            shotgun.insertShells(liveshells, blankshells)
            clear()
            print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
            sleep(5)
            clear()
            while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
                clear()
                testmodeLog(player1, player2, shotgun, testmode)
                print()
                player1.turn(shotgun)
                clear()
                if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                    break
                testmodeLog(player1, player2, shotgun, testmode)
                print()
                player2.turn(shotgun)
                clear()
        if player1.lives == 0:
            print(f"{player2.name} wins. end of round 2")
            player2.wins += 1
        elif player2.lives == 0:
            print(f"{player1.name} wins. end of round 2")
            player1.wins += 1
    sleep(5)

def round3(shotgun: Shotgun, testmode: bool=False, *players):
    player1: Player_R3 = players[0]
    player2: Player_R3 = players[1]
    if len(players) > 2:
        player3: Player_R3 = players[2]
        while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0):
                liveshells = r(1,4)
                blankshells = r(1,4)
                shotgun.insertShells(liveshells, blankshells)
                clear()
                print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
                sleep(5)
                clear()
                while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0) and (len(shotgun.content) > 0):
                    clear()
                    testmodeLog(shotgun, testmode, *players)
                    print()
                    player1.turn(shotgun)
                    clear()
                    if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                        break
                    testmodeLog(shotgun, testmode, *players)
                    print()
                    player2.turn(shotgun)
                    clear()
                    if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                        break
                    testmodeLog(shotgun, testmode, *players)
                    print()
                    player3.turn(shotgun)
                    clear()
        if player1.lives == 0:
            print(f"{player2.name} and {player3.name} both get a win. end of round 3")
            player2.wins += 1
            player3.wins += 1
        elif player2.lives == 0:
            print(f"{player1.name} and {player3.name} both get a win. end of round 3")
            player1.wins += 1
            player3.wins += 1
        elif player3.lives == 0:
            print(f"{player1.name} and {player2.name} both get a win. end of round 3")
            player1.wins += 1
            player2.wins += 1

    else:
        while (player1.lives > 0) and (player2.lives > 0):
            liveshells = r(1,4)
            blankshells = r(1,4)
            shotgun.insertShells(liveshells, blankshells)
            clear()
            print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
            sleep(5)
            clear()
            while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
                clear()
                testmodeLog(player1, player2, shotgun, testmode)
                print()
                player1.turn(shotgun)
                clear()
                if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                    break
                testmodeLog(player1, player2, shotgun, testmode)
                print()
                player2.turn(shotgun)
                clear()
        if player1.lives == 0:
            print(f"{player2.name} wins. end of round 3")
            player2.wins += 1
        elif player2.lives == 0:
            print(f"{player1.name} wins. end of round 3")
            player1.wins += 1

if __name__ == "__main__": # this is not a script, just a lib
    print("wrong file idiot")