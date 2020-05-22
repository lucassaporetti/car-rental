from src.core.repository.file.file_repository import FileRepository
from core.config.app_configs import AppConfigs
from core.model.employee import Employee


class EmployeeRepository(FileRepository):
    def __init__(self):
        super().__init__("{}/../data/employees.dat".format(AppConfigs.root_dir()))

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)
