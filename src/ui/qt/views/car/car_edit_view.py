from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from core.enum.color import Color
from core.enum.fuel import Fuel
from core.eventbus.event_bus import EventBus
from core.model.car import Car
from core.service.service_facade import ServiceFacade
from ui.qt.views.qt_view import QtView


class CarEditView(QtView):
    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.car_service = ServiceFacade.get_car_service()
        self.selected_car = None
        self.leCarName = self.qt.find_line_edit('leCarName')
        self.leChassis = self.qt.find_line_edit('leChassis')
        self.cmbColor = self.qt.find_combo_box('cmbColor')
        self.spbDoors = self.qt.find_spin_box('spbDoors')
        self.cmbFuel = self.qt.find_combo_box('cmbFuel')
        self.lePlate = self.qt.find_line_edit('lePlate')
        self.spbPrice = self.qt.find_double_spin_box('spbPrice')
        self.bbAddCar = self.qt.find_button_box('bbAddCar')
        self.setup_ui()

    def setup_ui(self):
        EventBus.get('car-selection-bus').subscribe('rowSelected', self.car_selected)
        self.bbAddCar.accepted.connect(self.on_save)
        self.bbAddCar.rejected.connect(self.on_cancel)
        self.bbAddCar.button(QDialogButtonBox.Reset).clicked.connect(self.on_reset)

    def car_selected(self, args):
        car = args['selected_item']
        self.log.info('Car selected for update: {}'.format(car))
        self.selected_car = car
        self.leCarName.setText(car.name)
        self.leChassis.setText(car.chassis)
        self.cmbColor.setCurrentText(car.color.name)
        self.spbDoors.setValue(car.doors)
        self.cmbFuel.setCurrentText(car.fuel.name)
        self.lePlate.setText(car.plate)
        self.spbPrice.setValue(car.price)

    def on_reset(self):
        self.log.info('Car form reset')
        self.selected_car = None
        self.leCarName.setText(None)
        self.leChassis.setText(None)
        self.cmbColor.setCurrentIndex(0)
        self.spbDoors.setValue(3)
        self.cmbFuel.setCurrentIndex(0)
        self.lePlate.setText(None)
        self.spbPrice.setValue(0.00)
        self.window.repaint()

    def on_save(self):
        self.selected_car = self.selected_car if self.selected_car else Car()
        self.selected_car.name = self.leCarName.text()
        self.selected_car.chassis = self.leChassis.text()
        self.selected_car.color = Color[self.cmbColor.currentText()]
        self.selected_car.doors = self.spbDoors.value()
        self.selected_car.fuel = Fuel[self.cmbFuel.currentText()]
        self.selected_car.plate = self.lePlate.text()
        self.selected_car.price = self.spbPrice.value()
        self.selected_car.available = self.selected_car.available.value
        self.car_service.save(self.selected_car)
        self.parent.car_search.btn_search_user_clicked()
        self.parent.car_search.stackedPanelCars.setCurrentIndex(0)
        self.on_reset()
        self.log.info('Car saved: {}'.format(self.selected_car))

    def on_cancel(self):
        self.on_reset()
        self.parent.car_search.stackedPanelCars.setCurrentIndex(0)
