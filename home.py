import tkinter as tk
from booking import BookingPage
from reservations import ReservationListPage

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        tk.Label(self, text="Flight Reservation System", font=("Arial", 20)).pack(pady=20)
        
        tk.Button(self, text="Book Flight", width=20, command=self.go_to_booking).pack(pady=10)
        tk.Button(self, text="View Reservations", width=20, command=self.go_to_reservations).pack(pady=10)

    def go_to_booking(self):
        self.destroy()
        BookingPage(self.master)

    def go_to_reservations(self):
        self.destroy()
        ReservationListPage(self.master)
