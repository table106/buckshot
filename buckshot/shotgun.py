from random import shuffle

class Shotgun:
    def __init__(self):
        self.content = []
        self.dmg = 1

    def insertShells(self, live, blank):
        for i in range(live):
            self.content.append("live")
        for i in range(blank):
            self.content.append("blank")
        shuffle(self.content)

    def shoot(self):
        self.content.pop(0)
        self.dmg = 1