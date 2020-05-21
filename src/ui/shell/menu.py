from abc import ABC, abstractmethod

from src.core.tools.commons import print_error, prompt
from ui.shell.menu_facade import MenuFacade


class Menu(ABC):

    def __init__(self):
        self.done = False
        self.op = None
        self.menu = ''
        self.options = []

    def execute(self):
        while not self.op == 0 and not self.done:
            print(self.menu)
            self.op = prompt("$ ")
            if not self.op:
                return MenuFacade.main_menu()
            elif self.op.isalnum() and self.op_in_options():
                return self.trigger_menu_item()
            else:
                print_error("### Error: Invalid option \"{}\"".format(self.op))
                self.op = None

    @abstractmethod
    def trigger_menu_item(self):
        pass

    def op_in_options(self) -> bool:
        if self.op.isdigit():
            return int(self.op) in self.options
        else:
            return False
