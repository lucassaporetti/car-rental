from src.core.factories.mysql.car_factory import CarFactory
from src.core.repositories.db.mysql.mysql_repository import MySqlRepository
from core.models.car import Car
from core.models.entity import Entity


class CarRepository(MySqlRepository):
    def __init__(self):
        super().__init__(CarFactory())

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)

    def row_to_entity(self, row: tuple) -> Entity:
        return Car.of(list(row))
