from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.service import Service

from core.model.employee import Employee


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
