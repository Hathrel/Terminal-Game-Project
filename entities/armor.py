"""Model worn armor and its durability rules."""

from equipment import Material
from math import floor
from . import Item
from ..utils import BreakableItem

class Armor(Item, BreakableItem):
    """A wearable item that contributes defense and armor."""

    def __init__(self, name: str, defense: int, armor: int, value: int, durability: int, material: Material):
        """Set the armor's name, defense, protection, value, and material."""
        super().__init__(" ".join([material.name, name]), floor(value * material.value_modifier))
        BreakableItem.__init__(self, floor(durability * material.stat_mod))
        self._material: Material = material
        self._defense: int = defense
        self._armor: int = armor

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
    def armor(self):
        return floor(self._armor * self.__stat_mod)

    def __repr__(self):
        """Return the armor's name."""
        return self.name


