from abc import ABC

from core.enums.menu_type import MenuType
# from ui.shell.car_info_ui import CarInfoUi
# from ui.shell.listing_ui import ListingUi
# from ui.shell.main_menu_ui import MainMenuUi
# from ui.shell.rental_ui import RentalUi
# from ui.shell.user_ui import UserUi


class ShellMenus(ABC):
    menus = {
        # MenuType.EXIT_MENU: None
        # , MenuType.CAR_INFO: CarInfoUi()
        # , MenuType.LISTING: ListingUi()
        # , MenuType.MAIN: MainMenuUi()
        # , MenuType.RENTAL: RentalUi()
        # , MenuType.USER: UserUi()
    }
