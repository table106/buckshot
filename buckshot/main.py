from time import sleep
from os import environ
from dotenv import load_dotenv, dotenv_values

load_dotenv()

threeplayers_pass=environ["THREE"]
testmode_pass=environ["TEST"]

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
    print("v1.0-pre3\n")
    print("press enter to start")
    print("or type 'how' for a how-to-play")
    ans = query("you can also check out the credits with 'credits'")
    shotgun: Shotgun = Shotgun()
    clear()
    if ans == "how":
        with open("buckshot/guide.txt", "r") as gi:
            for line in gi:
                print(line, end="")
            print()
        
        ans = query("when you finish reading, just press enter")

    elif ans == "credits":
        with open("buckshot/credits.txt", "r") as cr:
            for line in cr:
                print(line, end="")
            print()
    
        ans = query("when you finish reading, just press enter")

    elif ans == testmode_pass:
        round, threeP = query("very well, round and 3P please").split(" ")
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
            player1: Player_R2 = Player_R2("plr1", 4, 0)
            player2: Player_R2 = Player_R2("plr2", 4, 0)
            if threeP == "y":
                player3: Player_R2 = Player_R2("plr3", 4, 0)
                initOpponents(player1, player2, player3)
                round_3P(shotgun, player1, player2, player3, roundNo=2)
            else:
                initOpponents(player1, player2)
                round_2P(shotgun, player1, player2, roundNo=2)
        elif round == "3":
            player1: Player_R3 = Player_R3("plr1", 6, 0)
            player2: Player_R3 = Player_R3("plr2", 6, 0)
            if threeP == "y":
                player3: Player_R3 = Player_R3("plr3", 6, 0)
                initOpponents(player1, player2, player3)
                round_3P(shotgun, player1, player2, player3, roundNo=3)
            else:
                initOpponents(player1, player2)
                round_2P(shotgun, player1, player2, roundNo=3)
        else:
            main()
            exit()
    
    elif ans == "..":
        clear()
        print("oh did i plan for people like you.")
        sleep(2)
        exit()

    clear()
    if ans == threeplayers_pass:
        player1: Player = Player(query("what does player 1 call themselves?"), 2)

        if not validName(player1.name, tuple()):
            player1: Player = Player("Player 1", 2)

        player2: Player = Player(query("what about player 2?"), 2)

        if not validName(player2.name, player1.name):
            player2: Player = Player("Player 2", 2)
        
        player3: Player = Player(query("and player 3?"), 2)

        if not validName(player3.name, player1.name, player2.name):
            player3: Player = Player("Player 3", 2)
        
        initOpponents(player1, player2, player3)

        print("good luck.")
        sleep(3)

        round_3P(shotgun, player1, player2, player3, roundNo=1)

        clear()
        print("all of you can now have items. (max 8)")
        sleep(3)

        player1: Player_R2 = Player_R2(player1.name, 4, player1.wins)
        player2: Player_R2 = Player_R2(player2.name, 4, player2.wins)
        player3: Player_R2 = Player_R2(player3.name, 4, player3.wins)

        initOpponents(player1, player2, player3)
        shotgun.empty()

        round_3P(shotgun, player1, player2, player3, roundNo=2)

        clear()
        print("let's make this a little bit more interesting.")
        sleep(2)
        print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
        sleep(4)

        player1: Player_R3 = Player_R3(player1.name, 6, player1.wins)
        player2: Player_R3 = Player_R3(player2.name, 6, player2.wins)
        player3: Player_R3 = Player_R3(player3.name, 6, player3.wins)

        initOpponents(player1, player2, player3)
        shotgun.empty()

        round_3P(shotgun, player1, player2, player3, roundNo=3)

    
    else:
        player1: Player = Player(query("what does player 1 call themselves?"), 2)

        if not validName(player1.name, tuple()):
            player1: Player = Player("Player 1", 2)

        player2: Player = Player(query("what about player 2?"), 2)

        if not validName(player2.name, player1.name):
            player2: Player = Player("Player 2", 2)
        
        initOpponents(player1, player2)

        print("good luck.")
        sleep(2)

        round_2P(shotgun, player1, player2, roundNo=1)

        shotgun.empty()

        player1: Player_R2 = Player_R2(player1.name, 4, player1.wins)
        player2: Player_R2 = Player_R2(player2.name, 4, player2.wins)

        initOpponents(player1, player2)
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
        
        player1: Player_R3 = Player_R3(player1.name, 6, player1.wins)
        player2: Player_R3 = Player_R3(player2.name, 6, player2.wins)

        initOpponents(player1, player2)
        
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
    ans = query("y/n")
    if ans == "y":
        main()
    else:
        exit()

if __name__ == "__main__":
    main()