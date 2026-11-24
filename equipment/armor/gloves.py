from ..materials import Material
from ...entities import Armor

class Gauntlets(Armor):
    def __init__(self, material: Material):
        super().__init__("Gauntlets", 1, 4, 20, 10, material)
