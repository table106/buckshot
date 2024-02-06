def useBeer(shotgun):
    print(f"you unloaded a {shotgun.content[0]} shell.")
    try:
        shotgun.shoot()
    except IndexError:
        print('ATTEMPTED TO UNLOAD EMPTY SHOTGUN')

def useKnife(shotgun):
    shotgun.dmg = 2
    print("the next shot will deal 2 damage.")

def useGlass(shotgun):
    print(f"the shell in the chamber is a {shotgun.content[0]} one")

def useCigarette(wer):
    wer.heal()

def useCuffs(wer):
    wer.cuffed = 1