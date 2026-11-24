from ...entities import Shield
from ..materials import Material

class ShieldArm(Shield):
    def __init__(self, material: Material):
        super().__init__("Shield", 5, 40, 40, material) 
