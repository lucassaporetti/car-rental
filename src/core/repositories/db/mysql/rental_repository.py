from src.core.factories.mysql.rental_factory import RentalFactory
from src.core.repositories.db.mysql.mysql_repository import MySqlRepository
from src.models.entity import Entity
from src.models.rental import Rental


class RentalRepository(MySqlRepository):
    def __init__(self):
        super().__init__(RentalFactory())

    def count(self):
        pass

    def insert(self, rental: Rental):
        super().insert(rental)

    def update(self, rental: Rental):
        super().update(rental)

    def delete(self, rental: Rental):
        super().delete(rental)

    def row_to_entity(self, row: tuple) -> Entity:
        return Rental.of(list(row))
