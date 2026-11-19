from equipment import Armor
from ..dialogue import already_wearing_armor_m, wrong_armor_type_m
from ..utils import Armor_Slot

class ArmorStand:
    def __init__(self):
        self._head_slot: Armor|None = None
        self._shoulder_slot: Armor|None = None
        self._chest_slot: Armor|None = None
        self._hands_slot: Armor|None = None
        self._legs_slot: Armor|None = None
        self._boots_slot: Armor|None = None
        self._shield_slot: Armor|None = None

    @property
    def head_slot(self):
        return self._head_slot

    @head_slot.setter
    def head_slot(self, item: Armor):
        slot = Armor_Slot.HEAD
        if item.slot_type == slot and self._head_slot is None:
            self._head_slot = item
        elif item.slot_type != slot:
            wrong_armor_type_m(item, slot)
        elif self._head_slot is not None:
            already_wearing_armor_m(item, self._head_slot)
        
    @property
    def shoulder_slot(self):
        return self._shoulder_slot

    @shoulder_slot.setter
    def shoulder_slot(self, item: Armor):
        slot = Armor_Slot.SHOULDERS
        if item.slot_type == slot and self._shoulder_slot is None:
            self._shoulder_slot = item
        elif item.slot_type != slot:
            wrong_armor_type_m(item, slot)
        elif self._shoulder_slot is not None:
            already_wearing_armor_m(item, self._shoulder_slot)
        
    @property
    def chest_slot(self):
        return self._chest_slot

    @chest_slot.setter
    def chest_slot(self, item:Armor):
        slot = Armor_Slot.CHEST
        if item.slot_type == slot and self._chest_slot is None:
            self._chest_slot = item
        elif item.slot_type != slot:
            wrong_armor_type_m(item, slot)
        elif self._chest_slot is not None:
            already_wearing_armor_m(item, self._chest_slot)

