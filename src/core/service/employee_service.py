from src.core.base.service import Service
from src.core.repository.db.employee_repository import EmployeeRepository
from src.model.employee import Employee


class EmployeeService(Service):
    def __init__(self):
        super().__init__(EmployeeRepository())

    def save(self, employee: Employee):
        super().save(employee)
