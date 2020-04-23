import uuid


class User:
    def __init__(self, name: str = None, age: int = None, address: str = None, phone: str = None, email: str = None):
        self.uuid = str(uuid.uuid4())[:2]
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Name: {}\tAge: {}\tAddress: {}\tPhone: {}\tEmail: {}\t".format(
            self.name, self.age, self.address, self.phone, self.email)

