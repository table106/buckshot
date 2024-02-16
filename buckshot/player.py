from system import clear
from time import sleep
from random import randint as r

import logging
logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w", format="%(asctime)s at line no. %(lineno)d - %(message)s")

from items import *

from shotgun import *

class Player:
    def __init__(self, num: int, name: str, lives: int):
        self.num = num
        self.name = name
        self.lives = lives
        self.wins = 0
        self.lifeCap = lives
        self.opponent = None

    def __str__(self) -> str:
        if self.lives > 1:
            return f"{self.name}'s turn\nyou have {self.lives} lives"
        return f"{self.name}'s turn\nyou have 1 life"
    
    def __repr__(self) -> str:
        return f"{self.num}: {self.name}\
             | lives: {self.lives}\
             | wins: {self.wins}\
             | life cap: {self.lifeCap}"
    
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
                            logging.debug(f"player {self.num} took damage from self")
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            logging.debug(f"player {self.num} gets another turn")
                            sleep(2)
                            clear()
                            if len(shotgun.content) != 0:
                                self.turn(shotgun)
                    case "enemy":
                        sleep(4)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.opponent.takeDmg(1)
                            logging.debug(f"player {self.opponent.num} took damage from enemy")
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            logging.debug(f"player {self.num} didn't damage the enemy")
                    case default:
                        print("failed to pick the target")
                        logging.info(f"player {self.num} failed to pick a target")
            case default:
                print("failed to pick an action")
                logging.info(f"player {self.num} failed to pick an action")
        sleep(2)
        clear()

allitems = ["beer", "knife", "magnifying glass", "cigarette", "cuffs"]

class Player_R2(Player):
    def __init__(self, num: int, name: str, lives: int):
        super().__init__(num, name, lives)
        self.inv = []
        self.cuffed = 0

    def __str__(self) -> str:
        return super().__str__()+f"\nyour items: {self.inv}"
    
    def __repr__(self) -> str:
        return super().__repr__()+f" | inventory: {self.inv}\
             | cuffed state: {self.cuffed}"

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

    def useItem(self, item: str, shotgun: Shotgun):
        match(item):
            case "beer":
                useBeer(self, shotgun)
                logging.debug(f"player {self.num} used a beer")
            case "knife":
                useKnife(self, shotgun)
                logging.debug(f"player {self.num} used a knife")
            case "magnifying glass":
                useGlass(self, shotgun)
                logging.debug(f"player {self.num} used a glass")
            case "cigarette":
                useCigarette(self)
                logging.debug(f"player {self.num} used a cig")
            case "cuffs":
                useCuffs(self.opponent)
                logging.debug(f"player {self.num} used cuffs")
            case default:
                logging.info(f"player {self.num} failed to pick an item")
    
    def turn(self, shotgun: Shotgun):
        print(self)
        ans = input("say to use:\nshotgun - shoot\nitem - item\n>")
        match (ans):
            case "shoot":
                logging.debug(f"player {self.num} chose to shoot")
                ans = input("shoot self or enemy?\n>")
                match (ans):
                    case "self":
                        logging.debug(f"player {self.num} chose to shoot self")
                        sleep(4)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.takeDmg()
                            logging.debug(f"player {self.num} took damage from self")
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            logging.debug(f"player {self.num} gets another turn")
                            sleep(2)
                            clear()
                            if len(shotgun.content) != 0:
                                self.turn(shotgun)
                            self.turn(shotgun)
                    case "enemy":
                        logging.debug(f"player {self.num} chose to shoot the enemy")
                        sleep(4)
                        if shotgun.content[0] == "live":
                            print("BANG")
                            shotgun.shoot()
                            self.opponent.takeDmg(shotgun.dmg)
                            logging.debug(f"player {self.opponent.num} took damage from enemy")
                        elif shotgun.content[0] == "blank":
                            print("*click")
                            shotgun.shoot()
                            logging.debug(f"player {self.num} didn't damage the enemy")
                    case default:
                        print("failed to pick target")
                        logging.info(f"player {self.num} failed to pick a target")
            case "item":
                logging.debug(f"player {self.num} chose to use an item")
                ans = input(f"pick an item. {self.inv}\n>")
                self.useItem(ans)
            case default:
                print("failed to pick an action")
                logging.info(f"player {self.num} failed to pick an action")
        sleep(2)
        clear()