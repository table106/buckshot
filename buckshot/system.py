from os import system

def clear() -> None:
    system("cls")

def validName(name: str, *players: tuple[str]) -> bool:
    return (name not in players and name != "" and name != " ")

def initOpponents(plr1: object, plr2: object, plr3: object=None) -> None:
    if plr3 != None:
        plr1.addOpponents(plr2, plr3)
        plr2.addOpponents(plr1, plr3)
        plr3.addOpponents(plr1, plr2)
    else:
        plr1.addOpponents(plr2)
        plr2.addOpponents(plr1)

def playersAlive(plr1: object, plr2: object, plr3: object=None, /) -> bool:
    if plr3 != None:
        return plr1.lives > 0 and plr2.lives > 0 and plr3.lives > 0
    return plr1.lives > 0 and plr2.lives > 0

def shotgunNotEmpty(shotgun: object, /) -> bool:
    return len(shotgun.content) > 0

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")