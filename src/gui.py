import tkinter as tk
from tkinter import ttk
from config import load_settings


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

        ttk.Button(self.frame, text="Launch", command=self.print_test).grid(column=2, row=3)
        ttk.Button(self.frame, text="Quit", command=root.destroy).grid(column=0, row=3)

    def print_test(self):
        print(self.nb_key.get())



if __name__ == '__main__':
    root = tk.Tk()
    botgui = BotGui(root)
    botgui.mainloop()