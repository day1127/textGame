import random
import os
from config.data import gear
import items


def d6():
    return random.randint(1,6)

def fourD6MinusLow():
    rolls = []
    for i in range(4):
        rolls.append(d6())
    rolls.sort(reverse = True)
    rolls.pop()
    return sum(rolls)


class character:

    def __init__(self, name, charisma = 0, strength = 0, dexterity = 0, Hp = 100, stamina = 100):
        self.name = name
        self.Hp = Hp
        self.inventory = []
        self.stam = stamina
        self.chr = charisma
        self.str = strength
        self.dex = dexterity

        if self.chr == 0 and self.str == 0 and self.dex == 0:
            self.getStats()

    def addToInv(self, item):
        self.inventory.append(item)

    def dropItem(self):
        menuCounter = 1
        for inventoryItem in self.inventory:
            print(f"{menuCounter}, {inventoryItem}")
            menuCounter += 1

        choice = input ("What are you dropping?: ")
        try:
            choice = int(choice)
            temp = self.inventory[choice -1]
            self.inventory.remove(self.inventory[choice -1])
            print(temp, 'removed')
            temp = input("Hit ENTER to continue")


        except ValueError:
            if choice in self.inventory:
                self.inventory.remove(choice)
                print(choice, "removed")
                temp = input("Hit ENTER to continue")
            elif choice == "nothing" or "none" or "nither":
                print("nothing was dropped")
                temp = input ("Hit ENTER to continue")

        except IndexError:
            print("Sorry that dose not exist")
            temp = input("Hit ENTER to continue")
            self.dropItem()


    def getStats(self):
        self.chr = fourD6MinusLow()
        self.str = fourD6MinusLow() + d6()
        self.dex = fourD6MinusLow() + d6() + d6() - d6()


    def __str__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        return f"{self.name} has {self.Hp} Hp and {self.stam} stamina\n {self.chr} charisma, {self.str} strength {self.dex} dexterity\n {self.inventory}"

    def printInv(self):
        return self.inventory

    def inspect(self):
        MenuCounter = 1
        for inventoryItem in self.inventory:
            print(f"{MenuCounter}, {inventoryItem}")
            MenuCounter += 1

        choice = input ("What are you inspecting?: ")
        try:
            choice = int(choice)
            #temp = self.inventory[choice -1]
            inspected = gear[self.inventory[choice -1]].split(", ")
            print(inspected)
            temp = input("Hit ENTER to continue")

        except ValueError:
            if choice in self.inventory:
                inspected = gear[choice].split(", ")
                print(inspected)
                #print(choice, "removed")
                temp = input("Hit ENTER to continue")
            elif choice == "nothing" or "none" or "nither":
                print("nothing was inspected")
                temp = input ("Hit ENTER to continue")







if __name__ == "__main__":
    a = character("Jeff")

    a.addToInv("Sword")
    a.addToInv("Torch")
    a.addToInv("Rations")
    a.addToInv("Shield")
    a.addToInv("Water")
    a.addToInv("Coffee")

    print(a)

    #a.dropItem()
    a.inspect()

    #print(a.printInv())
