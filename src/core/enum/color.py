from enum import Enum


class Color(Enum):
    NC = '\033[0;0;0m'
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    ORANGE = '\033[38;5;202m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    GRAY = '\033[38;5;8m'
    WHITE = '\033[0;97m'
    YELLOW = '\033[0;93m'
    VIOLET = '\033[0;95m'

    def __str__(self):
        return "{}".format(self.name.upper())
