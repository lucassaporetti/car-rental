from src.core.base.Service import Service
from src.core.repository.EmployeeRepository import EmployeeRepository
from src.models.Employee import Employee


class EmployeeService(Service):
    def __init__(self):
        super().__init__(EmployeeRepository())

    def save(self, employee: Employee):
        super().save(employee)
