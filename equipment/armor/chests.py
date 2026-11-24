from ..materials import Material
from ...entities import Armor

class Cuirass(Armor):
    def __init__(self, material: Material):
        super().__init__("Cuirass", 4, 8, 80, 40, material)
