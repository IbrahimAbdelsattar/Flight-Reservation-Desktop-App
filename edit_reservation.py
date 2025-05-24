import tkinter as tk
from tkinter import messagebox
import sqlite3
from reservations import ReservationListPage

class EditReservationPage(tk.Frame):
    def __init__(self, master, reservation):
        super().__init__(master)
        self.master = master
        self.reservation = reservation
        self.pack()

        tk.Label(self, text="Edit Reservation", font=("Arial", 16)).pack(pady=10)

        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        for i, field in enumerate(fields):
            tk.Label(self, text=field).pack()
            entry = tk.Entry(self)
            entry.insert(0, reservation[i+1])
            entry.pack()
            self.entries[field] = entry

        tk.Button(self, text="Update", command=self.update).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete).pack(pady=5)
        tk.Button(self, text="Back", command=self.back).pack(pady=5)

    def update(self):
        data = [entry.get() for entry in self.entries.values()] + [self.reservation[0]]
        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?
        """, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation updated successfully")
        self.back()

    def delete(self):
        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reservations WHERE id=?", (self.reservation[0],))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Reservation deleted")
        self.back()

    def back(self):
        self.destroy()
        ReservationListPage(self.master)