from time import sleep as s
from random import randint as r
from random import shuffle
from os import system
clear = lambda: system("cls")

print("well hello there! welcome to...")
s(3)
print("=====================")
print("||BUCKSHOT ROULETTE||")
print("||   (text version)||")
print("=====================")
input("press enter to start ")
player1name = input("what does player 1 call themselves? ")
player1lives = 2
player1inv = []
player1wins = 0
player2name = input("what about player 2? ")
player2lives = 2
player2inv = []
player2wins = 0
shotgun = []
dmg = 1
player1cuffed = 0
player2cuffed = 0
allitems = ["beer", "knife", "magnifying glass", "cigarette", "cuffs"]

def getitem(wer):
    global allitems
    id1 = r(0,4)
    id2 = r(0,4)
    if wer == 1:
        global player1inv
        global player1name
        player1inv.append(allitems[id1])
        player1inv.append(allitems[id2])
        print(f"{player1name} got {allitems[id1]}, and {allitems[id2]}.")
    elif wer == 2:
        global player2inv
        global player2name
        player2inv.append(allitems[id1])
        player2inv.append(allitems[id2])
        print(f"{player2name} got {allitems[id1]}, and {allitems[id2]}.")

def usebeer():
    print(f"you unloaded a {shotgun[0]} shell.")
    shotgun.pop(0)

def useknife():
    global dmg; dmg = 2
    print("the next shot will deal 2x damage.")

def useglass():
    print(f"the shell in the chamber is a {shotgun[0]} one")

def usecigarette(wer):
    if wer == 1:
        global player1lives
        player1lives += 1
        print("you feel refreshed. +1 life")
    elif wer == 2:
        global player2lives
        player2lives += 1
        print("you feel refreshed. +1 life")

def usecuffs(wer):
    global player1cuffed
    global player2cuffed
    if wer == 1:
        player2cuffed = 1 
    elif wer == 2:
        player1cuffed = 1

def insertshells(live, blank):
    while live:
        shotgun.append("live")
        live -= 1
    while blank:
        shotgun.append("blank")
        blank -= 1
    shuffle(shotgun)

def player2turn():
    global player2lives
    global player1lives
    clear()
    if len(shotgun) == 0 or player1lives == 0:
        return None
    print(f"{player2name}'s turn")
    if player2lives == 1:
        print('you have 1 life')
    else:
        print(f'you have {player2lives} lives')
    ans = input(f"say to use:\nshoot - shotgun\n>")
    if ans == "shoot": # if chose to shoot
        ans = input("shoot self or enemy?\n>")
        if ans == "self": # if chose to shoot self
            s(3)
            if shotgun[0] == "live": # if its a live
                print("BANG")
                shotgun.pop(0)
                s(2)
                player2lives -= 1
            elif shotgun[0] == "blank": # if its a blank
                print("*click")
                shotgun.pop(0)
                s(2)
                player2turn()
        elif ans == "enemy": # if chose to shoot enemy
            s(3)
            if shotgun[0] == "live": # if its a live
                print("BANG")
                shotgun.pop(0)
                s(2)
                player1lives -= 1
            elif shotgun[0] == "blank": # if its a blank
                print("*click")
                shotgun.pop(0)
                s(2)
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
            return None
    else: # if neither
        print("something went wrong. ending current turn")
        s(2)
        return None
    s(2)

print("good luck.")
s(2)

while (player1lives > 0) and (player2lives > 0): # round 1
    liveshells = r(1,4)
    blankshells = r(1,4)
    insertshells(liveshells, blankshells)
    clear()
    print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
    s(5)
    clear()
    while (player1lives > 0) and (player2lives > 0) and (len(shotgun) > 0):
        clear()
        print(f"{player1name}'s turn") # start of player 1's turn
        if player1lives == 1:
            print('you have 1 life left')
        else:
            print(f"you have {player1lives} lives left")
        ans = input("say to use:\nshoot - shotgun\n>")
        if ans == "shoot": # if chose to shoot
            ans = input("shoot self or enemy?\n>")
            if ans == "self": # if chose to shoot self
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player1lives -= 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    if len(shotgun):
                        continue
                    else:
                        break
            elif ans == "enemy": # if chose to shoot enemy
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player2lives -= 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
            else: # if neither
                print("something went wrong. ending current turn")
                s(2)
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
        # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        s(2)
        clear()
        if player1lives == 0 or player2lives == 0 or len(shotgun) == 0:
            break
        print(f"{player2name}'s turn") # start of player 2's turn
        if player2lives == 1:
            print('you have 1 life left')
        else:
            print(f"you have {player2lives} lives left")
        ans = input("say to use:\nshoot - shotgun\n>")
        if ans == "shoot": # if chose to shoot
            ans = input("shoot self or enemy?\n>")
            if ans == "self": # if chose to shoot self
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player2lives -= 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    if len(shotgun):
                        player2turn()
                    else:
                        break
            elif ans == "enemy": # if chose to shoot enemy
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player1lives -= 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
            else: # if neither
                print("something went wrong. ending current turn")
                s(2)
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
        # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        s(2)
        clear()
      
