from src.core.enum.model import Model
from src.core.service.service_facade import ServiceFacade
from src.main import Main
from src.ui.car_info_ui import CarInfoUi
from src.ui.rental_ui import CarRentalUi
from src.ui.listing_ui import ListingUi
from src.ui.menu import *
from src.ui.user_ui import UserUi

MENU = """\033[2J\033[H
\033[0;32m[0]\033[0;0;0m Exit
\033[0;32m[1]\033[0;0;0m Car Models
\033[0;32m[2]\033[0;0;0m Users
\033[0;32m[3]\033[0;0;0m Rentals
\033[0;32m[4]\033[0;0;0m Listing
"""


class MainMenuUi(Menu):
    def __init__(self):
        super().__init__()
        self.menu = str(MENU)
        self.options = range(0, 5)
        self.car_service = ServiceFacade.get(Main.repository_type, Main.database_type, Model.CAR)

    def __str__(self):
        return self.menu

    def trigger_menu_item(self):
        int_op = int(str(self.op).strip())
        if int_op == 0:
            return MenuReturn.MENU_EXIT
        elif int_op == 1:
            return CarInfoUi()
        elif int_op == 2:
            return UserUi()
        elif int_op == 3:
            return CarRentalUi()
        elif int_op == 4:
            return ListingUi()

        return MenuReturn.SAME_MENU
