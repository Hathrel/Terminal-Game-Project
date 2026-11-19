
from ..equipment import Inventory

def inventory_check_m(inventory: Inventory) -> str:
    items = inventory.inventory
    money = inventory.money

    if not items:
        output_string = "Your footchest is empty."
    elif len(items) == 1:
        output_string = f"In your footchest, you find {items[0]}."
    elif len(items) == 2:
        output_string = (
            f"In your footchest, you find {items[0]} and {items[1]}."
        )
    else:
        item_list = ", ".join(str(item) for item in items[:-1])
        output_string = (
            f"In your footchest, you find {item_list}, and {items[-1]}."
        )

    if money > 0:
        output_string += f" You also find {money} coins."

    return output_string
