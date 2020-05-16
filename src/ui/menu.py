from abc import ABC, abstractmethod

from src.core.enum.menu_return import MenuReturn
from src.core.tools import print_error, prompt


class Menu(ABC):

    def __init__(self):
        self.done = False
        self.op = None
        self.menu = ''
        self.options = []

    def execute(self):
        while not self.op == MenuReturn.MAIN_MENU and not self.done:
            print(self.menu)
            self.op = prompt("$ ", end='')
            if self.op and self.op.isalnum() and self.op_in_options():
                return self.trigger_menu_item()
            else:
                print_error("### Error: Invalid option \"{}\"".format(self.op))
                self.op = None

    @abstractmethod
    def trigger_menu_item(self):
        pass

    def op_in_options(self):
        if self.op.isdigit():
            return int(self.op) in self.options
        else:
            return False
