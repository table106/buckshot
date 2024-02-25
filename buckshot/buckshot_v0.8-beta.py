from time import sleep as s
from dotenv import load_dotenv
import os

load_dotenv()
testmode_pass=os.environ["TESTMODE_CODE"]
threeplayers_pass=os.environ["3P_CODE"]

from system import *

from player import *

from shotgun import *

from items import *

from rounds import *

def main() -> None:
    clear()
    print("well hello there! welcome to...")
    s(3)
    print("=======================")
    print("|| BUCKSHOT ROULETTE ||")
    print("|| (console version) ||")
    print("=======================")
    print("version v0.8-beta\n")
    print("press enter to start")
    ans = input("or type 'how' for a how-to-play\n>")
    shotgun = Shotgun()
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
    
    elif ans == testmode_pass:
        print("hello world!")
        ans = "1"
        while ans in ["1", "2", "3", "3P"]:
            ans = input("where to?\n>")
            if ans == "1":
                shotgun.empty()
                player1 = Player(1,"plr1",2)
                player2 = Player(2,"plr2",2)
                initOpponents(player1, player2)

                round1(shotgun, False, player1, player2)
            
            elif ans == "2":
                shotgun.empty()
                player1 = Player_R2(1,"plr1",4)
                player2 = Player_R2(2,"plr2",4)
                initOpponents(player1, player2)

                round2(shotgun, False, player1, player2)
            
            elif ans == "3":
                shotgun.empty()
                player1 = Player_R2(1,"plr1",6)
                player2 = Player_R2(2,"plr2",6)
                initOpponents(player1, player2)

                round3(shotgun, False, player1, player2)
            
            elif ans == "3P":
                while ans in ["1", "2", "3"]:
                    print("where to? (3P mode)\n>")
                    if ans == "1":
                        shotgun.empty()
                        player1 = Player(1,"plr1",2)
                        player2 = Player(2,"plr2",2)
                        player3 = Player(3,"plr3",2)
                        initOpponents(player1, player2, player3)

                        round1(shotgun, False, player1, player2, player3)
                    
                    elif ans == "2":
                        shotgun.empty()
                        player1 = Player_R2(1,"plr1",4)
                        player2 = Player_R2(2,"plr2",4)
                        initOpponents(player1, player2, player3)

                        round2(shotgun, False, player1, player2, player3)
                    
                    elif ans == "3":
                        shotgun.empty()
                        player1 = Player_R2(1,"plr1",6)
                        player2 = Player_R2(2,"plr2",6)
                        initOpponents(player1, player2, player3)

                        round2(shotgun, False, player1, player2, player3)
                break
        
        print("ending your testmode session")
        sleep(3)
        exit()
    
    elif ans == threeplayers_pass:
        player1 = Player(1,input("what does player 1 call themselves? "),2)
        player2 = Player(2,input("what about player 2? "),2)

        while not checkNames(player2.name, player1.name):
            player2 = Player(2,input("pick another name "),2)
        
        player3 = Player(3,input("and player 3? "),2)

        while not checkNames(player3.name, player1.name, player2.name):
            player3 = Player(2,input("pick another name "),2)
        
        initOpponents(player1, player2, player3)

        print("good luck.")
        sleep(3)

        round1(shotgun, False, player1, player2, player3)

        print("all of you can now have items. (max 8)")
        s(3)

        player1 = Player_R2(1,player1.name,4)
        player2 = Player_R2(2,player2.name,4)
        player3 = Player_R2(3,player3.name,4)
        initOpponents(player1, player2, player3)
        shotgun.empty()

        player1.getItem(1)
        player2.getItem(1)
        player3.getItem(1)

        round2(shotgun, False, player1, player2, player3)

        clear()
        print("let's make this a little bit more interesting.")
        s(2)
        print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
        s(5)

        player1 = Player_R3(1,player1.name,6)
        player2 = Player_R3(2,player2.name,6)
        player3 = Player_R3(3,player3.name,6)
        initOpponents(player1, player2, player3)
        shotgun.empty()

        player1.getItem(2)
        player2.getItem(2)
        player3.getItem(2)

        round3(shotgun, False, player1, player2, player3)

        print("you have finished 3P mode! exiting in 5")
        s(5)
        exit()
    
    else:
        player1 = Player(1,input("what does player 1 call themselves? "),2)
        player2 = Player(2,input("what about player 2? "),2)
        initOpponents(player1, player2)

        print("good luck.")
        s(2)

        round1(shotgun, False, player1, player2)

        shotgun.empty()
        player1 = Player_R2(1,player1.name,4)
        player2 = Player_R2(2,player2.name,4)
        initOpponents(player1, player2)

        clear()
        print("both of you can now have items. (max 8)")
        s(3)

        round2(shotgun, False, player1, player2)

        clear()
        print("let's make this a little bit more interesting.")
        s(2)
        print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
        s(5)

        shotgun.empty()
        player1 = Player_R3(1,player1.name,6)
        player2 = Player_R3(2,player2.name,6)
        initOpponents(player1, player2)
        
        round3(shotgun, False, player1, player2)

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