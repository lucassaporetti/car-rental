from src.core.enum.MenuReturn import MenuReturn
from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.service_facade import ServiceFacade
from src.ui.builders.customer_builder import CustomerBuilder
from src.ui.builders.employee_builder import EmployeeBuilder
from src.ui.menu import Menu

MENU = """\033[2J\033[H
\033[0;32m[A]\033[0;0;0m Employee
\033[0;32m[B]\033[0;0;0m Customer
\033[0;32m[C]\033[0;0;0m Previous Menu
"""


class UserUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = ['A', 'B', 'C']
        self.employee_service = ServiceFacade.get(RepositoryType.DATABASE, DatabaseType.MYSQL, Model.EMPLOYEE)
        self.customer_service = ServiceFacade.get(RepositoryType.DATABASE, DatabaseType.MYSQL, Model.CUSTOMER)

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            employee = EmployeeBuilder.build()
            self.employee_service.save(employee)
        elif str_op == 'B':
            customer = CustomerBuilder.build()
            self.customer_service.save(customer)
        elif str_op == 'C':
            return MenuReturn.MAIN_MENU

        return MenuReturn.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options
