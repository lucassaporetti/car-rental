from src.core.base.service import Service
from src.core.repository.db.car_repository import CarRepository

from src.model.car import Car


class CarService(Service):
    def __init__(self):
        super().__init__(CarRepository())

    def save(self, car: Car):
        super().save(car)

