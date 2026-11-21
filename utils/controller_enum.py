"""Define the controller types available to characters."""

from enum import Enum

class Controller_Type(Enum):
    """Distinguish player-controlled characters from AI-controlled characters."""

    PLAYER = 0
    AI = 1
