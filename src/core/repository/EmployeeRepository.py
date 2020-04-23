from src.core.base.Repository import Repository
from src.model.Employee import Employee


class EmployeeRepository(Repository):
    def __init__(self):
        super().__init__("/home/musik/GIT-Repository/car-rental/data/employees.dat")

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)

