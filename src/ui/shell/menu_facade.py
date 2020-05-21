from abc import ABC

from core.enums.menu_type import MenuType
from ui.shell.menu_factory import MenuFactory


class MenuFacade(ABC):
    @staticmethod
    def get(menu_type: MenuType):
        return MenuFactory.get(menu_type)

    @staticmethod
    def exit_menu():
        return MenuFactory.get()

    @staticmethod
    def car_info_menu():
        return MenuFactory.get(MenuType.CAR_INFO)

    @staticmethod
    def listing_menu():
        return MenuFactory.get(MenuType.LISTING)

    @staticmethod
    def main_menu():
        return MenuFactory.get(MenuType.MAIN)

    @staticmethod
    def rental_menu():
        return MenuFactory.get(MenuType.RENTAL)

    @staticmethod
    def user_menu():
        return MenuFactory.get(MenuType.USER)
