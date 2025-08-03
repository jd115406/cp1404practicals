"""
CP1404 Practicals
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represents a Silver Service Taxi"""
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise the taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Get the current fare"""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string representation of the taxi"""
        return f"{super().__str__()} plus flagfall of {self.flagfall:.2f}"