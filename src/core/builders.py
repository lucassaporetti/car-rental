import uuid

from src.core.enum.access_type import AccessType
from src.core.enum.color import Color
from src.core.enum.fuel import Fuel
from src.core.tools import print_error
from src.core.validators import validate_string, validate_int, validate_enum, validate_date, validate_float
from src.model.car import Car
from src.model.customer import Customer
from src.model.employee import Employee


def create_car():
    valid = False
    car = Car()
    while not valid:
        car.name = input("Name: ").strip() if car.name is None else car.name
        if not validate_string(car.name, "[a-zA-Z0-9]+", min_len=2, max_len=30):
            car.name = print_error('Invalid name', car.name)
            continue
        car.chassis = input("Chassis: ").strip() if car.chassis is None else car.chassis
        if not validate_string(car.chassis, "[a-zA-Z0-9]+", min_len=11, max_len=11):
            car.chassis = print_error('Invalid chassis', car.chassis)
            continue
        car.color = input("Color: ").strip() if car.color is None else car.color
        if not validate_enum(car.color, Color):
            car.color = print_error('Invalid color', car.color)
            continue
        car.doors = input("Doors: ").strip() if car.doors is None else car.doors
        if not validate_int(car.doors, min_value=3, max_value=6):
            car.doors = print_error('Invalid doors', car.doors)
            continue
        car.fuel = input("Fuel: ").strip() if car.fuel is None else car.fuel
        if not validate_enum(car.fuel, Fuel):
            car.fuel = print_error('Invalid fuel', car.fuel)
            continue
        car.plate = input("Plate: ").strip() if car.plate is None else car.plate
        if not validate_string(car.plate, "[a-zA-Z]{3}-[0-9]{4}", min_len=8, max_len=8):
            car.plate = print_error('Invalid plate', car.plate)
            continue
        car.price = input("Price: ").strip() if car.price is None else car.price
        if not validate_float(car.price, min_value=50.0, max_value=1000.0):
            car.price = print_error('Invalid price', car.price)
            continue
        valid = True

    return car


def create_employee():
    valid = False
    employee = Employee()
    while not valid:
        employee.name = input("Name: ").strip() if employee.name is None else employee.name
        if not validate_string(employee.name, "[a-zA-Z0-9]+", min_len=2, max_len=30):
            employee.name = print_error('Invalid name', employee.name)
            continue
        employee.age = input("Age: ").strip() if employee.age is None else employee.age
        if not validate_int(employee.age, min_value=18, max_value=110):
            employee.age = print_error('Invalid age', employee.age)
            continue
        employee.address = input("Address: ").strip() if employee.address is None else employee.address
        if not validate_string(employee.address, "[a-zA-Z0-9]+", min_len=5, max_len=120):
            employee.address = print_error("Invalid address", employee.address)
            continue
        employee.phone = input("Phone: ").strip() if employee.phone is None else employee.phone
        if not validate_string(employee.phone, "[0-9]+", min_len=9, max_len=15):
            employee.phone = print_error("Invalid phone", employee.phone)
            continue
        employee.email = input("Email: ").strip() if employee.email is None else employee.email
        if not validate_string(employee.email, ".+@.+\\..+", min_len=5, max_len=128):
            employee.email = print_error("Invalid email", employee.email)
            continue
        employee.access_type = input("Access Type: ").strip() if employee.access_type is None else employee.access_type
        if not validate_enum(employee.access_type, AccessType):
            employee.access_type = print_error("Invalid access type", employee.access_type)
            continue
        employee.hired_date = input("Hired Date: ").strip() if employee.hired_date is None else employee.hired_date
        if not validate_date(employee.hired_date, "%d/%m/%Y"):
            employee.hired_date = print_error("Invalid hired date", employee.hired_date)
            continue
        employee.salary = input("Salary: US$ ") if employee.salary is None else employee.salary
        if not validate_float(employee.salary, min_value=450.00, max_value=20000.00):
            employee.salary = print_error("Invalid salary", employee.salary)
            continue
        valid = True

    return employee


def create_customer():
    valid = False
    customer = Customer()
    while not valid:
        customer.name = input("Name: ").strip() if customer.name is None else customer.name
        if not validate_string(customer.name, "[a-zA-Z0-9]+", min_len=2, max_len=30):
            customer.name = print_error('Invalid name', customer.name)
            continue
        customer.age = input("Age: ").strip() if customer.age is None else customer.age
        if not validate_int(customer.age, min_value=18, max_value=110):
            customer.age = print_error('Invalid age', customer.age)
            continue
        customer.address = input("Address: ").strip() if customer.address is None else customer.address
        if not validate_string(customer.address, "[a-zA-Z0-9]+", min_len=5, max_len=120):
            customer.address = print_error("Invalid address", customer.address)
            continue
        customer.phone = input("Phone: ").strip() if customer.phone is None else customer.phone
        if not validate_string(customer.phone, "[0-9]+", min_len=9, max_len=15):
            customer.phone = print_error("Invalid phone", customer.phone)
            continue
        customer.email = input("Email: ").strip() if customer.email is None else customer.email
        if not validate_string(customer.email, ".+@.+\\..+", min_len=5, max_len=128):
            customer.email = print_error("Invalid email", customer.email)
            continue
        customer.drv_license = input("Driver License: ")
        if validate_string(customer.drv_license, "[a-zA-Z0-9]+", 8, 8):
            customer.drv_license = print_error("Invalid driver license", customer.drv_license)
            continue
        valid = True

    return customer
