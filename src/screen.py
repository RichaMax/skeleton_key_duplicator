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
        image_array = np.array(screen, dtype=np.int64)       
        small_rec = image_array[-30:, -30:]
        print('before carre')
        with open('test.npy', 'wb') as f:
            np.save(f, small_rec)
        if np.mean(small_rec) > 3.0:
            print('after carre')
            sleep(0.2)
            # if i == 0:
            #     raise Exception
            break