"""
Guitar Class
"""
class Guitar:
    """Guitar Class for storing details about a Guitar."""
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, {self.year} : ${self.cost:,.2f}"

    def get_age(self):
        current_age = 2025 - int(self.year)
        return current_age

    def __lt__(self, other):
        return self.year < other.year

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False