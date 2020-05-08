from src.core.base.menu import Menu
from src.core.builders import create_car
from src.core.service.car_service import CarService
from src.ui.car_info_ui import CarInfoUi
from src.ui.car_rental_ui import CarRentalUi
from src.ui.listing_ui import ListingUi
from src.ui.user_ui import UserUi

MENU = """\033[2J\033[H
[0] Exit
[1] Add Car Model
[2] Add User
[3] Rent a Car
[4] Return a Car
[5] Car Information
[6] Listing
"""


class MainMenuUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = range(0, 7)
        self.car_service = CarService()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        int_op = int(str(self.op).strip())
        if int_op == 0:
            return Menu.EXIT_REQUEST
        elif int_op == 1:
            car = create_car()
            self.car_service.save(car)
        elif int_op == 2:
            return UserUi()
        elif int_op == 3:
            return CarRentalUi()
        elif int_op == 4:
            print('Return a Car')
        elif int_op == 5:
            return CarInfoUi()
        elif int_op == 6:
            return ListingUi()

        return Menu.SAME_MENU
