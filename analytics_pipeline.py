import pandas as pd
import time
import os

input_file = "live_sales.csv"
output_file = "analytic_summary.csv"

print("Ctrl + C : for stopping!!!!")

try:
    while True:
        if os.path.exists(input_file):
            df = pd.read_csv(input_file)
            
            if 'price' in df.columns and 'Quantity' in df.columns:
                df["total_price"] = df["price"] * df["Quantity"]
                
                df.to_csv(output_file, index=False)
                print(f" Donne Save to :  {os.path.abspath(output_file)}")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("\nAnalytics account stopped.")
   