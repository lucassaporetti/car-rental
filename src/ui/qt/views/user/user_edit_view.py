from datetime import date

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from core.dto.UserDto import UserDto
from core.enum.access_type import AccessType
from core.enum.user_type import UserType
from core.eventbus.event_bus import EventBus
from core.service.service_facade import ServiceFacade
from ui.qt.views.qt_view import QtView


class UserEditView(QtView):
    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.customer_service = ServiceFacade.get_customer_service()
        self.employee_service = ServiceFacade.get_employee_service()
        self.selected_user = None
        self.leUserName = self.qt.find_line_edit('leUserName')
        self.spbAge = self.qt.find_spin_box('spbAge')
        self.leAddress = self.qt.find_line_edit('leAddress')
        self.lePhone = self.qt.find_line_edit('lePhone')
        self.leEmail = self.qt.find_line_edit('leEmail')
        self.cmbUserType = self.qt.find_combo_box('cmbUserType')
        self.leDrvLicense = self.qt.find_line_edit('leDrvLicense')
        self.cmbAccessType = self.qt.find_combo_box('cmbAccessType')
        self.deHiredDate = self.qt.find_date_edit('deHiredDate')
        self.spbSalary = self.qt.find_double_spin_box('spbSalary')
        self.bbAddUser = self.qt.find_button_box('bbAddUser')
        self.lblDrvLicense = self.qt.find_label('lblDrvLicense')
        self.lblAccessType = self.qt.find_label('lblAccessType')
        self.lblHiredDate = self.qt.find_label('lblHiredDate')
        self.lblSalary = self.qt.find_label('lblSalary')
        self.setup_ui()

    def setup_ui(self):
        EventBus.get('user-selection-bus').subscribe('rowSelected', self.user_selected)
        self.bbAddUser.accepted.connect(self.on_save)
        self.bbAddUser.rejected.connect(self.on_cancel)
        self.bbAddUser.button(QDialogButtonBox.Reset).clicked.connect(self.on_reset)
        self.cmbUserType.currentIndexChanged.connect(self.user_type_changed)

    def user_selected(self, args):
        user = args['selected_item']
        user_type = user.user_type()
        self.log.info('User selected for update: {}'.format(user))
        self.selected_user = user
        self.leUserName.setText(user.name)
        self.spbAge.setValue(user.age)
        self.leAddress.setText(user.address)
        self.lePhone.setText(user.phone)
        self.leEmail.setText(user.email)
        self.cmbUserType.setCurrentText(user_type.name)
        if user_type == UserType.CUSTOMER:
            self.leDrvLicense.setText(user.drv_license)
        else:
            self.cmbAccessType.setCurrentText(user.access_type)
            self.deHiredDate.setDate(QDate.fromString(user.hired_date))
            self.spbSalary.setValue(user.salary)

    def user_type_changed(self):
        user_type = UserType[self.cmbUserType.currentText()]
        self.lblDrvLicense.setEnabled(user_type == UserType.CUSTOMER)
        self.lblAccessType.setEnabled(user_type == UserType.EMPLOYEE)
        self.lblHiredDate.setEnabled(user_type == UserType.EMPLOYEE)
        self.lblSalary.setEnabled(user_type == UserType.EMPLOYEE)
        self.leDrvLicense.setEnabled(user_type == UserType.CUSTOMER)
        self.cmbAccessType.setEnabled(user_type == UserType.EMPLOYEE)
        self.deHiredDate.setEnabled(user_type == UserType.EMPLOYEE)
        self.spbSalary.setEnabled(user_type == UserType.EMPLOYEE)
        self.window.repaint()

    def on_reset(self):
        self.log.info('User form reset')
        self.selected_user = None
        self.leUserName.setText(None)
        self.spbAge.setValue(18)
        self.leAddress.setText(None)
        self.lePhone.setText(None)
        self.leEmail.setText(None)
        self.cmbUserType.setCurrentText(UserType.CUSTOMER.name)
        self.leDrvLicense.setText(None)
        self.cmbAccessType.setCurrentText(AccessType.ADMIN.name)
        self.deHiredDate.setDate(QDate.fromString(date.today().strftime("%d/%m/%Y"), "dd/MM/yyyy"))
        self.spbSalary.setValue(450.0)
        self.window.repaint()

    def on_save(self):
        self.selected_user = self.selected_user if self.selected_user else UserDto()
        user_type = UserType[self.cmbUserType.currentText()]
        self.selected_user.name = self.leUserName.text()
        self.selected_user.age = self.spbAge.value()
        self.selected_user.address = self.leAddress.text()
        self.selected_user.phone = self.lePhone.text()
        self.selected_user.email = self.leEmail.text()
        if user_type == UserType.CUSTOMER:
            self.selected_user.drv_license = self.leDrvLicense.text()
            self.customer_service.save(self.selected_user.to_customer())
        else:
            self.selected_user.access_type = AccessType[self.cmbAccessType.currentText()]
            self.selected_user.hired_date = self.deHiredDate.text()
            self.selected_user.salary = self.spbSalary.value()
            self.employee_service.save(self.selected_user.to_employee())
        self.parent.user_search.btn_search_user_clicked()
        self.parent.user_search.stackedPanelUsers.setCurrentIndex(0)
        self.on_reset()
        self.log.info('{} saved: {}'.format(user_type, self.selected_user))

    def on_cancel(self):
        self.on_reset()
        self.parent.user_search.stackedPanelUsers.setCurrentIndex(0)
