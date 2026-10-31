from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'ecommerce-sales'

print("Started sending live sales data... (press Ctrl+C to stop)")
try:
    while True:
        order_data = {
            'order_id': random.randint(1000, 9999),
            'product': random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']),
            'price': random.randint(50, 1500),
            'Quantity' : random.randint(1,9)
        }
        
        producer.send(topic_name, order_data)
        
        print(f"Event sent:{order_data}")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("\nData generation has been stopped.")
finally:
    producer.close()