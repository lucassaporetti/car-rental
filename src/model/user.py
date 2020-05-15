from src.model.entity import Entity


class User(Entity):
    def __init__(self, entity_id: str = None, name: str = None, age: int = None, address: str = None, phone: str = None,
                 email: str = None):
        super().__init__(entity_id)
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{} | {} | {} | {} | {} | {}".format(
            super().__str__(), self.name, self.age, self.address, self.phone, self.email)
