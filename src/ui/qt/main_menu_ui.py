from PyQt5 import uic

from src.configs import AppConfigs


class MainMenuUi:
    def __init__(self):
        form, window = uic.loadUiType(f"{AppConfigs.cur_dir}/ui/qt/forms/car_rental.ui")
        self.window = window()
        self.form = form()
        self.form.setupUi(self.window)
        self.setup_ui()
        self.button = None

    def setup_ui(self):
        pass

    def show(self):
        self.window.show()
