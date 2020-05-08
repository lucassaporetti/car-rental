import pathlib
import sys

from src.core.base.db_repository import DbRepository
from src.model.rental import Rental

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()


class RentalRepository(DbRepository):
    def __init__(self):
        super().__init__(f"{CUR_DIR}/../data/rentals.dat")

    def insert(self, rental: Rental):
        super().insert(rental)

    def update(self, rental: Rental):
        super().update(rental)

    def delete(self, rental: Rental):
        super().delete(rental)

