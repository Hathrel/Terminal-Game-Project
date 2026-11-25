"""Track equipped armor and handle changes to equipment slots."""
from types import coroutine

from entities import Armor, Shield
from .armor import (
    Helmet,
    Shoulders,
    Chest,
    Hands,
    Legs,
    Feet,
    ShieldArm
        )
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
from ..utils import Armor_Slot, Armor_Result, Message_Enum
from ..dialogue import Dialogue_Courier
from debugging import failure_message_auto, success_message_auto


class ArmorStand:
    """The armor and shield slots for a character's worn equipment."""

    def __init__(self):
        """Initialize every equipment slot as empty."""
        self.head_slot: Helmet | None = None
        self.shoulder_slot: Shoulders | None = None
        self.chest_slot: Chest | None = None
        self.hands_slot: Hands | None = None
        self.legs_slot: Legs | None = None
        self.boots_slot: Feet | None = None
        self.shield_slot: ShieldArm | None = None

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

    def equip_helmet(self, helmet: Helmet) -> Dialogue_Courier:
        courier = Dialogue_Courier()
        if helmet is None:
            courier.message = Armor_Result.NO_ARMOR_SPECIFIED_EQUIP
            courier.success_status = False

        elif not isinstance(helmet, Helmet):
            courier.message = Armor_Result.WRONG_ARMOR_TYPE
            courier.success_status = False
            courier.message_entity = helmet

        elif self.head_slot and self.head_slot is helmet:
            courier.message = Armor_Result.ALREADY_WEARING
            courier.success_status = False
            courier.message_entity = helmet
        


        return courier



    def equip(self, item: Armor | Shield | None, armor_slot: Armor_Slot) -> Dialogue_Courier:
        """Attempt to equip an item in the requested slot and report success."""
        slot: str = slot_string(armor_slot)

        match slot:
            case "head":
                current = self.head_slot
                if item is None:
                    return Armor_Result.NO_ARMOR_SPECIFIED_EQUIP
                if current is item:
                    return Armor_Result.ALREADY_WEARING
                if not isinstance(item, Helmet):
                    return Armor_Result.WRONG_ARMOR_TYPE
                if current is not None:
                    return Armor_Result.ALREADY_WEARING
                self.head_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.head_slot is item

            case "shoulders":
                current = self.shoulder_slot
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if not isinstance(item, Shoulders):
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.shoulder_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.shoulder_slot is item

            case "chest":
                current = self.chest_slot
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if not isinstance(item, Chest):
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.chest_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.chest_slot is item

            case "hands":
                current = self.hands_slot
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if not isinstance(item, Hands):
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.hands_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.hands_slot is item

            case "legs":
                current = self.legs_slot
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if not isinstance(item, Legs):
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.legs_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.legs_slot is item

            case "feet":
                current = self.boots_slot
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if not isinstance(item, Feet):
                    output(wrong_armor_type_m(item, armor_slot))
                    return False
                if current is not None:
                    output(already_wearing_armor_m(item, current))
                    return False
                self.boots_slot = item
                output(successful_equip_m(item, armor_slot))
                return self.boots_slot is item

            case "shield arm":
                current = self.shield_slot
                if item is None:
                    output(no_armor_specified_m(armor_slot))
                    return False
                if current is item:
                    output(already_wearing_item_m(item))
                    return True
                if not isinstance(item, ShieldArm):
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
