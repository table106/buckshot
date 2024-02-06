from random import randint, shuffle

class Shotgun:
    def __init__(self):
        self.content = []
        self.dmg = 1

    def insertShells(self):
        live = randint(1,4)
        blank = randint(1,4)
        for i in range(live):
            self.content.append("live")
        
        for i in range(blank):
            self.content.append("blank")
        shuffle(self.content)

    def shoot(self):
        self.content.pop(0)
        self.dmg = 1