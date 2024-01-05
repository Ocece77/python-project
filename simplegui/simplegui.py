import tkinter as tk

class LoginGUI:
    
    def __init__(self) :
        
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Login GUI")
        self.root.geometry("500x350")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=12)

        self.label = tk.Label(self.frame, font=("Arial", 30), text="Login")
        self.label.pack(padx=10, pady=12)

        self.username = tk.Entry(self.frame)
        self.username.pack(padx=10, pady=12)

        self.password = tk.Entry(self.frame, show="*")
        self.password.pack(padx=10, pady=12)

        self.btn_in = tk.Button(self.frame, text="Login in" ,command=self.show)
        self.btn_in.pack(padx=10, pady=12)

        self.btn_inscription = tk.Button(self.frame, text="Create an account")
        self.btn_inscription.pack(padx=10, pady=12)

        self.root.mainloop()

    def show(self):
        print(f"The username is {self.username.get()}/nThe account password is {self.password.get()}" )

 

LoginGUI()