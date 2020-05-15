from src.core.service.car_service import CarService
from src.core.service.customer_service import CustomerService
from src.core.service.employee_service import EmployeeService
from src.core.service.rental_service import RentalService
from src.core.tools import press_enter, print_list
from src.ui.menu import Menu

MENU = """\033[2J\033[H
\033[0;32m[A]\033[0;0;0m Employees
\033[0;32m[B]\033[0;0;0m Customers
\033[0;32m[C]\033[0;0;0m Cars
\033[0;32m[D]\033[0;0;0m Rentals
\033[0;32m[E]\033[0;0;0m Previous Menu
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
            print_list(self.employee_service.list())
        elif str_op == 'B':
            print_list(self.customer_service.list())
        elif str_op == 'C':
            print_list(self.car_service.list())
        elif str_op == 'D':
            print_list(self.rentals_service.list())
        elif str_op == 'E':
            return Menu.MAIN_MENU

        return Menu.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options

