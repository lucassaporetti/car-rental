from src.core.enum.database_type import DatabaseType
from src.core.enum.model import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.service_facade import ServiceFacade
from src.ui.builders.car_builder import CarBuilder
from src.ui.car_info_ui import CarInfoUi
from src.ui.car_rental_ui import CarRentalUi
from src.ui.listing_ui import ListingUi
from src.ui.menu import *
from src.ui.user_ui import UserUi

MENU = """\033[2J\033[H
\033[0;32m[0]\033[0;0;0m Exit
\033[0;32m[1]\033[0;0;0m Add Car Model
\033[0;32m[2]\033[0;0;0m Add User
\033[0;32m[3]\033[0;0;0m Rent a Car
\033[0;32m[4]\033[0;0;0m Return a Car
\033[0;32m[5]\033[0;0;0m Car Information
\033[0;32m[6]\033[0;0;0m Listing
"""


class MainMenuUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = range(0, 7)
        self.car_service = ServiceFacade.get(RepositoryType.DATABASE, DatabaseType.MYSQL, Model.CAR)

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        int_op = int(str(self.op).strip())
        if int_op == 0:
            return Menu.EXIT_REQUEST
        elif int_op == 1:
            self.car_service.save(CarBuilder.build())
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
