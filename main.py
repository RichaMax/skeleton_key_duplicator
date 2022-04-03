from keys import exit_to_main_menu, continue_game, open_mail
from screen import wait_for_end_loading_screen
from time import sleep
from pynput import keyboard

from utils import ticker

ACTIVE = False
        
def on_release(key: keyboard.Key):
    global ACTIVE
    if isinstance(key, keyboard._win32.KeyCode):
        if key.char.lower() == 'm':
            ACTIVE = not ACTIVE

if __name__ == '__main__':
    listener = keyboard.Listener(
        on_release=on_release,
    )
    
    listener.start()
    
    for _ in ticker(0.1):
        if not ACTIVE:
            continue
            
        continue_game()
        
        wait_for_end_loading_screen()

        # open_mail()
        
        sleep(0.2)
        
        exit_to_main_menu()
        
        wait_for_end_loading_screen()