from ..materials import Material
from ...entities import Armor

class Hands(Armor):
    def __init__(self, name: str, material: Material, defense: int = 1, armor: int = 4, value: int = 20, durability: int = 10):
        super().__init__(name, defense, armor, value, durability, material)
