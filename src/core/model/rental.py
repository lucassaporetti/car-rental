from datetime import datetime

from core.model.employee import Employee
from core.model.entity import Entity


class Rental(Entity):
    @staticmethod
    def of(values: list):
        return Rental(values[0], values[1], values[2], values[3], values[4], values[5])

    def __init__(self, entity_id: str = None, date: str = None, return_date: str = None, price: float = None,
                 pending: bool = None, attendant: Employee = None):
        super().__init__(entity_id)
        self.date = date if date is not None else datetime.today().strftime('%Y-%m-%d')
        self.return_date = return_date
        self.price = price
        self.pending = pending
        self.attendant = attendant

    def __str__(self):
        return "{} | {} | {} | {} | {} | {}".format(
            super().__str__(), self.date, self.return_date, self.price, self.pending, self.attendant)
