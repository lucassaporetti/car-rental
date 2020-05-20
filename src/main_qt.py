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
import pathlib
import signal
import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication

from src.core.enums.database_type import DatabaseType
from src.core.enums.repository_type import RepositoryType
from src.core.tools.commons import log_init
from src.core.tools.properties import Properties
from src.ui.qt.main_menu_ui import MainMenuUi


class CarRental:
    cur_dir = pathlib.Path(sys.argv[0]).parent.absolute()
    log_file = f"{cur_dir}/../log/car-rental.log"
    log = log_init(log_file)
    log.info('Car Rental started {}'.format(datetime.now()))
    app_properties = Properties(f"{cur_dir}/resources/application.properties").read()
    log.info('Successfully read {} properties'.format(app_properties.size()))
    repository_type = RepositoryType[app_properties.get('persistence.repository.type').upper()]
    database_type = DatabaseType[app_properties.get('persistence.database.type').upper()]

    def __init__(self):
        self.app = QApplication([])
        self.ui = MainMenuUi()

    def run(self):
        self.ui.show()
        self.app.exec_()


def exit_app(sig=None, frame=None):
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    main = CarRental()
    main.run()
    signal.signal(signal.SIGINT, exit_app)
    exit_app(0)
