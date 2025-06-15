import os
import time

from Config import LOCATION
from core import ScreenCapture, OCR, Translator


async def translate_pipeline_async(
    region: tuple[int, int, int, int],
    ocr_method: str = "tesseract",
    ocr_lang: str = "eng",
    src_lang: str = "auto",
    dest_lang: str = "vi",
    is_save_image: bool = True,
) -> str:
    """
    Asynchronous translation pipeline that captures a screen region, extracts text using OCR, and translates it.
    :param region: The screen region to capture (x, y, width, height).
    :param ocr_method: The OCR method to use (e.g., "tesseract").
    :param ocr_lang: The language for OCR.
    :param src_lang: The source language for translation.
    :param dest_lang: The destination language for translation.
    :param is_save_image: Whether to save the captured image.
    :return: The translated text.
    """
    if is_save_image:
        cid = int(time.time())
        file_dir = f"{LOCATION}/asset/capture"
        os.makedirs(file_dir, exist_ok=True)
        fp = f"{file_dir}/capture-{cid}.png"
    else:
        fp = None

    image = ScreenCapture.capture_screen(region, fp)
    if image is None:
        raise ValueError("TranslatePipeline[translate_pipeline_async]: Screen capture failed, image is None")

    text = OCR.dispatch_ocr(ocr_method, image, lang=ocr_lang)
    if text is None:
        raise ValueError("TranslatePipeline[translate_pipeline_async]: OCR extraction failed, text is None")

    translated_text = await Translator.translate_google(text, src_lang, dest_lang)
    if translated_text is None:
        raise ValueError("TranslatePipeline[translate_pipeline_async]: Translation failed, translated_text is None")

    return translated_text
