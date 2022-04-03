import logging
from enum import Enum
from time import sleep
from pynput import keyboard

from keys import exit_to_main_menu, continue_game, open_mail
from screen import wait_for_end_loading_screen
from utils import ticker

ACTIVE = False

class BotStoppedError(Exception):
    pass
        
def switch_active(key: keyboard.Key):
    global ACTIVE
    if isinstance(key, keyboard._win32.KeyCode):
        if key.char.lower() == 'm':
            if not ACTIVE:
                ACTIVE = True
                print('Bot started')
            else:
                print('Bot stopped')
                raise BotStoppedError

if __name__ == '__main__':
    listener = keyboard.Listener(
        on_release=switch_active,
    )
    
    listener.start()

    print('Bot ready. Press M to activate/deactivate')
    
    duplications = 0

    try:
        for _ in ticker(0.1):
            if not ACTIVE:
                continue
                
            continue_game()
            
            wait_for_end_loading_screen()

            open_mail()
            
            exit_to_main_menu()
            
            wait_for_end_loading_screen()

            duplications += 1
    except KeyboardInterrupt:
        print(f'{duplications} duplications')