def useBeer(player: object, shotgun: object):
    print(f"you unloaded a {shotgun.content[0]} shell.")
    shotgun.shoot()
    player.inv.remove("beer")

def useKnife(player: object, shotgun: object):
    print("the next shot will deal 2 damage.")
    shotgun.dmg = 2
    player.inv.remove("knife")

def useGlass(player: object, shotgun: object):
    print(f"the shell in the chamber is a {shotgun.content[0]} one")
    player.inv.remove("magnifying glass")
    

def useCigarette(player: object):
    if player.lives == player.lifeCap:
        print("you already have max lives.")
    else:
        player.heal()
    player.inv.remove("cigarette")

def useCuffs(player: object):
    if player.cuffed:
        print("they're already cuffed. (item not consumed)")
    else:
        player.cuffed = 1
        player.inv.remove("cuffs")