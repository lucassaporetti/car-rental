from src.core.enums.database_type import DatabaseType
from src.core.enums.model import Model
from src.core.enums.repository_type import RepositoryType
from src.core.repositories.repository_facade import RepositoryFacade
from src.core.services.service import Service

from src.models.employee import Employee


class EmployeeService(Service):
    def __init__(self, repository_type: RepositoryType, database_type: DatabaseType):
        super().__init__(repository_type, database_type, Model.EMPLOYEE)

    def save(self, employee: Employee):
        super().save(employee)

    def remove(self, employee: Employee):
        super().remove(employee)

    def get(self, uuid: str) -> Employee:
        entity = super().get(uuid)
        employee = Employee()
        employee.__dict__ = entity.__dict__
        return employee
