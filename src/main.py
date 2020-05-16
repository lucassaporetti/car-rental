#!/usr/bin/env python

"""
  @package: TODO describe
   @script: ${app.py}
  @purpose: ${purpose}
  @created: Mon DD, YYYY
   @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior
   @mailto: yorevs@hotmail.com
"""
import pathlib
import signal
import sys
from datetime import datetime

from src.core.properties import Properties
from src.core.tools import log_init
from src.ui.main_menu_ui import *


class Main:
    cur_dir = pathlib.Path(sys.argv[0]).parent.absolute()
    log_file = f"{cur_dir}/../log/car-rental.log"
    log = log_init(log_file)
    log.info('Car Rental started {}'.format(datetime.now()))
    app_properties = Properties(f"{cur_dir}/application.properties").read()
    log.info('Successfully read {} properties'.format(app_properties.size()))

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
    main = Main()
    signal.signal(signal.SIGINT, exit_app)
    main.run()
    exit_app(0)
