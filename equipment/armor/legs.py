
from ..materials import Material
from ...entities import Armor

class Cuisses(Armor):
    def __init__(self, material: Material):
        super().__init__("Cuisses", 3, 6, 60, 30, material)
