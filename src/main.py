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

from ui.shell.menu import Menu
from ui.shell.menu_facade import MenuFacade


class CarRental:
    def __init__(self):
        self.done = False
        self.ui = MenuFacade.main_menu()
        self.prev_ui = self.ui

    def change_ui(self, ui: Menu):
        self.prev_ui = self.ui
        self.ui = ui

    def run(self):
        while not self.done:
            next_ui = self.ui.execute()
            if next_ui is None:
                self.done = True
            else:
                self.change_ui(next_ui)


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
