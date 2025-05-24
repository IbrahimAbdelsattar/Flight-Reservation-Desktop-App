# ✈️ Simple Flight Reservation Desktop App

A user-friendly desktop application built with **Python**, **Tkinter**, and **SQLite** that allows users to book, view, update, and delete flight reservations. This app demonstrates how to implement GUI-based CRUD functionality and is ideal for beginners learning desktop app development with Python.

---

## 📌 Project Features

- ✍️ **Book Flights** with passenger details
- 🗂 **View All Reservations** in a structured table
- ✏️ **Edit and Update** existing reservations
- ❌ **Delete** unwanted or outdated bookings
- 🗂️ Structured with **multi-page GUI navigation**
- 🧠 Built using **Tkinter** for GUI and **SQLite** for backend

---

## 🧩 Technologies Used

- Python 3
- Tkinter (GUI)
- SQLite (Database)
- PyInstaller (for `.exe` generation)
- Git & GitHub (Version Control)

---

## 📂 File Structure

flight_reservation_app/
├── main.py # Main application launcher
├── database.py # DB connection and table setup
├── home.py # Home UI with navigation
├── booking.py # Booking form page
├── reservations.py # List and manage reservations
├── edit_reservation.py # Edit/Delete reservations
├── flights.db # SQLite database file
├── requirements.txt # Required Python packages
├── README.md # Project documentation

## 💡 Usage Instructions

### 🏠 Home Page
- **Book Flight**: Navigate to the booking form to add a new reservation.
- **View Reservations**: Display all current bookings in a structured table.

---

### 📝 Booking a Flight
1. Click the **Book Flight** button on the home page.
2. Fill in the following fields:
   - **Name**: Passenger's full name
   - **Flight Number**: The assigned flight number
   - **Departure**: Departure city or airport
   - **Destination**: Arrival city or airport
   - **Date**: Date of the flight
   - **Seat Number**: Assigned seat
3. Click **Submit** to save the reservation.

---

### 📋 Viewing Reservations
1. Click the **View Reservations** button from the home page.
2. All reservations are displayed in a table format.
3. Each entry includes **Edit** and **Delete** buttons.

---

### ✏️ Editing a Reservation
1. In the reservations list, click **Edit** on the reservation you want to change.
2. A form pre-filled with the existing data will appear.
3. Update the desired fields and click **Update** to save changes.

---

### ❌ Deleting a Reservation
1. In the reservations list, click the **Delete** button for the reservation you want to remove.
2. Confirm the deletion if prompted.
3. The record will be permanently removed from the database.

---

🐍 Set Up Python Environment
- pip install -r requirements.txt

🚀 Run the App
- python main.py
تحرير
