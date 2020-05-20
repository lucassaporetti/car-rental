from PyQt5.QtWidgets import QDialog

from src.ui.qt.qt_view import QtView


class CarSearchView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)
        self.stackedPanelCarModels = self.qt.find_stacked_widget('stackedPanelCarModels')
        self.btnAddCarModel = self.qt.find_tool_button('btnAddCarModel')
        self.setup_ui()

    def setup_ui(self):
        self.btnAddCarModel.clicked.connect(self.btn_add_car_clicked)

    def btn_add_car_clicked(self):
        self.stackedPanelCarModels.setCurrentIndex(1)
        self.log.info('Tool button: btnAddCarModel clicked')
