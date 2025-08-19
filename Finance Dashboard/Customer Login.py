#Customer Login Title

from tkinter import *

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Login")
        self.root.geometry("300x200")
        self.root.configure(bg="lightblue")

        #Logo Frame
        self.logo_frame = Frame(self.root, bg="lightblue")
        self.logo_frame.pack(pady=10)
        self.logo_label = Label(self.logo_frame, text="Finance Dashboard", font=("Arial", 16), bg="lightblue")
        self.logo_label.pack()

        #Logo Image
        #Put chosen image path here
        # self.logo_image = PhotoImage(file="path_to_logo.png")
        # self.logo_label.config(image=self.logo_image) 

        #Email Entry
        self.entry_frame = Frame(self.root, bg="lightblue")
        self.entry_frame.pack(pady=20)

        self.email_label = Label(self.entry_frame, text="Email:", bg="lightblue") 
        self.email_label.grid(row=1, column=0, sticky=W, padx=10, pady=2)
        self.email_entry = Entry(self.entry_frame, font=("Arial", 11), width=20, relief=FLAT)
        self.email_entry.grid(row=1, column=1, pady=2)

        #Password Entry
        self.password_frame = Frame(self.root, bg="lightblue")
        self.password_frame.pack(pady=10)

        self.password_label = Label(self.password_frame, text="Password:", bg="lightblue")
        self.password_label.grid(row=2, column=0, sticky=W, padx=10, pady=2)
        self.password_entry = Entry(self.password_frame, font=("Arial", 11), show='*', width=20, relief=FLAT)
        self.password_entry.grid(row=2, column=1, pady=2)

        #Login Button
        self.login_button = Button(self.root, text="Login", command=self.login, bg="blue", fg="white", font=("Arial", 12))
        self.login_button.pack(pady=20)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Here you would typically validate the email and password
        print(f"Email: {email}, Password: {password}")

if __name__ == "__main__":
    root = Tk()
    login_view = LoginView(root)
    root.mainloop()

