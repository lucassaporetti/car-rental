from typing import Type

from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt5.QtWidgets import QTableView

from core.model.entity import Entity
from core.tools.commons import class_attribute_names, class_attribute_values


class DefaultTableModel(QAbstractTableModel):
    def __init__(self, clazz: Type[Entity], headers: list = None, table_data: list = None, parent: QTableView = None):
        QAbstractTableModel.__init__(self, parent)
        self.clazz = clazz
        self.table_data = table_data or []
        self.headers = headers if headers else self.headers_by_entity()

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.DisplayRole:
            entity = class_attribute_values(self.table_data[index.row()])[index.column()]
            return entity
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section].upper() if len(self.headers) >= section else '-'
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return section
        return None

    def headers_by_entity(self):
        return class_attribute_names(self.clazz)

    def rowCount(self, parent: QModelIndex = ...):
        return len(self.table_data) if self.table_data and len(self.table_data) > 0 else 0

    def columnCount(self, parent: QModelIndex = ...):
        return len(self.table_data[0].__dict__.keys()) if self.table_data and len(self.table_data) > 0 else 0
