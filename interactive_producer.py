from kafka import KafkaProducer
import json
import random


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("=== Welcome to the Interactive Sales Entry System ===")
print("Enter order details to send them immediately to Kafka (or type 'exit' to quit)\n")

try:
    while True:
        product = input("Product name : (Laptop, Mouse, Monitor): ")
        if product.lower() == 'exit':
            break
            
        price = input("Price :  ")
        if price.lower() == 'exit':
            break
            
        quantity = input("Quantite :  ")
        if quantity.lower() == 'exit':
            break

        try:
            
            order_data = {
                "order_id": random.randint(1000, 9999),
                "product": product.strip(),
                "price": float(price),
                "Quantity": int(quantity)
            }

            
            producer.send('ecommerce-sales', value=order_data)
            producer.flush()
            print(f"The request has been sent successfully ✅ : {order_data}\n")

        except ValueError:
            print("Error: Please enter valid numbers for the price and quantity! ❌ \n")

except KeyboardInterrupt:
    pass

print("\n The input system has been closed.")
producer.close()