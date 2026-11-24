from uuid import uuid4, UUID

class Entity:
    def __init__(self):
        self._id: UUID = uuid4()

    @property
    def id(self) -> UUID:
        return self._id
