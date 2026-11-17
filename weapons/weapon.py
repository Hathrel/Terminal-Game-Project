from abc import ABC, abstractmethod


class Weapon(ABC):
    damage: int
    attack: int

    @abstractmethod
    def roll_attack(self):
        raise NotImplementedError

    @abstractmethod
    def roll_damage(self):
        raise NotImplementedError

#        self.stats = {
#            "Longsword": {"damage": 5, "attack": 10},
#            "Mace": {"damage": 3, "attack": 3},
#            "Dagger": {"damage": 2, "attack": 15},
#            "Greatsword": {"damage": 15, "attack": 5}
#        }

