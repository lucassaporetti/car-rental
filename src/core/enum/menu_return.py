from enum import Enum


class MenuReturn(Enum):
    MENU_EXIT = None
    MAIN_MENU = 0
    SAME_MENU = 1

    def __str__(self):
        return "{}".format(self.name.upper())
