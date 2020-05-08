from src.core.base.service import Service
from src.core.repository.customer_repository import CustomerRepository

from src.model.customer import Customer


class CustomerService(Service):
    def __init__(self):
        super().__init__(CustomerRepository())

    def save(self, customer: Customer):
        super().save(customer)

