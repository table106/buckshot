from time import sleep
from random import randint as r

from system import clear, query
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
        ans = query("type to use:\nshotgun - shoot")
        match (ans):
            case "shoot":
                ans = query("shoot self or rival?")
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
                            ans = query(f"who will you shoot?\n{self.displayOpponents()}")
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
            self.inv.append(ITEMS[id1])
            self.inv.append(ITEMS[id2])
            print(f"{self.name} got {ITEMS[id1]}, and {ITEMS[id2]}.")
            sleep(2)

    def useItem(self, item: str, shotgun: Shotgun, /) -> None:
        match(item):
            case "beer":
                useBeer(self, shotgun)
            case "knife":
                useKnife(self, shotgun)
            case "magnifying glass":
                useGlass(self, shotgun)
            case "cigarette":
                useCigarette(self)
            case _:
                print("failed to use a valid item")

    def displayItems(self) -> str:
        return ", ".join([item for item in self.inv])

    def _cycleCuffs(self) -> None | bool:
        if self.cuffed == 1:
            self.cuffed += 1
            print(f"{self.name} is cuffed")
        elif self.cuffed == 2:
            print(f"{self.name} broke free from cuffs")
            self.cuffed = 0
        sleep(2)
        if self.cuffed:
            return True
        else:
            clear()
    
    def turn(self, shotgun: Shotgun, /) -> None:
        if self._cycleCuffs():
            return
        print(self)
        ans = query("type to use:\nshotgun - shoot\nitem - item")
        match (ans):
            case "shoot":
                ans = query("shoot self or rival?")
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
                            ans = query(f"who will you shoot?\n{self.displayOpponents()}")
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
                ans = query(f"pick an item. ({self.displayItems()})")
                if ans == "..":
                    clear()
                    self.turn(shotgun)
                    clear()
                    return
                if ans == "cuffs":
                    if len(self.opponents) > 1:
                        ans = query(f"who are you using them on?\n{self.displayOpponents()}")
                        for op in self.opponents:
                            if op.name == ans:
                                if useCuffs(self, op) == 1:
                                    clear()
                                    self.turn(shotgun)
                                    clear()
                                    return
                    else:
                        if useCuffs(self, self.opponents[0]) == 1:
                            clear()
                            self.turn(shotgun)
                            clear()
                            return
                else:
                    self.useItem(ans, shotgun)
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
        self.lifeLocked: bool = False
        
    def __str__(self) -> str:
        if self.lifeLocked == True:
            return f"{self.name}'s turn\nyou have # lives\nyour items: {self.displayItems()}"
        return super().__str__()
    
    def _checkForLifelock(self) -> None:
        if self.lifeLocked == False and self.lives <= 2:
            print("are you ready?")
            sleep(2)
            print(f"{r(1000, 9999)} ERR: ${self.name} DEFIBRILLATORS UNRESPONSIVE :;")
            sleep(3)
            self.lifeLocked = True
            self.lives = 1
    
    def turn(self, shotgun: Shotgun, /) -> None:
        self._checkForLifelock()
        self._cycleCuffs()
        print(self)
        ans = query("type to use:\nshotgun - shoot\nitem - item")
        match (ans):
            case "shoot":
                ans = query("shoot self or rival?")
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
                            ans = query(f"who will you shoot?\n{self.displayOpponents()}")
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
                ans = query(f"pick an item. ({self.displayItems()})")
                if ans == "..":
                    clear()
                    self.turn(shotgun)
                    clear()
                    return
                if ans == "cuffs":
                    if len(self.opponents) > 1:
                        ans = query(f"who are you using them on?\n{self.displayOpponents()}")
                        for op in self.opponents:
                            if op.name == ans:
                                if useCuffs(self, op) == 1:
                                    clear()
                                    self.turn(shotgun)
                                    clear()
                                    return
                    else:
                        if useCuffs(self, self.opponents[0]) == 1:
                            clear()
                            self.turn(shotgun)
                            clear()
                            return
                else:
                    self.useItem(ans, shotgun)
                self.turn(shotgun)
                clear()
                return
            case _:
                print("failed to pick an action")
        sleep(2)
        clear()