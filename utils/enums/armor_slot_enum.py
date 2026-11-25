"""Define the slots used for armor and shields."""

from enum import Enum, auto

class Armor_Slot(Enum):
    """Identify the slots that armor and shields can occupy."""

    HEAD = auto()
    SHOULDERS = auto()
    CHEST = auto()
    HANDS = auto()
    LEGS = auto()
    FEET = auto()
    SHIELD = auto()
