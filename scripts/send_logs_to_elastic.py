import json
import random
import time
from datetime import datetime, timezone

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ================================
# Elastic Cloud Connection
# ================================

ELASTICSEARCH_ENDPOINT = "https://my-security-project-a582d4.es.us-east-2.aws.elastic.cloud"
API_KEY = "N1UxQmk1d0JEMndUMzJkQ24tZ3A6dDVMbWRWSzdnTDFFY0NmRmF0VG5NZw=="

INDEX_NAME = "soc-logs"
INGEST_URL = f"{ELASTICSEARCH_ENDPOINT}/{INDEX_NAME}/_doc"

# ================================
# Sample Data
# ================================

users = ["admin", "j.doe", "a.smith", "m.brown"]
ips = ["203.0.113.45", "198.51.100.23", "192.0.2.10", "203.0.113.99"]

# ================================
# Generate Log Event
# ================================

def generate_event():
    outcome = random.choice(["failed", "failed", "failed", "success"])
    user = random.choice(users)
    ip = random.choice(ips)

    return {
        "@timestamp": datetime.now(timezone.utc).isoformat(),
        "event.category": "authentication",
        "event.action": "login",
        "event.outcome": outcome,
        "user.name": user,
        "source.ip": ip,
        "message": f"Login {outcome} for user {user} from {ip}",
    }

# ================================
# HTTP Session With Retries
# ================================

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

# ================================
# Send Logs Forever
# ================================

while True:
    event = generate_event()

    try:
        r = session.post(
            INGEST_URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"ApiKey {API_KEY}",
            },
            data=json.dumps(event),
            timeout=45,
        )

        if 200 <= r.status_code < 300:
            print(
                "Sent:",
                event["event.outcome"],
                event["user.name"],
                event["source.ip"],
            )
        else:
            print("FAILED:", r.status_code, r.text)
            time.sleep(5)

    except requests.exceptions.RequestException as e:
        print("Network hiccup (retrying):", e)
        time.sleep(5)

    time.sleep(2)

  
