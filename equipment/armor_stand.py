from equipment import Armor, Shield
from ..dialogue import already_wearing_armor_m, wrong_armor_type_m, no_armor_specified_m, already_wearing_item_m, successful_equip
from ..utils import Armor_Slot, output

class ArmorStand:
    def __init__(self):
        self._head_slot: Armor|None = None
        self._shoulder_slot: Armor|None = None
        self._chest_slot: Armor|None = None
        self._hands_slot: Armor|None = None
        self._legs_slot: Armor|None = None
        self._boots_slot: Armor|None = None
        self._shield_slot: Shield|None = None

    @property
    def head_slot(self):
        return self._head_slot

    @head_slot.setter
    def head_slot(self, item: Armor):
        slot = Armor_Slot.HEAD
        if item is None:
            output(no_armor_specified_m(slot))
            return 
        if self._head_slot is item:
            output(already_wearing_item_m(item))
            return
        if item.slot_type == slot and self._head_slot is None:
            self._head_slot = item
            output(successful_equip(item, slot))
        elif item.slot_type != slot:
            output(wrong_armor_type_m(item, slot))
        elif self._head_slot is not None:
            output(already_wearing_armor_m(item, self._head_slot))
        
    @property
    def shoulder_slot(self):
        return self._shoulder_slot

    @shoulder_slot.setter
    def shoulder_slot(self, item: Armor):
        slot = Armor_Slot.SHOULDERS
        if item is None:
            output(no_armor_specified_m(slot))
            return 
        if self._shoulder_slot is item:
            output(already_wearing_item_m(item))
            return
        if item.slot_type == slot and self._shoulder_slot is None:
            self._shoulder_slot = item
            output(successful_equip(item, slot))
        elif item.slot_type != slot:
            output(wrong_armor_type_m(item, slot))
        elif self._shoulder_slot is not None:
            output(already_wearing_armor_m(item, self._shoulder_slot))
        
    @property
    def chest_slot(self):
        return self._chest_slot

    @chest_slot.setter
    def chest_slot(self, item:Armor):
        slot = Armor_Slot.CHEST
        if item is None:
            output(no_armor_specified_m(slot))
            return 
        if self._chest_slot is item:
            output(already_wearing_item_m(item))
            return
        if item.slot_type == slot and self._chest_slot is None:
            self._chest_slot = item
            output(successful_equip(item, slot))
        elif item.slot_type != slot:
            output(wrong_armor_type_m(item, slot))
        elif self._chest_slot is not None:
            output(already_wearing_armor_m(item, self._chest_slot))
    
    @property
    def hands_slot(self):
        return self._hands_slot

    @hands_slot.setter
    def hands_slot(self, item: Armor):
        slot = Armor_Slot.HANDS
        if item is None:
            output(no_armor_specified_m(slot))
            return 
        if self._hands_slot is item:
            output(already_wearing_item_m(item))
            return
        if item.slot_type == slot and self._hands_slot is None:
            self._hands_slot = item
            output(successful_equip(item, slot))
        elif item.slot_type != slot:
            output(wrong_armor_type_m(item, slot))
        elif self._hands_slot is not None:
            output(already_wearing_armor_m(item, self._hands_slot))

    @property
    def legs_slot(self):
        return self._legs_slot

    @legs_slot.setter
    def legs_slot(self, item: Armor):
        slot = Armor_Slot.LEGS
        if item is None:
            output(no_armor_specified_m(slot))
            return 
        if self._legs_slot is item:
            output(already_wearing_item_m(item))
            return
        if item.slot_type == slot and self._legs_slot is None:
            self._legs_slot = item
            output(successful_equip(item, slot))
        elif item.slot_type != slot:
            output(wrong_armor_type_m(item, slot))
        elif self._legs_slot is not None:
            output(already_wearing_armor_m(item, self._legs_slot))

    @property
    def boots_slot(self):
        return self._boots_slot

    @boots_slot.setter
    def boots_slot(self, item: Armor):
        slot = Armor_Slot.FEET
        if item is None:
            output(no_armor_specified_m(slot))
            return 
        if self._boots_slot is item:
            output(already_wearing_item_m(item))
            return
        if item.slot_type == slot and self._boots_slot is None:
            self._boots_slot = item
            output(successful_equip(item, slot))
        elif item.slot_type != slot:
            output(wrong_armor_type_m(item, slot))
        elif self._boots_slot is not None:
            output(already_wearing_armor_m(item, self._boots_slot))

    @property
    def shield_slot(self):
        return self._shield_slot

    @shield_slot.setter
    def shield_slot(self, item: Shield):
        slot = Armor_Slot.SHIELD
        if item is None:
            output(no_armor_specified_m(slot))
            return 
        if self._shield_slot is item:
            output(already_wearing_item_m(item))
            return
        if item.slot_type == slot and self._shield_slot is None:
            self._shield_slot = item
            output(successful_equip(item, slot))
        elif item.slot_type != slot:
            output(wrong_armor_type_m(item, slot))
        elif self._shield_slot is not None:
            output(already_wearing_armor_m(item, self._shield_slot))

    def equip(self, item, slot: str):
        slot = slot.lower()
        match(slot):
            case "head":
                self.head_slot = item
                return item is not None and self.head_slot is item
            case "shoulders":
                self.shoulder_slot = item
                return item is not None and self.shoulder_slot is item
            case "chest":
                self.chest_slot = item
                return item is not None and self.chest_slot is item
            case "hands":
                self.hands_slot = item
                return item is not None and self.hands_slot is item
            case "legs":
                self.legs_slot = item
                return item is not None and self.legs_slot is item
            case "feet":
                self.boots_slot = item
                return item is not None and self.boots_slot is item
            case "arm":
                self.shield_slot = item
                return item is not None and self.shield_slot is item
