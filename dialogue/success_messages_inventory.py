from ..utils import Armor_Slot
from equipment.armor import Armor, Shield
from .error_messages_inventory import slot_string
from random import choice

body_part_verbs_equip = {
        "head": ["pull", "slide", "put"],
        "shoulders": ["slide", "pull", "strap", "clasp"],
        "hands": ["pull", "put", "clasp", "slide"],
        "chest": ["pull", "clasp", "strap"],
        "legs": ["pull", "slide", "clasp"],
        "feet": ["pull", "slide", "clasp", "put"],
        "shield arm": ["slide", "clasp", "strap"]
        }

body_part_verbs_unequip = {
        "head": ["pull", "slide", "slip", "remove"],
        "shoulders": ["unclasp", "remove", "unfasten", "slip"],
        "hands": ["pull", "remove", "unclasp", "slip"],
        "chest": ["unclasp", "unfasten", "remove"],
        "legs": ["pull", "unfasten", "slip", "remove"],
        "feet": ["pull", "slip", "remove", "unclasp"],
        "shield arm": ["remove", "slip", "unstrap"]
        }

def successful_equip_m(item: Armor|Shield, slot: Armor_Slot):
    body_part = slot_string(slot) 
    verb = choice(body_part_verbs_equip[body_part]) 
    return f"You {verb} the {item} onto your {body_part}"

def successful_unequip_m(item: Armor|Shield, slot: Armor_Slot):
    body_part = slot_string(slot)
    verb = choice(body_part_verbs_unequip[body_part])
    return f"You {verb} the {item} from your {body_part}"
