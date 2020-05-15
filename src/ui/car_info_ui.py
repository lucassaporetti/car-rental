from pymysql import InternalError

from src.core.base.menu import Menu
from src.core.service.car_service import CarService
from src.core.tools import press_enter, print_list, print_warning, print_error, print_one

MENU = """\033[2J\033[H
\033[0;32m[A]\033[0;0;0m Search model
\033[0;32m[B]\033[0;0;0m Get Information
\033[0;32m[C]\033[0;0;0m Previous Menu
"""

SEARCH_CRITERIA = 'criteria_1 .. criteria_N ([name|chassis|fuel|color|price|doors|plate]=value)'


class CarInfoUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = ['A', 'B', 'C']
        self.car_service = CarService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        str_op = str(self.op).strip().upper()
        if str_op == 'A':
            self.search_model()
        elif str_op == 'B':
            self.get_information()
        elif str_op == 'C':
            return Menu.MAIN_MENU

        return Menu.SAME_MENU

    def op_in_options(self):
        return str(self.op).upper() in self.options

    def search_model(self):
        print("Please type the search criteria: {}".format(SEARCH_CRITERIA))
        criteria = input('$ ')
        if criteria:
            try:
                found = self.car_service.list(filters=criteria)
                if len(found) > 0:
                    print_list(found)
                else:
                    print_warning('No cars found for the matching criteria {}'.format(criteria))
            except InternalError:
                print_error('Invalid criteria {}'.format(criteria))

    def get_information(self):
        entity_id = input("Car UUID: ")
        if entity_id:
            found = self.car_service.get(entity_id)
            if found is not None:
                print_one(found)
            else:
                print_warning('Model with uuid={}  was not found'.format(entity_id))
