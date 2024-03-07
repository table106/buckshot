from shotgun import Shotgun

def useBeer(player: object, shotgun: Shotgun):
    print(f"you unloaded a {shotgun.content[0]} shell.")
    shotgun.shoot()
    player.inv.remove("beer")

def useKnife(player: object, shotgun: Shotgun):
    print("the next shot will deal 2 damage.")
    shotgun.dmg = 2
    player.inv.remove("knife")

def useGlass(player: object, shotgun: Shotgun):
    print(f"the shell in the chamber is a {shotgun.content[0]} one")
    player.inv.remove("magnifying glass")
    
def useCigarette(player: object):
    if player.lives == player.lifeCap:
        print("you already have max lives. (item consumed)")
    else:
        player.heal()
    player.inv.remove("cigarette")

def useCuffs(using: object, cuffed: object):
    if cuffed.cuffed == 1:
        print("they're already cuffed. (item not consumed)")
    else:
        cuffed.cuffed = 1
        using.inv.remove("cuffs")

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")