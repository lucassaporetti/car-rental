from src.core.factories.mysql.customer_factory import CustomerFactory
from src.core.repositories.db.mysql.mysql_repository import MySqlRepository
from src.models.customer import Customer
from src.models.entity import Entity


class CustomerRepository(MySqlRepository):
    def __init__(self):
        super().__init__(CustomerFactory())

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
