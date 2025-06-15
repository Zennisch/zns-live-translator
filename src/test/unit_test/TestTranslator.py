from core import Translator
from test.Mark import MARK


@MARK.asyncio
async def test_translate_no_text():
    result = await Translator.translate_google("")
    assert result == ""


@MARK.asyncio
async def test_translate_whitespace_text():
    result = await Translator.translate_google("   ")
    assert result == ""


@MARK.asyncio
async def test_translate_src_auto():
    result = await Translator.translate_google("Xin chào, Thế giới!")
    assert result == "Hello, World!"


@MARK.asyncio
async def test_translate_src_ja():
    result = await Translator.translate_google("こんにちは、世界！", src_lang="ja")
    assert result == "Hello World!"


@MARK.asyncio
async def test_translate_dest_ja():
    result = await Translator.translate_google("Hello, World!", dest_lang="ja")
    assert result == "こんにちは世界！"


@MARK.asyncio
async def test_translate_src_ja_dest_vi():
    result = await Translator.translate_google("こんにちは、世界！", src_lang="ja", dest_lang="vi")
    assert result == "Xin chào Thế giới!"
