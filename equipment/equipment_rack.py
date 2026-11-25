"""Define the game's predefined armor and weapon items."""

from .armor import *
from .materials import Material

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
