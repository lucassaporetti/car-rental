#!/usr/bin/env python

"""
  @package: TODO describe
   @script: ${app.py}
  @purpose: ${purpose}
  @created: Mon DD, YYYY
   @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior
   @mailto: yorevs@hotmail.com
"""
import os
import sys

from src.core.base.menu import Menu
from src.ui.main_menu_ui import MainMenuUi


class Main:
    def __init__(self):
        self.done = False
        self.ui = MainMenuUi()

    def run(self):
        while not self.done:
            next_ui = self.ui.execute()
            if next_ui is None:
                self.done = True
            elif next_ui == Menu.MAIN_MENU:
                self.ui = MainMenuUi()
            elif next_ui == Menu.SAME_MENU:
                continue
            else:
                self.ui = next_ui
        print('Done.')


# Application entry point
if __name__ == "__main__":
    main = Main()
    main.run()
    sys.exit(0)
