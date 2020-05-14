
from src.core.base.mysql_repository import MySqlRepository
from src.model.customer import Customer


class CustomerRepository(MySqlRepository):
    def __init__(self):
        super().__init__()

    def count(self):
        pass

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)

