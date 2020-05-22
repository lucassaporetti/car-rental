from core.enum.database_type import DatabaseType
from core.enum.model import Model
from core.factory.sql_factory_facade import SqlFactoryFacade
from core.model.entity import Entity
from core.model.rental import Rental
from src.core.repository.db.mysql.mysql_repository import MySqlRepository


class RentalRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactoryFacade.get(DatabaseType.MYSQL, Model.RENTAL))

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
