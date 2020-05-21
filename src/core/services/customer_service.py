from src.core.enums.database_type import DatabaseType
from src.core.enums.model import Model
from src.core.enums.repository_type import RepositoryType
from src.core.services.service import Service

from core.models.customer import Customer


class CustomerService(Service):
    def __init__(self, repository_type: RepositoryType, database_type: DatabaseType):
        super().__init__(repository_type, database_type, Model.CUSTOMER)

    def save(self, customer: Customer):
        super().save(customer)

    def remove(self, customer: Customer):
        super().remove(customer)

    def get(self, uuid: str) -> Customer:
        entity = super().get(uuid)
        customer = Customer()
        customer.__dict__ = entity.__dict__
        return customer
