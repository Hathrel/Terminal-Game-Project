from . import ArmorStand, Armor, Weapon, Shield, BreakableArmor, BreakableShield, FISTS
from ..dialogue import inventory_check_m
from ..utils import output, Armor_Slot
from ..debugging import success_message_auto, failure_message_auto, generic_message_auto
import copy

class Inventory:
    def __init__(self):
        self.inventory: list[Armor|Weapon|Shield] = []
        self.money: int = 0
        self._weapon: Weapon|None = None
        self.armor: ArmorStand = ArmorStand()

    @property
    def weapon(self) -> Weapon:
        if self._weapon is None:
            return FISTS
        else:
            return self._weapon
      
    @weapon.setter
    def weapon(self, weapon: Weapon|None):
        self._weapon = weapon

    def peek_inventory(self):
        output(inventory_check_m(self))

    def equip_armor(self, item: Shield|Armor|None, slot: Armor_Slot):
        self.armor.equip(item, slot)

    def unequip_armor(self, slot: Armor_Slot):
        item = self.armor.unequip(slot)
        if item:
            self.inventory.append(item)

    def buy(self, item: Shield|Armor|Weapon):
        if self.money >= item.value:
            self.money -= item.value
            self.inventory.append(copy.copy(item))
            success_message_auto()
            return True
        else:
            failure_message_auto()
            return False

    def sell(self, item: Shield|Armor|Weapon):
        item_list = []
        for obj in self.inventory:
            if obj.name == item.name:
                item_list.append(obj)
        if not item_list:
            failure_message_auto()
            return False
        generic_message_auto("Shopping List")
        item_debug = item_list[0] # Get the player's input here instead of this assignemtn
        sale_item = item_debug
        if sale_item is None:
            generic_message_auto("Sale cancellation")
            return False
        self.inventory.remove(sale_item)
        sale_price = (sale_item.value//2)
        if isinstance(sale_item, (BreakableShield, BreakableArmor)): 
            sale_price -= sale_item.max_durability - sale_item.current_durability
            if sale_item.broken:
                sale_price //= 10
        self.money += sale_price 
        success_message_auto()
        return True

    def trash(self, item: Shield|Armor|Weapon):
        if item in self.inventory:
            self.inventory.remove(item)
            success_message_auto()
            return True
        else:
           failure_message_auto()
           return False
