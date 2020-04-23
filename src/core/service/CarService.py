from src.core.base.Service import Service
from src.core.repository.CarRepository import CarRepository

from src.model.Car import Car


class CarService(Service):
    def __init__(self):
        super().__init__(CarRepository())

    def save(self, car: Car):
        super().save(car)

