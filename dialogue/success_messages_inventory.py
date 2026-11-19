from ..utils import Armor_Slot
from equipment.armor import Armor, Shield
from .error_messages_inventory import slot_string
from random import choice

body_part_verbs = {
        "head": ["pull", "slide", "put"],
        "shoulders": ["slide", "pull", "strap", "clasp"],
        "hands": ["pull", "put", "clasp", "slide"],
        "chest": ["pull", "clasp", "strap"],
        "legs": ["pull", "slide", "clasp"],
        "feet": ["pull", "slide", "clasp", "put"],
        "shield arm": ["slide", "clasp", "strap"]
        }

def successful_equip(item: Armor|Shield, slot: Armor_Slot):
    body_part = slot_string(slot) 
    verb = choice(body_part_verbs[body_part]) 
    return f"You {verb} the {item} onto your {body_part}"

