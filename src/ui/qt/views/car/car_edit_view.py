from PyQt5.QtWidgets import QDialog

from src.ui.qt.qt_view import QtView


class CarEditView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)
