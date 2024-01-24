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
print("version v0.5-beta\n")
input("press enter to start ")
shotgun = []
dmg = 1
allitems = ["beer", "knife", "magnifying glass", "cigarette", "cuffs"]

def useBeer():
    print(f"you unloaded a {shotgun[0]} shell.")
    try:
        shotgun.pop(0)
    except IndexError:
        print('ATTEMPTED TO UNLOAD EMPTY SHOTGUN')

def useKnife():
    global dmg; dmg = 2
    print("the next shot will deal 2x damage.")

def useGlass():
    print(f"the shell in the chamber is a {shotgun[0]} one")

def useCigarette(wer):
    if wer == 1:
        player1.heal()
    elif wer == 2:
        player2.heal()

def useCuffs(wer):
    if wer == 1:
        player2.cuffed = 1
    elif wer == 2:
        player1.cuffed = 1

otherdmg = False
class Player:
    def __init__(self, num, name, lives):
        self.num = num
        self.name = name
        self.lives = lives
        self.inv = []
        self.wins = 0
        self.cuffed = 0

    def __str__(self):
        if self.lives > 1:
            return f"{self.name}'s turn\nyou have {self.lives} lives"
        return f"{self.name}'s turn\nyou have 1 life"

    def takeDmg(self, viel=1):
        self.lives -= viel

    def heal(self):
        self.lives += 1

    def getItem(self, viel):
        global allitems
        for i in range(viel):
            id1 = r(0,4)
            id2 = r(0,4)
            self.inv.append(allitems[id1])
            self.inv.append(allitems[id2])
            print(f"{self.name} got {allitems[id1]}, and {allitems[id2]}.")
            s(2)

    # def useItem(self, item):
    #     match(item):
    #         case "beer":
    #             useBeer()
    #             break
    #         case "knife":
    #             useKnife()
    #             break
    #         case "magnifying glass":
    #             useGlass()
    #             break
    #         case "cigarette":
    #             useCigarette(self.num)
    #             break
    #         case "cuffs":
    #             useCuffs(self.num)
    #             break
    
    def turn(self):
        print(self)
        ans = input("say to use:\nshotgun - shoot\n>")
        match (ans):
            case "shoot":
                global shotgun
                global otherdmg
                ans = input("shoot self or enemy?\n>")
                match (ans):
                    case "self":
                        s(5)
                        if shotgun[0] == "live":
                            print("BANG")
                            shotgun.pop(0)
                            self.takeDmg()
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.pop(0)
                            self.turn()
                        else:
                            print("failed checking the shotgun")
                    case "enemy":
                        s(5)
                        if shotgun[0] == "live":
                            print("BANG")
                            shotgun.pop(0)
                            otherdmg = True
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.pop(0)
                        else:
                            print("failed checking the shotgun")
                    case default:
                        print("failed to pick the target")
            case default:
                print("failed to pick an action")
        s(2)
        clear()
                            
def insertshells(live, blank):
    for i in range(live):
        shotgun.append("live")
    for i in range(blank):
        shotgun.append("blank")
    shuffle(shotgun)

player1 = Player(1,input("what does player 1 call themselves? "),2)
player2 = Player(2,input("what about player 2? "),2)

print("good luck.")
s(2)

while (player1.lives > 0) and (player2.lives > 0): # round 1
    liveshells = r(1,4)
    blankshells = r(1,4)
    insertshells(liveshells, blankshells)
    clear()
    print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
    s(5)
    clear()
    while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun) > 0):
        clear()
        player1.turn()
        if otherdmg == True:
            player2.takeDmg()
            otherdmg = False
        # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        clear()
        if player1.lives == 0 or player2.lives == 0 or len(shotgun) == 0:
            break
        player2.turn()
        if otherdmg == True:
            player1.takeDmg()
            otherdmg = False
        # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        clear()
      
if player1.lives == 0:
    print(f"{player2.name} wins.",end=" ")
    player2.wins += 1
elif player2.lives == 0:
    print(f"{player1.name} wins.",end=" ")
    player1.wins += 1
print("end of round 1.")
s(5)

class Player:
    def __init__(self, num, name, lives):
        self.num = num
        self.name = name
        self.lives = lives
        self.inv = []
        self.wins = 0
        self.cuffed = 0

    def __str__(self):
        if self.lives > 1:
            return f"{self.name}'s turn\nyou have {self.lives} lives"
        return f"{self.name}'s turn\nyou have 1 life"

    def takeDmg(self, viel=1):
        self.lives -= viel

    def heal(self):
        self.lives += 1

    def getItem(self, viel):
        global allitems
        for i in range(viel):
            id1 = r(0,4)
            id2 = r(0,4)
            self.inv.append(allitems[id1])
            self.inv.append(allitems[id2])
            print(f"{self.name} got {allitems[id1]}, and {allitems[id2]}.")
            s(2)

    def useItem(self, item):
        match(item):
            case "beer":
                self.useBeer()
            case "knife":
                self.useKnife()
            case "magnifying glass":
                self.useGlass()
            case "cigarette":
                self.useCigarette(self.num)
            case "cuffs":
                self.useCuffs(self.num)
            case default:
                print("failed to pick item")
    
    def turn(self):
        print(self)
        ans = input("say to use:\nshotgun - shoot\n>")
        match (ans):
            case "shoot":
                global otherdmg
                global shotgun
                ans = input("shoot self or enemy?\n>")
                match (ans):
                    case "self":
                        s(5)
                        if shotgun[0] == "live":
                            print("BANG")
                            shotgun.pop(0)
                            self.takeDmg()
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.pop(0)
                            self.turn()
                        else:
                            print("failed checking the shotgun")
                    case "enemy":
                        s(5)
                        if shotgun[0] == "live":
                            print("BANG")
                            shotgun.pop(0)
                            otherdmg = True
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.pop(0)
                        else:
                            print("failed checking the shotgun")
                    case default:
                        print(f"failed to pick target")
            case "item":
                ans = input(f"pick an item. {self.inv}\n>")
                self.useItem(ans)
            case default:
                print("failed to pick an action as player")
        s(2)
        clear()

