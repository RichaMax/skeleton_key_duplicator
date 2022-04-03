from keys import *
from screen import *
from time import sleep
from pynput import keyboard

ACTIVE = False

def on_press(key: Key):
    if isinstance(key, keyboard._win32.KeyCode):
        if key.char == 'm':
            print('boooop')
        
def on_release(key: Key):
    global ACTIVE
    if isinstance(key, keyboard._win32.KeyCode):
        if key.char == 'm':
            print('beeeep')
            ACTIVE = not ACTIVE

if __name__ == '__main__':
    listener = keyboard.Listener(
        on_press=on_press,
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