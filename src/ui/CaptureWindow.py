from PyQt5 import QtCore, QtGui, QtWidgets

from thread.TranslateThread import TranslateThread


class CaptureWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._mouse_position = None
        self._translate_thread = None

        self.init_ui()
        self.init_shortcut()

    def init_ui(self):
        flags = QtCore.Qt.FramelessWindowHint
        flags |= QtCore.Qt.WindowSystemMenuHint
        flags |= QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.resize(400, 300)

        main_lyt = QtWidgets.QHBoxLayout(self)
        main_lyt.setContentsMargins(10, 10, 10, 10)

        content_lyt = QtWidgets.QVBoxLayout()
        content_lbl = QtWidgets.QLabel()
        content_lbl.setText(
            "Kéo di chuyển hoặc resize cửa sổ này.\n"
            "Nhấn Ctrl+Shift+S để test."
        )
        content_lbl.setAlignment(QtCore.Qt.AlignCenter)
        content_lbl.setStyleSheet(
            """
            QLabel {
                background-color: rgba(0, 0, 0, 100);
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            """
        )
        content_lyt.addWidget(content_lbl)
        main_lyt.addLayout(content_lyt, 1)

        grip_lyt = QtWidgets.QVBoxLayout()
        grip_lyt.addStretch()
        grip = QtWidgets.QSizeGrip(self)
        grip_lyt.addWidget(grip)
        main_lyt.addLayout(grip_lyt, 0)

    def init_shortcut(self):
        default_capture_sequence = QtGui.QKeySequence("Ctrl+Shift+S")
        capture_shortcut = QtWidgets.QShortcut(default_capture_sequence, self)
        capture_shortcut.activated.connect(self.on_capture_shortcut)

    def on_capture_shortcut(self):
        def finish(translated_text: str):
            print(f"Translated text: {translated_text}")
            self.show()

        self.hide()

        region = self.x(), self.y(), self.width(), self.height()
        ocr_method = "tesseract"
        ocr_lang = "eng"
        src_lang = "auto"
        dest_lang = "vi"
        is_save_image = True

        self._translate_thread = TranslateThread(
            region=region,
            ocr_method=ocr_method,
            ocr_lang=ocr_lang,
            src_lang=src_lang,
            dest_lang=dest_lang,
            is_save_image=is_save_image
        )
        self._translate_thread.signal_finish.connect(finish)
        self._translate_thread.start()

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
