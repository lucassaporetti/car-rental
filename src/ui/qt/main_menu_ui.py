from PyQt5 import uic


class MainMenuUi:
    def __init__(self):
        form, window = uic.loadUiType('ui/qt/forms/car_rental.ui', import_from='')
        self.window = window()
        self.form = form()
        self.form.setupUi(self.window)
        self.setup_ui()
        self.button = None

    def setup_ui(self):
        pass

    def show(self):
        self.window.show()
