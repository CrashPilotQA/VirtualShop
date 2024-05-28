import sqlite3

# Establish a connection to the SQLite database file
conn = sqlite3.connect('virtual_shop.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute the SQL command to create the items table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL,
                    stock_quantity INTEGER
                 )''')

# List of additional items and their prices
additional_items = [
    ("Apple", 0.7),
    ("Orange", 0.8),
    ("Banana", 1.1),
    ("Pear", 0.95),
    ("Kiwi", 2),
    ("Cake", 0.3),
    ("Wafer", 0.2),
    ("Bicky", 1.15),
    ("Choco", 2.2),
    ("Fudge", 0.5)
]

# Insert the additional items and their prices into the database table
cursor.executemany('''INSERT INTO items (name, price) VALUES (?, ?)''', additional_items)

# Set the stock quantity for each item to 20
cursor.execute('''UPDATE items SET stock_quantity = 20''')

# Commit the changes and close the connection
conn.commit()
conn.close()
