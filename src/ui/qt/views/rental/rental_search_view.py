from PyQt5.QtWidgets import QDialog

from src.ui.qt.qt_view import QtView


class RentalSearchView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)
        self.stackPanelRentals = self.qt.find_stacked_widget('stackPanelRentals')
        self.btnRentCar = self.qt.find_tool_button('btnRentCar')

    def setup_ui(self):
        self.btnRentCar.clicked.connect(self.btn_rent_car_clicked)

    def btn_rent_car_clicked(self):
        self.stackPanelRentals.setCurrentIndex(1)
        self.log.info('Tool button: btnRentCar clicked')
