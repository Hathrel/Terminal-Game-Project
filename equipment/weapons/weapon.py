
from ...utils import roll_dice


class Weapon:
    def __init__(self, name: str, damage: int, attack: int, value: int):
        self.name: str = name
        self.damage: int = damage
        self.attack: int = attack
        self.value: int = value

    def __repr__(self):
        return self.name

    def roll_attack(self, defense: int) -> bool:
        return roll_dice(30) + self.attack >= defense

    def roll_damage(self, armor: int) -> int:
        return roll_dice(self.damage) + self.damage - armor

class BluntWeapon(Weapon):
    def __init__(self, name: str, damage: int, attack: int, value: int, knockout_chance: int):
        super().__init__(name, damage, attack, value)
        self.knockout = knockout_chance

    def roll_knockout(self, hit: bool) -> bool:
        if hit:
            return self.knockout >= roll_dice(100)
        return False
