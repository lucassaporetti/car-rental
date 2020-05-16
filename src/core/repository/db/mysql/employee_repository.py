from src.core.factory.mysql.employee_factory import EmployeeFactory
from src.core.repository.db.mysql.mysql_repository import MySqlRepository
from src.model.employee import Employee
from src.model.entity import Entity


class EmployeeRepository(MySqlRepository):
    def __init__(self):
        super().__init__(EmployeeFactory())

    def count(self):
        pass

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)

    def row_to_entity(self, row: tuple) -> Entity:
        return Employee.of(list(row))
