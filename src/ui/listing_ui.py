from src.core.base.menu import Menu
from src.core.service.CarService import CarService
from src.core.service.CustomerService import CustomerService
from src.core.service.EmployeeService import EmployeeService
from src.core.service.RentalService import RentalService

MENU = """\033[2J\033[H
[A] Employees
[B] Customers
[C] Cars
[D] Rentals
[E] Previous Menu
"""


class ListingUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = ['A', 'B', 'C', 'D', 'E']
        self.employee_service = EmployeeService()
        self.customer_service = CustomerService()
        self.car_service = CarService()
        self.rentals_service = RentalService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            print(str(self.employee_service.list()))
        elif str_op == 'B':
            print(str(self.customer_service.list()))
        elif str_op == 'C':
            print(str(self.car_service.list()))
        elif str_op == 'D':
            print(str(self.rentals_service.list()))
        elif str_op == 'E':
            return Menu.MAIN_MENU

        print('')
        input('Press  [Enter] to continue ...')

        return Menu.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options

