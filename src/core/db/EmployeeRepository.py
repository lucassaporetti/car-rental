from src.core.base.Repository import Repository
from src.models.Employee import Employee


class EmployeeDao(Repository):
    def __init__(self):
        self.employees = []

    def insert(self, employee: Employee):
        self.employees.append(employee.__dict__)
        print("Employee has been saved !")

    def update(self, employee: Employee):
        idx = self.employees.index(employee)
        self.employees[idx] = employee
        print("Employee has been updated !")

    def delete(self, employee: Employee):
        idx = self.employees.index(employee)
        self.employees.remove(self.employees[idx])
        print("Employee has been deleted !")

    def find_all(self):
        return self.employees

    def find_by_id(self, uuid: str):
        return None

