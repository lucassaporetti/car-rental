from src.core.base.Repository import Repository
from src.models.Car import Car


class CarRepository(Repository):
    def __init__(self):
        super().__init__("/home/musik/GIT-Repository/car-rental/data/cars.dat")

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)

