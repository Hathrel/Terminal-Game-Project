from ..materials import Material
from ...entities import Armor

class Legs(Armor):
    def __init__(self, name: str, material: Material, defense: int = 3, armor: int = 6, value: int = 60, durability: int = 30):
        super().__init__(name, defense, armor, value, durability, material)
