from random import randint as r
from time import sleep

from shotgun import Shotgun
from items import handoutItems
from system import clear

def round_2P(shotgun: Shotgun, player1: object, player2: object, /, *, roundNo: int) -> None:
    while (player1.lives > 0) and (player2.lives > 0):
        if roundNo >= 2:
            handoutItems(roundNo-1, player1, player2)
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        sleep(5)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun.content) > 0):
            clear()
            player1.turn(shotgun)
            clear()
            if player1.lives == 0 or player2.lives == 0 or len(shotgun.content) == 0:
                break
            player2.turn(shotgun)
            clear()
    if player1.lives == 0:
        print(f"{player2.name} wins.",end=" ")
        player2.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} wins.",end=" ")
        player1.wins += 1
    print(f"end of round {roundNo}.")
    sleep(5)

def round_3P(shotgun: Shotgun, player1: object, player2: object, player3: object, /, *, roundNo: int) -> None:
    while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0):
        if roundNo >= 2:
            handoutItems(roundNo-1, player1, player2, player3)
        liveshells = r(1,4)
        blankshells = r(1,4)
        shotgun.insertShells(liveshells, blankshells)
        clear()
        print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
        sleep(5)
        clear()
        while (player1.lives > 0) and (player2.lives > 0) and (player3.lives > 0) and (len(shotgun.content) > 0):
            clear()
            player1.turn(shotgun)
            clear()
            if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                break
            player2.turn(shotgun)
            clear()
            if player1.lives == 0 or player2.lives == 0 or player3.lives == 0 or len(shotgun.content) == 0:
                break
            player3.turn(shotgun)
            clear()
    if player1.lives == 0:
        print(f"{player2.name} and {player3.name} both get a win. end of round {roundNo}")
        player2.wins += 1
        player3.wins += 1
    elif player2.lives == 0:
        print(f"{player1.name} and {player3.name} both get a win. end of round {roundNo}")
        player1.wins += 1
        player3.wins += 1
    elif player3.lives == 0:
        print(f"{player1.name} and {player2.name} both get a win. end of round {roundNo}")
        player1.wins += 1
        player2.wins += 1
    sleep(5)

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")