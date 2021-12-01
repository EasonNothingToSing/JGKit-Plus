# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from viewer.MainWidget import Ui_JGKitPlusMainWindows
from PyQt5.QtCore import QSize


class JGKitSize(QSize):
    FONT_HEIGHT = 25
    FONT_WIDTH = 15

    def __init__(self):
        super(JGKitSize, self).__init__()
        self.setHeight(JGKitSize.FONT_HEIGHT)
        self.setWidth(JGKitSize.FONT_WIDTH)


class JGKitDeviceModel(QStandardItemModel):
    header_labels = ["Name", "Address", "Field", "Property"]
    header_width = [200, 100, 100, 50]

    def __init__(self, handler):
        super(JGKitDeviceModel, self).__init__()
        self.setHorizontalHeaderLabels(JGKitDeviceModel.header_labels)
        JGKitDeviceModelItemDisplay(handler, self)


class JGKitStandardItem(QStandardItem):
    def __init__(self, _str):
        super(JGKitStandardItem, self).__init__(_str)
        self.setEditable(False)
        self.setSizeHint(JGKitSize())


class JGKitDeviceModelItemDisplay:
    def __init__(self, handler, parent):

        for device in handler:
            register_parent = self.info_load(device, parent)
            for register in device:
                field_parent = self.info_load(register, register_parent)
                for field in register:
                    self.info_load(field, field_parent)

    def info_load(self, obj, parent):
        _temp_para_list = [JGKitStandardItem(""), JGKitStandardItem(""), JGKitStandardItem(""), JGKitStandardItem("")]

        # 将信息按照 header 顺序依次填入 参数list中
        for item in obj().items():
            for num, info in enumerate(JGKitDeviceModel.header_labels):
                if item[0] == info:
                    _temp_para_list[num] = JGKitStandardItem(str(item[1]))

        parent.appendRow(_temp_para_list)

        return _temp_para_list[0]


class JGKitRegister(QStandardItem):
    def __init__(self, register):
        super(JGKitRegister, self).__init__()
        self.register = register

    def __iter__(self):
        return self


class JGKitDeviceEditModel(QStandardItemModel):
    def __init__(self):
        super(JGKitDeviceEditModel, self).__init__()
        self.setHorizontalHeaderLabels(["Name", "Address | Field", "Property", "Write Value", "Read Value"])


class TShellMainWindow(QMainWindow, Ui_JGKitPlusMainWindows):
    def __init__(self, handler, parent=None):
        super(TShellMainWindow, self).__init__(parent)
        self.setupUi(self)

        # Load device model in tree view
        self.device_model = JGKitDeviceModel(handler)
        self.DeviceDisplayTree.setModel(self.device_model)
        for num, width in enumerate(JGKitDeviceModel.header_width):
            self.DeviceDisplayTree.setColumnWidth(num, width)

        # Load device edit model in tree view
        self.device_edit_model = JGKitDeviceEditModel()
        self.DeviceEditTree.setModel(self.device_edit_model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TShellMainWindow()

    win.show()
    sys.exit(app.exec_())
