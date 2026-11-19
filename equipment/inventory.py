from . import ArmorStand, Armor, Weapon, Shield
from ..dialogue import inventory_check_m
from ..utils import output, Armor_Slot
import copy

class Inventory:
    def __init__(self):
        self.inventory: list[Armor|Weapon|Shield] = []
        self.money: int = 0
        self.weapon: Weapon|None = None
        self.armor: ArmorStand = ArmorStand()

    def peek_inventory(self):
        output(inventory_check_m(self))

    def equip(self, item: Shield|Armor|None, slot: Armor_Slot):
        self.armor.equip(item, slot)

    def unequip(self, slot: Armor_Slot):
        self.armor.unequip(slot)

    def buy(self, item: Shield|Armor|Weapon):
        if self.money >= item.value:
            self.money -= item.value
            self.inventory.append(copy.copy(item))
            # success message
        else:
            pass
            # failure message


    def sell(self):
        pass

    def remove(self):
        pass
