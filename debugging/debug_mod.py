
class Debugger:
    debugging: bool = False

def debug(message: str) -> None:
    if Debugger.debugging:
        print(message)

def toggle() -> None:
    Debugger.debugging = not Debugger.debugging


