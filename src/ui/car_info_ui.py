from src.core.base.menu import Menu
from src.core.service.car_service import CarService

MENU = """\033[2J\033[H
[A] Search model
[B] Get Information
[C] Previous Menu
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
        results = []
        all_cars = self.car_service.list()
        print("Please type the search criteria: {}".format(SEARCH_CRITERIA))
        criteria = input('> ')
        if criteria:
            for next_crit in criteria.strip().split(','):
                fields = next_crit.split('=')
                found = [c for c in all_cars if fields[1] in c[fields[0]]]
                results.extend(found)
            if len(results) > 0:
                print(results)

    def get_information(self):
        entity_id = input("Car UUID: ")
        if entity_id:
            found = self.car_service.get(entity_id)
            if found is not None:
                print(found)
            else:
                print('Model with uuid={}  was not found'.format(entity_id))
