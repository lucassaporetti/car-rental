from core.enum.database_type import DatabaseType
from core.enum.model import Model
from core.factory.sql_factory_facade import SqlFactoryFacade
from src.core.factory.mysql.car_factory import CarFactory
from src.core.repository.db.mysql.mysql_repository import MySqlRepository
from core.model.car import Car
from core.model.entity import Entity


class CarRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactoryFacade.get(DatabaseType.MYSQL, Model.CAR))

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)

    def row_to_entity(self, row: tuple) -> Entity:
        return Car.of(list(row))
