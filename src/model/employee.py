from src.model.user import User


class Employee(User):
    @staticmethod
    def of(values: list):
        return Employee(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])

    def __init__(self, entity_id: str = None, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None, access_type: str = None, hired_date: str = None, salary: float = None):
        super().__init__(entity_id, name, age, address, phone, email)
        self.access_type = access_type
        self.hired_date = hired_date
        self.salary = salary

    def __str__(self):
        return "{} | {} | {} | {}".format(
            super().__str__(), self.access_type, self.hired_date, self.salary)

