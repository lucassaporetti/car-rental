from abc import ABC

from core.enums.menu_type import MenuType
from ui.shell.shell_menus import ShellMenus


class MenuFactory(ABC):

    @staticmethod
    def get(menu: MenuType = MenuType.EXIT_MENU):
        return ShellMenus.menus[menu] if menu in ShellMenus.menus else None
