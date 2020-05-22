from core.model.entity import Entity
from src.core.repository.file.file_repository import FileRepository
from core.config.app_configs import AppConfigs
from core.model.car import Car


class CarRepository(FileRepository):
    def __init__(self):
        super().__init__("{}/../data/cars.dat".format(AppConfigs.root_dir()))

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)

    def row_to_entity(self, row: dict) -> Entity:
        return Car.of(list(row.values()))
