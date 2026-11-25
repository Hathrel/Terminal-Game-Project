"""Define the game's predefined armor and weapon items."""

from .armor import *
from .materials import Material
from .weapons import *
# ---Armor---

def create_debug_helmet(material: Material) -> Helmet:
    return Helmet("Debug Helmet", material)

def create_debug_shoulders(material: Material) -> Shoulders:
    return Shoulders("Debug Pauldrons", material)

def create_debug_chest(material: Material) -> Chest:
    return Chest("Debug Chest", material)

def create_debug_hands(material: Material) -> Hands:
    return Hands("Debug Gloves", material)

def create_debug_legs(material: Material) -> Legs:
    return Legs("Debug Cuisses", material)

def create_debug_feet(material: Material) -> Feet:
    return Feet("Debug Greaves", material)

def create_debug_shield(material: Material) -> ShieldArm:
    return ShieldArm("Debug Shield", material)

# ---Weapons---

def create_debug_knife(material: Material) -> Knife:
    return Knife("Debug Knife", material)

def create_debug_longsword(material: Material) -> OneHandedSword:
    return OneHandedSword("Debug Longsword", material)

def create_debug_greatsword(material: Material) -> TwoHandedSword:
    return TwoHandedSword("Debug Greatsword", material)

def create_debug_mace(material: Material) -> OneHandedMace:
    return OneHandedMace("Debug Mace", material)

def create_debug_warhammer(material: Material) -> TwoHandedMace:
    return TwoHandedMace("Debug Warhammer", material)

def create_debug_spear(material: Material) -> Spear:
    return Spear("Debug Spear", material)
