from core.enum.menu_type import MenuType
from src.core.service.service_facade import ServiceFacade
from ui.shell.menu import Menu

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
        self.car_service = ServiceFacade.get_car_service()

    def __str__(self):
        return self.menu

    def trigger_menu_item(self) -> MenuType:
        int_op = int(str(self.op).strip())
        if int_op == 0:
            return MenuType.EXIT_MENU
        elif int_op == 1:
            return MenuType.CAR_INFO
        elif int_op == 2:
            return MenuType.USER
        elif int_op == 3:
            return MenuType.RENTAL
        elif int_op == 4:
            return MenuType.LISTING

        return MenuType.MAIN
