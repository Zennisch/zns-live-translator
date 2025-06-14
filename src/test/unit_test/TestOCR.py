from Config import LOCATION
from core import OCR


def test_extract_text_from_image_file_path():
    fp = f"{LOCATION}/asset/test/test_extract_text_from_image_file_path.png"
    text = OCR.extract_text_from_image_tesseract(fp, lang="vie")
    print(text)
    assert text != "", "OCR extraction failed, text is empty"
