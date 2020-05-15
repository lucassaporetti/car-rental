from src.model.user import User


class Customer(User):
    @staticmethod
    def of(values: list):
        return Customer(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7])

    def __init__(self, entity_id: str, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None, drv_license: str = None, rentals=None):
        super().__init__(entity_id, name, age, address, phone, email)
        self.drv_license = drv_license
        self.rentals = rentals if rentals else []

    def __str__(self):
        return "{}{}"\
            .format(super().__str__(), "License: {}\tRentals: {}\t"
                    .format(self.drv_license, self.rentals))

