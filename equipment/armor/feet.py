from ..materials import Material
from ...entities import Armor

class Feet(Armor):
    def __init__(self, name: str, material: Material):
        super().__init__(name, 2, 4, 20, 10, material)
