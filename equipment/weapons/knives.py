from ...entities import Weapon
from ..materials import Material

class Knife(Weapon):
    def __init__(self, name: str, material: Material, damage: int = 16, attack: int = 8, value: int = 25, durability: int = 20):
        super().__init__(name, damage, attack, value, durability, material, False)
