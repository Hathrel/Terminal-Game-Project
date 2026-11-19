from equipment import Armor
from equipment import Shield
from utils import Armor_Slot

def plural_check(item:Armor|Shield) -> str:
    if plural_object(item):
        return f"{item}"
    else:
        if item.name[0].lower() in "aeiou":
            return f"an {item}"
        else:
            return f"a {item}"

def plural_object(item:Armor|Shield) -> bool:
    singular_objects = [
            Armor_Slot.HEAD,
            Armor_Slot.SHIELD,
            Armor_Slot.CHEST
            ]
    return item.slot_type not in singular_objects

def they_it_check(item:Armor|Shield) -> str:
    if plural_object(item):
        return "they"
    else:
        return "it"

def slot_string(slot: Armor_Slot):
    match(slot):
        case Armor_Slot.HEAD:
            return "head"
        case Armor_Slot.SHOULDERS:
            return "shoulders"
        case Armor_Slot.CHEST:
            return "chest"
        case Armor_Slot.HANDS:
            return "hands"
        case Armor_Slot.FEET:
            return "feet"
        case Armor_Slot.SHIELD:
            return "shield arm"

def already_wearing_armor_m(item: Armor|Shield, slot: Armor|Shield):
    print(f"You cannot equip {item}, you're already wearing {plural_check(slot)}!")

def wrong_armor_type_m(item: Armor|Shield, slot_type: Armor_Slot):
    verb = "fall" if plural_object(item) else "falls"
    print(f"You try to put the {item} on your {slot_string(slot_type)}. {they_it_check(item).capitalize()} {verb} off...") 
