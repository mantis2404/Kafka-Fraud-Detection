from kafka import KafkaConsumer, KafkaProducer
import os
import json

KAFKA_SERVER = "localhost:9092" 
TRANSACTIONS_TOPIC = "TRANSACTIONS_TOPIC"

LEGIT_TOPIC = "LEGIT-TOPIC"
FRAUD_TOPIC = "FRAUD-TOPIC"

def is_fraudulent(transaction):
    """Simple fraud detection logic based on transaction amount."""
    return transaction['amount'] >= 1000

if __name__ == "__main__":
    consumer = KafkaConsumer(TRANSACTIONS_TOPIC, bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    for message in consumer:
        transaction = message.value
        if is_fraudulent(transaction):
            producer.send(FRAUD_TOPIC, value=transaction)
        else:
            producer.send(LEGIT_TOPIC, value=transaction)

    consumer.flush()
    consumer.close()
    producer.flush()
    producer.close()

