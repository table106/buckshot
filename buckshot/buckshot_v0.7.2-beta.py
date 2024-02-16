from time import sleep as s

from system import *

from player import *

from shotgun import *

from items import *

from rounds import *

def main() -> None:
    print("well hello there! welcome to...")
    s(3)
    print("=====================")
    print("||BUCKSHOT ROULETTE||")
    print("||   (text version)||")
    print("=====================")
    print("version v0.7.2-beta\n")
    print("press enter to start")
    ans = input("or type 'how' for a how-to-play ")
    if ans == "how":
        clear()
        print("alright, so\
              \nthere's a shotgun\
              \nevery time it is empty we load some shells in\
              \nthey can be blank, or live, and will be in a random sequence\
              \nyou only get the numbers though!\
              \nevery turn, you use the shotgun\
              \nyou point it either at yourself, or your enemy\
              \nif you shoot yourself with a blank you get to go again!\
              \n\nITEMS (from round 2 onwards)\
              \n-beer:\
              \nyou eject a round from the shotgun, if its the last one we reload the shotgun\
              \n\n-knife:\
              \nyou saw the shotgun, next shot will deal 2 damage\
              \n\n-magnifying glass:\
              \nyou look into the chamber, revealing the shell inside only to you\
              \n\n-cigarette:\
              \nyou regain a life (not how it works irl)\
              \n\n-cuffs:\
              \nyou cuff your enemy skipping their next turn")
        input("when you finish reading, just press enter")
    elif ans == "therealtable":
        print("hello world!")
        lel = ["1", "2", "3"]
        ans = "1"
        shotgun = Shotgun()
        while ans in lel:
            ans = input("where to? ")
            if ans == "1":
                shotgun.content = []
                player1 = Player(1,"plr1",2,2)
                player2 = Player(2,"plr2",2,2)
                player1.addOpponent(player2)
                player2.addOpponent(player1)
                round1(player1, player2, shotgun, True)
            elif ans == "2":
                shotgun.content = []
                player1 = Player_R2(1,"plr1",4,4)
                player2 = Player_R2(2,"plr2",4,4)
                player1.addOpponent(player2)
                player2.addOpponent(player1)
                round2(player1, player2, shotgun, True)
            elif ans == "3":
                shotgun.content = []
                player1 = Player_R2(1,"plr1",6,6)
                player2 = Player_R2(2,"plr2",6,6)
                player1.addOpponent(player2)
                player2.addOpponent(player1)
                round3(player1, player2, shotgun, True)
    clear()
    shotgun = Shotgun()

    player1 = Player(1,input("what does player 1 call themselves? "),2,2)
    player2 = Player(2,input("what about player 2? "),2,2)
    player1.addOpponent(player2)
    player2.addOpponent(player1)

    print("good luck.")
    s(2)

    round1(player1, player2, shotgun)

    shotgun.content = []
    player1 = Player_R2(1,player1.name,4,4)
    player2 = Player_R2(2,player2.name,4,4)
    player1.addOpponent(player2)
    player2.addOpponent(player1)
    clear()
    print("both of you can now have items. (max 8)")
    s(3)

    round2(player1, player2, shotgun)

    clear()
    print("lets make this a little bit more interesting.")
    s(2)
    print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
    s(5)

    shotgun.content = []
    round3(player1, player2, shotgun)

    clear()
    if player1.wins > player2.wins:
        print(f'{player1.name} wins with a score of {player1.wins} to {player2.wins}')
    elif player2.wins > player1.wins:
        print(f'{player2.name} wins with a score of {player2.wins} to {player1.wins}')
    s(5)
    clear()
    print("end")
    s(2)
    print("engage again?")
    s(2)
    ans = input("yes/no")
    if ans == "yes":
        main()
    else:
        exit()

if __name__ == "__main__":
    main()