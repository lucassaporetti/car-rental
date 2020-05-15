import pathlib
import sys

from src.core.factories import SqlFactory
from src.core.repository.db.mysql_repository import MySqlRepository
from src.model.entity import Entity
from src.model.rental import Rental

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
RENTAL_TEMPLATES = f"{CUR_DIR}/sql/mysql/ddl/rental_templates.properties"


class RentalRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactory(RENTAL_TEMPLATES))

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
