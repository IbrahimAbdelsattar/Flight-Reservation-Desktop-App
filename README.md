# Flight Reservation Desktop App

A small Tkinter desktop project for creating, viewing, editing, and deleting local flight reservation records.

**Technology:** Python · Tkinter · SQLite

## Features

- Create reservations with passenger name, flight number, route, date, and seat.
- List stored reservations and open individual records for editing or deletion.
- Persist records in a local `flights.db` SQLite database initialized by `database.py`.

## Repository guide

| Path | Purpose |
|---|---|
| [main.py](main.py) | Application entry point and main window. |
| [home.py](home.py) | Navigation between booking and reservation pages. |
| [booking.py](booking.py) | Reservation creation form. |
| [reservations.py](reservations.py) | Reservation list. |
| [edit_reservation.py](edit_reservation.py) | Update and delete actions. |
| [database.py](database.py) | Database initialization. |

## Requirements and current limitations

**Current source limitation:** `home.py`, `booking.py`, `reservations.py`, and `edit_reservation.py` import each other at module scope. This circular import can prevent `python main.py` from starting. The command is the intended entry point; resolve the import cycle before expecting a successful source run.

`sqlite3` ships with Python, and Tkinter is provided by the Python/Tk installation. The existing `requirements.txt` lists these standard-library modules; do not install it with pip. On systems without Tk support, install the platform's Python Tk package. A Windows executable is also included, but its runtime behavior has not been validated here.

## Getting started

```bash
git clone https://github.com/IbrahimAbdelsattar/Flight-Reservation-Desktop-App.git
cd Flight-Reservation-Desktop-App
```

Use a Python virtual environment:

```bash
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` in PowerShell.

```bash
python main.py
```
