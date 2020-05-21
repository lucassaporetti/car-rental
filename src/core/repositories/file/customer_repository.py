from src.core.repositories.file.file_repository import FileRepository
from core.config.app_configs import AppConfigs
from src.models.customer import Customer


class CustomerRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{AppConfigs.root_dir()}/../data/customers.dat")

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)
