from src.core.base.menu import Menu
from src.core.builders import create_employee, create_customer
from src.core.service.CustomerService import CustomerService
from src.core.service.EmployeeService import EmployeeService

MENU = """\033[2J\033[H
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
        self.customer_service = CustomerService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            employee = create_employee()
            self.employee_service.save(employee)
        elif str_op == 'B':
            customer = create_customer()
            self.customer_service.save(customer)
        elif str_op == 'C':
            return Menu.MAIN_MENU

        return Menu.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options
