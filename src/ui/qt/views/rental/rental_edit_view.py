from PyQt5.QtWidgets import QDialog

from ui.qt.views.qt_view import QtView


class RentalEditView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)

    def setup_ui(self):
        pass
