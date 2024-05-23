from time import sleep
from os import path

threeplayers_pass="actuallytheres3"
testmode_pass="test time"

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
    print(f"version {path.basename(__file__)[9:-3]}\n")
    print("press enter to start")
    print("or type 'how' for a how-to-play")
    ans = input("you can also check out the credits with 'credits'\n>")
    shotgun: Shotgun = Shotgun()
    clear()
    if ans == "how":
        print("alright, so\
              \nthere's a shotgun\
              \nevery time it is empty we load some shells in\
              \nthey can be blank, or live, and will be in a random sequence\
              \nyou only get the numbers though!\
              \nevery turn, you use the shotgun\
              \nyou point it either at yourself, or a rival\
              \nif you shoot yourself with a blank you get to go again!\
              \n\nITEMS (from round 2 onwards)\
              \n-beer:\
              \nyou eject a round from the shotgun, if its the last one we reload it\
              \n\n-knife:\
              \nyou saw the barrel of the shotgun, making the next shot deal 2 damage (the barrel regenerates after)\
              \n\n-magnifying glass:\
              \nyou look into the chamber, revealing the shell inside\
              \n\n-cigarette:\
              \nyou regain a life (smoking is bad kids dont do it)\
              \n\n-cuffs:\
              \nyou cuff a rival skipping their next turn\
              \n\nALSO: you can type \'..\' at (almost) any time to go to the previous screen\n")
        
        ans = input("when you finish reading, just press enter\n>")

    elif ans == "credits":
        print("THE HALL OF SHAME I MEAN FAME\
              \nfor those that for some reason contributed\
              \n\ntable106 (me!) - programming, literally almost everything\
              \nStackOverflow (the website) - saving me from \"wait how do i make x\"\
              \n\nmy friends:\
              \nAridemis - ideas and early game testing\
              \nkt00s - thoughts on my ideas and testing\
              \n\nspecial thanks to my cat for keeping me sane\n")
    
        ans = input("when you finish reading, just press enter\n>")

    elif ans == testmode_pass:
        round, threeP = input("very well, round and 3P please\n>").split(" ")
        if round == "1":
            player1: Player = Player("plr1", 2)
            player2: Player = Player("plr2", 2)
            if threeP == "y":
                player3: Player = Player("plr3", 2)
                initOpponents(player1, player2, player3)
                round_3P(shotgun, player1, player2, player3, roundNo=1)
            else:
                initOpponents(player1, player2)
                round_2P(shotgun, player1, player2, roundNo=1)
        elif round == "2":
            player1: Player_R2 = Player_R2("plr1", 4)
            player2: Player_R2 = Player_R2("plr2", 4)
            if threeP == "y":
                player3: Player_R2 = Player_R2("plr3", 4)
                initOpponents(player1, player2, player3)
                round_3P(shotgun, player1, player2, player3, roundNo=2)
            else:
                initOpponents(player1, player2)
                round_2P(shotgun, player1, player2, roundNo=2)
        elif round == "3":
            player1: Player_R3 = Player_R3("plr1", 6)
            player2: Player_R3 = Player_R3("plr2", 6)
            if threeP == "y":
                player3: Player_R3 = Player_R3("plr3", 6)
                initOpponents(player1, player2, player3)
                handoutItems(2, player1, player2, player3)
                round_3P(shotgun, player1, player2, player3, roundNo=3)
            else:
                initOpponents(player1, player2)
                handoutItems(2, player1, player2)
                round_2P(shotgun, player1, player2, roundNo=3)
        else:
            main()
            exit()
    
    if ans == "..":
        main()
        exit()

    clear()
    if ans == threeplayers_pass:
        player1: Player = Player(input("what does player 1 call themselves?\n>"), 2)

        if not validName(player1.name, tuple()):
            player1: Player = Player("plr1", 2)

        player2: Player = Player(input("what about player 2?\n>"), 2)

        if not validName(player2.name, player1.name):
            player2: Player = Player("plr2", 2)
        
        player3: Player = Player(input("and player 3? "), 2)

        if not validName(player3.name, player1.name, player2.name):
            player3: Player = Player("plr3", 2)
        
        initOpponents(player1, player2, player3)

        print("good luck.")
        sleep(3)

        round_3P(shotgun, player1, player2, player3, roundNo=1)

        print("all of you can now have items. (max 8)")
        sleep(3)

        player1: Player_R2 = Player_R2(player1.name, 4)
        player2: Player_R2 = Player_R2(player2.name, 4)
        player3: Player_R2 = Player_R2(player3.name, 4)

        initOpponents(player1, player2, player3)
        shotgun.empty()
        handoutItems(1, player1, player2, player3)

        round_3P(shotgun, player1, player2, player3, roundNo=2)

        clear()
        print("let's make this a little bit more interesting.")
        sleep(2)
        print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
        sleep(4)

        player1: Player_R3 = Player_R3(player1.name, 6)
        player2: Player_R3 = Player_R3(player2.name, 6)
        player3: Player_R3 = Player_R3(player3.name, 6)

        initOpponents(player1, player2, player3)
        shotgun.empty()
        handoutItems(2, player1, player2, player3)

        round_3P(shotgun, player1, player2, player3, roundNo=3)

    
    else:
        player1: Player = Player(input("what does player 1 call themselves?\n>"), 2)

        if not validName(player1.name, ...):
            player1: Player = Player("plr1", 2)

        player2: Player = Player(input("what about player 2?\n>"), 2)

        if not validName(player2.name, player1.name):
            player2: Player = Player("plr2", 2)
        
        initOpponents(player1, player2)

        print("good luck.")
        sleep(2)

        round_2P(shotgun, player1, player2, roundNo=1)

        shotgun.empty()

        player1: Player_R2 = Player_R2(player1.name, 4)
        player2: Player_R2 = Player_R2(player2.name, 4)

        initOpponents(player1, player2)
        clear()
        print("both of you can now have items. (max 8)")
        sleep(3)
        handoutItems(1, player1, player2)

        round_2P(shotgun, player1, player2, roundNo=2)

        clear()
        print("let's make this a little bit more interesting.")
        sleep(2)
        print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
        sleep(5)

        shotgun.empty()
        
        player1: Player_R3 = Player_R3(player1.name, 6)
        player2: Player_R3 = Player_R3(player2.name, 6)

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