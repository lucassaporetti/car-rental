
from src.core.base.mysql_repository import MySqlRepository
from src.model.rental import Rental


class RentalRepository(MySqlRepository):
    def __init__(self):
        super().__init__()

    def count(self):
        pass

    def insert(self, rental: Rental):
        super().insert(rental)

    def update(self, rental: Rental):
        super().update(rental)

    def delete(self, rental: Rental):
        super().delete(rental)

