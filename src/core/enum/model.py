from enum import Enum


class Model(Enum):
    CAR = 1
    EMPLOYEE = 2
    CUSTOMER = 3
    RENTAL = 4

    def __str__(self):
        return "{}".format(self.name.upper())
