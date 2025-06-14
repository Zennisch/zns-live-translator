from core import OCR


def test_extract_text_from_image_file_path():
    image_path = "../asset/test/"
    text = OCR.extract_text_from_image(image_path, lang="vie")
    print(text)
    assert text != "", "OCR extraction failed, text is empty"
