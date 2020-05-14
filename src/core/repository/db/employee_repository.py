
from src.core.base.mysql_repository import MySqlRepository
from src.model.employee import Employee


class EmployeeRepository(MySqlRepository):
    def __init__(self):
        super().__init__()

    def count(self):
        pass

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)

