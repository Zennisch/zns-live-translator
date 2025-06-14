from typing import Tuple, Optional

import mss
from PIL import Image


def capture_screen(region=Tuple[int, int, int, int], fp=None) -> Optional[Image.Image]:
    """
    Capture a screenshot of the specified region of the screen.

    :param region: A tuple (left, top, width, height) defining the region to capture.
    :param fp: Optional file path to save the screenshot. If provided, the image will be saved in PNG format.
    :return: An Image object containing the screenshot.
    """
    x, y, width, height = region
    capture_area = {"top": y, "left": x, "width": width, "height": height}

    with mss.mss() as sct:
        try:
            screenshot = sct.grab(capture_area)
            image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
            if fp:
                image.save(fp, format='PNG')
            return image
        except Exception as e:
            print(f"ScreenCapture[capture_screen]: Error capturing screen: {e}")
            return None
