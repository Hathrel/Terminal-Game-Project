"""Provide random dice rolls for game mechanics."""

import random as r

def roll_dice(faces: int) -> int:
    """Roll a die and return a random integer from one through its face count."""
    return r.randint(1, faces)
