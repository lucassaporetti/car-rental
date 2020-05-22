from core.enum.database_type import DatabaseType
from core.enum.model import Model
from core.factory.sql_factory_facade import SqlFactoryFacade
from core.model.employee import Employee
from core.model.entity import Entity
from src.core.repository.db.mysql.mysql_repository import MySqlRepository


class EmployeeRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactoryFacade.get(DatabaseType.MYSQL, Model.EMPLOYEE))

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
