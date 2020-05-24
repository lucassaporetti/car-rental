from enum import Enum


class UserType(Enum):
    CUSTOMER = 1
    EMPLOYEE = 2
    UNDEFINED = 3

    def __str__(self):
        return "{}".format(self.name.upper())
