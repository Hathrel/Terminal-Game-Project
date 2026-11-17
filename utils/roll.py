import random as r

def roll_int(num1, num2):
    roll = r.randint(num1, num2)
    return roll

def roll_dice(faces: int):
    return r.randint(1, faces)
