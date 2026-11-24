from ..materials import Material
from ...entities import Armor

class Chest(Armor):
    def __init__(self, name: str, material: Material):
        super().__init__(name, 4, 8, 80, 40, material)
