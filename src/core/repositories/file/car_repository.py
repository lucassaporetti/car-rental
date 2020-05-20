from src.core.repositories.file.file_repository import FileRepository
from src.configs import AppConfigs
from src.models.car import Car


class CarRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{AppConfigs.cur_dir}/../data/cars.dat")

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)
