"""Model shields, blocking rolls, and shield durability."""

from ...utils import roll_dice, Armor_Slot

class Shield:
    """A shield that contributes defense and can block while defending."""

    def __init__(self, name: str, block_chance: int, defense: int, value: int):
        """Set the shield's name, block chance, defense, and value."""
        self.name: str = name
        self.block_chance: int = block_chance
        self.defense: int = defense
        self.value: int = value
        self.slot_type: Armor_Slot = Armor_Slot.SHIELD

    def __repr__(self):
        """Return the shield's name."""
        return self.name

    def block(self, blocking: bool) -> bool:
        """Roll to block if blocking is active, otherwise return False."""
        if blocking:
            return roll_dice(100) <= self.block_chance
        else:
            return False

class BreakableShield(Shield):
    """A shield that can break from durability loss or a defensive roll."""

    def __init__(self, name: str, block_chance: int, defense: int, value: int, durability: int, defensive_break: bool):
        """Initialize a shield with its starting durability and break mode."""
        super().__init__(name, block_chance, defense, value)
        self.current_durability = durability
        self.max_durability = durability
        self.defensive_break = defensive_break

    @property
    def broken(self) -> bool:
        """Return whether maximum durability is zero or below."""
        return self.max_durability <= 0

    def break_check(self) -> bool:
        """Check for depleted durability or roll for a defensive break."""
        if self.current_durability <= 0 and not self.defensive_break:
            return True
        elif self.defensive_break:
            return self.max_durability >= roll_dice(100)
        else:
            return False

    def damage_armor(self, damage: int) -> bool:
        """Apply durability damage when applicable and report whether the shield is broken."""
        if not self.defensive_break:
            self.current_durability -= damage
        if self.break_check():
            self.current_durability = 0
            self.max_durability = 0
        return self.broken
