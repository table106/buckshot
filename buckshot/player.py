from time import sleep
from random import randint as r

from system import clear

from items import *

from shotgun import *

class Player:
    def __init__(self, num: int, name: str, lives: int):
        self.num = num
        if name != None:
            self.name = name
        else:
            self.name = f"plr{self.num}"
        self.lives = lives
        self.wins = 0
        self.lifeCap = lives
        self.opponents = []
    
    def __str__(self) -> str:
        if self.lives > 1:
            return f"{self.name}'s turn\nyou have {self.lives} lives"
        return f"{self.name}'s turn\nyou have 1 life"
    
    def addOpponent(self, *opponents) -> None:
        for op in opponents:
            self.opponents.append(op)

    def takeDmg(self, dmg: int=1) -> None:
        self.lives -= dmg
    
    def turn(self, shotgun: Shotgun) -> None:
        print(self)
        ans = input("type to use:\nshotgun - shoot\n>")
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
                        if len(self.opponents) > 1:
                            ans = input(f"who will you shoot?\n{', '.join([plr.name for plr in self.opponents])}\n>")
                            sleep(4)
                            if shotgun.content[0] == "live":
                                print("BANG")
                                shotgun.shoot()
                                for op in self.opponents:
                                    if op.name == ans:
                                        op.takeDmg(1)
                            elif shotgun.content[0] == "blank":
                                print("*click")
                                shotgun.shoot()
                        else:
                            sleep(4)
                            if shotgun.content[0] == "live":
                                print("BANG")
                                shotgun.shoot()
                                self.opponents[0].takeDmg(1)
                            elif shotgun.content[0] == "blank":
                                print("*click")
                                shotgun.shoot()
                    case _:
                        print("failed to pick the target")
            case _:
                print("failed to pick an action")
        sleep(2)
        clear()

allitems = ["beer", "knife", "magnifying glass", "cigarette", "cuffs"]

class Player_R2(Player):
    def __init__(self, num: int, name: str, lives: int):
        super().__init__(num, name, lives)
        self.inv = []
        self.cuffed = 0
    
    def __str__(self) -> str:
        return super().__str__()+f"\nyour items: {', '.join([item for item in self.inv])}"

    def heal(self) -> None:
        self.lives += 1

    def getItem(self, cnt: int) -> None:
        for i in range(cnt):
            id1 = r(0,4)
            id2 = r(0,4)
            self.inv.append(allitems[id1])
            self.inv.append(allitems[id2])
            print(f"{self.name} got {allitems[id1]}, and {allitems[id2]}.")
            sleep(2)

    def useItem(self, item: str, * , shotgun: Shotgun=None, target: object=None) -> None:
        match(item):
            case "beer":
                useBeer(self, shotgun)
            case "knife":
                useKnife(self, shotgun)
            case "magnifying glass":
                useGlass(self, shotgun)
            case "cigarette":
                useCigarette(self)
            case "cuffs":
                useCuffs(self, target)
            case _:
                print("failed to use a valid item")

    def _cycleCuffs(self) -> None:
        if self.cuffed == 1:
            self.cuffed += 1
            print(f"{self.name} is cuffed")
        elif self.cuffed == 2:
            print(f"{self.name} broke free from cuffs")
            self.cuffed = 0
    
    def turn(self, shotgun: Shotgun) -> None:
        self._cycleCuffs()
        if self.cuffed:
            sleep(2)
            return
        else:
            sleep(2)
            clear()
            pass
        print(self)
        ans = input("say to use:\nshotgun - shoot\nitem - item\n>")
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
                        if len(self.opponents) > 1:
                            ans = input(f"who will you shoot?\n{', '.join([plr.name for plr in self.opponents])}\n>")
                            sleep(4)
                            if shotgun.content[0] == "live":
                                print("BANG")
                                shotgun.shoot()
                                for op in self.opponents:
                                    if op.name == ans:
                                        op.takeDmg(1)
                            elif shotgun.content[0] == "blank":
                                print("*click")
                                shotgun.shoot()
                        else:
                            sleep(4)
                            if shotgun.content[0] == "live":
                                print("BANG")
                                shotgun.shoot()
                                self.opponents[0].takeDmg(1)
                            elif shotgun.content[0] == "blank":
                                print("*click")
                                shotgun.shoot()
                    case _:
                        print("failed to pick target")
            case "item":
                ans = input(f"pick an item. {', '.join([item for item in self.inv])}\n>")
                if ans == "cuffs":
                    ans = input(f"who are you using them on?\n{', '.join([plr.name for plr in self.opponents])}\n>")
                    for op in self.opponents:
                        if op.name == ans:
                            useCuffs(self, op)
                else:
                    self.useItem(ans, shotgun=shotgun, target=self.opponents[0])
            case _:
                print("failed to pick an action")
        sleep(2)
        clear()

class Player_R3(Player_R2):
    def __init__(self, num: int, name: str, lives: int):
        super().__init__(num, name, lives)
        self.lifeLocked = False
        
    def __str__(self) -> str:
        if self.lifeLocked == True:
            return f"{self.name}'s turn\nyou have # lives\nyour items: {', '.join([item for item in self.inv])}"
        return f"{self.name}'s turn\nyou have {self.lives} lives\nyour items: {', '.join([item for item in self.inv])}"

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")