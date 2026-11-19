from __future__ import annotations
from utils import roll_dice, Controller
from equipment.weapons import Weapon
from equipment.armor import Armor
from equipment import FISTS
from debugging import debug, Debugger

debug = Debugger.debugging

class Human:
    def __init__(self, name: str, age: int, controller: Controller):
       
        self.name: str = name
        self.experience: int = 0
        self.level: int = 1
        self.age: int = age

        self.strength: int = 1
        self.agility: int = 1
        self.endurance: int = 1
        
        self.health: int = self.endurance * 10 + 90
        self.conscious: bool = True
        self.controller: Controller = controller
        self.is_defending = False
        self._weapon = None
  
    @property
    def alive(self) -> bool:
        return self.health > 0

    @property 
    def conscious_alive(self) -> bool:
        return self.conscious and self.alive

    @property
    def weapon(self) -> Weapon:
        if self._weapon is None:
            return FISTS
        else:
            return self._weapon
      
    @weapon.setter
    def weapon(self, weapon: Weapon|None):
        self._weapon = weapon

    def defend(self):
        if self.conscious_alive:
            self.is_defending = True
