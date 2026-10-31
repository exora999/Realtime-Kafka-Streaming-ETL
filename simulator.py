import sqlite3
import time
import random
from datetime import datetime

print("Sales simulator started... (press Ctrl+C to stop)")
while True:
    conn = sqlite3.connect("super_store.db")
    cursor = conn.cursor()

    customer_id = random.randint(1, 1000)
    product_id = random.randint(1, 100)
    quantity = random.randint(1, 5)
    order_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("SELECT price FROM products WHERE product_id = ?", (product_id,))
    price_at_purchase = cursor.fetchone()[0]

    cursor.execute("INSERT INTO orders (customer_id, order_date, status) VALUES (?, ?, 'Completed')", 
                   (customer_id, order_date))
    order_id = cursor.lastrowid

    cursor.execute("INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase) VALUES (?, ?, ?, ?)",
                   (order_id, product_id, quantity, price_at_purchase))

    conn.commit()
    conn.close()

    print(f"🛒 New customer! {quantity} units of product {product_id} sold.")
    time.sleep(3) 