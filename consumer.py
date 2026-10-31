from kafka import KafkaConsumer
import json
import pandas as pd
import os

consumer = KafkaConsumer(
    'ecommerce-sales',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest', 
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

csv_file = 'live_sales.csv'
print("Listening to live data and saving it to a CSV file... (Press Ctrl+C to stop)")
try:
    for message in consumer:
        data = message.value 
        
        df = pd.DataFrame([data])
        
        df.to_csv(csv_file, mode='a', index=False, header=not os.path.exists(csv_file))
        
        print(f"Received and saved: {data}")

except KeyboardInterrupt:
    print("\nThe receiver has been stopped.")
finally:
    consumer.close()