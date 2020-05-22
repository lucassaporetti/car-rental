from core.enum.access_type import AccessType
from core.model.employee import Employee
from core.model.user import User


class UserDto(User):
    def __init__(self, entity_id: str = None, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None, drv_license: str = None, access_type: str = None, hired_date: str = None,
                 salary: float = None):
        super().__init__(entity_id, name, age, address, phone, email)
        self.drv_license = drv_license
        self.access_type = access_type
        self.hired_date = hired_date
        self.salary = salary

    def __str__(self):
        return "{} | {} | {} | {} | {}".format(
            super().__str__(), self.drv_license, self.access_type, self.hired_date, self.salary)

    class Builder(Employee.Builder):
        def __init__(self):
            self.drv_license = None
            self.access_type = None
            self.hired_date = None
            self.salary = None

        def with_drv_license(self, drv_license: str):
            self.drv_license = drv_license
            return self

        def with_access_type(self, access_type: AccessType):
            self.access_type = access_type
            return self

        def with_hired_date(self, hired_date: str):
            self.hired_date = hired_date
            return self

        def with_salary(self, salary: float):
            self.salary = salary
            return self

        def build(self):
            return UserDto(
                self.uuid, self.name, self.age, self.address, self.phone, self.email, self.drv_license,
                self.access_type, self.hired_date, self.salary
            )