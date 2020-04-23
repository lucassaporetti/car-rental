from src.model.User import User


class Customer(User):
    def __init__(self, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None, drv_license: str = None, rentals=None):
        super().__init__(name, age, address, phone, email)
        self.drv_license = drv_license
        self.rentals = rentals if rentals else []

    def __str__(self):
        return "{}{}"\
            .format(super().__str__(), "License: {}\tRentals: {}\t"
                    .format(self.drv_license, self.rentals))

