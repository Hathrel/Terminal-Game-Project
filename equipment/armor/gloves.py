from ..materials import Material
from ...entities import Armor

class Hands(Armor):
    def __init__(self, name: str, material: Material):
        super().__init__(name, 1, 4, 20, 10, material)
