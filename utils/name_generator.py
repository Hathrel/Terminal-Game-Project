"""Generate unique character names from predefined first and last names."""

from random import choice

class Name_Generator:
    """Generate names and track those already assigned."""

    used_names: list[str] = []
    first_names = ["Nicostratus", "Sostratus", "Patricius", "Leonius", "Beringarius", "Nerva", "Saul", "Demetrius", "Viggo", "Philandrus", "Philocrates", "Ladislaus", "Amatus", "Fidelis"]
    last_names = ["Procillus", "Cossus", "Clineas", "Blasio", "Laevinus", "Regillensis", "Pictor", "Libo", "Spinther", "Rutilus", "Mocilla", "Sacerdos", "Sisenna", "Crus", "Potitus"]

    @staticmethod
    def assign_name() -> str:
        """Generate and record an unused name, or raise RuntimeError after failed attempts."""
        name = None
        loop_counter = len(Name_Generator.first_names) * len(Name_Generator.last_names)
        while (name is None or name in Name_Generator.used_names) and loop_counter > 0:
            name = choice(Name_Generator.first_names) + " " + choice(Name_Generator.last_names) 
            loop_counter -= 1
        if name in Name_Generator.used_names:
            raise RuntimeError("Failed to generate a unique name")
        if name is not None:
            Name_Generator.used_names.append(name)
        else:
            raise RuntimeError("Failed to generate a name")
        return name


