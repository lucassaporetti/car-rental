from src.model.user import User


class Employee(User):
    def __init__(self, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None, access_type: str = None, hired_date: str = None, salary: float = None):
        super().__init__(name, age, address, phone, email)
        self.access_type = access_type
        self.hired_date = hired_date
        self.salary = salary

    def __str__(self):
        return "{}{}"\
            .format(super().__str__(), "Access Type: {}\tHired Date: {}\tSalary: US$ {}\t"
                    .format(self.access_type, self.hired_date, self.salary))

