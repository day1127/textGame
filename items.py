from config.data import gear


"""

class Item:
    def __init__(self, name, light, melee, range, damage, healing, armour, uses, equip, equiped):
        self.name = name   : str
        self.light = light : bool
        self.melee = melee : bool
        self.range = range : int
        self.damage = damage : int
        self.healing = healing : bool
        self.armour = armour : bool
        self.uses = uses : int
        self.equip = equip : bool
        self.equiped = equiped : bool
"""


def returnBool(boolIn):
    if boolIn.lower() == "true":
        return True
    elif boolIn.lower() == "false":
        return False
    else:
        # Make this better
        print("We are only accepting true or false")


class Item:
    def __init__(self, name, light, melee, range, damage, healing, armour, uses, equip, equiped):
        self.name = name
        self.light = light
        self.melee = melee
        self.range = range
        self.damage = damage
        self.healing = healing
        self.armour = armour
        self.uses = uses
        self.equip = equip
        self.equiped = equiped





    def __str__(self):
        stringOut = ""
        stringOut += f"Name: {self.name} \n"
        stringOut += f"Light: {self.light} \n"
        stringOut += f"Melee: {self.melee} \n"
        stringOut += f"Range: {self.range} \n"
        stringOut += f"Damage: {self.damage} \n"
        stringOut += f"Healing: {self.healing} \n"
        stringOut += f"Armour: {self.armour} \n"
        stringOut += f"Uses: {self.uses} \n"
        stringOut += f"Equipable: {self.equip} \n"
        stringOut += f"Equiped: {self.equiped} \n"
        return stringOut



if __name__ == "__main__":
    Knife = gear['Knife'].split(', ')
    print(Knife, Knife[1])
    a = Item('Knife',
        returnBool(Knife[0]),
        returnBool(Knife[1]),
        int(Knife[2]),
        int(Knife[3]),
        returnBool(Knife[4]),
        returnBool(Knife[5]),
        int(Knife[6]),
        returnBool(Knife[7]),
        returnBool(Knife[8])
        )

    Hammer = gear['Hammer'].split(', ')
    print(Hammer, Hammer[1])
    b = Item('Hammer',
        returnBool(Hammer[0]),
        returnBool(Hammer[1]),
        int(Hammer[2]),
        int(Hammer[3]),
        returnBool(Hammer[4]),
        returnBool(Hammer[5]),
        int(Hammer[6]),
        returnBool(Hammer[7]),
        returnBool(Hammer[8])
        )

    print(a)
    print(b)
