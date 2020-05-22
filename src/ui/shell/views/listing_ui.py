from core.enum.menu_type import MenuType
from src.core.service.service_facade import ServiceFacade
from src.core.tools.commons import print_list
from ui.shell.menu import Menu

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
        self.car_service = ServiceFacade.get_car_service()
        self.customer_service = ServiceFacade.get_customer_service()
        self.employee_service = ServiceFacade.get_employee_service()
        self.rentals_service = ServiceFacade.get_rental_service()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self) -> MenuType:
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
            return MenuType.MAIN

        return MenuType.LISTING

    def op_in_options(self):
        return str(self.op).upper() in self.options
