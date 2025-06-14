import os

from test.Mark import MARK
from core import ScreenCapture


@MARK.test
def test_screen_capture():
    x, y, width, height = 0, 0, 800, 600
    image = ScreenCapture.capture_screen((x, y, width, height))
    assert image is not None, "Screen capture failed, image is None"
    assert image.size == (width, height), "Captured image size does not match expected dimensions"

@MARK.test
def test_screen_capture_invalid_region():
    image = ScreenCapture.capture_screen((0, 0, -100, -100))
    assert image is None, "Screen capture should return None for invalid region"

@MARK.test
def test_screen_capture_fp():
    x, y, width, height = 0, 0, 800, 600
    fp = "../asset/test/test_capture.png"
    image = ScreenCapture.capture_screen((x, y, width, height), fp)
    assert image is not None, "Screen capture failed, image is None"
    assert image.size == (width, height), "Captured image size does not match expected dimensions"
    assert os.path.exists(fp), "Captured image file does not exist"
