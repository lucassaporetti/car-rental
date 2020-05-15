import pathlib
import sys

from src.core.base.mysql_repository import MySqlRepository
from src.core.factories import SqlFactory
from src.model.customer import Customer

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
CUSTOMER_TEMPLATES = f"{CUR_DIR}/sql/mysql/ddl/customer_templates.properties"


class CustomerRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactory(CUSTOMER_TEMPLATES))

    def count(self):
        pass

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)

    def row_to_entity(self, row: tuple) -> dict:
        return Customer.of(list(row)).__dict__
