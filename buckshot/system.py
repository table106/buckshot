from os import system

def clear() -> None:
    system("cls")

def checkNames(name, *players) -> bool:
    return name in players

def initOpponents(plr1: object, plr2: object, plr3: object=None) -> None:
    plr1.addOpponent(plr2, plr3)
    plr2.addOpponent(plr1, plr3)
    if plr3 != None:
        plr3.addOpponent(plr1, plr2)

def handoutItems(count: int, plr1: object, plr2: object, plr3: object=None) -> None:
    plr1.getItem(count)
    plr2.getItem(count)
    if plr3 != None:
        plr3.getItem(count)

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")