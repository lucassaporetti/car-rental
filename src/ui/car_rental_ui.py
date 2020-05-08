from src.core.base.menu import Menu
from src.core.service.car_service import CarService
from src.core.service.employee_service import EmployeeService
from src.model.rental import Rental

MENU = """\033[2J\033[H
[A] Search available cars
[B] Rent
[C] Previous Menu
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
        all_cars = self.car_service.list()
        available_cars = [c for c in all_cars if c['available']]
        if len(available_cars) > 0:
            print(available_cars)
        else:
            print('There are no cars available at the moment')

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
                else:
                    print('There are no attendants yet')
            else:
                print('Model with uuid={} was not found'.format(entity_id))
