import logging
from enum import Enum
from time import sleep, time
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
    
    number_of_keys = 30

    duplications = 0

    while not ACTIVE:
        sleep(0.1)

    print('Bot started')
    start_time = time()

    while ACTIVE and duplications < number_of_keys:
            
        continue_game()
        
        wait_for_end_loading_screen()

        open_mail()
        
        exit_to_main_menu()
        
        wait_for_end_loading_screen()

        duplications += 1

    print('Bot finished')
    end_time = time()

    print(f'{duplications} duplications')
    print(f'Total time: {(end_time - start_time):.2f}s - mean: {((end_time - start_time)/duplications):.2f}s')
