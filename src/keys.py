from pynput.keyboard import Key, Controller, Listener
from typing import Union
from time import sleep

# Wait times
ESCAPE_MENU_NAVIGATION = 0.1
SOCIAL_MENU_NAVIGATION = 0.2
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
    press_key(Key.enter)
    sleep(0.2)