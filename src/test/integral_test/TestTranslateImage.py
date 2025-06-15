import os.path
import time

from Config import LOCATION
from core import OCR
from core import ScreenCapture
from core import Translator
from test.Mark import MARK


@MARK.asyncio
async def test_translate_image():
    x, y, w, h = 500, 100, 1200, 600
    cid = int(time.time())
    fp = f"{LOCATION}/asset/test/test_translate_image-{cid}.png"

    image = ScreenCapture.capture_screen((x, y, w, h), fp)
    assert image is not None, "Screen capture failed, image is None"
    assert image.size == (w, h), "Captured image size does not match expected dimensions"
    assert os.path.exists(fp), "Captured image file does not exist"

    text = OCR.extract_text_from_image_tesseract(image, lang="eng")
    assert text != "", "OCR extraction failed, text is empty"

    translated_text = await Translator.translate(text, source_lang="auto", target_lang="ja")
    assert translated_text != "", "Translation failed, translated text is empty"

    with open(f"{LOCATION}/asset/test/test_translate_image-{cid}.txt", "w", encoding="utf-8") as f:
        f.write(translated_text)
    assert os.path.exists(f"{LOCATION}/asset/test/test_translate_image-{cid}.txt"), "Translation output file does not exist"
