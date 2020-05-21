from enum import Enum


class MenuType(Enum):
    EXIT_MENU = 0
    CAR_INFO = 1
    LISTING = 2
    MAIN = 3
    RENTAL = 4
    USER = 5

    def __str__(self):
        return "{}".format(self.name.upper())