from src.model.entity import Entity


class Car(Entity):
    def __init__(self, name: str = None, chassis: str  = None, fuel: str = None, color: str = None, price: str = None, doors: int = None, plate: str = None):
        super().__init__()
        self.name = name
        self.chassis = chassis
        self.fuel = fuel
        self.color = color
        self.price = price
        self.doors = doors
        self.plate = plate
        self.available = True

    def __str__(self):
        return "Name: {}\tChassis: {}\tFuel: {}\tColor: {}\tPrice: {}\tDoors: {}\tPlate: {}\t".format(
            self.name, self.chassis, self.fuel, self.color, self.price, self.doors, self.plate)

