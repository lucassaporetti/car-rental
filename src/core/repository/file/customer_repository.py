from src.core.repository.file.file_repository import FileRepository
from core.config.app_configs import AppConfigs
from core.model.customer import Customer


class CustomerRepository(FileRepository):
    def __init__(self):
        super().__init__("{}/../data/customers.dat".format(AppConfigs.root_dir()))

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)
