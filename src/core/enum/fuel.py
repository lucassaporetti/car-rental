from enum import Enum


class Fuel(Enum):
    GASOLINE = 1
    ALCOHOL = 2
    FLEX = 3
    DIESEL = 4

    def __str__(self):
        return "{}".format(self.name.upper())
