"""Define the controller types available to characters."""

from enum import Enum, auto

class Controller_Type(Enum):
    """Distinguish player-controlled characters from AI-controlled characters."""

    PLAYER = auto()
    AI = auto()
