from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo):
        new_cargo = self.cargo + cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        temp = self.cargo
        self.cargo = 0
        return temp
