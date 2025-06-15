import os.path

from Config import LOCATION
from core import ScreenCapture
from test.Mark import MARK


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
    x, y, width, height = 500, 100, 1200, 600
    fp = f"{LOCATION}/asset/test/test_screen_capture_fp.png"
    image = ScreenCapture.capture_screen((x, y, width, height), fp)
    assert image is not None, "Screen capture failed, image is None"
    assert image.size == (width, height), "Captured image size does not match expected dimensions"
    assert os.path.exists(fp), "Captured image file does not exist"
