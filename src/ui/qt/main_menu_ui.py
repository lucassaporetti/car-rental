from typing import Type, Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QStackedWidget, QToolButton, QWidget, QTabWidget

from src.configs import AppConfigs
from src.core.tools import log_init

LOG = log_init(AppConfigs.log_file)


class MainMenuUi:
    def __init__(self):
        form, window = uic\
            .loadUiType(f"{AppConfigs.cur_dir}/ui/qt/forms/car_rental.ui")
        self.window = window()
        self.form = form()
        self.form.setupUi(self.window)
        # Initialize components
        self.tabPanel = self.find(QTabWidget, 'tabPanel')
        self.stackPanelCarModels = self.find(QStackedWidget, 'stackedPanelCarModels')
        self.stackPanelUsers = self.find(QStackedWidget, 'stackedPanelUsers')
        self.stackPanelRentals = self.find(QStackedWidget, 'stackedPanelRentals')
        self.btnAddCarModel = self.find(QToolButton, 'btnAddCarModel')
        self.btnAddUser = self.find(QToolButton, 'btnAddUser')
        self.btnRentCar = self.find(QToolButton, 'btnRentCar')
        # Setup events
        self.setup_ui()

    def find(self, widget: Type, name: str) -> Optional[QWidget]:
        return self.window.findChild(widget, name)

    def setup_ui(self):
        self.btnAddCarModel.clicked.connect(self.btn_add_car_clicked)
        self.btnAddUser.clicked.connect(self.btn_add_user_clicked)
        self.btnRentCar.clicked.connect(self.btn_rent_car_clicked)
        self.tabPanel.currentChanged.connect(self.tab_changed)

    def show(self):
        self.window.show()

    def btn_add_car_clicked(self):
        self.stackPanelCarModels.setCurrentIndex(1)
        LOG.info('Tool button: btnAddCarModel clicked')

    def btn_add_user_clicked(self):
        self.stackPanelUsers.setCurrentIndex(1)
        LOG.info('Tool button: btnAddUser clicked')

    def btn_rent_car_clicked(self):
        self.stackPanelRentals.setCurrentIndex(1)
        LOG.info('Tool button: btnRentCar clicked')

    def tab_changed(self, idx: int):
        self.stackPanelCarModels.setCurrentIndex(0)
        self.stackPanelUsers.setCurrentIndex(0)
        self.stackPanelRentals.setCurrentIndex(0)
        LOG.info('Tab: tabPanel changed to {}'.format(idx))

