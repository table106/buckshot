from time import sleep
from random import randint as r

from system import clear
from items import *
from shotgun import *

class Player:
    def __init__(self, name: str, lives: int):
        self.name: str = name
        self.lives: int = lives
        self.wins: int = 0
        self.opponents: list[str] = []
    
    def __str__(self) -> str:
        if self.lives > 1:
            return f"{self.name}'s turn\nyou have {self.lives} lives"
        return f"{self.name}'s turn\nyou have 1 life"
    
    def addOpponents(self, *opponents) -> None:
        for op in opponents:
            self.opponents.append(op)

    def displayOpponents(self) -> str:
        return ", ".join([op.name for op in self.opponents])

    def takeDmg(self, dmg: int=1) -> None:
        self.lives -= dmg
    
    def turn(self, shotgun: Shotgun, /) -> None:
        print(self)
        ans = input("type to use:\nshotgun - shoot\n>")
        match (ans):
            case "shoot":
                ans = input("shoot self or rival?\n>")
                if ans == "..":
                    clear()
                    self.turn(shotgun)
                    clear()
                    return
                match (ans):
                    case "self":
                        sleep(4)
                        if shotgun.shell() == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg(1)
                        elif shotgun.shell() == "blank":
                            print("*click")
                            shotgun.shoot()
                            sleep(2)
                            clear()
                            if len(shotgun.content) != 0:
                                self.turn(shotgun)
                                clear()
                                return
                    case "rival":
                        if len(self.opponents) > 1:
                            ans = input(f"who will you shoot?\n{self.displayOpponents()}\n>")
                            if ans == "..":
                                clear()
                                self.turn(shotgun)
                                clear()
                                return
                            sleep(4)
                            if shotgun.shell() == "live":
                                print("BANG")
                                shotgun.shoot()
                                for op in self.opponents:
                                    if op.name == ans:
                                        op.takeDmg(1)
                            elif shotgun.shell() == "blank":
                                print("*click")
                                shotgun.shoot()
                        else:
                            sleep(4)
                            if shotgun.shell() == "live":
                                print("BANG")
                                shotgun.shoot()
                                self.opponents[0].takeDmg(1)
                            elif shotgun.shell() == "blank":
                                print("*click")
                                shotgun.shoot()
                    case _:
                        print("failed to pick a target")
            case _:
                print("failed to pick an action")
        sleep(2)
        clear()

allitems = ["beer", "knife", "magnifying glass", "cigarette", "cuffs"]

class Player_R2(Player):
    def __init__(self, name: str, lives: int, wins: int):
        super().__init__(name, lives)
        self.wins: int = wins
        self.inv: list[str] = []
        self.lifeCap: int = lives
        self.cuffed: int = 0
    
    def __str__(self) -> str:
        return super().__str__()+f"\nyour items: {self.displayItems()}"

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

    def useItem(self, item: str, shotgun: Shotgun=None, * , target: object=None) -> None:
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

    def displayItems(self) -> str:
        return ", ".join([item for item in self.inv])

    def _cycleCuffs(self) -> None:
        if self.cuffed == 1:
            self.cuffed += 1
            print(f"{self.name} is cuffed")
        elif self.cuffed == 2:
            print(f"{self.name} broke free from cuffs")
            self.cuffed = 0
    
    def turn(self, shotgun: Shotgun, /) -> None:
        self._cycleCuffs()
        if self.cuffed:
            sleep(2)
            return
        else:
            sleep(2)
            clear()
        print(self)
        ans = input("say to use:\nshotgun - shoot\nitem - item\n>")
        match (ans):
            case "shoot":
                ans = input("shoot self or rival?\n>")
                if ans == "..":
                    clear()
                    self.turn(shotgun)
                    clear()
                    return
                match (ans):
                    case "self":
                        sleep(4)
                        if shotgun.shell() == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg(shotgun.dmg)
                        elif shotgun.shell() == "blank":
                            print("*click")
                            shotgun.shoot()
                            sleep(2)
                            clear()
                            if len(shotgun.content) != 0:
                                self.turn(shotgun)
                                clear()
                                return
                    case "rival":
                        if len(self.opponents) > 1:
                            ans = input(f"who will you shoot?\n{self.displayOpponents()}\n>")
                            if ans == "..":
                                clear()
                                self.turn(shotgun)
                                clear()
                                return
                            sleep(4)
                            if shotgun.shell() == "live":
                                print("BANG")
                                shotgun.shoot()
                                for op in self.opponents:
                                    if op.name == ans:
                                        op.takeDmg(shotgun.dmg)
                            elif shotgun.shell() == "blank":
                                print("*click")
                                shotgun.shoot()
                        else:
                            sleep(4)
                            if shotgun.shell() == "live":
                                print("BANG")
                                shotgun.shoot()
                                self.opponents[0].takeDmg(shotgun.dmg)
                            elif shotgun.shell() == "blank":
                                print("*click")
                                shotgun.shoot()
                    case _:
                        print("failed to pick target")
            case "item":
                ans = input(f"pick an item. ({self.displayItems()})\n>")
                if ans == "..":
                    clear()
                    self.turn(shotgun)
                    clear()
                    return
                if ans == "cuffs":
                    ans = input(f"who are you using them on?\n{self.displayOpponents()}\n>")
                    for op in self.opponents:
                        if op.name == ans:
                            useCuffs(self, op)
                else:
                    self.useItem(ans, shotgun, target=self.opponents[0])
                self.turn(shotgun)
                clear()
                return
            case _:
                print("failed to pick an action")
        sleep(2)
        clear()

