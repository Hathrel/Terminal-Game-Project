"""Model weapon attacks, damage, and knockout checks."""

from . import Item
from ..utils import roll_dice, BreakableItem
from ..equipment import Material
from math import floor


class Weapon(Item, BreakableItem):
    """A weapon with attack, damage, and value ratings."""

    def __init__(self, name: str, damage: int, attack: int, value: int, durability: int, material: Material, two_handed: bool):
        """Set the weapon's name, damage, attack, and value."""
        super().__init__(" ".join([material.name, name]), floor(value * material.value_modifier))
        BreakableItem.__init__(self, floor(durability * material.stat_mod))
        self._material: Material = material
        self._damage: int = damage
        self._attack: int = attack
        self._two_handed: bool = two_handed

    @property
    def material(self):
        return self._material

    @property
    def __stat_mod(self):
        return self.material.stat_mod

    @property
    def damage(self):
        return floor(self._damage * self.__stat_mod)

    @property
    def attack(self):
        return floor(self._attack * self.__stat_mod)

    def roll_attack(self, defense: int) -> bool:
        """Add the attack bonus to a 30-sided roll and compare it with defense."""
        return roll_dice(30) + self.attack >= defense

    def roll_damage(self, armor: int) -> int:
        """Roll weapon damage, add base damage, and subtract target armor."""
        return roll_dice(self.damage) + self.damage - armor

class Blunt():
    """A weapon that can knock out a target on a hit."""

    def __init__(self, knockout_chance: int):
        """Initialize the weapon with a percentile knockout chance."""
        self.knockout = knockout_chance

    def roll_knockout(self, hit: bool) -> bool:
        """Roll for a knockout after a hit and return False on a miss."""
        if hit:
            return self.knockout >= roll_dice(100)
        return False
