from src.core.enum.access_type import AccessType
from src.core.tools import prompt, print_error
from src.core.validators import validate_string, validate_enum, validate_int, validate_float, validate_date
from src.model.employee import Employee


class EmployeeBuilder:
    def __init__(self):
        self.build()

    @staticmethod
    def build():
        valid = False
        employee = name = age = address = phone = email = access_type = hired_date = salary = None
        while not valid:
            name = prompt("Name: ").strip() if name is None else name
            if not validate_string(name, "[a-zA-Z0-9]+", min_len=2, max_len=30):
                name = print_error('Invalid name', name)
                continue
            age = prompt("Age: ").strip() if age is None else age
            if not validate_int(age, min_value=18, max_value=110):
                age = print_error('Invalid age', age)
                continue
            address = prompt("Address: ").strip() if address is None else address
            if not validate_string(address, "[a-zA-Z0-9]+", min_len=5, max_len=120):
                address = print_error("Invalid address", address)
                continue
            phone = prompt("Phone: ").strip() if phone is None else phone
            if not validate_string(phone, "[0-9]+", min_len=9, max_len=15):
                phone = print_error("Invalid phone", phone)
                continue
            email = prompt("Email: ").strip() if email is None else email
            if not validate_string(email, ".+@.+\\..+", min_len=5, max_len=128):
                email = print_error("Invalid email", email)
                continue
            access_type = prompt("Access Type: ").strip() if access_type is None else access_type
            if not validate_enum(access_type, AccessType):
                access_type = print_error("Invalid access type", access_type)
                continue
            hired_date = prompt("Hired Date: ").strip() if hired_date is None else hired_date
            if not validate_date(hired_date, "%d/%m/%Y"):
                hired_date = print_error("Invalid hired date", hired_date)
                continue
            salary = prompt("Salary: US$ ") if salary is None else salary
            if not validate_float(salary, min_value=450.00, max_value=20000.00):
                salary = print_error("Invalid salary", salary)
                continue
            valid = True
            employee = Employee.Builder() \
                .with_name(name) \
                .with_age(age) \
                .with_address(address) \
                .with_phone(phone)\
                .with_email(email)\
                .with_access_type(access_type) \
                .with_hired_date(hired_date) \
                .with_salary(salary) \
                .build()

        return employee
