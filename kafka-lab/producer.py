from confluent_kafka import Producer

p = Producer({"bootstrap.servers": "localhost:9092"})
for i in range(10):
    p.produce("orders", key=f"user-{i % 3}", value=f"order-{i}")
remaining = p.flush()
print(f"{remaining} messages are not delivered")

