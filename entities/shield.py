"""Model shields, blocking rolls, and shield durability."""

from items import Item
from ..utils import roll_dice, BreakableItem

class Shield(Item, BreakableItem):
    """A shield that contributes defense and can block while defending."""

    def __init__(self, name: str, block_chance: int, defense: int, value: int, durability: int):
        """Set the shield's name, block chance, defense, and value."""
        super().__init__(name, value)
        BreakableItem.__init__(self, durability)
        self.block_chance: int = block_chance
        self.defense: int = defense

    def block(self, blocking: bool) -> bool:
        """Roll to block if blocking is active, otherwise return False."""
        if blocking:
            return roll_dice(100) <= self.block_chance
        else:
            return False
