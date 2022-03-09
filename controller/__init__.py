from viewer import *
from module import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui


class JGKitMainwindows(QMainWindow, MainWidget.Ui_JGKitPlusMainWindows):
    def __init__(self, parent=None):
        super(JGKitMainwindows, self).__init__(parent)
        self.setupUi(self)

        # Load device model in tree view
        self.exl_handler = ExlParser().get_handler()

        # Device display tree
        self.device_model = JGKitDeviceModel()
        self.DeviceDisplayTree.setModel(self.device_model)
        self.DeviceDisplayTree.setStyle(QStyleFactory.create('windows'))
        for num, width in enumerate(JGKitDeviceModel.header_width):
            self.DeviceDisplayTree.setColumnWidth(num, width)

        # self.edit_device_model = JGKitDeviceEditModel()
        # self.DeviceEditTree.setModel(self.edit_device_model)
        # self.DeviceEditTree.setStyle(QStyleFactory.create('windows'))
        # for num, width in enumerate(JGKitDeviceEditModel.header_width):
        #     self.DeviceEditTree.setColumnWidth(num, width)

        def _list_render(info):
            t_list = []
            for i in JGKitDeviceModel.header_labels:
                if i not in info().keys():
                    t_list.append("")
                else:
                    t_list.append(info()[i])
            return t_list

        # Display tree render
        for _device in self.exl_handler:
            _device.render_list = list(map(JGKitStandardItem, _list_render(_device)))
            _device.render_list[0].setIcon(QIcon(JGKit_Display_TreeViewer_Device_Icon))

            self.device_model.appendRow(_device.render_list)
            for _register in _device:
                _register.render_list = list(map(JGKitStandardItem, _list_render(_register)))
                _register.render_list[0].setIcon(QIcon(JGKit_Display_TreeViewer_Register_Icon))

                _device.render_list[0].appendRow(_register.render_list)
                for _field in _register:
                    _field.render_list = list(map(JGKitStandardItem, _list_render(_field)))
                    _field.render_list[0].setIcon(QIcon(JGKit_Display_TreeViewer_Field_Icon))

                    _register.render_list[0].appendRow(_field.render_list)

        # Load device edit model in tree view
        self.device_edit_model = JGKitDeviceEditModel()
        self.DeviceEditTree.setModel(self.device_edit_model)
        self.DeviceEditTree.setStyle(QStyleFactory.create('windows'))
        for num, width in enumerate(JGKitDeviceEditModel.header_width):
            self.DeviceEditTree.setColumnWidth(num, width)

    @pyqtSlot()
    def on_Connect_clicked(self):
        checked = self.Connect.isChecked()
        self._status_invert(checked)
        if checked:
            self._status_bar_show_message("Connect to jlink")
        else:
            self._status_bar_show_message("Disconnect")

    @pyqtSlot()
    def on_Save_clicked(self):
        pass

    @pyqtSlot()
    def on_Open_clicked(self):
        pass

    @pyqtSlot()
    def on_Refresh_clicked(self):
        pass

    @pyqtSlot()
    def on_MemAdd_clicked(self):
        pass

    @pyqtSlot()
    def on_MemDel_clicked(self):
        pass

    @pyqtSlot()
    def on_LeftMove_clicked(self):
        pass

    @pyqtSlot()
    def on_RightMove_clicked(self):
        _index = self.DeviceDisplayTree.currentIndex()
        _sub_index = _index.model()
        data = _sub_index.itemData()
        print(_sub_index)

    @pyqtSlot()
    def on_Refresh_Hold_stateChanged(self):
        checked = self.Refresh_Hold.isChecked()
        if checked:
            self._status_bar_show_message("Enable auto refresh")
        else:
            self._status_bar_show_message("Disable auto refresh")

    @pyqtSlot()
    def on_RightMove_clicked(self):
        index_list = self.DeviceDisplayTree.selectionModel().selectedIndexes()
        print(index_list)
        _item = []
        for index in index_list:
            print(index.data())
            _item.append(index)
        # self.device_edit_model.appendRow(index_list)

    def _status_bar_show_message(self, msg, timeout=2000):
        self.statusbar.showMessage(msg, timeout)

    def _status_invert(self, clicked):
        if clicked:
            self.Save.setEnabled(True)
            self.Open.setEnabled(True)
            self.Refresh.setEnabled(True)
            self.Refresh_Hold.setEnabled(True)
            self.MemAdd.setEnabled(True)
            self.MemDel.setEnabled(True)
            self.actionSave_Configure.setEnabled(True)
            self.actionSave_Configure_As.setEnabled(True)
            self.actionImport_Configure.setEnabled(True)

            self.Status.setPixmap(QtGui.QPixmap(JGKit_Status_Connect_Icon))
        else:
            self.Save.setEnabled(False)
            self.Open.setEnabled(False)
            self.Refresh.setEnabled(False)
            self.Refresh_Hold.setEnabled(False)
            self.Refresh_Hold.setChecked(False)

            self.MemAdd.setEnabled(False)
            self.MemDel.setEnabled(False)
            self.actionSave_Configure.setEnabled(False)
            self.actionSave_Configure_As.setEnabled(False)
            self.actionImport_Configure.setEnabled(False)

            self.Status.setPixmap(QtGui.QPixmap(JGKit_Status_Disconnect_Icon))
