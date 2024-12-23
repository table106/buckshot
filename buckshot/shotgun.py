from random import shuffle

class Shotgun:
    def __init__(self):
        self.content: list[str] = []
        self.dmg: int = 1

    def insertShells(self, live: int, blank: int, /) -> None:
        for i in range(live):
            self.content.append("live")
        for i in range(blank):
            self.content.append("blank")
        shuffle(self.content)

    def shoot(self) -> None:
        self.content.pop(0)
        self.dmg = 1

    def empty(self) -> None:
        self.content = []
        self.dmg = 1

    def shell(self) -> str:
        return self.content[0]