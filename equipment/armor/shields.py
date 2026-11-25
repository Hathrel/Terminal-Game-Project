from ...entities import Shield
from ..materials import Material

class ShieldArm(Shield):
    def __init__(self,name: str, material: Material, defense: int = 5, value: int = 40, durability: int = 40):
        super().__init__(name, defense, value, durability, material) 
