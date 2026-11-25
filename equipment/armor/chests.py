from ..materials import Material
from ...entities import Armor

class Chest(Armor):
    def __init__(self, name: str, material: Material, defense: int = 4, armor: int = 8, value: int = 80, durability: int = 40):
        super().__init__(name, defense, armor, value, durability, material)
