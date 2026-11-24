"""Model human characters, their attributes, and combat state."""

from __future__ import annotations
from .entity import Entity
from utils import roll_dice, Controller_Type
from equipment.weapons import Weapon
from equipment import Inventory

class Human(Entity):
    """A human character with attributes, health, and an inventory."""

    def __init__(self, name: str, age: int, controller: Controller_Type):
        """Initialize a level-one character with default attributes and an empty inventory."""
        self.name: str = name
        self.experience: int = 0
        self.level: int = 1
        self.age: int = age

        self.strength: int = 1 # Damage Bonus half of strength value rounded down
        self.dexterity: int = 1 # Attack Bonus, Luck % chance at a second attack
        self.agility: int = 1 # Defense Bonus and Dodge bonus(?) and luck % chance to block without defending
        self.fortitude: int = 1 # Health*10 bonus, modifier contributes to armor bonus, luck based chance on non-combat Recovery of fortitude number of HP
        self.luck: int = 1 # 1% chance at every luck level for luck*10 exp every time exp is earned, and a luck level bonus to rolls
        
        self.health: int = self.fortitude * 10 + 90
        self.conscious: bool = True
        self.controller: Controller_Type = controller
        self.is_defending = False
        self.inventory: Inventory = Inventory() 

# -------Attributes Modifiers-------

    @property
    def strength_mod(self) -> int:
        """Return the strength modifier, rounded down from half of strength."""
        return self.strength//2

    @property
    def dexterity_mod(self) -> int:
        """Return the dexterity modifier, rounded down from one third of dexterity."""
        return self.dexterity//3

    @property
    def agility_mod(self) -> int:
        """Return the agility modifier, rounded down from one third of agility."""
        return self.agility//3

    @property
    def fortitude_mod(self) -> int:
        """Return the fortitude modifier, rounded down from one third of fortitude."""
        return self.fortitude//3

# -----Luck Rolls and Modifiers-----

    @property
    def luck_roll(self) -> bool:
        """Roll a percentile check against luck capped at 65."""
        return min(self.luck, 65) >= roll_dice(100)

    @property
    def luck_stat_boost(self) -> int:
        """Return the luck stat as a bonus on a successful luck roll, or zero."""
        if self.luck_roll:
            return self.luck
        else:
            return 0

    @property
    def luck_exp_boost(self) -> int:
        """Return ten times luck on a successful luck roll, or zero."""
        if self.luck_roll:
            return self.luck * 10
        else:
            return 0

    @property
    def second_attack_roll(self) -> bool:
        """Roll for a second attack using dexterity and luck, capped at 65 percent."""
        return min(self.dexterity_mod * self.luck, 65) >= roll_dice(100)

    @property
    def instinct_block_roll(self) -> bool:
        """Roll for an instinctive block using agility and luck, capped at 65 percent."""
        return min(self.agility_mod * self.luck, 65) >= roll_dice(100)

    @property
    def fortitude_recovery(self) -> int:
        """Roll for recovery and return fortitude on success or zero on failure."""
        if min(self.fortitude_mod * self.luck, 65) >= roll_dice(100):
            return self.fortitude
        else:
            return 0

# -------------Checks---------------

    @property
    def alive(self) -> bool:
        """Return whether the character has positive health."""
        return self.health > 0

    @property 
    def conscious_alive(self) -> bool:
        """Return whether the character is both conscious and alive."""
        return self.conscious and self.alive


# ------------Actions---------------

    def defend(self):
        """Enter the defending state if the character is conscious and alive."""
        if self.conscious_alive:
            self.is_defending = True
