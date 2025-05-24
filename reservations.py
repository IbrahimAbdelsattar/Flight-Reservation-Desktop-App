import tkinter as tk
import sqlite3
from edit_reservation import EditReservationPage
from home import HomePage

class ReservationListPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        tk.Label(self, text="All Reservations", font=("Arial", 16)).pack(pady=10)

        self.load_data()
        tk.Button(self, text="Back", command=self.back).pack(pady=10)

    def load_data(self):
        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            tk.Label(self, text=str(row)).pack()
            tk.Button(self, text="Edit", command=lambda r=row: self.edit(r)).pack()

    def edit(self, reservation):
        self.destroy()
        EditReservationPage(self.master, reservation)

    def back(self):
        self.destroy()
        HomePage(self.master)