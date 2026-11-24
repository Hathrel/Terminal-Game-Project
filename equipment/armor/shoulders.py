from ..materials import Material
from ...entities import Armor

class Pauldrons(Armor):
    def __init__(self, material: Material):
        super().__init__("Pauldrons", 2, 4, 30, 20, material)
