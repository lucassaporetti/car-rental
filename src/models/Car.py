from src.models.Entity import Entity


class Car(Entity):
    def __init__(self, name: str, chassis: str, fuel: str, color: str, price: str, doors: int, plate: str):
        super().__init__()
        self.name = name
        self.chassis = chassis
        self.fuel = fuel
        self.color = color
        self.price = price
        self.doors = doors
        self.plate = plate

    def __str__(self):
        return "Name: {}\tChassis: {}\tFuel: {}\tColor: {}\tPrice: {}\tDoors: {}\tPlate: {}\t".format(
            self.name, self.chassis, self.fuel, self.color, self.price, self.doors, self.plate)

