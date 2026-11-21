"""Route game text through a shared output function."""

def output(string: str):
    """
    Standardized shim for outputting text onto any interface

    Modify this to redirect text to whatever medium used
    """
    print(string)
