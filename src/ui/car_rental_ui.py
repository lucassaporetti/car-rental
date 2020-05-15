from src.core.base.menu import Menu
from src.core.service.car_service import CarService
from src.core.service.employee_service import EmployeeService
from src.core.tools import press_enter, print_warning, print_error, print_list
from src.model.rental import Rental

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
        self.car_service = CarService()
        self.employee_service = EmployeeService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            self.search_available()
        elif str_op == 'B':
            self.do_rent()
        elif str_op == 'C':
            return Menu.MAIN_MENU

        return Menu.SAME_MENU

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
        entity_id = input("Car UUID: ")
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
                        idx = int(input('Attendant: '))
                        rental.attendant = all_attendants[idx]
                        # TODO Finish the implementation
                        print('TODO')
                    press_enter()
                else:
                    print_warning('There are no attendants yet')
            else:
                print_error('Model with uuid={} was not found'.format(entity_id))
