from PyQt5 import QtCore, QtGui, QtWidgets

class CaptureWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._mouse_position = None

        self.init_ui()
        self.init_shortcut()

    def init_ui(self):
        flags = QtCore.Qt.FramelessWindowHint
        flags |= QtCore.Qt.WindowSystemMenuHint
        flags |= QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.resize(400, 300)

        lyt = QtWidgets.QVBoxLayout(self)
        lyt.setContentsMargins(10, 10, 10, 10)
        lbl = QtWidgets.QLabel()
        lbl.setText(
            "Kéo di chuyển hoặc resize cửa sổ này.\n"
            "Nhấn Ctrl+Shift+S để test."
        )
        lbl.setAlignment(QtCore.Qt.AlignCenter)
        lbl.setStyleSheet(
            """
            QLabel {
                background-color: rgba(0, 0, 0, 100);
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            """
        )
        lyt.addWidget(lbl)

        lyt_size = QtWidgets.QHBoxLayout()
        lyt_size.addStretch()
        grip = QtWidgets.QSizeGrip(self)
        lyt_size.addWidget(grip)
        lyt.addLayout(lyt_size)

    def init_shortcut(self):
        def on_capture_shortcut():
            print("Shortcut Ctrl+Shift+S detected!")
            print(f"x: {self.x()}, y: {self.y()}")
            print(f"w: {self.width()}, h: {self.height()}")
            print()

        default_sequence = QtGui.QKeySequence("Ctrl+Shift+S")
        shortcut = QtWidgets.QShortcut(default_sequence, self)
        shortcut.activated.connect(on_capture_shortcut)

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
