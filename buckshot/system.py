from os import system
from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG, filename="buckshot\debug.log", filemode="w", format="%(asctime)s at line no. %(lineno)d - %(message)s")

def clear() -> None:
    system("cls")

def trySleep(duration: int, testmode: bool=False) -> None:
    if not testmode:
        sleep(duration)

def testmodeLog(shotgun: object, testmode: bool=False, *players) -> None:
    if testmode:
        for j,player in enumerate(players):
            print(f"{j+1}: {player:dev}")
            logging.debug(f"plr {j+1} state: {player:dev}")
        print(f"shotgun: {shotgun}")
        logging.debug(f"shotgun: {shotgun}")
        print()

def checkNames(name, *players):
    if name in players:
        return False
    return True

def initOpponents(plr1: object, plr2: object, plr3: object=None):
    if plr3 != None:
        plr1.addOpponent(plr2, plr3)
        plr2.addOpponent(plr1, plr3)
        plr3.addOpponent(plr1, plr2)
    else:
        plr1.addOpponent(plr2)
        plr2.addOpponent(plr1)

def handoutItems(count: int, plr1: object, plr2: object, plr3: object=None):
    plr1.getItem(count)
    plr2.getItem(count)
    if plr3:
        plr3.getItem(count)

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")