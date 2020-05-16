from src.core.repository.file.file_repository import FileRepository
from src.main import Main
from src.model.customer import Customer


class CustomerRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{Main.cur_dir}/../data/customers.dat")

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)

