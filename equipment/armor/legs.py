from ..materials import Material
from ...entities import Armor

class Legs(Armor):
    def __init__(self, name: str, material: Material):
        super().__init__(name, 3, 6, 60, 30, material)
