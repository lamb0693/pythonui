# frame3_module.py
import tkinter as tk

class HomeFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label_title = tk.Label(self, text="Hello World", font=("Arial", 16))
        self.label_title.pack(pady=10)
        


