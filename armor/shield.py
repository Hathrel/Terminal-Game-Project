from ..utils import roll_dice


class Shield:
    def __init__(self, block_chance: int, defense: int):
        self.block_chance = block_chance
        self.defense = defense

    def block(self, blocking: bool):
        if blocking:
            return roll_dice(100) > self.block_chance
         
