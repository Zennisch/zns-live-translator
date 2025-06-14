import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class TransparentWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._mouse_position = None

        self.init_ui()
        self.init_shortcut()

    def init_ui(self):
        flags = QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.resize(400, 200)

        label = QtWidgets.QLabel("Kéo di chuyển hoặc resize cửa sổ này.\nNhấn Ctrl+Shift+S để test.", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet(
            """
                    QLabel {
                        background-color: rgba(0, 0, 0, 100);
                        color: white;
                        border-radius: 8px;
                        padding: 10px;
                    }
                """
        )

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(label)

        grip = QtWidgets.QSizeGrip(self)
        size_layout = QtWidgets.QHBoxLayout()
        size_layout.addStretch()
        size_layout.addWidget(grip)
        layout.addLayout(size_layout)

    def init_shortcut(self):
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+S"), self)
        shortcut.activated.connect(self.on_shortcut)

    def on_shortcut(self):
        print("Shortcut Ctrl+Shift+S detected!")
        print(f"Current position - x: {self.x()}, y: {self.y()}")
        print(f"Current dimensions - width: {self.width()}, height: {self.height()}")

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._mouse_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._mouse_position is not None and event.buttons() & QtCore.Qt.LeftButton:
            new_position = event.globalPos() - self._mouse_position
            self.move(new_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._mouse_position = None
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec_())
