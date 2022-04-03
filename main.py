import logging
from time import sleep
from pynput import keyboard

from keys import exit_to_main_menu, continue_game, open_mail
from screen import wait_for_end_loading_screen
from utils import ticker

ACTIVE = False
        
def switch_active(key: keyboard.Key):
    global ACTIVE
    if isinstance(key, keyboard._win32.KeyCode):
        if key.char.lower() == 'm':
            ACTIVE = not ACTIVE
            print('Bot ' + ('de' if  not ACTIVE else '') + 'activated')

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