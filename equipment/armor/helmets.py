from ..materials import Material
from ...entities import Armor

class Helmet(Armor):
    def __init__(self, name: str, material: Material):
        super().__init__(name, 2, 4, 30, 20, material)
