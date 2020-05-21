from src.app_configs import AppConfigs
from src.core.enums.menu_return import MenuReturn
from src.core.enums.model import Model
from src.core.services.service_facade import ServiceFacade
from src.core.tools.commons import print_list
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
        self.employee_service = ServiceFacade.get(AppConfigs.repository_type, AppConfigs.database_type, Model.EMPLOYEE)
        self.customer_service = ServiceFacade.get(AppConfigs.repository_type, AppConfigs.database_type, Model.CUSTOMER)
        self.car_service = ServiceFacade.get(AppConfigs.repository_type, AppConfigs.database_type, Model.CAR)
        self.rentals_service = ServiceFacade.get(AppConfigs.repository_type, AppConfigs.database_type, Model.RENTAL)

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
            return MenuReturn.MAIN_MENU

        return MenuReturn.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options
