from src.core.enum.MenuReturn import MenuReturn
from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.service_facade import ServiceFacade
from src.core.tools import print_warning, print_error, print_list, prompt, wait_enter
from src.model.rental import Rental
from src.ui.menu import Menu

MENU = """\033[2J\033[H
\033[0;32m[A]\033[0;0;0m Available cars
\033[0;32m[B]\033[0;0;0m Rent
\033[0;32m[C]\033[0;0;0m Previous Menu
"""


class CarRentalUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = ['A', 'B', 'C']
        self.car_service = ServiceFacade.get(RepositoryType.DATABASE, DatabaseType.MYSQL, Model.CAR)
        self.employee_service = ServiceFacade.get(RepositoryType.DATABASE, DatabaseType.MYSQL, Model.EMPLOYEE)

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            self.search_available()
        elif str_op == 'B':
            self.do_rent()
        elif str_op == 'C':
            return MenuReturn.MAIN_MENU

        return MenuReturn.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options

    def search_available(self):
        available_cars = self.car_service.list(filters='AVAILABLE = 1')
        if len(available_cars) > 0:
            print_list(available_cars)
        else:
            print_warning('There are no cars available at the moment')

    def do_rent(self):
        rental = Rental()
        entity_id = prompt("Car UUID: ", clear=True)
        if entity_id:
            found = self.car_service.get(entity_id)
            if found is not None:
                all_attendants = self.employee_service.list()
                if len(all_attendants) > 0:
                    while not rental.attendant:
                        idx = 0
                        for next_att in all_attendants:
                            print('{} {}'.format(idx, next_att))
                            idx += 1
                        # idx = int(input('Attendant: '))
                        # rental.attendant = all_attendants[idx]
                        # TODO Finish the implementation
                        print('##TODO##')
                    wait_enter()
                else:
                    print_warning('There are no attendants yet')
            else:
                print_error('Model with uuid={} was not found'.format(entity_id))