if player1lives == 0:
    print(f"{player2name} wins. end of round 1")
    player2wins += 1
elif player2lives == 0:
    print(f"{player1name} wins. end of round 1")
    player1wins += 1
s(5)

def player2turn():
    global player2lives
    global player1lives
    global dmg
    clear()
    if len(shotgun) == 0 or player1lives == 0:
        return None
    print(f"{player2name}'s turn")
    if player2lives == 1:
        print('you have 1 life left')
    else:
        print(f"you have {player2lives} lives left")
    ans = input(f"say to use:\nshoot - shotgun\nitem - item\nyour items: {player2inv}\n>")
    if ans == "shoot": # if chose to shoot
        ans = input("shoot self or enemy?\n>")
        if ans == "self": # if chose to shoot self
            s(3)
            if shotgun[0] == "live": # if its a live
                print("BANG")
                shotgun.pop(0)
                s(2)
                player2lives -= dmg
                dmg = 1
            elif shotgun[0] == "blank": # if its a blank
                print("*click")
                shotgun.pop(0)
                s(2)
                player2turn()
        elif ans == "enemy": # if chose to shoot enemy
            s(3)
            if shotgun[0] == "live": # if its a live
                print("BANG")
                shotgun.pop(0)
                s(2)
                player1lives -= dmg
                dmg = 1
            elif shotgun[0] == "blank": # if its a blank
                print("*click")
                shotgun.pop(0)
                s(2)
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
            return None
    elif ans == "item":
        ans = input(f"say items name to use it. your items: {player2inv} ")
        if (ans == "beer") and ("beer" in player2inv):
            usebeer()
            player2inv.remove("beer")
            s(2)
            player2turn()
        elif (ans == "knife") and ("knife" in player2inv):
            useknife()
            player2inv.remove("knife")
            s(2)
            player2turn()
        elif (ans == "magnifying glass") and ("magnifying glass" in player2inv):
            useglass()
            player2inv.remove("magnifying glass")
            s(2)
            player2turn()
        elif (ans == "cigarette") and ("cigarette" in player2inv):
            usecigarette(2)
            player2inv.remove("cigarette")
            s(2)
            player2turn()
        elif (ans == "cuffs") and ("cuffs" in player2inv):
            usecuffs(2)
            player2inv.remove("cuffs")
            s(2)
            player2turn()
    else: # if neither
        print("something went wrong. ending current turn")
        s(2)
        return None
    s(2)

player1lives = 4
player1inv = []
player2lives = 4
player2inv = []
shotgun = []
clear()
print("both of you can now have items. (max 8)")
s(3)

