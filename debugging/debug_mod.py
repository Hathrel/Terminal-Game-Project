from utils import output
import inspect
from pathlib import Path

class Debugger:
    debugging: bool = False

def debug(message: str) -> None:
    if Debugger.debugging:
        print(message)

def toggle() -> None:
    Debugger.debugging = not Debugger.debugging

def success_message_auto() -> None:
    frame = inspect.currentframe()

    if frame is None or frame.f_back is None:
        return

    caller = frame.f_back

    filename = Path(caller.f_code.co_filename).name
    method = caller.f_code.co_name

    instance = caller.f_locals.get("self")
    class_name = type(instance).__name__ if instance is not None else None

    if class_name:
        details = f"{filename}/{class_name}/{method}"
    else:
        details = f"{filename}/{method}"

    success_message_shim(details)

def success_message_shim(details: str):
    output(f"Success string not implemented for {details}")

def failure_message_auto() -> None:
    frame = inspect.currentframe()

    if frame is None or frame.f_back is None:
        return

    caller = frame.f_back

    filename = Path(caller.f_code.co_filename).name
    method = caller.f_code.co_name

    instance = caller.f_locals.get("self")
    class_name = type(instance).__name__ if instance is not None else None

    if class_name:
        details = f"{filename}/{class_name}/{method}"
    else:
        details = f"{filename}/{method}"

    failure_message_shim(details)

def failure_message_shim(details: str):
    output(f"Failure string not implemented for {details}")

def generic_message_auto(message_type: str) -> None:
    frame = inspect.currentframe()

    if frame is None or frame.f_back is None:
        return

    caller = frame.f_back

    filename = Path(caller.f_code.co_filename).name
    method = caller.f_code.co_name

    instance = caller.f_locals.get("self")
    class_name = type(instance).__name__ if instance is not None else None

    if class_name:
        details = f"{filename}/{class_name}/{method}"
    else:
        details = f"{filename}/{method}"

    generic_message_shim(message_type, details)

def generic_message_shim(message_type: str, details: str):
    output(f"{message_type} string not implemented for {details}")
