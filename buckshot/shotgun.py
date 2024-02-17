from random import shuffle

class Shotgun:
    def __init__(self):
        self.content = []
        self.dmg = 1

    def __str__(self) -> str:
        return f"{self.content}"

    def insertShells(self, live: int, blank: int) -> None:
        for i in range(live):
            self.content.append("live")
        for i in range(blank):
            self.content.append("blank")
        shuffle(self.content)

    def shoot(self) -> None:
        self.content.pop(0)
        self.dmg = 1

if __name__ == "__main__":
    print("wrong file idiot")