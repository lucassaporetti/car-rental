from src.core.repository.file.file_repository import FileRepository
from src.configs import AppConfigs
from src.model.employee import Employee


class EmployeeRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{AppConfigs.cur_dir}/../data/employees.dat")

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)
