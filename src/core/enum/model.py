from enum import Enum


class Model(Enum):
    CAR = 'Car model'
    EMPLOYEE = 'Employee model'
    CUSTOMER = 'Customer model'
    RENTAL = 'Rental model'

    def __str__(self):
        return "{}".format(self.name.upper())
