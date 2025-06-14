import os.path

from Config import LOCATION
from core import OCR
from core import ScreenCapture
from core import Translator
from test.Mark import MARK


@MARK.asyncio
async def test_translate_image():
    x, y, width, height = 500, 100, 1200, 600
    fp = f"{LOCATION}/asset/test/test_translate_image.png"
    image = ScreenCapture.capture_screen((x, y, width, height), fp)
    assert image is not None, "Screen capture failed, image is None"
    assert image.size == (width, height), "Captured image size does not match expected dimensions"
    assert os.path.exists(fp), "Captured image file does not exist"

    text = OCR.extract_text_from_image_tesseract(image, lang="eng")
    assert text != "", "OCR extraction failed, text is empty"

    translated_text = await Translator.translate(text, source_lang="auto", target_lang="ja")
    assert translated_text != "", "Translation failed, translated text is empty"
    print(translated_text)
