from PyQt5.QtWidgets import QDialog

from src.ui.qt.qt_view import QtView


class RentalSearchView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)
        self.stackedPanelRentals = self.qt.find_stacked_widget('stackedPanelRentals')
        self.btnRentCar = self.qt.find_tool_button('btnRentCar')
        self.setup_ui()

    def setup_ui(self):
        self.btnRentCar.clicked.connect(self.btn_rent_car_clicked)

    def btn_rent_car_clicked(self):
        self.stackedPanelRentals.setCurrentIndex(1)
        self.log.info('Tool button: btnRentCar clicked')
