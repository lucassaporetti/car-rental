import uuid

from src.core.Validators import Validators
from src.core.enum.AccessType import AccessType
from src.model.Customer import Customer
from src.model.Employee import Employee


class Builders:
    @staticmethod
    def create_employee():
        valid = False
        employee = Employee()
        while not valid:
            employee.name = input("Name: ").strip() if employee.name is None else employee.name
            if not Validators.validate_string(employee.name, "[a-zA-Z0-9]+", min_len=2, max_len=30):
                continue
            employee.age = input("Age: ").strip() if employee.age is None else employee.age
            if employee.age.isdigit() and Validators.validate_int(employee.age, min_value=18, max_value=110):
                continue
            employee.address = input("Address: ").strip() if employee.address is None else employee.address
            if Validators.validate_string(employee.address, "[a-zA-Z0-9]+", min_len=5, max_len=120):
                continue
            employee.phone = input("Phone: ").strip() if employee.phone is None else employee.phone
            if Validators.validate_string(employee.phone, "[0-9]+", min_len=9, max_len=15):
                continue
            employee.email = input("Email: ").strip() if employee.email is None else employee.email
            if Validators.validate_string(employee.email, ".+@.+\\..+", min_len=5, max_len=128):
                continue
            employee.access_type = input("Access Type: ").strip() if employee.access_type is None else employee.access_type
            if Validators.validate_enum(employee.access_type, AccessType):
                continue
            employee.hired_date = input("Hired Date: ").strip() if employee.hired_date is None else employee.hired_date
            if Validators.validate_date(employee.hired_date, "%d/%m/%Y"):
                continue
            employee.salary = input("Salary: US$ ") if employee.salary is None else employee.salary
            if Validators.validate_float(employee.salary, min_value=450.00, max_value=20000.00):
                continue
            employee.uuid = str(uuid.uuid4())[:2]

        return employee

    @staticmethod
    def create_customer():
        valid = False
        customer = Customer()
        while not valid:
            customer.name = input("Name: ").strip() if customer.name is None else customer.name
            if not Validators.validate_string(customer.name, "[-a-zA-Z0-9_ ]+", 2, 30):
                continue
            customer.age = input("Age: ").strip() if customer.age is None else customer.age
            if customer.age.isdigit() and Validators.validate_int(customer.age, 18, 110):
                continue
            customer.address = input("Address: ").strip() if customer.address is None else customer.address
            if Validators.validate_string(customer.address, "[-a-zA-Z0-9_ ]+", 5, 120):
                continue
            customer.phone = input("Phone: ").strip() if customer.phone is None else customer.phone
            if Validators.validate_string(customer.phone, "[0-9]+", 9, 15):
                continue
            customer.email = input("Email: ").strip() if customer.email is None else customer.email
            if Validators.validate_string(customer.email, ".+@.+\\..+", 5, 128):
                continue
            customer.drv_license = input("Driver License: ")
            if Validators.validate_string(customer.drv_license, "[a-zA-Z0-9]+", 8, 8):
                continue
            customer.uuid = str(uuid.uuid4())[:2]

        return customer
