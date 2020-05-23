from PyQt5.QtWidgets import QDialog

from ui.qt.views.qt_view import QtView


class CarEditView(QtView):
    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)

    def setup_ui(self):
        pass

