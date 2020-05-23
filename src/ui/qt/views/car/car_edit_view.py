from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from core.eventbus.event_bus import EventBus
from ui.qt.views.qt_view import QtView


class CarEditView(QtView):
    def __init__(self, window: QDialog, parent: QtView):
        super().__init__(window, parent)
        self.selected_uuid = None
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
        EventBus.get('selection-bus').subscribe('rowSelected', self.car_selected)
        self.bbAddCar.accepted.connect(self.on_save)
        self.bbAddCar.rejected.connect(self.on_cancel)
        self.bbAddCar.button(QDialogButtonBox.Reset).clicked.connect(self.on_reset)

    def car_selected(self, args):
        car = args['selected_item']
        self.log.info('Car selected for update: {}'.format(car))
        self.selected_uuid = car.uuid
        self.leCarName.setText(car.name)
        self.leChassis.setText(car.chassis)
        self.cmbColor.setCurrentText(car.color.name)
        self.spbDoors.setValue(car.doors)
        self.cmbFuel.setCurrentText(car.fuel.name)
        self.lePlate.setText(car.plate)
        self.spbPrice.setValue(car.price)

    def on_reset(self):
        self.log.info('Car form reset')
        self.selected_uuid = None
        self.leCarName.setText(None)
        self.leChassis.setText(None)
        self.cmbColor.setCurrentIndex(0)
        self.spbDoors.setValue(3)
        self.cmbFuel.setCurrentIndex(0)
        self.lePlate.setText(None)
        self.spbPrice.setValue(0.00)
        self.window.repaint()

    def on_save(self):
        pass

    def on_cancel(self):
        self.parent.car_search.stackedPanelCars.setCurrentIndex(0)
