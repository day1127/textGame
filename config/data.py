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





gear = {
    'Knife': "False, True, 10, 4, False, False, -1, True, False",
    'Hammer': "False, True, 6, 6, False, False, -1, True, False",
    'Bandages': "False, False, 0, 10, True, False, 10, False, False",
    'Flashlight': "True, True, 10, 2, False, False, -1, True, False"


}
