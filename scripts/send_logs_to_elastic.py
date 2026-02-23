import json
import random
import time
from datetime import datetime, timezone

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ✅ Your Elastic details
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
        "@timestamp": datetime.now(timezone.utc).isoformat(),  # ✅ fixes warning
        "event.category": "authentication",
        "event.action": "login",
        "event.outcome": outcome,
        "user.name": user,
        "source.ip": ip,
        "message": f"Login {outcome} for user {user} from {ip}",
    }

# ✅ Retry + backoff so timeouts don't kill the script
session = requests.Session()
retries = Retry(
    total=20,
    connect=20,
    read=20,
    backoff_factor=1.2,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["POST"],
)
session.mount("https://", HTTPAdapter(max_retries=retries))

while True:
    event = generate_event()
    try:
        r = session.post(
            INGEST_URL,
            auth=(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"},
            data=json.dumps(event),
            timeout=45,  # ✅ longer timeout
        )

        if 200 <= r.status_code < 300:
            print("Sent:", event["event.outcome"], event["user.name"], event["source.ip"])
        else:
            print("FAILED:", r.status_code, r.text)
            time.sleep(5)

    except requests.exceptions.RequestException as e:
        # ✅ Handles handshake timeouts + read timeouts without crashing
        print("Network hiccup (retrying):", e)
        time.sleep(5)

    time.sleep(2)