class Player_R3(Player_R2):
    def __init__(self, name: str, lives: int, wins: int):
        super().__init__(name, lives, wins)
        self.wins: int = wins
        self.lifeLocked: bool = False
        
    def __str__(self) -> str:
        if self.lifeLocked == True:
            return f"{self.name}'s turn\nyou have # lives\nyour items: {self.displayItems()}"
        return f"{self.name}'s turn\nyou have {self.lives} lives\nyour items: {self.displayItems()}"
    
    def lifelock(self, turn: function) -> function:
        def wrapper():
            turn()
            if self.lifeLocked == False and self.lives <= 2:
                print("are you ready?")
                sleep(2)
                print("ERR: DEFFIBRILATORS UNRESPONSIVE")
                self.lifeLocked == True
                self.lives = 1
        return wrapper
    
    @lifelock
    def turn(self, shotgun: Shotgun, /) -> None:
        self._cycleCuffs()
        if self.cuffed:
            sleep(2)
            return
        else:
            sleep(2)
            clear()
        print(self)
        ans = input("say to use:\nshotgun - shoot\nitem - item\n>")
        match (ans):
            case "shoot":
                ans = input("shoot self or rival?\n>")
                if ans == "..":
                    clear()
                    self.turn(shotgun)
                    clear()
                    return
                match (ans):
                    case "self":
                        sleep(4)
                        if shotgun.shell() == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg(shotgun.dmg)
                        elif shotgun.shell() == "blank":
                            print("*click")
                            shotgun.shoot()
                            sleep(2)
                            clear()
                            if len(shotgun.content) != 0:
                                self.turn(shotgun)
                                clear()
                                return
                    case "rival":
                        if len(self.opponents) > 1:
                            ans = input(f"who will you shoot?\n{self.displayOpponents()}\n>")
                            if ans == "..":
                                clear()
                                self.turn(shotgun)
                                clear()
                                return
                            sleep(4)
                            if shotgun.shell() == "live":
                                print("BANG")
                                shotgun.shoot()
                                for op in self.opponents:
                                    if op.name == ans:
                                        op.takeDmg(shotgun.dmg)
                            elif shotgun.shell() == "blank":
                                print("*click")
                                shotgun.shoot()
                        else:
                            sleep(4)
                            if shotgun.shell() == "live":
                                print("BANG")
                                shotgun.shoot()
                                self.opponents[0].takeDmg(shotgun.dmg)
                            elif shotgun.shell() == "blank":
                                print("*click")
                                shotgun.shoot()
                    case _:
                        print("failed to pick target")
            case "item":
                ans = input(f"pick an item. ({self.displayItems()})\n>")
                if ans == "..":
                    clear()
                    self.turn(shotgun)
                    clear()
                    return
                if ans == "cuffs":
                    ans = input(f"who are you using them on?\n{self.displayOpponents()}\n>")
                    for op in self.opponents:
                        if op.name == ans:
                            useCuffs(self, op)
                else:
                    self.useItem(ans, shotgun, target=self.opponents[0])
                self.turn(shotgun)
                clear()
                return
            case _:
                print("failed to pick an action")
        sleep(2)
        clear()

if __name__ == "__main__": # this is not a script, just a module
    print("wrong file idiot")