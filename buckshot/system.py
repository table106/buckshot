from os import system
import log

def clear() -> None:
    system("cls")

def trySleep(duration: int, testmode: bool=False) -> None:
    if testmode:
        return None
    else:
        from time import sleep
        sleep(duration)

def printAndLogInfo(plr1: object, plr2: object, shotgun: object) -> None:
    print(f"1: {plr1.__repr__()}\
          \n2: {plr2.__repr__()}\
          \nshotgun: {shotgun}")
    log.debug(f"plr1 state: {plr1.__repr__()}\
          \nplr2 state: {plr2.__repr__()}\
          \nshotgun: {shotgun}")