import json
import random
import time
from datetime import datetime

import requests

# Paste your Elastic details here
ELASTICSEARCH_ENDPOINT = "https://112f8d1130324b6b905c4661cc7980bd.us-east-2.aws.elastic-cloud.com:443"
USERNAME = "elastic"
PASSWORD = "ryTafWLU234NBrx7DS4f5fMF"

INDEX_NAME = "soc-logs"
INGEST_URL = f"{ELASTICSEARCH_ENDPOINT}/{INDEX_NAME}/_doc"

users = ["admin", "j.doe", "a.smith", "m.brown"]
ips = ["203.0.113.45", "198.51.100.23", "192.0.2.10", "203.0.113.99"]

def generate_event():
    outcome = random.choice(["failed", "failed", "failed", "success"])
    user = random.choice(users)
    ip = random.choice(ips)

    return {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "event.category": "authentication",
        "event.action": "login",
        "event.outcome": outcome,
        "user.name": user,
        "source.ip": ip,
        "message": f"Login {outcome} for user {user} from {ip}",
    }

while True:
    event = generate_event()

    r = requests.post(
        INGEST_URL,
        auth=(USERNAME, PASSWORD),
        headers={"Content-Type": "application/json"},
        data=json.dumps(event),
        timeout=10,
    )

    if 200 <= r.status_code < 300:
        print("Sent:", event["event.outcome"], event["user.name"], event["source.ip"])
    else:
        print("FAILED:", r.status_code, r.text)
        break

    time.sleep(2)
