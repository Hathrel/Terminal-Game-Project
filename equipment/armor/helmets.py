from ..materials import Material
from ...entities import Armor

class Helmet(Armor):
    def __init__(self, material: Material):
        super().__init__("Helmet", 2, 4, 30, 20, material)
