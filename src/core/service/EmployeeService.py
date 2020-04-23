from src.core.base.Service import Service
from src.core.db.EmployeeRepository import EmployeeDao
from src.models.Employee import Employee


class EmployeeService(Service):
    def __init__(self):
        self.dao = EmployeeDao()

    def save(self, employee: Employee):
        existing = self.dao.find_by_id(employee)
        if existing is None:
            self.dao.insert(employee)
        else:
            self.dao.update(employee)

    def list(self):
        return self.dao.find_all()

    def get(self, uuid: str):
        return self.dao.find_by_id(uuid)
