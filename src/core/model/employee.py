import uuid

from src.core.enum.access_type import AccessType
from core.model.user import User


class Employee(User):
    @staticmethod
    def of(values: list):
        return Employee(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7],
                        values[8])

    def __init__(self, entity_id: str = None, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None, access_type: str = None, hired_date: str = None, salary: float = None):
        super().__init__(entity_id, name, age, address, phone, email)
        self.access_type = access_type
        self.hired_date = hired_date
        self.salary = salary

    def __str__(self):
        return "{} | {} | {} | {}".format(
            super().__str__(), self.access_type, self.hired_date, self.salary)

    class Builder:

        def __init__(self):
            self.uuid = str(uuid.uuid4())
            self.name = None
            self.age = None
            self.address = None
            self.phone = None
            self.email = None
            self.access_type = None
            self.hired_date = None
            self.salary = None

        def with_name(self, name: str):
            self.name = name
            return self

        def with_age(self, age: int):
            self.age = age
            return self

        def with_address(self, address: str):
            self.address = address
            return self

        def with_phone(self, phone: str):
            self.phone = phone
            return self

        def with_email(self, email: str):
            self.email = email
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
            return Employee(
                self.uuid, self.name, self.age, self.address, self.phone, self.email, self.access_type,
                self.hired_date, self.salary
            )
