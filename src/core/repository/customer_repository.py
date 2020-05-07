import pathlib
import sys

from src.core.base.file_repository import FileRepository
from src.model.customer import Customer

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()


class CustomerRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{CUR_DIR}/../data/customers.dat")

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)

