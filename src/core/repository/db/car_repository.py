
from src.core.base.mysql_repository import MySqlRepository
from src.model.car import Car


class CarRepository(MySqlRepository):
    def __init__(self):
        super().__init__()
        self.cursor = self.connector.cursor()

    def count(self):
        super().count()

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)

