#Customer Login Title

from tkinter import *

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Login")
        self.root.geometry("300x200")
        self.root.configure(bg="lightblue")

        self.email_label = Label(self.entry_frame, "Email:") 
        self.email_label.grid(row=1, column=0, sticky=W, padx=10, pady=2)
        self.email_entry = Entry(self.entry_frame, font=("Arial", 11), width=30, relief=FLAT)
        self.email_entry.grid(row=1, column=1, pady=2)