#!/usr/bin/env python

"""
  @package: TODO describe
   @script: ${app.py}
  @purpose: ${purpose}
  @created: Mon DD, YYYY
   @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior
   @mailto: yorevs@hotmail.com
"""
import signal

from core.enums.menu_type import MenuType
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


def exit_app(sig=None, frame=None):
    print(frame)
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    main = CarRental()
    signal.signal(signal.SIGINT, exit_app)
    main.run()
    exit_app(0)
