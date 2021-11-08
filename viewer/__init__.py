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
from MainWidget import Ui_JGKitPlusMainWindows


class JGKitDeviceModel(QStandardItemModel):
    def __init__(self):
        super(JGKitDeviceModel, self).__init__()


class TShellMainWindow(QMainWindow, Ui_JGKitPlusMainWindows):
    def __init__(self, parent=None):
        super(TShellMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TShellMainWindow()

    attr = vars(win)
    print(', '.join("%s: %s" % item for item in attr.items()))
    win.show()
    sys.exit(app.exec_())
