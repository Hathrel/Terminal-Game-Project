from ...entities import Weapon, Blunt
from ..materials import Material

class OneHandedMace(Weapon, Blunt):
    def __init__(self, name: str, material: Material, damage: int = 24, attack: int = 4, value: int = 50, durability: int = 45):
        super().__init__(name, damage, attack, value, durability, material, False)

class TwoHandedMace(Weapon, Blunt):
    def __init__(self, name: str, material: Material, damage: int = 30, attack: int = 2, value: int = 80, durability: int = 60):
        super().__init__(name, damage, attack, value, durability, material, True)
