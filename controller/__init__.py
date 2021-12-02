from viewer import *
from module import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory


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
        for num, width in enumerate(JGKitDeviceEditModel.header_width):
            self.DeviceEditTree.setColumnWidth(num, width)
