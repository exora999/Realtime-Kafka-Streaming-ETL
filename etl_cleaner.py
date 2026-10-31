import pandas as pd
import time
import os

input_file = "live_sales.csv"
output_parquet = "clean_sales.parquet"

valid_products = ["laptop", "mouse", "monitor", "headphones", "keyboard"]

try:
    while True:
        if os.path.exists(input_file):
            df = pd.read_csv(input_file)
            
            if not df.empty and all(col in df.columns for col in ['product', 'price', 'Quantity']):
                
                df['product'] = df['product'].astype(str).str.strip().str.lower()
                
                condition = (
                    df['product'].isin(valid_products) & 
                    (df['Quantity'] > 0) & 
                    (df['price'] > 0)
                )
                
                clean_df = df[condition].copy()
                clean_df["total_price"] = clean_df["price"] * clean_df["Quantity"]
                
                clean_df.to_parquet(output_parquet, index=False)
                
                print(f"Data cleaned successfully | Original: {len(df)} | Filtered: {len(clean_df)}")
        
        time.sleep(3)

except KeyboardInterrupt:
    print("\nPipeline stopped.")