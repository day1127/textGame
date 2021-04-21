import random

def d6():
    return random.randint(1, 6)

def fourD6MinusLow():
    rolls = []
    for i in range(4):
        rolls.append(d6())
        rolls.sort(reverse = True)
        rolls.pop()
        return sum(rolls)

class character:

    def __init__(self, name, Hp = 100, stamina = 100, charisma = 0, strength = 0, dexterity = 0):
        self.name = name
        self.Hp = Hp
        self.inventory = []
        self.stam = stamina
        self.chr = charisma
        self.str = strength
        self.dex = dexterity
        self.getStats()



    def addToInv(self, item):
        self.inventory.append(item)


    def getStats(self):
        self.chr = fourD6MinusLow()
        self.str = fourD6MinusLow() + d6()
        self.dex = fourD6MinusLow() + d6() + d6() - d6()


    def __str__(self):
        return f"{self.name} has {self.Hp} Hp, and {self.inventory} in their inventory, they have {self.chr} charisma, {self.str} strength, and {self.dex} dexterity"

if __name__ == "__main__":
    a = character("Jeff")

    a.addToInv("sword")
    print (a.__str__())
