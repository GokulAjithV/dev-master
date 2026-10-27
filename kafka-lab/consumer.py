from confluent_kafka import Consumer

c = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "py",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False
})
c.subscribe(["orders"])
while True:
    m = c.poll(1.0)
    if m is None:
        continue
    if m.error():
        print(m.error())
        continue
    print(m.partition(), m.offset(), m.key().decode(), m.value().decode())
    c.commit(m)
