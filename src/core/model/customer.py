import uuid

from core.model.user import User


class Customer(User):
    @staticmethod
    def of(values: list):
        return Customer(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7])

    def __init__(self, entity_id: str = None, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None, drv_license: str = None, rentals=0):
        super().__init__(entity_id, name, age, address, phone, email)
        self.drv_license = drv_license
        self.rentals = rentals

    def __str__(self):
        return "{} | {} | {}".format(
            super().__str__(), self.drv_license, self.rentals)

    class Builder:
        def __init__(self):
            self.uuid = str(uuid.uuid4())
            self.name = None
            self.age = None
            self.address = None
            self.phone = None
            self.email = None
            self.drv_license = None
            self.rentals = 0

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

        def with_drv_license(self, drv_license: str):
            self.drv_license = drv_license
            return self

        def with_rentals(self, rentals: int):
            self.rentals = rentals
            return self

        def build(self):
            return Customer(
                self.uuid, self.name, self.age, self.address, self.phone, self.email, self.drv_license, self.rentals
            )
