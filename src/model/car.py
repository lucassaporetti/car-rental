from src.core.enum.color import Color
from src.core.enum.fuel import Fuel
from src.core.enum.yes_no import YesNo
from src.model.entity import Entity


class Car(Entity):
    @staticmethod
    def of(values: list):
        return Car(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])

    def __init__(self, entity_id: str, name: str = None, chassis: str = None, color: Color = None, doors: int = None,
                 fuel: Fuel = None, plate: str = None, price: str = None, available: YesNo = YesNo.YES):
        super().__init__(entity_id)
        self.name = name
        self.chassis = chassis
        self.color = color
        self.doors = doors
        self.fuel = fuel
        self.plate = plate
        self.price = price
        self.available = available

    def __str__(self):
        return "Name: {}\tChassis: {}\tColor: {}\tDoors: {}\tFuel: {}\tPlate: {}\tPrice: {}\tAvailable: {}".format(
            self.name, self.chassis, self.color, self.doors, self.fuel, self.plate, self.price, self.available.name)
