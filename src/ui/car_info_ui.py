from pymysql.err import InternalError

from src.configs import AppConfigs
from src.core.enums.menu_return import MenuReturn
from src.core.enums.model import Model
from src.core.services.service_facade import ServiceFacade
from src.core.tools.commons import *
from src.ui.builders.car_builder import CarBuilder
from src.ui.menu import Menu

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
        self.car_service = ServiceFacade.get(AppConfigs.repository_type, AppConfigs.database_type, Model.CAR)

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
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
            return MenuReturn.MAIN_MENU

        return MenuReturn.SAME_MENU

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
