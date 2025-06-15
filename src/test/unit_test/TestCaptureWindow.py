import sys

from PyQt5 import QtWidgets

from ui.CaptureWindow import CaptureWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CaptureWindow()
    window.show()
    sys.exit(app.exec_())
