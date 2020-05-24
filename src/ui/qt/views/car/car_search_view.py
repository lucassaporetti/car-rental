from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractScrollArea, QDialogButtonBox
from pymysql.err import InternalError

from core.enum.color import Color
from core.eventbus.event_bus import EventBus
from core.model.car import Car
from core.service.service_facade import ServiceFacade
from ui.qt.table_model.entity_table_model import DefaultTableModel
from ui.qt.views.qt_view import QtView


class CarSearchView(QtView):

    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.car_service = ServiceFacade.get_car_service()
        self.stackedPanelCars = self.qt.find_stacked_widget('stackedPanelCars')
        self.tableCars = self.qt.find_table_view('tableCars')
        self.btnSearchCars = self.qt.find_tool_button('btnSearchCars')
        self.leSearchCar = self.qt.find_line_edit('leSearchCar')
        self.btnAddCar = self.qt.find_tool_button('btnAddCar')
        self.btnRemoveCar = self.qt.find_tool_button('btnRemoveCar')
        self.setup_ui()

    def setup_ui(self):
        self.stackedPanelCars.setCurrentIndex(0)
        self.tableCars.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableCars.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableCars.horizontalHeader().setStretchLastSection(True)
        self.tableCars.doubleClicked.connect(self.double_clicked_row)
        self.btnSearchCars.clicked.connect(self.btn_search_car_clicked)
        self.btnAddCar.clicked.connect(self.btn_add_car_clicked)
        self.btnRemoveCar.clicked.connect(self.btn_remove_car_clicked)

    def btn_search_car_clicked(self):
        self.log.info('Tool button: btnSearchCars clicked')
        criteria = self.leSearchCar.text() or '*'
        try:
            if criteria or criteria == '*':
                found = self.car_service.list(filters=criteria if criteria != '*' else None)
                if found and len(found) > 0:
                    self.populate_table_cars(found)
                    self.parent.set_status('Found {} car models matching: {}'.format(len(found), criteria))
                else:
                    msg = 'No cars found for the matching criteria: {}'.format(criteria)
                    self.parent.set_status(msg, Color.ORANGE)
                    self.log.warn(msg)
        except InternalError:
            msg = 'Invalid criteria {}'.format(criteria)
            self.parent.set_status(msg, Color.RED)
            self.log.error(msg)

    def btn_add_car_clicked(self):
        self.parent.car_edit.bbAddCar.button(QDialogButtonBox.Save).setDefault(True)
        self.stackedPanelCars.setCurrentIndex(1)
        self.log.info('Tool button: btnAddCar clicked')

    def btn_remove_car_clicked(self):
        indexes = self.tableCars.selectionModel().selectedRows()
        for index in indexes:
            car = self.tableCars.model().row(index)
            self.car_service.remove(car)
        self.btn_search_car_clicked()
        self.log.info('Tool button: btnRemoveCar clicked')

    def populate_table_cars(self, table_data: list):
        self.log.info('Found = {}'.format(table_data))
        self.tableCars.setModel(DefaultTableModel(Car, table_data=table_data, parent=self.tableCars))

    def double_clicked_row(self, index: QModelIndex):
        car = self.tableCars.model().row(index)
        self.log.info('Table: tableCars clicked: {}'.format(car))
        self.stackedPanelCars.setCurrentIndex(1)
        self.parent.car_edit.bbAddCar.button(QDialogButtonBox.Save).setDefault(True)
        EventBus.get('car-selection-bus').emit('rowSelected', selected_item=car)
