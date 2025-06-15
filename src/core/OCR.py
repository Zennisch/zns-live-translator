from typing import overload, Union

import pytesseract
from PIL import Image


def dispatch_ocr(method: str, image: Union[Image.Image, str], lang: str = "eng") -> str:
    """
    Dispatch OCR method based on the method name.

    :param method: The OCR method to use (e.g., 'tesseract').
    :param image: Either an Image object or a path to an image file.
    :param lang: Language for OCR, default is "eng" (English).
    :return: Extracted text as a string.
    """
    if method == 'tesseract':
        return extract_text_from_image_tesseract(image, lang)
    else:
        raise ValueError(f"Unsupported OCR method: {method}")


@overload
def extract_text_from_image_tesseract(image: Image.Image, lang: str = "eng") -> str: ...

@overload
def extract_text_from_image_tesseract(image_path: str, lang: str = "eng") -> str: ...

def extract_text_from_image_tesseract(image: Union[Image.Image, str], lang: str = "eng") -> str:
    """
    Extract text from an image using OCR.

    :param image: Either an Image object or a path to an image file.
    :param lang: Language for OCR, default is "eng" (English).
    :return: Extracted text as a string.
    """
    try:
        if isinstance(image, str):
            img = Image.open(image)
        else:
            img = image

        text = pytesseract.image_to_string(img, lang=lang)
        return text.strip()
    except ImportError:
        print("pytesseract is not installed. Please install it to use OCR functionality.")
        return ""
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""
