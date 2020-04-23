from src.models.User import User


class Customer(User):
    def __init__(self, name: str, age: int, address: str, phone: str, email: str, drv_license: str, rentals: list):
        super().__init__(name, age, address, phone, email)
        self.drv_license = drv_license
        self.rentals = rentals

    def __str__(self):
        return "{}{}"\
            .format(super().__str__(), "License: {}\tRentals: {}\t"
                    .format(self.drv_license, self.rentals))

