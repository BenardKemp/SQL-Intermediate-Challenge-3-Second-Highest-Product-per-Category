import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, " \
"name TEXT, " \
"Category TEXT, " \
"price DECIMAL )")

cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (201, 'Wireless Mouse', 'Accessories', 24.99)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (202, 'Mechanical Keyboard', 'Accessories', 89.00)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (203, 'Pro Keyboard', 'Accessories', 89.00)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (204, 'USB-C Hub', 'Accessories', 34.50)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (205, 'Monitor', 'Displays', 299.00)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (106, '34-inch Monitor', 'Displays', 399.00)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (207, 'Desk Lamp', 'Workspace', 49.99)")
cursor.execute("INSERT INTO products (product_id, name, category, price) " \
" VALUES (208, 'Chairmat', 'Workspace', 79.99)")

conn.commit()
conn.close()