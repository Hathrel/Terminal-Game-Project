from uuid import uuid4, UUID

class Entity:
    def __init__(self, name: str):
        self._id: UUID = uuid4()
        self._name: str = name

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self):
        return self.name
