from ...entities import Weapon, Blunt
from ..materials import NoMaterial
from sys import maxsize

class Fists(Weapon, Blunt):
    def __init__(self):
        super().__init__("Fists", 4, 3, 0, maxsize, NoMaterial(), False)
        Blunt.__init__(self,4)
