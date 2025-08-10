"""
CP1404 Practicals
"""

from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Driver the car, based on reliability"""
        random_reliability = randint(1,100)
        if random_reliability >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
