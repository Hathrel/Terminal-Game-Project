from . import ArmorStand, Armor, Weapon, Shield
from ..dialogue import inventory_check
from ..utils import output

class Inventory:
    def __init__(self):
        self.inventory: list[Armor|Weapon|Shield] = []
        self.money: int = 0
        self.weapon: Weapon|None = None
        self.armor: ArmorStand = ArmorStand()

    def peek_inventory(self):
        output(inventory_check(self))

    def equip(self):
        pass

    def unequip(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass

    def remove(self):
        pass
