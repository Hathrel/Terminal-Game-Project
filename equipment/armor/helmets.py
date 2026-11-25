from ..materials import Material
from ...entities import Armor

class Helmet(Armor):
    def __init__(self, name: str, material: Material, defense: int = 2, armor: int = 4, value: int = 30, durability: int = 20):
        super().__init__(name, defense, armor, value, durability, material)
