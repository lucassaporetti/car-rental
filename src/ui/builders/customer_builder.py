from src.core.tools.commons import prompt, print_error
from src.core.tools.validators import validate_string, validate_int
from core.models.customer import Customer


class CustomerBuilder:
    def __init__(self):
        self.build()

    @staticmethod
    def build():
        valid = False
        customer = name = age = address = phone = email = drv_license = None
        while not valid:
            name = prompt("Name: ").strip() if name is None else name
            if not validate_string(name, "[a-zA-Z0-9]+", min_len=2, max_len=30):
                name = None
                print_error('Invalid name', name)
                continue
            age = prompt("Age: ").strip() if age is None else age
            if not validate_int(age, min_value=18, max_value=110):
                age = None
                print_error('Invalid age', age)
                continue
            address = prompt("Address: ").strip() if address is None else address
            if not validate_string(address, "[a-zA-Z0-9]+", min_len=5, max_len=120):
                address = None
                print_error("Invalid address", address)
                continue
            phone = prompt("Phone: ").strip() if phone is None else phone
            if not validate_string(phone, "[0-9]+", min_len=9, max_len=15):
                phone = None
                print_error("Invalid phone", phone)
                continue
            email = prompt("Email: ").strip() if email is None else email
            if not validate_string(email, ".+@.+\\..+", min_len=5, max_len=128):
                email = None
                print_error("Invalid email", email)
                continue
            drv_license = prompt("Driver License: ").strip() if drv_license is None else drv_license
            if not validate_string(drv_license, "[a-zA-Z0-9]+", min_len=8, max_len=8):
                drv_license = None
                print_error("Invalid driver license", drv_license)
                continue
            valid = True
            customer = Customer.Builder() \
                .with_name(name) \
                .with_age(age) \
                .with_address(address) \
                .with_phone(phone)\
                .with_email(email)\
                .with_drv_license(drv_license) \
                .build()

        return customer
