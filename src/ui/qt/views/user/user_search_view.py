from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractScrollArea
from pymysql.err import InternalError

from core.dto.UserDto import UserDto
from core.enum.color import Color
from core.service.service_facade import ServiceFacade
from ui.qt.table_model.default_table_model import DefaultTableModel
from ui.qt.views.qt_view import QtView


class UserSearchView(QtView):
    @staticmethod
    def customers_to_userdto(customers: list) -> list:
        return list(map(lambda c: UserDto.from_customer(c), customers))

    @staticmethod
    def employees_to_userdto(employees: list) -> list:
        return list(map(lambda c: UserDto.from_employee(c), employees))

    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.customer_service = ServiceFacade.get_customer_service()
        self.employee_service = ServiceFacade.get_employee_service()
        self.stackedPanelUsers = self.qt.find_stacked_widget('stackedPanelUsers')
        self.tableUsers = self.qt.find_table_view('tableUsers')
        self.btnSearchUsers = self.qt.find_tool_button('btnSearchUsers')
        self.leSearchUser = self.qt.find_line_edit('leSearchUser')
        self.btnAddUser = self.qt.find_tool_button('btnAddUser')
        self.setup_ui()

    def setup_ui(self):
        self.stackedPanelUsers.setCurrentIndex(0)
        self.tableUsers.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableUsers.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableUsers.horizontalHeader().setStretchLastSection(True)
        self.btnSearchUsers.clicked.connect(self.btn_search_user_clicked)
        self.btnAddUser.clicked.connect(self.btn_add_user_clicked)

    def btn_add_user_clicked(self):
        self.stackedPanelUsers.setCurrentIndex(1)
        self.log.info('Tool button: btnAddUser clicked')

    def btn_search_user_clicked(self):
        self.log.info('Tool button: btnSearchUsers clicked')
        criteria = self.leSearchUser.text() or '*'
        found = []
        try:
            if criteria or criteria == '*':
                found_customers = self.customer_service.list(filters=criteria if criteria != '*' else None)
                if found_customers and len(found_customers) > 0:
                    found.extend(UserSearchView.customers_to_userdto(found_customers))
                found_employees = self.employee_service.list(filters=criteria if criteria != '*' else None)
                if found_employees and len(found_customers) > 0:
                    found.extend(UserSearchView.employees_to_userdto(found_employees))
                if len(found) > 0:
                    self.populate_table_users(found)
                    self.parent.set_status('Found {} users matching: {}'.format(len(found), criteria))
                else:
                    msg = 'No users found for the matching criteria: {}'.format(criteria)
                    self.parent.set_status(msg, Color.ORANGE)
                    self.log.warn(msg)
        except InternalError:
            msg = 'Invalid criteria {}'.format(criteria)
            self.parent.set_status(msg, Color.RED)
            self.log.error(msg)

    def populate_table_users(self, table_data: list):
        self.log.info('Found = {}'.format(table_data))
        self.tableUsers.setModel(DefaultTableModel(UserDto, table_data=table_data, parent=self.tableUsers))
