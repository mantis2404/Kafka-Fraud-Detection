from kafka import KafkaProducer
import os
import json
import time
import random
from faker import Faker

fake = Faker()

KAFKA_SERVER = "localhost:9092"
TRANSACTIONS_TOPIC = "TRANSACTIONS_TOPIC"

def generate_transaction():
    transaction_types = ["deposit", "withdrawal", "transfer", "payment"]
    transaction_type = random.choice(transaction_types)
    amount = round(random.uniform(10, 5000), 2)
    date = fake.date_time_between(start_date="-1y", end_date="now")
    return {
        "transaction_id": fake.uuid4(),
        "date": date.isoformat(),
        "type": transaction_type,
        "amount": amount,
        "currency": fake.currency_code(),
        "description": fake.bs(),
        "account_number": fake.bban(),
        "merchant": fake.company() if transaction_type in ["payment", "withdrawal"] else None,
        "category": fake.word(ext_word_list=["food", "transport", "entertainment", "utilities", "shopping"]) if transaction_type != "transfer" else None,
        "balance_after": round(random.uniform(100, 10000), 2)
    }

if __name__=="__main__":
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    while True:
        transaction = generate_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        time.sleep(1)

