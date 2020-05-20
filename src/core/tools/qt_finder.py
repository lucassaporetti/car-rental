from abc import ABC
from typing import Type, Optional

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QToolButton, QStackedWidget


class QtFinder(ABC):
    @staticmethod
    def find_widget(window: QWidget, widget: Type, name: str) -> Optional[QObject]:
        return window.findChild(widget, name)

    def __init__(self, window: QWidget):
        super().__init__()
        self.window = window

    def find_tool_button(self, name: str) -> Optional[QToolButton]:
        return QtFinder.find_widget(self.window, QToolButton, name)

    def find_stacked_widget(self, name: str) -> Optional[QStackedWidget]:
        return QtFinder.find_widget(self.window, QStackedWidget, name)
