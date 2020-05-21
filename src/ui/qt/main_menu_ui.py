from PyQt5 import uic
from PyQt5.QtWidgets import QTabWidget

from src.app_configs import AppConfigs
from src.ui.qt.qt_view import QtView
from src.ui.qt.views.car.car_edit_view import CarEditView
from src.ui.qt.views.car.car_search_view import CarSearchView
from src.ui.qt.views.rental.rental_edit_view import RentalEditView
from src.ui.qt.views.rental.rental_search_view import RentalSearchView
from src.ui.qt.views.user.user_edit_view import UserEditView
from src.ui.qt.views.user.user_search_view import UserSearchView


class MainMenuUi(QtView):
    form, window = uic \
        .loadUiType(f"{AppConfigs.root_dir()}/ui/qt/forms/car_rental.ui")

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.tabPanel = self.qt.find_widget(self.window, QTabWidget, 'tabPanel')
        self.car_search = CarSearchView(self.window)
        self.car_edit = CarEditView(self.window)
        self.user_search = UserSearchView(self.window)
        self.user_edit = UserEditView(self.window)
        self.rental_search = RentalSearchView(self.window)
        self.rental_edit = RentalEditView(self.window)
        self.setup_ui()

    def setup_ui(self):
        self.tabPanel.currentChanged.connect(self.tab_changed)

    def show(self):
        self.window.show()

    def tab_changed(self, idx: int):
        self.car_search.stackedPanelCarModels.setCurrentIndex(0)
        self.user_search.stackedPanelUsers.setCurrentIndex(0)
        self.rental_search.stackedPanelRentals.setCurrentIndex(0)
        self.log.info('Tab: tabPanel changed to {}'.format(idx))
