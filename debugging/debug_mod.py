"""Provide debug output and placeholders for unwritten game messages."""

from utils import output
import inspect
from pathlib import Path

class Debugger:
    """Store the shared flag that controls debug output."""

    debugging: bool = False

def debug(message: str) -> None:
    """Print a message when debugging is enabled."""
    if Debugger.debugging:
        print(message)

def toggle() -> None:
    """Flip the shared debugging flag."""
    Debugger.debugging = not Debugger.debugging

def success_message_auto() -> None:
    """Report a missing success message using the caller's location."""
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
    """Print a placeholder for a missing success message."""
    output(f"Success string not implemented for {details}")

def failure_message_auto() -> None:
    """Report a missing failure message using the caller's location."""
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
    """Print a placeholder for a missing failure message."""
    output(f"Failure string not implemented for {details}")

def generic_message_auto(message_type: str) -> None:
    """Report a missing message of the given type using the caller's location."""
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
    """Print a placeholder for the given message type and location."""
    output(f"{message_type} string not implemented for {details}")
