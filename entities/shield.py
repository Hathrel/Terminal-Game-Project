"""Model shields, blocking rolls, and shield durability."""

from equipment import Material
from items import Item
from ..utils import roll_dice, BreakableItem
from math import floor

class Shield(Item, BreakableItem):
    """A shield that contributes defense and can block while defending."""

    def __init__(self, name: str, defense: int, value: int, durability: int, material: Material):
        """Set the shield's name, block chance, defense, and value."""
        super().__init__(" ".join([material.name, name]), floor(value * material.value_modifier))
        BreakableItem.__init__(self, floor(durability * material.stat_mod))
        self._material = material
        self._block_chance: int = material.block_chance
        self._defense: int = defense

    @property
    def material(self):
        return self._material

    @property
    def __stat_mod(self):
        return self.material.stat_mod

    @property
    def defense(self):
        return floor(self._defense * self.__stat_mod)

    @property
    def block_chance(self):
        return self._block_chance

    def block(self, blocking: bool) -> bool:
        """Roll to block if blocking is active, otherwise return False."""
        if blocking:
            return roll_dice(100) <= self.block_chance
        else:
            return False
