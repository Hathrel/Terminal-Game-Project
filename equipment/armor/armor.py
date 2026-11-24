"""Model worn armor and its durability rules."""

from entities import Entity

from ...utils import Armor_Slot, roll_dice

class Armor(Entity):
    """A wearable item that contributes defense and armor."""

    def __init__(self, name: str, defense: int, armor: int, value: int, slot_type: Armor_Slot):
        """Set the armor's name, defense, protection, value, and compatible slot."""
        self.name: str = name
        self.defense: int = defense 
        self.armor: int = armor
        self.value: int = value
        self.slot_type: Armor_Slot = slot_type

    def __repr__(self):
        """Return the armor's name."""
        return self.name

class BreakableArmor(Armor):
    """Armor that can break from durability loss or a defensive roll."""

    def __init__(self, name: str, defense: int, armor: int, value: int, slot_type: Armor_Slot, durability: int, defensive_break: bool = False):
        """Initialize armor with its starting durability and break mode."""
        super().__init__(name, defense, armor, value, slot_type)
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
        """Apply durability damage when applicable and report whether the armor is broken."""
        if not self.defensive_break:
            self.current_durability -= damage
        if self.break_check():
            self.current_durability = 0
            self.max_durability = 0
        return self.broken

