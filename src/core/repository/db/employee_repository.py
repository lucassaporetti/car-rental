import pathlib
import sys

from src.core.base.mysql_repository import MySqlRepository
from src.core.factories import SqlFactory
from src.model.employee import Employee

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()
EMPLOYEE_TEMPLATES = f"{CUR_DIR}/sql/mysql/ddl/employee_templates.properties"


class EmployeeRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactory(EMPLOYEE_TEMPLATES))

    def count(self):
        pass

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)

