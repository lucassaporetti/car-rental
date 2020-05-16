from src.core.repository.file.file_repository import FileRepository
from src.main import Main
from src.model.car import Car


class CarRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{Main.cur_dir}/../data/cars.dat")

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)
