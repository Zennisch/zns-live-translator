from core import TranslatePipeline
from test.Mark import MARK


@MARK.asyncio
async def test_translate_image():
    region = 500, 100, 1200, 600
    translated_text = await TranslatePipeline.translate_pipeline_async(region)
    print(f"Translated text: {translated_text}")
