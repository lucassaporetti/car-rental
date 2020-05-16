from src.core.repository.file.file_repository import FileRepository
from src.main import Main
from src.model.employee import Employee


class EmployeeRepository(FileRepository):
    def __init__(self):
        super().__init__(f"{Main.cur_dir}/../data/employees.dat")

    def insert(self, employee: Employee):
        super().insert(employee)

    def update(self, employee: Employee):
        super().update(employee)

    def delete(self, employee: Employee):
        super().delete(employee)
