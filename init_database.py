import sqlite3
conn = sqlite3.connect('sensor_data.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE temperature
             (date real, temperature real)''')

c.execute('''CREATE TABLE pressure
             (date real, pressure real)''')

conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()