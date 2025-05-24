import tkinter as tk
from home import HomePage
from database import connect_db

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("500x500")
        connect_db()
        self.show_home()

    def show_home(self):
        for widget in self.winfo_children():
            widget.destroy()
        HomePage(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
