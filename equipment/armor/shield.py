from ...utils import roll_dice, Armor_Slot

class Shield:
    def __init__(self, name: str, block_chance: int, defense: int, value: int):
        self.name: str = name
        self.block_chance: int = block_chance
        self.defense: int = defense
        self.value: int = value
        self.slot_type: Armor_Slot = Armor_Slot.SHIELD

    def __repr__(self):
        return self.name

    def block(self, blocking: bool) -> bool:
        if blocking:
            return roll_dice(100) <= self.block_chance
        else:
            return False
