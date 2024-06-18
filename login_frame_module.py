# frame3_module.py
import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, master, update_username, **kwargs):
        super().__init__(master, **kwargs)
        self.update_user_callback = update_username
        
        # Login form
        self.label_title = tk.Label(self, text="Login", font=("Arial", 16))
        self.label_title.pack(pady=10)
        
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(pady=5)
        
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)
        
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=5)
        
        self.entry_password = tk.Entry(self, show='*')
        self.entry_password.pack(pady=5)
        
        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.update_user_callback(username)


        


