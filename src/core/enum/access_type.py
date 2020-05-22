from enum import Enum


class AccessType(Enum):
    ADMIN = 1
    MANAGER = 2
    ATTENDANT = 3

    def __str__(self):
        return "{}".format(self.name.upper())
