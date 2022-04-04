from PIL import Image, ImageGrab
from time import sleep
import numpy as np

from utils import ticker

def read_screen() -> Image:
    return ImageGrab.grab()

def wait_for_end_loading_screen():
    sleep(0.2)
    for i in ticker(0.1):
        screen = read_screen()
        image_array = np.array(screen, dtype=np.int8)       
        small_rec = image_array[-30:, -30:]
        if np.mean(small_rec) > 3.0:
            sleep(0.2)
            # if i == 0:
            #     raise Exception
            break