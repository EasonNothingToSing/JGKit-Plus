# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from .assets import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from viewer.MainWidget import Ui_JGKitPlusMainWindows
from PyQt5.QtCore import QSize


class JGKitSize(QSize):
    FONT_HEIGHT = 20
    FONT_WIDTH = 15

    def __init__(self):
        super(JGKitSize, self).__init__()
        self.setHeight(JGKitSize.FONT_HEIGHT)
        self.setWidth(JGKitSize.FONT_WIDTH)


class JGKitDeviceModel(QStandardItemModel):
    header_labels = ["Name", "Address", "Field", "Property"]
    header_width = [250, 200, 100, 100]

    def __init__(self):
        super(JGKitDeviceModel, self).__init__()
        self.setHorizontalHeaderLabels(JGKitDeviceModel.header_labels)


class JGKitStandardItem(QStandardItem):
    def __init__(self, _str):
        super(JGKitStandardItem, self).__init__(_str)
        self.setEditable(False)
        self.setSizeHint(JGKitSize())


# class JGKitRegister(QStandardItem):
#     def __init__(self, register):
#         super(JGKitRegister, self).__init__()
#         self.register = register
#
#     def __iter__(self):
#         return self


class JGKitDeviceEditModel(QStandardItemModel):
    header_labels = ["Name", "Address | Field", "Property", "Write Value", "Read Value"]
    header_width = [250, 200, 100, 150, 150]

    def __init__(self):
        super(JGKitDeviceEditModel, self).__init__()
        self.setHorizontalHeaderLabels(JGKitDeviceEditModel.header_labels)
