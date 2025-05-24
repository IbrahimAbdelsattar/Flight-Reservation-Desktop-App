import tkinter as tk
from tkinter import messagebox
import sqlite3
from home import HomePage

class BookingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        tk.Label(self, text="Book a Flight", font=("Arial", 16)).pack(pady=10)

        self.entries = {}
        for field in ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]:
            tk.Label(self, text=field).pack()
            entry = tk.Entry(self)
            entry.pack()
            self.entries[field] = entry

        tk.Button(self, text="Submit", command=self.book_flight).pack(pady=10)
        tk.Button(self, text="Back", command=self.back).pack()

    def book_flight(self):
        data = [entry.get() for entry in self.entries.values()]
        if all(data):
            conn = sqlite3.connect("flights.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                VALUES (?, ?, ?, ?, ?, ?)
            """, data)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Flight booked successfully!")
            self.back()
        else:
            messagebox.showerror("Error", "All fields are required")

    def back(self):
        self.destroy()
        HomePage(self.master)