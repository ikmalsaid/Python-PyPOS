import sqlite3

def add_product(product_name, product_price, product_quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO products (product_name, product_price, product_quantity)
                      VALUES (?, ?, ?)''', (product_name, product_price, product_quantity))
    conn.commit()
    conn.close()

def batch_add_products(products_data):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO products (product_name, product_price, product_quantity)
                           VALUES (?, ?, ?)''', products_data)
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM products''')
    rows = cursor.fetchall()
    conn.close()
    return rows

def edit_product(product_id, product_name, product_price, product_quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE products SET product_name = ?, product_price = ?, product_quantity = ?
                      WHERE product_id = ?''', (product_name, product_price, product_quantity, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM products WHERE product_id = ?''', (product_id,))
    conn.commit()
    conn.close()
