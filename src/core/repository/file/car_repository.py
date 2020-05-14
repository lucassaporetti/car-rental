import pathlib
import sys

from src.core.base.file_repository import FileRepository
from src.model.car import Car

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()


class CarRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{CUR_DIR}/../data/cars.dat")

    def insert(self, car: Car):
        super().insert(car)

    def update(self, car: Car):
        super().update(car)

    def delete(self, car: Car):
        super().delete(car)
