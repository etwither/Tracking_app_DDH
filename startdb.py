import sqlite3

conn = sqlite3.connect('location.db')      #opens the database
print ("Opened database successfully")

conn.execute('CREATE TABLE Position (Id INT, Lat FLOAT, Log FLOAT)')  #creates the table

print ("Table created successfully")
conn.close()
