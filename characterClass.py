

class character:

    def __init__(self, name, gender, Hp = 100, stamina = 100,  hight = 6,):
        self.name = name
        self.Hp = Hp
        self.inventory = []
        self.stam = stamina
        self.gender = gender
        self.hight = hight
        self.their = "their"
        self.heOrShe = "they"
        self.himOrHer = "them"

    def __str__(self):
        return f"{self.name} has {self.Hp} Hp, and {self.inventory} in {self.their} inventory, their gender is {self.gender}, and they are {self.hight} tall"



    def addToInv(self,item):
        self.inventory.append(item)

if __name__ == "__main__":
    a = character("Jeff", "non-binary")

    addToInv("sword")
    print (a.__str__())
