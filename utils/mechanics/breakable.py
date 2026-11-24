    
class BreakableItem:
    def __init__(self, durability: int):
        self.current_durability = durability
        self.max_durability = durability

    @property
    def broken(self) -> bool:
        """Return whether maximum durability is zero or below."""
        return self.max_durability <= 0

    def damage_item(self, damage: int) -> bool:
        """Apply durability damage when applicable and report whether the shield is broken."""
        self.current_durability -= damage
        if self.current_durability <= 0:
            self.max_durability = 0
        return self.broken

