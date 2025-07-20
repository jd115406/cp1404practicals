class ProgrammingLanguage:
    """Programming Language class takes language name, typing style, reflection and year"""
    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if the language is dynamic."""
        return self.typing == "Dynamic"