from googletrans import Translator
from googletrans.models import Translated


async def translate(text: str, source_lang: str = "auto", target_lang: str = "en") -> str:
    """
    Translates the given text from source language to target language.

    :param text: The text to translate.
    :param source_lang: The language of the input text (default is 'auto').
    :param target_lang: The language to translate the text into (default is 'en').
    :return: The translated text.
    """
    async with Translator(service_urls=["translate.googleapis.com"]) as translator:
        if not text.strip():  # Check if the text is empty or contains only whitespace
            return ""

        try:
            result: Translated = await translator.translate(text, src=source_lang, dest=target_lang)
            return result.text
        except Exception as e:
            print(f"Translator[translate]: Error translating text: {e}")
            return text
