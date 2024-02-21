from os import system
from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w", format="%(asctime)s at line no. %(lineno)d - %(message)s")

def clear() -> None:
    system("cls")

def trySleep(duration: int, testmode: bool=False) -> None:
    if not testmode:
        sleep(duration)

def testmodeLog(shotgun: object, testmode: bool=False, *players) -> None:
    if testmode:
        for j,player in enumerate(players):
            print(f"{j+1}: {player.__repr__()}")
            logging.debug(f"plr {j+1} state: {player.__repr__()}")
        print(f"shotgun: {shotgun}")
        logging.debug(f"shotgun: {shotgun}")

def checkNames(name, *players):
    if name in players:
        return False
    return True

if __name__ == "__main__": # this is not a script, just a lib
    print("wrong file idiot")