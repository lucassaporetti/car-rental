from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractScrollArea
from pymysql.err import InternalError

from core.model.car import Car
from core.service.service_facade import ServiceFacade
from ui.qt.views.qt_view import QtView
from ui.shell.views.table_model.default_table_model import DefaultTableModel


class CarSearchView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)
        self.car_service = ServiceFacade.get_car_service()
        self.stackedPanelCarModels = self.qt.find_stacked_widget('stackedPanelCarModels')
        self.tableCarModels = self.qt.find_table_view('tableCarModels')
        self.btnSearchModel = self.qt.find_tool_button('btnSearchModel')
        self.editSearchModel = self.qt.find_line_edit('editSearchModel')
        self.btnAddCarModel = self.qt.find_tool_button('btnAddCarModel')
        self.setup_ui()

    def setup_ui(self):
        self.tableCarModels.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableCarModels.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.stackedPanelCarModels.setCurrentIndex(0)
        self.btnSearchModel.clicked.connect(self.btn_search_model_clicked)
        self.btnAddCarModel.clicked.connect(self.btn_add_car_clicked)

    def btn_add_car_clicked(self):
        self.log.info('Tool button: btnAddCarModel clicked')
        self.stackedPanelCarModels.setCurrentIndex(1)

    def btn_search_model_clicked(self):
        self.log.info('Tool button: btnSearchModel clicked')
        criteria = self.editSearchModel.text()
        try:
            if criteria or criteria == '*':
                found = self.car_service.list(filters=criteria if criteria != '*' else None)
                if found and len(found) > 0:
                    self.populate_table_car_models(found)
                else:
                    self.log.warn('No cars found for the matching criteria {}'.format(criteria))
        except InternalError:
            self.log.error('Invalid criteria {}'.format(criteria))

    def populate_table_car_models(self, table_data: list):
        self.log.info('Found = {}'.format(table_data))
        self.tableCarModels.setModel(DefaultTableModel(Car, table_data=table_data, parent=self.window))
        self.tableCarModels.resizeColumnsToContents()
