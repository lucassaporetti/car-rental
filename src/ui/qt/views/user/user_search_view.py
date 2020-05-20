from PyQt5.QtWidgets import QDialog, QStackedWidget

from src.ui.qt.qt_view import QtView


class UserSearchView(QtView):
    def __init__(self, window: QDialog):
        super().__init__(window)
        self.stackPanelUsers = self.qt.find_stacked_widget('stackPanelUsers')
        self.btnAddUser = self.qt.find_tool_button('btnAddUser')

    def setup_ui(self):
        self.btnAddUser.clicked.connect(self.btn_add_user_clicked)

    def btn_add_user_clicked(self):
        self.stackPanelUsers.setCurrentIndex(1)
        self.log.info('Tool button: btnAddUser clicked')
