from core.model.user import User


class UserDto(User):
    def __init__(self, drv_license: str = None, access_type: str = None, hired_date: str = None, salary: float = None):
        super().__init__()
        self.drv_license = drv_license
        self.access_type = access_type
        self.hired_date = hired_date
        self.salary = salary

    def __str__(self):
        return "{} | {} | {} | {} | {}".format(
            super().__str__(), self.drv_license, self.access_type, self.hired_date, self.salary)