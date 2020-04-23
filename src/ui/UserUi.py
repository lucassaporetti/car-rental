from src.core.base.Menu import Menu
from src.core.service.EmployeeService import EmployeeService
from src.models.Employee import Employee

MENU = """\033[2J
[A] Employee
[B] Customer
[C] Previous Menu
"""


class UserUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = ['A', 'B', 'C']
        self.employee_service = EmployeeService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            employee = self.create_employee()
            self.employee_service.save(employee)
        elif str_op == 'B':
            print('Add Customer')
        elif str_op == 'C':
            print('Previous Menu')
            return Menu.MAIN_MENU

        return Menu.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options

    def create_employee(self):
        employee = Employee()
        employee.name = input("Name: ")
        employee.age = input("Age: ")
        employee.address = input("Address: ")
        employee.phone = input("Phone: ")
        employee.email = input("Email: ")
        employee.access_type = input("Access Type: ")
        employee.hired_date = input("Hired Date: ")
        employee.salary = input("Salary: US$ ")

        return employee
