from ...entities import Weapon
from ..materials import Material

class OneHandedSword(Weapon):
    def __init__(self, name: str, material: Material, damage: int = 26, attack: int = 5, value: int = 60, durability: int = 40):
        super().__init__(name, damage, attack, value, durability, material, False)

class TwoHandedSword(Weapon):
    def __init__(self, name: str, material: Material, damage: int = 32, attack: int = 3, value: int = 100, durability: int = 50):
        super().__init__(name, damage, attack, value, durability, material, True)

