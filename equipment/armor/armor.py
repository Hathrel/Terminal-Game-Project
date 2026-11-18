from abc import ABC
from ...utils import Armor_Slot

class Armor:
    def __init__(self, name: str, defense: int, armor: int, slot_type: Armor_Slot):
        self.name: str = name
        self.defense: int = defense 
        self.armor: int = armor
        self.slot_type: Armor_Slot = slot_type

    def __repr__(self):
        return self.name
