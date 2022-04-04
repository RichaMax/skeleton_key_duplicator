import logging
from enum import Enum
from time import sleep
from pynput import keyboard

from keys import exit_to_main_menu, continue_game, open_mail
from screen import wait_for_end_loading_screen

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