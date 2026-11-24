"""Model worn armor and its durability rules."""

from . import Item
from ..utils import BreakableItem

class Armor(Item, BreakableItem):
    """A wearable item that contributes defense and armor."""

    def __init__(self, name: str, defense: int, armor: int, value: int, durability: int):
        """Set the armor's name, defense, protection, value, and compatible slot."""
        super().__init__(name, value)
        BreakableItem.__init__(self, durability)
        self.defense: int = defense 
        self.armor: int = armor

    def __repr__(self):
        """Return the armor's name."""
        return self.name


