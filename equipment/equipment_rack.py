from armor import Armor, Shield
from weapons import Weapon
from ..utils import Armor_Slot


# Shields
LEATHER_SHIELD = Shield("Leather Shield", 15, 2)
IRON_SHIELD = Shield("Iron Shield", 25, 3)
STEEL_SHIELD = Shield("Steel Shield", 30, 4)

# BODY ARMOR

# Head Armor
LEATHER_HELM = Armor("Leather Helmet", 1, 3, Armor_Slot.HEAD)
IRON_HELM = Armor("Iron Helmet", 2, 4, Armor_Slot.HEAD)
STEEL_HELM = Armor("Steel Helmet", 3, 5, Armor_Slot.HEAD)

# Shoulder Armor
LEATHER_PAULDRON = Armor("Leather Pauldrons", 2, 3, Armor_Slot.SHOULDERS)
IRON_PAULDRON = Armor("Iron Pauldrons", 3, 4, Armor_Slot.SHOULDERS)
STEEL_PAULDRON = Armor("Steel Pauldrons", 4, 5, Armor_Slot.SHOULDERS)

# Chest Armor
LEATHER_VEST = Armor("Leather Vest", 5, 4, Armor_Slot.CHEST)
IRON_CUIRASS = Armor("Iron Cuirass", 6, 6, Armor_Slot.CHEST)
STEEL_PLATE = Armor("Steel PLate Armor", 7, 8, Armor_Slot.CHEST)

# Gloves
LEATHER_GLOVES = Armor("Leather Gloves", 0, 2, Armor_Slot.HANDS)
IRON_GAUNTLETS = Armor("Iron Gauntlets", 1, 3, Armor_Slot.HANDS)
STEEL_GAUNTLETS = Armor("Steel Gauntlets", 2, 4, Armor_Slot.HANDS)

# Leg Armor
LEATHER_PANTS = Armor("Leather Pants", 3, 3, Armor_Slot.LEGS)
IRON_GREAVES = Armor("Iron Greaves", 4, 5, Armor_Slot.LEGS)
STEEL_GREAVES = Armor("Steel Greaves", 5, 7, Armor_Slot.LEGS)

# Boots
LEATHER_BOOTS = Armor("Leather Boots", 1, 2, Armor_Slot.FEET)
IRON_SABATONS = Armor("Iron Sabatons", 2, 3, Armor_Slot.FEET)
STEEL_SABATONS = Armor("Steel Sabatons", 3, 4, Armor_Slot.FEET)

# WEAPONS

# Basic
# Damage - Attack - Blunt
FISTS = Weapon("Fists", 4, 3, True)
