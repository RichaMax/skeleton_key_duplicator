import logging
from enum import Enum
from time import sleep
from pynput import keyboard

from time import sleep
from pynput.keyboard import Key, Controller, Listener
from typing import Union
from time import sleep

from PIL import Image, ImageGrab
from time import sleep
import numpy as np

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
            if i == 0:
                raise Exception
            break
# Wait times
ESCAPE_MENU_NAVIGATION = 0.1
SOCIAL_MENU_NAVIGATION = 0.1
EXIT_POPUP_NAVIGATION = 0.2

ESCAPE_MENU_OPEN = 0.2
SOCIAL_MENU_OPEN = 0.3
EXIT_POPUP_OPEN = 0.2

clavier = Controller()

def press_key(key: Union[Key, str], times: int = 1, pause: float = 0.):
    for _ in range(times):
        clavier.press(key)
        clavier.release(key)
        sleep(pause)

def continue_game():
    press_key(Key.enter, times=2)
    
def exit_to_main_menu():
    press_key(Key.esc, pause=ESCAPE_MENU_OPEN)
    press_key(Key.down, times=4, pause=ESCAPE_MENU_NAVIGATION)
    press_key(Key.enter, pause=EXIT_POPUP_OPEN)
    press_key(Key.left, times=2, pause=EXIT_POPUP_NAVIGATION)
    press_key(Key.enter)
    
def open_mail():
    press_key(Key.esc, pause=ESCAPE_MENU_OPEN)
    press_key(Key.down, pause=ESCAPE_MENU_NAVIGATION)
    press_key(Key.enter, pause=SOCIAL_MENU_OPEN)
    press_key('c', times=3, pause=SOCIAL_MENU_NAVIGATION)
    sleep(0.4)
    press_key('e')
    sleep(0.3)


def ticker(interval: float):
    i = 0
    while True:
        yield i
        i += 1
        sleep(interval)
        

ACTIVE = False

class BotStoppedError(Exception):
    pass
        
def switch_active(key: keyboard.Key):
    global ACTIVE
    if isinstance(key, keyboard._win32.KeyCode):
        if key.char.lower() == 'm':
            ACTIVE = not ACTIVE

if __name__ == '__main__':
    listener = keyboard.Listener(
        on_release=switch_active,
    )
    
    listener.start()

    print('Bot ready. Press M to activate/deactivate')
    
    duplications = 0

    while not ACTIVE:
        sleep(0.1)

    print('Bot started')

    while ACTIVE:
            
        continue_game()
        
        wait_for_end_loading_screen()

        open_mail()
        
        exit_to_main_menu()
        
        wait_for_end_loading_screen()

        duplications += 1

    print('Bot finished')

    print(f'{duplications} duplications')