shotgun = []
player1 = Player(1,player1.name,4)
player2 = Player(2,player2.name,4)
clear()
print("both of you can now have items. (max 8)")
s(3)

while (player1.lives > 0) and (player2.lives > 0): # round 2
    player1.getitem(2)
    s(2)
    player2.getitem(2)
    s(2)
    liveshells = r(1,4)
    blankshells = r(1,4)
    insertshells(liveshells, blankshells)
    clear()
    print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
    s(5)
    clear()
    while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun) > 0):
        clear()
        if player1.cuffed == 2:
            print(f"{player1.name} broke free from cuffs.")
            player1.cuffed = 0
            s(2)
        elif player1.cuffed == 1:
            print(f"{player1.name} is cuffed.")
            player1.cuffed += 1
            s(2)
            player2.turn()
            continue
        clear()
        player1.turn()
        if otherdmg == True:
            player2.takeDmg(dmg)
            otherdmg = False
        # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        clear()
        if player1.lives == 0 or player2.lives == 0 or len(shotgun) == 0:
            break
        if player2.cuffed == 2:
            print(f"{player2.name} broke free from cuffs.")
            player2.cuffed = 0
        elif player2.cuffed == 1:
            print(f"{player2.name} is cuffed.")
            player2.cuffed += 1
            s(2)
            continue
        clear()
        player2.turn()
        if otherdmg == True:
            player1.takeDmg(dmg)
            otherdmg = False
        # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        clear()
    clear()

if player1.lives == 0:
    print(f"{player2.name} wins. end of round 2")
    player2.wins += 1
elif player2.lives == 0:
    print(f"{player1.name} wins. end of round 2")
    player1.wins += 1
s(5)

clear()
print("lets make this a little bit more interesting.")
s(2)
print("now, when you reach less than 3 lives, your defibrillator will be cut.\nthe life display will glitch when that happens")
s(5)
shotgun = []
player1 = Player(1,player1.name,6)
player2 = Player(2,player2.name,6)
clear()
while (player1.lives > 0) and (player2.lives > 0): # round 3
    player1.getItem(4)
    s(2)
    player2.getItem(4)
    s(2)
    while len(player1.inv) > 8:
        player1.inv.pop()
    while len(player2.inv) > 8:
        player2.inv.pop()
    liveshells = r(1,4)
    blankshells = r(1,4)
    insertshells(liveshells, blankshells)
    clear()
    print(f"LOADED SHELLS: {liveshells} LIVE AND {blankshells} BLANK")
    s(5)
    clear()
    while (player1.lives > 0) and (player2.lives > 0) and (len(shotgun) > 0): 
        clear()
        if player1.cuffed == 2:
            print(f"{player1.name} broke free from cuffs.")
            player1.cuffed = 0
            s(2)
        elif player1.cuffed == 1:
            print(f"{player1.name} is cuffed.")
            player1.cuffed += 1
            s(2)
            player2.turn()
            continue
        clear()
        player1.turn()
        if otherdmg == True:
            player2.takeDmg(dmg)
            otherdmg = False
        clear()
        # print(player1lives, player2lives, shotgun, player1cuffed, player2cuffed)
        s(2)
        clear()
        if player1.lives == 0 or player2.lives == 0 or len(shotgun) == 0:
            break
        if player2.cuffed == 2:
            print(f"{player2.name} broke free from cuffs.")
            player2.cuffed = 0
        elif player2.cuffed == 1:
            print(f"{player2.name} is cuffed.")
            player2.cuffed += 1
            s(2)
            continue
        clear()
        player2.turn()
        if otherdmg == True:
            player1.takeDmg(dmg)
            otherdmg = False
        s(2)
        clear()
    clear()

if player1.lives == 0:
    print(f"{player2.name} wins.")
    player2.wins += 1
elif player2.lives == 0:
    print(f"{player1.name} wins.")
    player1.wins += 1
s(5)

clear()
if player1.wins > player2.wins:
    print(f'{player1.name} wins with a score of {player1.wins} to {player2.wins}')
elif player2.wins > player1.wins:
    print(f'{player2.name} wins with a score of {player2.wins} to {player1.wins}')
s(5)
clear()
print('and this is it!')
s(2)
print('hope you enjoyed this thing')
s(2)
print('love and kisses, table106') # if youre contributing, add yourself here!
s(2) # also might want to change the time before end of program
exit()
