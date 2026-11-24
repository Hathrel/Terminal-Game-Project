from dataclasses import dataclass

@dataclass(frozen=True)
class Material:
    name: str
    stat_mod: float
    block_chance: int
    value_modifier: float

@dataclass(frozen=True)
class Wood(Material):
    name: str = "Wooden"
    stat_mod: float = 0.25
    block_chance: int = 10
    value_modifier: float = 0.1

@dataclass(frozen=True)
class Leather(Material):
    name: str = "Leather"
    stat_mod: float = 0.45 
    block_chance: int = 15
    value_modifier: float = 0.25

@dataclass(frozen=True)
class Iron(Material):
    name: str = "Iron"
    stat_mod: float = 0.75
    block_chance: int = 20
    value_modifier: float = 0.65

@dataclass(frozen=True)
class Bronze(Material):
    name: str = "Bronze"
    stat_mod: float = 1.0
    block_chance: int = 25
    value_modifier: float = 1.0

@dataclass(frozen=True)
class Steel(Material):
    name: str = "Steel"
    stat_mod: float = 1.5
    block_chance: int = 30
    value_modifier: float = 1.5



