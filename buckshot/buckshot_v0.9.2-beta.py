from time import sleep

threeplayers_pass="actuallytheres3"

from system import *

from player import *

from shotgun import *

from items import *

from rounds import *

def main() -> None:
    clear()
    print("well hello there! welcome to...")
    sleep(3)
    print("=======================")
    print("|| BUCKSHOT ROULETTE ||")
    print("|| (console version) ||")
    print("=======================")
    print("version v0.9.2-beta\n")
    print("press enter to start")
    ans = input("or type 'how' for a how-to-play\n>")
    shotgun: Shotgun = Shotgun()
    clear()
    if ans == "how":
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
    
    elif ans == threeplayers_pass:
        player1: Player = Player(1, input("what does player 1 call themselves?\n>"), 2)
        player2: Player = Player(2, input("what about player 2?\n>"), 2)

        while not checkNames(player2.name, player1.name):
            player2: Player = Player(2, input("pick another name\n>"), 2)
        
        player3: Player = Player(3, input("and player 3? "), 2)

        while not checkNames(player3.name, player1.name, player2.name):
            player3: Player = Player(3, input("pick another name\n>"), 2)
        
        initOpponents(player1, player2, player3)

        print("good luck.")
        sleep(3)

        round_3P(shotgun, player1, player2, player3, roundNo=1)

        print("all of you can now have items. (max 8)")
        sleep(3)

        player1: Player_R2 = Player_R2(1, player1.name, 4)
        player2: Player_R2 = Player_R2(2, player2.name, 4)
        player3: Player_R2 = Player_R2(3, player3.name, 4)
        initOpponents(player1, player2, player3)
        shotgun.empty()
        handoutItems(1, player1, player2, player3)

        round_3P(shotgun, player1, player2, player3, roundNo=2)

        clear()
        print("let's make this a little bit more interesting.")
        sleep(2)
        print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
        sleep(4)

        player1: Player_R3 = Player_R3(1, player1.name, 6)
        player2: Player_R3 = Player_R3(2, player2.name, 6)
        player3: Player_R3 = Player_R3(3, player3.name, 6)
        initOpponents(player1, player2, player3)
        shotgun.empty()
        handoutItems(2, player1, player2, player3)

        round_3P(shotgun, player1, player2, player3, roundNo=2)

    
    else:
        player1: Player = Player(1, input("what does player 1 call themselves?\n>"), 2)
        player2: Player = Player(2, input("what about player 2?\n>"), 2)
        initOpponents(player1, player2)

        print("good luck.")
        sleep(2)

        round_2P(shotgun, player1, player2, roundNo=1)

        shotgun.empty()
        player1: Player_R2 = Player_R2(1, player1.name, 4)
        player2: Player_R2 = Player_R2(2, player2.name, 4)
        initOpponents(player1, player2)
        handoutItems(1, player1, player2)

        clear()
        print("both of you can now have items. (max 8)")
        sleep(3)

        round_2P(shotgun, player1, player2, roundNo=2)

        clear()
        print("let's make this a little bit more interesting.")
        sleep(2)
        print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
        sleep(5)

        shotgun.empty()
        player1: Player_R3 = Player_R3(1, player1.name, 6)
        player2: Player_R3 = Player_R3(2, player2.name, 6)
        initOpponents(player1, player2)
        handoutItems(2, player1, player2)
        
        round_2P(shotgun, player1, player2, roundNo=3)

        clear()
        if player1.wins > player2.wins:
            print(f'{player1.name} wins with a score of {player1.wins} to {player2.wins}')
        elif player2.wins > player1.wins:
            print(f'{player2.name} wins with a score of {player2.wins} to {player1.wins}')
        sleep(5)
    
    clear()
    print("end")
    sleep(2)
    print("play again?")
    ans = input("y/n")
    if ans == "y":
        main()
    else:
        exit()

if __name__ == "__main__":
    main()