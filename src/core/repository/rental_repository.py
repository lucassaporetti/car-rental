import pathlib
import sys

from src.core.base.file_repository import FileRepository
from src.model import rental

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()


class RentalRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{CUR_DIR}/../data/rentals.dat")

    def insert(self, rental: rental):
        super().insert(rental)

    def update(self, rental: rental):
        super().update(rental)

    def delete(self, rental: rental):
        super().delete(rental)

