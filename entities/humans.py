from __future__ import annotations
from utils import roll_dice, Controller
from equipment.weapons import Weapon
from equipment import FISTS, ArmorStand
from debugging import debug, Debugger

class Human:
    def __init__(self, name: str, age: int, controller: Controller):
       
        self.name: str = name
        self.experience: int = 0
        self.level: int = 1
        self.age: int = age

        self.strength: int = 1 # Damage Bonus half of strength value rounded down
        self.dexterity: int = 1 # Attack Bonus, Luck % chance at a second attack
        self.agility: int = 1 # Defense Bonus and Dodge bonus(?) and luck % chance to block without defending
        self.fortitude: int = 1 # Health*10 bonus, modifier contributes to armor bonus, luck based chance on non-combat Recovery of fortitude number of HP
        self.luck: int = 1 # 1% chance at every luck level for luck*10 exp every time exp is earned, and a luck level bonus to rolls
        
        self.health: int = self.fortitude * 10 + 90
        self.conscious: bool = True
        self.controller: Controller = controller
        self.is_defending = False
        self._weapon: Weapon|None = None
        self.armor: ArmorStand = ArmorStand() 

# -------Attributes Modifiers-------

    @property
    def strength_mod(self) -> int:
        return self.strength//2

    @property
    def dexterity_mod(self) -> int:
        return self.dexterity//3

    @property
    def agility_mod(self) -> int:
        return self.agility//3

    @property
    def fortitude_mod(self) -> int:
        return self.fortitude//3

# -----Luck Rolls and Modifiers-----

    @property
    def luck_roll(self) -> bool:
        return min(self.luck, 65) >= roll_dice(100)

    @property
    def luck_stat_boost(self) -> int:
        if self.luck_roll:
            return self.luck
        else:
            return 0

    @property
    def luck_exp_boost(self) -> int:
        if self.luck_roll:
            return self.luck * 10
        else:
            return 0

    @property
    def second_attack_roll(self) -> bool:
        return min(self.dexterity_mod * self.luck, 65) >= roll_dice(100)

    @property
    def instinct_block_roll(self) -> bool:
        return min(self.agility_mod * self.luck, 65) >= roll_dice(100)

    @property
    def fortitude_recovery(self) -> int:
        if min(self.fortitude_mod * self.luck, 65) >= roll_dice(100):
            return self.fortitude
        else:
            return 0

# -------------Checks---------------

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

# -----------Actions---------------

    def defend(self):
        if self.conscious_alive:
            self.is_defending = True
