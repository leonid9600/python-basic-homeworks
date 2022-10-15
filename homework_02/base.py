from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight=10, fuel=40, fuel_consumption=1):
        self.weight = weight
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
