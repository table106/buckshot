from shotgun import Shotgun

def useBeer(player: object, shotgun: Shotgun, /) -> None:
    print(f"you unloaded a {shotgun.content[0]} shell.")
    shotgun.shoot()
    player.inv.remove("beer")

def useKnife(player: object, shotgun: Shotgun, /) -> None:
    print("the next shot will deal 2 damage.")
    shotgun.dmg = 2
    player.inv.remove("knife")

def useGlass(player: object, shotgun: Shotgun, /) -> None:
    print(f"the shell in the chamber is a {shotgun.content[0]} one")
    player.inv.remove("magnifying glass")
    
def useCigarette(player: object, /) -> None:
    if player.lives == player.lifeCap:
        print("you already have max lives. (item consumed)")
        player.inv.remove("cigarette")
        return
    try:
        if player.lifeLocked == True:
            print("...nothing happened")
    except AttributeError:
        print("you feel refreshed. +1 life")
        player.heal()
    player.inv.remove("cigarette")

def useCuffs(using: object, cuffed: object, /) -> int | None:
    if cuffed.cuffed == 1:
        print("they're already cuffed. (item not consumed)")
        return 1
    else:
        cuffed.cuffed = 1
        using.inv.remove("cuffs")

def handoutItems(count: int, plr1: object, plr2: object, plr3: object=None, /) -> None:
    plr1.getItem(count)
    plr2.getItem(count)
    if plr3 != None:
        plr3.getItem(count)

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")