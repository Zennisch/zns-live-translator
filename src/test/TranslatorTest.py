import pytest

from core import Translator

_mark = pytest.mark


@_mark.asyncio
async def test_translate_no_text():
    result = await Translator.translate("")
    assert result == ""


@_mark.asyncio
async def test_translate_whitespace_text():
    result = await Translator.translate("   ")
    assert result == ""


@_mark.asyncio
async def test_translate_source_auto():
    result = await Translator.translate("Xin chào, Thế giới!")
    assert result == "Hello, World!"


@_mark.asyncio
async def test_translate_source_ja():
    result = await Translator.translate("こんにちは、世界！", source_lang="ja")
    assert result == "Hello World!"


@_mark.asyncio
async def test_translate_target_ja():
    result = await Translator.translate("Hello, World!", target_lang="ja")
    assert result == "こんにちは世界！"

@_mark.asyncio
async def test_translate_source_ja_target_vi():
    result = await Translator.translate("こんにちは、世界！", source_lang="ja", target_lang="vi")
    assert result == "Xin chào Thế giới!"
