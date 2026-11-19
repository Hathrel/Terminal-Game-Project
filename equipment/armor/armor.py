from ...utils import Armor_Slot, roll_dice

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
    def __init__(self, name: str, defense: int, armor: int, value: int, slot_type: Armor_Slot, durability: int, defensive_break: bool = False):
        super().__init__(name, defense, armor, value, slot_type)
        self.current_durability = durability
        self.max_durability = durability
        self.defensive_break = defensive_break

    @property
    def broken(self) -> bool:
        return self.max_durability <= 0

    def break_check(self) -> bool:
        if self.current_durability <= 0 and not self.defensive_break:
            return True
        elif self.defensive_break:
            return self.max_durability >= roll_dice(100)
        else:
            return False

    def damage_armor(self, damage: int) -> bool:
        if not self.defensive_break:
            self.current_durability -= damage
        if self.break_check():
            self.current_durability = 0
            self.max_durability = 0
        return self.broken

