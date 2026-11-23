"""Track equipped armor and handle changes to equipment slots."""

from armor import Armor, Shield, BreakableArmor, BreakableShield
from ..dialogue import (
    already_wearing_armor_m,
    wrong_armor_type_m,
    no_armor_specified_m,
    already_wearing_item_m,
    successful_equip_m,
    successful_unequip_m,
    no_armor_specified_m2,
    slot_string,
)
from ..utils import Armor_Slot, output
from debugging import failure_message_auto, success_message_auto


class ArmorStand:
    """The armor and shield slots for a character's worn equipment."""

    def __init__(self):
        """Initialize every equipment slot as empty."""
        self.head_slot: Armor | None = None
        self.shoulder_slot: Armor | None = None
        self.chest_slot: Armor | None = None
        self.hands_slot: Armor | None = None
        self.legs_slot: Armor | None = None
        self.boots_slot: Armor | None = None
        self.shield_slot: Shield | None = None

    # -------- Aggregate Statistics --------

    @property
    def defense(self) -> int:
        """Return total defense from equipped armor and the shield."""
        defense = 0
        if self.head_slot:
            defense += self.head_slot.defense
        if self.shoulder_slot:
            defense += self.shoulder_slot.defense
        if self.chest_slot:
            defense += self.chest_slot.defense
        if self.hands_slot:
            defense += self.hands_slot.defense
        if self.legs_slot:
            defense += self.legs_slot.defense
        if self.boots_slot:
            defense += self.boots_slot.defense
        if self.shield_slot:
            defense += self.shield_slot.defense
        return defense

    @property
    def armor(self) -> int:
        """Return total armor protection from the six worn armor slots."""
        armor = 0
        if self.head_slot:
            armor += self.head_slot.armor
        if self.shoulder_slot:
            armor += self.shoulder_slot.armor
        if self.chest_slot:
            armor += self.chest_slot.armor
        if self.hands_slot:
            armor += self.hands_slot.armor
        if self.legs_slot:
            armor += self.legs_slot.armor
        if self.boots_slot:
            armor += self.boots_slot.armor
        return armor

    # -------- Equip --------

    def equip(self, item: Armor | Shield | None, armor_slot: Armor_Slot) -> bool:
        """Attempt to equip an item in the requested slot and report success."""
        slot: str = slot_string(armor_slot)

        match slot:
            case "head":
                armor_slot = Armor_Slot.HEAD
                current = self.head_slot
                if item is BreakableArmor and item.broken:
                    failure_message_auto()
                    return False
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if item.slot_type != armor_slot:
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.head_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.head_slot is item

            case "shoulders":
                armor_slot = Armor_Slot.SHOULDERS
                current = self.shoulder_slot
                if item is BreakableArmor and item.broken:
                    failure_message_auto()
                    return False
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if item.slot_type != armor_slot:
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.shoulder_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.shoulder_slot is item

            case "chest":
                armor_slot = Armor_Slot.CHEST
                current = self.chest_slot
                if item is BreakableArmor and item.broken:
                    failure_message_auto()
                    return False
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if item.slot_type != armor_slot:
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.chest_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.chest_slot is item

            case "hands":
                armor_slot = Armor_Slot.HANDS
                current = self.hands_slot
                if item is BreakableArmor and item.broken:
                    failure_message_auto() 
                    return False
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if item.slot_type != armor_slot:
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.hands_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.hands_slot is item

            case "legs":
                armor_slot = Armor_Slot.LEGS
                current = self.legs_slot
                if item is BreakableArmor and item.broken:
                    failure_message_auto()
                    return False               
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if item.slot_type != armor_slot:
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.legs_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.legs_slot is item

            case "feet":
                armor_slot = Armor_Slot.FEET
                current = self.boots_slot
                if item is BreakableArmor and item.broken:
                    failure_message_auto()
                    return False               
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if item.slot_type != armor_slot:
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.boots_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.boots_slot is item

            case "shield arm":
                armor_slot = Armor_Slot.SHIELD
                current = self.shield_slot
                if item is BreakableArmor and item.broken:
                    failure_message_auto()
                    return False               
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if item.slot_type != armor_slot:
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.shield_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.shield_slot is item

            case _:
                return False

    # -------- Unequip --------

    def unequip(self, armor_slot: Armor_Slot) -> Armor | Shield | None:
        """Clear the requested slot and return its item, or return None if empty."""
        slot: str = slot_string(armor_slot)

        match slot:
            case "head":
                if self.head_slot is None:
                    output(no_armor_specified_m2(Armor_Slot.HEAD))
                    return 
                output(successful_unequip_m(self.head_slot, Armor_Slot.HEAD))
                item_return = self.head_slot
                self.head_slot = None
                return item_return

            case "shoulders":
                if self.shoulder_slot is None:
                    output(no_armor_specified_m2(Armor_Slot.SHOULDERS))
                    return 
                output(successful_unequip_m(self.shoulder_slot, Armor_Slot.SHOULDERS))
                item_return = self.shoulder_slot
                self.shoulder_slot = None
                return item_return

            case "chest":
                if self.chest_slot is None:
                    output(no_armor_specified_m2(Armor_Slot.CHEST))
                    return 
                output(successful_unequip_m(self.chest_slot, Armor_Slot.CHEST))
                item_return = self.chest_slot
                self.chest_slot = None
                return item_return

            case "hands":
                if self.hands_slot is None:
                    output(no_armor_specified_m2(Armor_Slot.HANDS))
                    return 
                output(successful_unequip_m(self.hands_slot, Armor_Slot.HANDS))
                item_return = self.hands_slot
                self.hands_slot = None
                return item_return

            case "legs":
                if self.legs_slot is None:
                    output(no_armor_specified_m2(Armor_Slot.LEGS))
                    return 
                output(successful_unequip_m(self.legs_slot, Armor_Slot.LEGS))
                item_return = self.legs_slot
                self.legs_slot = None
                return item_return

            case "feet":
                if self.boots_slot is None:
                    output(no_armor_specified_m2(Armor_Slot.FEET))
                    return 
                output(successful_unequip_m(self.boots_slot, Armor_Slot.FEET))
                item_return = self.boots_slot
                self.boots_slot = None
                return item_return

            case "shield arm":
                if self.shield_slot is None:
                    output(no_armor_specified_m2(Armor_Slot.SHIELD))
                    return
                output(successful_unequip_m(self.shield_slot, Armor_Slot.SHIELD))
                item_return = self.shield_slot
                self.shield_slot = None
                return item_return
