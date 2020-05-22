from core.enum.menu_type import MenuType
from ui.shell.menu_factory import MenuFactory


class CarRental:
    def __init__(self):
        self.done = False
        self.ui = MenuFactory.get(MenuType.MAIN)
        self.prev_ui = self.ui

    def change_ui(self, menu_type: MenuType):
        self.prev_ui = self.ui
        self.ui = MenuFactory.get(menu_type)

    def run(self):
        while not self.done:
            if self.ui:
                next_ui = self.ui.execute()
                if next_ui is None or next_ui == MenuType.EXIT_MENU:
                    self.done = True
                else:
                    self.change_ui(next_ui)
            else:
                self.done = True
