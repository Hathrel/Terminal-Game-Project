from ...utils import Armor_Slot

class Armor:
    def __init__(self, name: str, defense: int, armor: int, value: int, slot_type: Armor_Slot):
        self.name: str = name
        self.defense: int = defense 
        self.armor: int = armor
        self.value: int = value
        self.slot_type: Armor_Slot = slot_type

    def __repr__(self):
        return self.name

class BreakableArmor(Armor):
    def __init__(self, name: str, defense: int, armor: int, value: int, slot_type: Armor_Slot, durability: int):
        super().__init__(name, defense, armor, value, slot_type)
        self.current_durability = durability
        self.max_durability = durability

     
