class User:
    def __init__(self, name: str, age: int, address: str, phone: str, email: str):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Name: {}\tAge: {}\tAddr: {}\tPhone: {}\tEmail: {}".format(
            self.name, self.age, self.address, self.phone, self.email)

