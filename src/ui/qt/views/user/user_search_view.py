from PyQt5.QtWidgets import QDialog, QStackedWidget

from src.ui.qt.qt_view import QtView


class UserSearchView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)
        self.stackedPanelUsers = self.qt.find_stacked_widget('stackedPanelUsers')
        self.btnAddUser = self.qt.find_tool_button('btnAddUser')
        self.setup_ui()

    def setup_ui(self):
        self.btnAddUser.clicked.connect(self.btn_add_user_clicked)

    def btn_add_user_clicked(self):
        self.stackedPanelUsers.setCurrentIndex(1)
        self.log.info('Tool button: btnAddUser clicked')
