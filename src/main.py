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

from src.ui.main_menu_ui import *


class CarRental:
    def __init__(self):
        self.done = False
        self.ui = MainMenuUi()

    def run(self):
        while not self.done:
            next_ui = self.ui.execute()
            if next_ui is None:
                self.done = True
            elif next_ui == MenuReturn.MAIN_MENU:
                self.ui = MainMenuUi()
            elif next_ui == MenuReturn.SAME_MENU:
                continue
            elif next_ui == MenuReturn.MENU_EXIT:
                break
            else:
                self.ui = next_ui


def exit_app(sig=None, frame=None):
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
