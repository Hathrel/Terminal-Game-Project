
from ...utils import roll_dice


class Weapon:
    def __init__(self, name: str, damage: int, attack: int, blunt: bool):
        self.name: str = name
        self.damage: int = damage
        self.attack: int = attack
        self.blunt: bool = blunt

    def __repr__(self):
        return self.name

    def roll_attack(self, defense: int) -> bool:
        return roll_dice(30) + self.attack >= defense

    def roll_damage(self, armor: int) -> int:
        return roll_dice(self.damage) + self.damage - armor

    def roll_knockout(self, hit: bool) -> bool:
        if self.blunt and hit:
            return roll_dice(100) <= 8
        else:
            return False

#        self.stats = {
#            "Longsword": {"damage": 5, "attack": 10},
#            "Mace": {"damage": 3, "attack": 3},
#            "Dagger": {"damage": 2, "attack": 15},
#            "Greatsword": {"damage": 15, "attack": 5}
#        }

