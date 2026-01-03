import sqlite3

def second_highest_product_per_category():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Intermediate Challenge #3
    query = "SELECT " \
  " p.category, " \
  " p.name, " \
  " p.price " \
  " FROM products p " \
  " WHERE p.product_id = ( " \
  " SELECT p2.product_id " \
  " FROM products p2 " \
  " WHERE p2.category = p.category " \
  " ORDER BY p2.price DESC, p2.product_id ASC " \
  " LIMIT 1 OFFSET 1 " \
  " ) " \
  " ORDER BY p.category ASC; "

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    second_highest_product_per_category()