import sys
from PyQt5.QtWidgets import QApplication
from controller import JGKitMainwindows


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = JGKitMainwindows()

    win.show()
    sys.exit(app.exec_())
