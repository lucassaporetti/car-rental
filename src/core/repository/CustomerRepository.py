from src.core.base.Repository import Repository
from src.model.Customer import Customer


class CustomerRepository(Repository):
    def __init__(self):
        super().__init__("/home/musik/GIT-Repository/car-rental/data/customers.dat")

    def insert(self, customer: Customer):
        super().insert(customer)

    def update(self, customer: Customer):
        super().update(customer)

    def delete(self, customer: Customer):
        super().delete(customer)

