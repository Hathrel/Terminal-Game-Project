from abc import ABC
from ..utils import Armor_Slot

class Armor(ABC):
    name: str
    defense: int 
    slot_type: Armor_Slot