while (player1lives > 0) and (player2lives > 0): # round 2
    getitem(1)
    s(2)
    getitem(2)
    s(2)
    liveshells = r(1,4)
    blankshells = r(1,4)
    insertshells(liveshells, blankshells)
    clear()
    print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
    s(5)
    clear()
    while (player1lives > 0) and (player2lives > 0) and (len(shotgun) > 0):
        clear()
        if player1cuffed == 2:
            print(f"{player1name} broke free from cuffs.")
            player1cuffed = 0
            s(2)
        elif player1cuffed == 1:
            print(f"{player1name} is cuffed.")
            player1cuffed += 1
            s(2)
            player2turn()
        print(f"{player1name}'s turn") # start of player 1's turn
        if player1lives == 1:
            print('you have 1 life left')
        else:
            print(f"you have {player1lives} lives left")
        ans = input(f"say to use:\nshoot - shotgun\nitem - item\n{player1name}s items: {player1inv}\n>")
        if ans == "shoot": # if chose to shoot
            ans = input("shoot self or enemy?\n>")
            if ans == "self": # if chose to shoot self
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player1lives -= dmg
                    dmg = 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
                    if len(shotgun):
                        continue
                    else:
                        break
            elif ans == "enemy": # if chose to shoot enemy
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player2lives -= dmg
                    dmg = 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
            else: # if neither
                print("something went wrong. ending current turn")
                continue
        elif ans == "item":
            ans = input(f"say items name to use it. your items: {player1inv} ")
            if (ans == "beer") and ("beer" in player1inv):
                usebeer()
                player1inv.remove("beer")
                s(2)
                continue
            elif (ans == "knife") and ("knife" in player1inv):
                useknife()
                player1inv.remove("knife")
                s(2)
                continue
            elif (ans == "magnifying glass") and ("magnifying glass" in player1inv):
                useglass()
                player1inv.remove("magnifying glass")
                s(2)
                continue
            elif (ans == "cigarette") and ("cigarette" in player1inv):
                usecigarette(1)
                player1inv.remove("cigarette")
                s(2)
                continue
            elif (ans == "cuffs") and ("cuffs" in player1inv):
                usecuffs(1)
                player1inv.remove("cuffs")
                s(2)
                continue
            else:
                print("something went wrong. ending current turn")
                s(2)
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        s(2)
        clear()
        if player1lives == 0 or player2lives == 0 or len(shotgun) == 0:
            break
        if player2cuffed == 2:
            print(f"{player2name} broke free from cuffs.")
            player2cuffed = 0
            s(2)
        elif player2cuffed == 1:
            print(f"{player2name} is cuffed.")
            player2cuffed += 1
            s(2)
            continue
        print(f"{player2name}'s turn") # start of player 2's turn
        if player2lives == 1:
            print('you have 1 life left')
        else:
            print(f"you have {player2lives} lives left")
        ans = input(f"say to use:\nshoot - shotgun\nitem - item\nyour items: {player2inv}\n>")
        if ans == "shoot": # if chose to shoot
            ans = input("shoot self or enemy?\n>")
            if ans == "self": # if chose to shoot self
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player2lives -= dmg
                    dmg = 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
                    if len(shotgun):
                        player2turn(player1lives,player2lives)
                    else:
                        break
            elif ans == "enemy": # if chose to shoot enemy
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player1lives -= dmg
                    dmg = 1
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
            else: # if neither
                print("something went wrong. ending current turn")
                s(2)
                continue
        elif ans == "item":
            ans = input(f"say items name to use it. your items: {player2inv} ")
            if (ans == "beer") and ("beer" in player2inv):
                usebeer()
                player2inv.remove("beer")
                s(2)
                player2turn()
            elif (ans == "knife") and ("knife" in player2inv):
                useknife()
                player2inv.remove("knife")
                s(2)
                player2turn()
            elif (ans == "magnifying glass") and ("magnifying glass" in player2inv):
                useglass()
                player2inv.remove("magnifying glass")
                s(2)
                player2turn()
            elif (ans == "cigarette") and ("cigarette" in player2inv):
                usecigarette(2)
                player2inv.remove("cigarette")
                s(2)
                player2turn()
            elif (ans == "cuffs") and ("cuffs" in player2inv):
                usecuffs(2)
                player2inv.remove("cuffs")
                s(2)
                player2turn()
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            continue
        s(2)
        clear()
    clear()

if player1lives == 0:
    print(f"{player2name} wins. end of round 2")
    player2wins += 1
elif player2lives == 0:
    print(f"{player1name} wins. end of round 2")
    player1wins += 1
s(5)

clear()
print("lets make this a little bit more interesting.")
s(2)
print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
s(5)
player1lives = 6
player1inv = []
player2lives = 6
player2inv = []
shotgun = []

