import sqlite3
import pandas as pd
def extract_data():
    conn = sqlite3.connect("/home/ecozero/pipeline Batch Processing/super_store.db")
    query = """
    SELECT products.product_name, products.category, order_items.quantity, order_items.price_at_purchase 
    FROM products
    INNER JOIN order_items ON order_items.product_id = products.product_id
    INNER JOIN orders ON orders.order_id = order_items.order_id

    WHERE orders.status = 'Completed'



    """
    df = pd.read_sql_query(query,conn)
    conn.close()
    return df
def transform_data(df):
    df['revenue'] =df['quantity'] * df['price_at_purchase']
    df_grouped = df.groupby(['product_name', 'category'])['revenue'].sum().reset_index()
    df_sorted = df_grouped.sort_values(by='revenue', ascending=False)
    return df_sorted
def load_data(df):
    df.to_csv("/home/ecozero/pipeline Batch Processing/Finale_data.csv", index=False)

df_raw = extract_data()
df_clean = transform_data(df_raw)
df_lead = load_data(df_clean)
#print(df_clean.head())

