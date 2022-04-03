from pynput.keyboard import Key, Controller, Listener
from typing import Union
from time import sleep

clavier = Controller()

def press_key(key: Union[Key, str]):
    clavier.press(key)
    clavier.release(key)

def continue_game():
    press_key(Key.enter)
    press_key(Key.enter)
    
def exit_to_main_menu():
    press_key(Key.esc)
    for _ in range(4):
        sleep(0.2)
        press_key(Key.down)
    press_key(Key.enter)
    for _ in range(2):
        sleep(0.2)
        press_key(Key.left)
    press_key(Key.enter)
    
def open_mail():
    press_key(Key.esc)
    sleep(0.2)
    press_key(Key.down)
    sleep(0.2)
    press_key(Key.enter)
    for _ in range(3):
        sleep(0.3)
        press_key('c')
    sleep(0.5)
    press_key(Key.enter)
    sleep(0.2)