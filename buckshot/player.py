from system import clear
from time import sleep
from random import randint as r
from log import *

from items import *

from shotgun import Shotgun

class Player:
    def __init__(self, num: int, name: str, lives: int, lifeCap: int):
        self.num = num
        self.name = name
        self.lives = lives
        self.wins = 0
        self.otherDmg = False
        self.lifeCap = lifeCap
        self.opponent = None

    def __str__(self):
        if self.lives > 1:
            return f"{self.name}'s turn\nyou have {self.lives} lives"
        return f"{self.name}'s turn\nyou have 1 life"
    
    def addOpponent(self, opponent: object):
        self.opponent = opponent

    def takeDmg(self, viel: int=None):
        if viel == None:
            viel = 1
        self.lives -= viel
    
    def turn(self, shotgun: Shotgun):
        print(self)
        ans = input("say to use:\nshotgun - shoot\n>")
        match (ans):
            case "shoot":
                ans = input("shoot self or enemy?\n>")
                match (ans):
                    case "self":
                        sleep(4)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg()
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            sleep(2)
                            clear()
                            if len(shotgun.content) != 0:
                                self.turn(shotgun)
                    case "enemy":
                        sleep(4)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.otherDmg = True
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                    case default:
                        print("failed to pick the target")
                        info(f"player {self.num} failed to pick a target")
            case default:
                print("failed to pick an action")
                info(f"player {self.num} failed to pick an action")
        sleep(2)
        clear()

allitems = ["beer", "knife", "magnifying glass", "cigarette", "cuffs"]

class Player_R2(Player):
    def __init__(self, num: int, name: str, lives: int, lifeCap: int):
        super().__init__(num, name, lives, lifeCap)
        self.inv = []
        self.cuffed = 0


    def __str__(self):
        return super().__str__()+f"\nyour items: {self.inv}"

    def heal(self):
        self.lives += 1

    def getItem(self, viel: int):
        for i in range(viel):
            id1 = r(0,4)
            id2 = r(0,4)
            self.inv.append(allitems[id1])
            self.inv.append(allitems[id2])
            print(f"{self.name} got {allitems[id1]}, and {allitems[id2]}.")
            sleep(2)

    def useItem(self, item: str):
        match(item):
            case "beer":
                useBeer()
            case "knife":
                useKnife()
            case "magnifying glass":
                useGlass()
            case "cigarette":
                useCigarette(self)
            case "cuffs":
                useCuffs(self.opponent)
            case default:
                info(f"player {self.num} failed to pick an item")
    
    def turn(self, shotgun: Shotgun):
        print(self)
        ans = input("say to use:\nshotgun - shoot\nitem - item>")
        match (ans):
            case "shoot":
                ans = input("shoot self or enemy?\n>")
                match (ans):
                    case "self":
                        sleep(4)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg()
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            sleep(2)
                            clear()
                            if len(shotgun.content) != 0:
                                self.turn(shotgun)
                            self.turn(shotgun)
                        else:
                            print("failed checking the shotgun")
                    case "enemy":
                        sleep(4)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.otherdmg = True
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                    case default:
                        print("failed to pick target")
                        info(f"player {self.num} failed to pick a target")
            case "item":
                ans = input(f"pick an item. {self.inv}\n>")
                self.useItem(ans)
            case default:
                print("failed to pick an action")
                info(f"player {self.num} failed to pick an action")
        sleep(2)
        clear()