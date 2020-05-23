from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractScrollArea
from pymysql.err import InternalError

from core.enum.color import Color
from core.model.rental import Rental
from core.service.service_facade import ServiceFacade
from ui.qt.table_model.default_table_model import DefaultTableModel
from ui.qt.views.qt_view import QtView


class RentalSearchView(QtView):
    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.stackedPanelRentals = self.qt.find_stacked_widget('stackedPanelRentals')
        self.rental_service = ServiceFacade.get_rental_service()
        self.tableRentals = self.qt.find_table_view('tableRentals')
        self.btnSearchRentals = self.qt.find_tool_button('btnSearchRentals')
        self.leSearchRental = self.qt.find_line_edit('leSearchRental')
        self.btnRentCar = self.qt.find_tool_button('btnRentCar')
        self.btnReturnCar = self.qt.find_tool_button('btnReturnCar')
        self.setup_ui()

    def setup_ui(self):
        self.stackedPanelRentals.setCurrentIndex(0)
        self.tableRentals.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableRentals.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableRentals.horizontalHeader().setStretchLastSection(True)
        self.btnSearchRentals.clicked.connect(self.btn_search_rentals_clicked)
        self.btnRentCar.clicked.connect(self.btn_rent_car_clicked)
        self.btnReturnCar.clicked.connect(self.btn_return_car_clicked)

    def btn_rent_car_clicked(self):
        self.stackedPanelRentals.setCurrentIndex(1)
        self.log.info('Tool button: btnRentCar clicked')

    def btn_return_car_clicked(self):
        self.stackedPanelRentals.setCurrentIndex(1)
        self.log.info('Tool button: btnReturnCar clicked')

    def btn_search_rentals_clicked(self):
        self.log.info('Tool button: btnSearchRentals clicked')
        criteria = self.leSearchRental.text() or '*'
        try:
            if criteria or criteria == '*':
                found = self.rental_service.list(filters=criteria if criteria != '*' else None)
                if found and len(found) > 0:
                    self.populate_table_rentals(found)
                    self.parent.set_status('Found {} rentals matching: {}'.format(len(found), criteria))
                else:
                    msg = 'No rentals found for the matching criteria: {}'.format(criteria)
                    self.parent.set_status(msg, Color.ORANGE)
                    self.log.warn(msg)
        except InternalError:
            msg = 'Invalid criteria {}'.format(criteria)
            self.parent.set_status(msg, Color.RED)
            self.log.error(msg)

    def populate_table_rentals(self, table_data: list):
        self.log.info('Found = {}'.format(table_data))
        self.tableRentals.setModel(DefaultTableModel(Rental, table_data=table_data, parent=self.tableRentals))
