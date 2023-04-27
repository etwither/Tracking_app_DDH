import sqlite3
import os


def create_db():
    if not os.path.isfile('./location.db'):
        conn = sqlite3.connect('location.db')  # opens the database
        print("Opened database successfully")

        conn.execute(
            'CREATE TABLE Position (Id INTEGER PRIMARY KEY AUTOINCREMENT, UUID VARCHAR(30), Lat FLOAT, Lon FLOAT, Alt FLOAT, Time DATETIME)')  # creates the table

        print("Table created successfully")
        conn.close()