def player2turn():
    global player2lives
    global player1lives
    global dmg
    clear()
    if len(shotgun) == 0 or player1lives == 0:
        return None
    print(f"{player2name}'s turn")
    if player2lives == 0.5:
        print("you have # lives left")
    else:
        print(f"you have {player2lives} lives left")
    ans = input(f"say to use:\nshoot - shotgun\nitem - item\nyour items: {player2inv}\n>")
    if ans == "shoot": # if chose to shoot
        ans = input("shoot self or enemy?\n>")
        if ans == "self": # if chose to shoot self
            s(3)
            if shotgun[0] == "live": # if its a live
                print("BANG")
                shotgun.pop(0)
                s(2)
                mylives -= dmg
                dmg = 1
                if mylives <= 2:
                    mylives = 0.5
            elif shotgun[0] == "blank": # if its a blank
                print("*click")
                shotgun.pop(0)
                s(2)
                player2turn()
        elif ans == "enemy": # if chose to shoot enemy
            s(3)
            if shotgun[0] == "live": # if its a live
                print("BANG")
                shotgun.pop(0)
                s(2)
                theirlives -= dmg
                dmg = 1
                if theirlives <= 2:
                    theirlives = 0.5
            elif shotgun[0] == "blank": # if its a blank
                print("*click")
                shotgun.pop(0)
                s(2)
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
            return None
    elif ans == "item":
        ans = input(f"say items name to use it. your items: {player2inv} ")
        if (ans == "beer") and ("beer" in player2inv):
            usebeer()
            player2inv.remove("beer")
            s(2)
            player2turn()
        elif (ans == "knife") and ("knife" in player2inv):
            useknife()
            player2inv.remove("knife")
            s(2)
            player2turn()
        elif (ans == "magnifying glass") and ("magnifying glass" in player2inv):
            useglass()
            player2inv.remove("magnifying glass")
            s(2)
            player2turn()
        elif (ans == "cigarette") and ("cigarette" in player2inv):
            if player2lives == 0.5:
                print("::LIFE_ADD FAIL")
            else:
                usecigarette(2)
            player2inv.remove("cigarette")
            s(2)
            player2turn()
        elif (ans == "cuffs") and ("cuffs" in player2inv):
            usecuffs(2)
            player2inv.remove("cuffs")
            s(2)
            player2turn()
    else: # if neither
        print("something went wrong. ending current turn")
        s(2)
        return None
    player2lives = mylives
    player1lives = theirlives
    s(2)

