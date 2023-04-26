import sqlite3

conn = sqlite3.connect('location.db')      #opens the database
print ("Opened database successfully")

conn.execute('CREATE TABLE Position (Id FLOAT, Name VARCHAR(30), Lat FLOAT, Log FLOAT, Alt FLOAT)')  #creates the table

print ("Table created successfully")
conn.close()
