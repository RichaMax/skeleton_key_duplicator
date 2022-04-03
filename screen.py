from mss import mss
from PIL import Image
from time import sleep
import numpy as np


def ticker(interval: float):
    while True:
        sleep(interval)
        yield


def read_screen() -> Image:
    with mss() as sct:
        sct.shot(output='output/screenshot.png')
        print('Screenshot taken.')
    
    return Image.open('output/screenshot.png')


def wait_for_end_loading_screen():
    sleep(0.2)
    for _ in ticker(0.1):
        screen = read_screen()
        image_array = np.array(screen, dtype=np.int8)       
        small_rec = image_array[-30:, -30:]
        if np.mean(small_rec) > 3.0:
            sleep(0.2)
            break
    

def wait_for_main_menu():
    screen = read_screen()