clear()
while (player1lives > 0) and (player2lives > 0): # round 3
    getitem(1)
    s(1)
    getitem(1)
    s(2)
    getitem(2)
    s(1)
    getitem(2)
    s(2)
    while len(player1inv) > 8:
        player1inv.pop()
    while len(player2inv) > 8:
        player2inv.pop()
    liveshells = r(1,4)
    blankshells = r(1,4)
    insertshells(liveshells, blankshells)
    clear()
    print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
    s(5)
    clear()
    while (player1lives > 0) and (player2lives > 0) and (len(shotgun) > 0): 
        clear()
        if player1cuffed == 2:
            print(f"{player1name} broke free from cuffs.")
            player1cuffed = 0
            s(2)
        elif player1cuffed == 1:
            print(f"{player1name} is cuffed.")
            player1cuffed += 1
            s(2)
            player2turn()
        clear()
        print(f"{player1name}'s turn") # start of player 1's turn
        if player1lives == 0.5:
            print("you have # lives left")
        else:
            print(f"you have {player1lives} lives left")
        ans = input(f"say to use:\nshoot - shotgun\nitem - item\n{player1name}s items: {player1inv}\n>")
        if ans == "shoot": # if chose to shoot
            ans = input("shoot self or enemy?\n>")
            if ans == "self": # if chose to shoot self
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player1lives -= dmg
                    dmg = 1
                    if player1lives <= 2:
                        player1lives = 0.5
                        print(f"{player1name}'s life support has been cut")
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
                    if len(shotgun):
                        continue
                    else:
                        break
            elif ans == "enemy": # if chose to shoot enemy
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player2lives -= dmg
                    dmg = 1
                    if player2lives <= 2:
                        player2lives = 0.5
                        print(f"{player2name}'s life support has been cut")
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
            else: # if neither
                print("something went wrong. ending current turn")
                continue
        elif ans == "item":
            ans = input(f"say items name to use it. your items: {player1inv}\n>")
            if (ans == "beer") and ("beer" in player1inv):
                usebeer()
                player1inv.remove("beer")
                s(2)
                continue
            elif (ans == "knife") and ("knife" in player1inv):
                useknife()
                player1inv.remove("knife")
                s(2)
                continue
            elif (ans == "magnifying glass") and ("magnifying glass" in player1inv):
                useglass()
                player1inv.remove("magnifying glass")
                s(2)
                continue
            elif (ans == "cigarette") and ("cigarette" in player1inv):
                if player1lives == 0.5:
                    print("::LIFE_ADD FAIL")
                else:
                    usecigarette(1)
                player1inv.remove("cigarette")
                s(2)
                continue
            elif (ans == "cuffs") and ("cuffs" in player1inv):
                usecuffs(1)
                player1inv.remove("cuffs")
                s(2)
                continue
            else:
                print("something went wrong. ending current turn")
                s(2)
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        s(2)
        clear()
        if player1lives == 0 or player2lives == 0 or len(shotgun) == 0:
            break
        if player2cuffed == 2:
            print(f"{player2name} broke free from cuffs.")
            player2cuffed = 0
            s(2)
        elif player2cuffed == 1:
            print(f"{player2name} is cuffed.")
            player2cuffed += 1
            s(2)
            continue
        clear()
        print(f"{player2name}'s turn") # start of player 2's turn
        if player2lives == 0.5:
            print("you have # lives left")
        else:
            print(f"you have {player2lives} lives left")
        ans = input(f"say to use:\nshoot - shotgun\nitem - item\nyour items: {player2inv}\n>")
        if ans == "shoot": # if chose to shoot
            ans = input("shoot self or enemy?\n>")
            if ans == "self": # if chose to shoot self
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player2lives -= dmg
                    dmg = 1
                    if player2lives <= 2:
                        player2lives = 0.5
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
                    if len(shotgun):
                        player2turn(player1lives,player2lives)
                    else:
                        break
            elif ans == "enemy": # if chose to shoot enemy
                s(3)
                if shotgun[0] == "live": # if its a live
                    print("BANG")
                    shotgun.pop(0)
                    s(2)
                    player1lives -= dmg
                    dmg = 1
                    if player1lives <= 2:
                        player1lives = 0.5
                elif shotgun[0] == "blank": # if its a blank
                    print("*click")
                    shotgun.pop(0)
                    s(2)
                    dmg = 1
            else: # if neither
                print("something went wrong. ending current turn")
                s(2)
                continue
        elif ans == "item":
            ans = input(f"say items name to use it. your items: {player2inv}\n>")
            if (ans == "beer") and ("beer" in player2inv):
                usebeer()
                player2inv.remove("beer")
                s(2)
                player2turn()
            elif (ans == "knife") and ("knife" in player2inv):
                useknife()
                player2inv.remove("knife")
                s(2)
                player2turn()
            elif (ans == "magnifying glass") and ("magnifying glass" in player2inv):
                useglass()
                player2inv.remove("magnifying glass")
                s(2)
                player2turn()
            elif (ans == "cigarette") and ("cigarette" in player2inv):
                if player2lives == 0.5:
                    print("::LIFE_ADD FAIL")
                else:
                    usecigarette(2)
                player2inv.remove("cigarette")
                s(2)
                player2turn()
            elif (ans == "cuffs") and ("cuffs" in player2inv):
                usecuffs(2)
                player2inv.remove("cuffs")
                s(2)
                player2turn()
            else: # if neither
                print("something went wrong. ending current turn")
                s(2)
                continue
        else: # if neither
            print("something went wrong. ending current turn")
            s(2)
            # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
            continue
        s(2)
        clear()
    clear()

if player1lives == 0:
    print(f"{player2name} wins.")
    player2wins += 1
elif player2lives == 0:
    print(f"{player1name} wins.")
    player1wins += 1
s(5)

clear()
if player1wins > player2wins:
    print(f'{player1name} wins with a score of {player1wins} to {player2wins}')
elif player2wins == player1wins:
    print('no one wins')
elif player2wins > player1wins:
    print(f'{player2name} wins with a score of {player2wins} to {player1wins}')
s(5)
clear()
print('and this is it!')
s(2)
print('hope you enjoyed this thing')
s(2)
print('love and kisses, table106') # if youre contributing, add yourself here!
s(2) # also might want to change the time before end of program
exit()
