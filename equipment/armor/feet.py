from ..materials import Material
from ...entities import Armor

class Chausses(Armor):
    def __init__(self, material: Material):
        super().__init__("Chausses", 2, 4, 20, 10, material)
