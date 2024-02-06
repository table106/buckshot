from system import clear
from time import sleep
from random import randint as r

from items import *

class Player:
    def __init__(self, num, name, lives):
        self.num = num
        self.name = name
        self.lives = lives
        self.wins = 0
        self.otherDmg = False

    def __str__(self):
        if self.lives > 1:
            return f"{self.name}'s turn\nyou have {self.lives} lives"
        return f"{self.name}'s turn\nyou have 1 life"

    def takeDmg(self, viel=1):
        self.lives -= viel
    
    def turn(self, shotgun):
        print(self)
        ans = input("say to use:\nshotgun - shoot\n>")
        match (ans):
            case "shoot":
                ans = input("shoot self or enemy?\n>")
                match (ans):
                    case "self":
                        sleep(5)
                        if shotgun[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg()
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            self.turn()
                        else:
                            print("failed checking the shotgun")
                    case "enemy":
                        sleep(5)
                        if shotgun[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.otherDmg = True
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                        else:
                            print("failed checking the shotgun")
                    case default:
                        print("failed to pick the target")
            case default:
                print("failed to pick an action")
        sleep(2)
        clear()

allitems = ["beer", "knife", "magnifying glass", "cigarette", "cuffs"]

class Player_R2(Player):
    def __init__(self):
        super().__init__(self)
        self.inv = []
        self.cuffed = 0

    def heal(self):
        self.lives += 1

    def getItem(self, viel):
        for i in range(viel):
            id1 = r(0,4)
            id2 = r(0,4)
            self.inv.append(allitems[id1])
            self.inv.append(allitems[id2])
            print(f"{self.name} got {allitems[id1]}, and {allitems[id2]}.")
            sleep(2)

    def useItem(self, item):
        match(item):
            case "beer":
                useBeer()
            case "knife":
                useKnife()
            case "magnifying glass":
                useGlass()
            case "cigarette":
                useCigarette(self.num)
            case "cuffs":
                useCuffs(self.num)
            case default:
                print("failed to pick item")
    
    def turn(self, shotgun):
        print(self)
        ans = input("say to use:\nshotgun - shoot\n>")
        match (ans):
            case "shoot":
                ans = input("shoot self or enemy?\n>")
                match (ans):
                    case "self":
                        sleep(5)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg()
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            self.turn()
                        else:
                            print("failed checking the shotgun")
                    case "enemy":
                        sleep(5)
                        if shotgun[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            otherdmg = True
                        elif shotgun[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                        else:
                            print("failed checking the shotgun")
                    case default:
                        print(f"failed to pick target")
            case "item":
                ans = input(f"pick an item. {self.inv}\n>")
                self.useItem(ans)
            case default:
                print("failed to pick an action as player")
        sleep(2)
        clear()