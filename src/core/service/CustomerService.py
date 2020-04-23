from src.core.base.Service import Service
from src.core.repository.CustomerRepository import CustomerRepository

from src.model.Customer import Customer


class CustomerService(Service):
    def __init__(self):
        super().__init__(CustomerRepository())

    def save(self, customer: Customer):
        super().save(customer)

