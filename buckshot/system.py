from os import system
from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w", format="%(asctime)s at line no. %(lineno)d - %(message)s")

def clear() -> None:
    system("cls")

def trySleep(duration: int, testmode: bool=False) -> None:
    if testmode:
        return None
    else:
        sleep(duration)

def testmodeLog(plr1: object, plr2: object, shotgun: object, testmode: bool=False) -> None:
    def printAndLogInfo() -> None:
        print(f"1: {plr1.__repr__()}\
              \n2: {plr2.__repr__()}\
              \nshotgun: {shotgun}")
        logging.debug(f"plr1 state: {plr1.__repr__()}\
              \nplr2 state: {plr2.__repr__()}\
              \nshotgun: {shotgun}")
    if testmode:
        printAndLogInfo()

if __name__ == "__main__":
    print("wrong file idiot")