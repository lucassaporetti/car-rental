import pathlib
import sys

from src.core.factories import SqlFactory
from src.core.repository.db.mysql_repository import MySqlRepository
from src.model.car import Car
from src.model.entity import Entity

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
CAR_TEMPLATES = f"{CUR_DIR}/sql/mysql/ddl/car_templates.properties"


class CarRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactory(CAR_TEMPLATES))

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)

    def row_to_entity(self, row: tuple) -> Entity:
        return Car.of(list(row))
