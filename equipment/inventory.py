"""Track carried items, equipped gear, and coin transactions."""

from ..entities import Armor, Weapon, Shield, Item
from ..equipment import Fists
from .armor_stand import ArmorStand
from ..utils import Armor_Slot, BreakableItem
from ..debugging import success_message_auto, failure_message_auto, generic_message_auto
from uuid import UUID

class Inventory:
    """A character's carried items, equipment, and money."""

    def __init__(self):
        """Start with no carried items, coins, or equipped gear."""
        self.inventory: dict[UUID, Item] = {}
        self.money: int = 0
        self._weapon: Weapon = Fists()
        self.armor: ArmorStand = ArmorStand()

    @property
    def weapon(self) -> Weapon:
        """Return the equipped weapon, defaulting to fists when unarmed."""
        return self._weapon

    def __is_in_inventory(self, item: Item) -> bool:
        if not isinstance(item, Item):
            return False
        else:
            return item.id in self.inventory

    def __is_item(self, item) -> bool:
        return isinstance(item, Item)

    def equip_weapon(self, weapon: Weapon | None) -> bool:
        pass

    def unequip_weapon(self) -> None:
        pass

    def peek_inventory(self) -> None:
        """Display the contents of the footchest and its coin balance."""
        pass

    def equip_armor(self, item: Shield|Armor|None, slot: Armor_Slot) -> bool:
        """Attempt to equip armor through the armor stand and return its result."""
        pass

    def unequip_armor(self, slot: Armor_Slot) -> None:
        """Remove the item in the given slot and store it in the inventory if present."""
        pass

    def buy(self, item: Item) -> bool:
        """Buy a shallow copy of an item if its price is affordable."""
        if self.money <= 0:
            self.money = 0
            generic_message_auto("Out of money")

    def sell(self, item: Item) -> bool:
        """Sell the first carried item with the given name at a durability-adjusted price."""
        pass

    def trash(self, item: Item) -> bool:
        """Discard the item if present and report whether it was removed."""
        pass
