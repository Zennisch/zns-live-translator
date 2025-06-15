import asyncio

from PyQt5.QtCore import QThread, pyqtSignal

from core import TranslatePipeline


class TranslateThread(QThread):
    signal_finish = pyqtSignal(str)

    def __init__(
        self,
        region: tuple[int, int, int, int],
        ocr_method: str = "tesseract",
        ocr_lang: str = "eng",
        src_lang: str = "auto",
        dest_lang: str = "vi",
        is_save_image: bool = True,
    ):
        super().__init__()
        self.region = region
        self.ocr_method = ocr_method
        self.ocr_lang = ocr_lang
        self.src_lang = src_lang
        self.dest_lang = dest_lang
        self.is_save_image = is_save_image

    def run(self):
        asyncio.run(self.translate())

    async def translate(self):
        translated_text = await TranslatePipeline.translate_pipeline_async(
            region=self.region,
            ocr_method=self.ocr_method,
            ocr_lang=self.ocr_lang,
            src_lang=self.src_lang,
            dest_lang=self.dest_lang,
            is_save_image=self.is_save_image
        )
        self.signal_finish.emit(translated_text)
