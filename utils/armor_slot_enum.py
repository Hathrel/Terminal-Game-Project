"""Define the slots used for armor and shields."""

from enum import Enum

class Armor_Slot(Enum):
    """Identify the slots that armor and shields can occupy."""

    HEAD = 0
    SHOULDERS = 1
    CHEST = 2
    HANDS = 3
    LEGS = 4
    FEET = 5
    SHIELD = 6
