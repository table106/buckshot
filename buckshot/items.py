def useBeer(shotgun: object):
    print(f"you unloaded a {shotgun.content[0]} shell.")
    try:
        shotgun.shoot()
    except IndexError:
        print('ATTEMPTED TO UNLOAD EMPTY SHOTGUN')

def useKnife(shotgun: object):
    shotgun.dmg = 2
    print("the next shot will deal 2 damage.")

def useGlass(shotgun: object):
    print(f"the shell in the chamber is a {shotgun.content[0]} one")

def useCigarette(player: object):
    if player.lives == player.lifeCap:
        print("you already have max lives.")
    else:
        player.heal()

def useCuffs(player: object):
    if player.cuffed:
        print("they're already cuffed. (item not consumed)")
    else:
        player.cuffed = 1