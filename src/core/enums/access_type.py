from enum import Enum


class AccessType(Enum):
    ADMIN = 'System Administrator'
    MANAGER = 'Line Manager'
    ATTENDANT = 'Attendant'

    def __str__(self):
        return "{}".format(self.name.upper())
