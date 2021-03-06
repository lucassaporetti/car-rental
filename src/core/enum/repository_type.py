from enum import Enum


class RepositoryType(Enum):
    FILE = 1
    DATABASE = 2

    def __str__(self):
        return "{}".format(self.name.upper())
