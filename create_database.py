import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('inventory.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the products table
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (product_id INTEGER PRIMARY KEY,
                   product_name TEXT NOT NULL,
                   product_price REAL NOT NULL,
                   product_quantity INTEGER NOT NULL)''')

# Commit the changes and close the connection
conn.commit()
conn.close()
