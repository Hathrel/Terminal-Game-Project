"""Format equipment errors and supply grammar helpers for item names."""

from equipment import Armor
from equipment import Shield
from utils import Armor_Slot

def plural_check(item:Armor|Shield) -> str:
    """Format an item name with an indefinite article when it is singular."""
    if plural_object(item):
        return f"{item}"
    else:
        if item.name[0].lower() in "aeiou":
            return f"an {item}"
        else:
            return f"a {item}"

def plural_object(item:Armor|Shield) -> bool:
    """Return whether the item's slot calls for plural wording."""
    singular_objects = [
            Armor_Slot.HEAD,
            Armor_Slot.SHIELD,
            Armor_Slot.CHEST
            ]
    return item.slot_type not in singular_objects

def they_it_check(item:Armor|Shield) -> str:
    """Return the pronoun that agrees with the item's grammatical number."""
    if plural_object(item):
        return "they"
    else:
        return "it"

def slot_string(slot: Armor_Slot):
    """Return the display name for an armor slot."""
    match(slot):
        case Armor_Slot.HEAD:
            return "head"
        case Armor_Slot.SHOULDERS:
            return "shoulders"
        case Armor_Slot.CHEST:
            return "chest"
        case Armor_Slot.HANDS:
            return "hands"
        case Armor_Slot.LEGS:
            return "legs"
        case Armor_Slot.FEET:
            return "feet"
        case Armor_Slot.SHIELD:
            return "shield arm"

def no_armor_specified_m(slot: Armor_Slot):
    """Describe an equip attempt made without specifying an item."""
    return f"You mime putting armor onto your {slot_string(slot)}..."

def no_armor_specified_m2(slot: Armor_Slot):
    """Describe an attempt to remove armor from an empty slot."""
    return f"You mime removing armor from your {slot_string(slot)}..."

def already_wearing_armor_m(item: Armor|Shield, slot: Armor|Shield):
    """Explain that another item already occupies the requested slot."""
    return f"You cannot equip {item}, you're already wearing {plural_check(slot)}!"

def already_wearing_item_m(item: Armor|Shield):
    """Explain that the requested item is already equipped."""
    return f"You're already wearing {item}!"

def wrong_armor_type_m(item: Armor|Shield, slot_type: Armor_Slot):
    """Describe what happens when an item is tried on the wrong slot."""
    verb = "fall" if plural_object(item) else "falls"
    return f"You try to put the {item} on your {slot_string(slot_type)}. {they_it_check(item).capitalize()} {verb} off..."
