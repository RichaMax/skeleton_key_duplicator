import tkinter as tk
from tkinter import ttk
from config import load_settings
import sys
from main import launch_bot
import threading
import time


class BotGui(tk.Frame):
    def __init__(self, main_root):
        super().__init__(main_root)
        settings = load_settings()
        main_root.title('Swaggy bot')
        self.frame = ttk.Frame(main_root, padding=10)
        self.frame.grid()

        self.speed_value = tk.DoubleVar()
        self.speed_value.set(settings.multiplicator)

        self.nb_key = tk.IntVar()
        self.nb_key.set(settings.nbr_keys)

        self.set_ui()

    def set_ui(self):
        ttk.Label(self.frame, text="Speed multiplicator:").grid(column=0, row=1)
        ttk.Entry(self.frame, textvariable=self.speed_value).grid(column=1, row=1)

        ttk.Label(self.frame, text="number of keys:").grid(column=0, row=2)
        ttk.Entry(self.frame, textvariable=self.nb_key).grid(column=1, row=2)

        terminal_gui = tk.Text(self.frame, wrap="word")
        terminal_gui.grid(column=1, row=3)
        terminal_gui.tag_configure("stdout", foreground="#000000")

        # sys.stdout.write=self.decorator(sys.stdout.write, terminal_gui)
        sys.stdout = TextRedirector(terminal_gui, "stdout")
        sys.stderr = TextRedirector(terminal_gui, "stderr")

        ttk.Button(self.frame, text="Quit", command=root.destroy).grid(column=0, row=4)
        ttk.Button(self.frame, text="Launch", command=self.gui_bot_launch).grid(column=2, row=4)
        
    def decorator(self, func, textbox):
        def inner(inputStr):
            try:
                textbox.text_area.update_idletasks()
                textbox.insert(tk.INSERT, inputStr)
                return func(inputStr)
            except:
                return func(inputStr)
        return inner
    
    def gui_bot_launch(self):
        t1 = threading.Thread(target=launch_bot, args=(self.nb_key.get(),))
        t1.start()


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")


if __name__ == '__main__':
    root = tk.Tk()
    botgui = BotGui(root)
    botgui.mainloop()