class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        print(f"{self.name} says yellow")


nsm = Character("Nasim", "100", "5")
rjb = NPC("Rajab", "98", "4")
NPC.speak(rjb)
