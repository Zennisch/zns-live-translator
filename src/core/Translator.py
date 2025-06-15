from googletrans import Translator
from googletrans.models import Translated


async def translate_google(text: str, src_lang: str = "auto", dest_lang: str = "en") -> str:
    """
    Translates the given text from source language to destination language using Google Translate.

    :param text: The text to translate.
    :param src_lang: The language of the input text (default is 'auto').
    :param dest_lang: The language to translate the text into (default is 'en').
    :return: The translated text.
    """
    async with Translator(service_urls=["translate.googleapis.com"]) as translator:
        if not text.strip():  # Check if the text is empty or contains only whitespace
            return ""

        try:
            result: Translated = await translator.translate(text, src=src_lang, dest=dest_lang)
            return result.text
        except Exception as e:
            raise RuntimeError(f"Translator[translate_google]: Translation failed with error: {e}") from e
