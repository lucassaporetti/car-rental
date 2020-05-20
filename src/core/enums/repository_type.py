from enum import Enum


class RepositoryType(Enum):
    FILE = 'File Repository'
    DATABASE = 'Database Repository'

    def __str__(self):
        return "{}".format(self.name.upper())