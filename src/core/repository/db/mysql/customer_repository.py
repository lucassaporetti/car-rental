from core.enum.database_type import DatabaseType
from core.enum.model import Model
from core.factory.sql_factory_facade import SqlFactoryFacade
from src.core.factory.mysql.customer_factory import CustomerFactory
from src.core.repository.db.mysql.mysql_repository import MySqlRepository
from core.model.customer import Customer
from core.model.entity import Entity


class CustomerRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactoryFacade.get(DatabaseType.MYSQL, Model.EMPLOYEE))

    def count(self):
        pass

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)

    def row_to_entity(self, row: tuple) -> Entity:
        return Customer.of(list(row))
