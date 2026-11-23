"""Model weapon attacks, damage, and knockout checks."""

from ...utils import roll_dice


class Weapon:
    """A weapon with attack, damage, and value ratings."""

    def __init__(self, name: str, damage: int, attack: int, value: int):
        """Set the weapon's name, damage, attack, and value."""
        self.name: str = name
        self.damage: int = damage
        self.attack: int = attack
        self.value: int = value

    def __repr__(self):
        """Return the weapon's name."""
        return self.name

    def roll_attack(self, defense: int) -> bool:
        """Add the attack bonus to a 30-sided roll and compare it with defense."""
        return roll_dice(30) + self.attack >= defense

    def roll_damage(self, armor: int) -> int:
        """Roll weapon damage, add base damage, and subtract target armor."""
        return roll_dice(self.damage) + self.damage - armor

class BluntWeapon(Weapon):
    """A weapon that can knock out a target on a hit."""

    def __init__(self, name: str, damage: int, attack: int, value: int, knockout_chance: int):
        """Initialize the weapon with a percentile knockout chance."""
        super().__init__(name, damage, attack, value)
        self.knockout = knockout_chance

    def roll_knockout(self, hit: bool) -> bool:
        """Roll for a knockout after a hit and return False on a miss."""
        if hit:
            return self.knockout >= roll_dice(100)
        return False

class BreakableWeapon(Weapon):
    """A weapon with attack, damaage, value, and durability ratings."""

    def __init__(self, name: str, damage: int, attack: int, value: int, durability: int):
        """Set the weapon's name, damage, attack, value, and durability."""
        super().__init__(name, damage, attack, value)
        self.current_durability = durability
        self.max_durability = durability

        @property
        def broken(self) -> bool:
            return self.max_durability > 0

class BreakableBluntWeapon(BluntWeapon):
    def __init__(self, name: str, damage: int, attack: int, value: int, knockout_chance: int, durability: int):
        super().__init__(name, damage, attack, value, knockout_chance)
        self.current_durability = durability
        self.max_durability = durability

        @property
        def broken(self) -> bool:
            return self.max_durability > 0
