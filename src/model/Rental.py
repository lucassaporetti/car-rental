from src.model.employee import Employee
from src.model.entity import Entity


class User(Entity):
    def __init__(self, date: str = None, price: float = None, pending: bool = None, attendant: Employee = None):
        super().__init__(None)
        self.date = date
        self.price = price
        self.pending = pending
        self.attendant = attendant

    def __str__(self):
        return "Date: {}\tPrice: {}\tPending: {}\tAttendant: {}\t".format(
            self.date, self.price, self.pending, self.attendant)

