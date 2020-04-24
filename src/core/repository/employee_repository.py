import pathlib
import sys

from src.core.base.repository import Repository
from src.model.employee import Employee

CUR_DIR = pathlib.Path(sys.argv[0]).parent.absolute()


class EmployeeRepository(Repository):
    def __init__(self):
        super().__init__(f"{CUR_DIR}/../data/employees.dat")

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)

