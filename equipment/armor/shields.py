from ...entities import Shield
from ..materials import Material

class ShieldArm(Shield):
    def __init__(self,name: str, material: Material):
        super().__init__(name, 5, 40, 40, material) 
