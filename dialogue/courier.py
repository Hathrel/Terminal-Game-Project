from utils import Message_Enum
from ..entities import Entity
from dataclasses import dataclass

@dataclass
class Dialogue_Courier:
    message: Message_Enum | None = None
    message_entity: Entity | None = None
    message_owner: Entity | None = None
    success_status: bool = True
    
