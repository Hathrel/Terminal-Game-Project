"""Model weapon attacks, damage, and knockout checks."""

from . import Item
from ..utils import roll_dice, BreakableItem


class Weapon(Item, BreakableItem):
    """A weapon with attack, damage, and value ratings."""

    def __init__(self, name: str, damage: int, attack: int, value: int, durability: int):
        """Set the weapon's name, damage, attack, and value."""
        super().__init__(name, value)
        BreakableItem.__init__(self, durability)
        self.damage: int = damage
        self.attack: int = attack

    def roll_attack(self, defense: int) -> bool:
        """Add the attack bonus to a 30-sided roll and compare it with defense."""
        return roll_dice(30) + self.attack >= defense

    def roll_damage(self, armor: int) -> int:
        """Roll weapon damage, add base damage, and subtract target armor."""
        return roll_dice(self.damage) + self.damage - armor

class BluntWeapon(Weapon):
    """A weapon that can knock out a target on a hit."""

    def __init__(self, name: str, damage: int, attack: int, value: int, durability: int, knockout_chance: int):
        """Initialize the weapon with a percentile knockout chance."""
        super().__init__(name, damage, attack, value, durability)
        self.knockout = knockout_chance

    def roll_knockout(self, hit: bool) -> bool:
        """Roll for a knockout after a hit and return False on a miss."""
        if hit:
            return self.knockout >= roll_dice(100)
        return False
