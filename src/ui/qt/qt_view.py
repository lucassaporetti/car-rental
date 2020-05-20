from PyQt5.QtWidgets import QWidget

from src.configs import AppConfigs
from src.core.tools.commons import log_init
from src.core.tools.qt_finder import QtFinder


class QtView:
    def __init__(self, window: QWidget):
        self.window = window
        self.log = log_init(AppConfigs.log_file)
        self.qt = QtFinder(self.window)
