
from ...entities import Weapon
from ..materials import Material

class Spear(Weapon):
    def __init__(self, name: str, material: Material, damage: int = 24, attack: int = 9, value: int = 45, durability: int = 30):
        super().__init__(name, damage, attack, value, durability, material, True)
