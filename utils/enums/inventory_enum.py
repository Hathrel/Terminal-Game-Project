from enum_type import Message_Enum
from enum import auto

class Armor_Result(Message_Enum):
    NO_ARMOR_SPECIFIED_EQUIP = auto(),
    NO_ARMOR_SPECIFIED_UNEQUIP = auto()
    NOT_ARMOR = auto()
    ALREADY_WEARING = auto()
    WRONG_ARMOR_TYPE = auto()
    BROKEN_ARMOR = auto()
    EQUIP_ARMOR = auto()
    UNEQUIP_ARMOR = auto()

