from .entity import Entity

class Item(Entity):
    def __init__(self, name: str, value: int):
        super().__init__(name)
        self.value = value
