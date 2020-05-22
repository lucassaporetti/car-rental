from pymysql.err import InternalError

from core.enum.menu_type import MenuType
from core.tools.commons import prompt, print_list, print_warning, print_error, print_one
from src.core.service.service_facade import ServiceFacade
from src.ui.builders.car_builder import CarBuilder
from ui.shell.menu import Menu

MENU = """\033[2J\033[H
\033[0;32m[A]\033[0;0;0m Search model
\033[0;32m[B]\033[0;0;0m Add model
\033[0;32m[C]\033[0;0;0m Remove model
\033[0;32m[D]\033[0;0;0m Car Information
\033[0;32m[E]\033[0;0;0m Previous Menu
"""


class CarInfoUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = ['A', 'B', 'C', 'D', 'E']
        self.car_service = ServiceFacade.get_car_service()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self) -> MenuType:
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            self.search_model()
        elif str_op == 'B':
            self.car_service.save(CarBuilder.build())
        elif str_op == 'C':
            self.remove_model()
        elif str_op == 'D':
            self.get_information()
        elif str_op == 'E':
            return MenuType.MAIN

        return MenuType.CAR_INFO

    def op_in_options(self):
        return str(self.op).upper() in self.options

    def search_model(self):
        criteria_hint = '* or criteria_1, ... criteria_N ([name|chassis|fuel|color|price|doors|plate]=value)'
        criteria = prompt("Please type the search criteria: {}\n$ ".format(criteria_hint), clear=True)
        try:
            if criteria or criteria == '*':
                found = self.car_service.list(filters=criteria if criteria != '*' else None)
                if found and len(found) > 0:
                    print_list(found)
                else:
                    print_warning('No cars found for the matching criteria {}'.format(criteria))
        except InternalError:
            print_error('Invalid criteria {}'.format(criteria))

    def remove_model(self):
        entity_id = prompt("Car UUID: ", clear=True)
        if entity_id:
            found = self.car_service.get(entity_id)
            if found is not None:
                self.car_service.remove(found)
            else:
                print_warning('Model with uuid={}  was not found'.format(entity_id))

    def get_information(self):
        entity_id = prompt("Car UUID: ", clear=True)
        if entity_id:
            found = self.car_service.get(entity_id)
            if found is not None:
                print_one(found)
            else:
                print_warning('Model with uuid={}  was not found'.format(entity_id))
