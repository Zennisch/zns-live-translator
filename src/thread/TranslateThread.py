import asyncio

from PyQt5.QtCore import QThread, pyqtSignal

from core import Translator


class TranslateThread(QThread):
    signal_finish = pyqtSignal(str)

    def __init__(self, text: str, source_lang: str = "auto", target_lang: str = "en"):
        super().__init__()
        self.text = text
        self.source_lang = source_lang
        self.target_lang = target_lang

    def run(self):
        asyncio.run(self.translate())

    async def translate(self):
        translated_text = await Translator.translate(self.text, self.source_lang, self.target_lang)
        self.signal_finish.emit(translated_text)
