from abc import ABC

from core.enum.menu_type import MenuType
from ui.shell.views.car_info_ui import CarInfoUi
from ui.shell.views.listing_ui import ListingUi
from ui.shell.views.main_menu_ui import MainMenuUi
from ui.shell.views.rental_ui import RentalUi
from ui.shell.views.user_ui import UserUi


class MenuFactory(ABC):
    __menus = {
        MenuType.EXIT_MENU: None
        , MenuType.CAR_INFO: CarInfoUi()
        , MenuType.LISTING: ListingUi()
        , MenuType.MAIN: MainMenuUi()
        , MenuType.RENTAL: RentalUi()
        , MenuType.USER: UserUi()
    }

    @staticmethod
    def get(menu: MenuType = MenuType.EXIT_MENU):
        return MenuFactory.__menus[menu] if menu in MenuFactory.__menus else None
