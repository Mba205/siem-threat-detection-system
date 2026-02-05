import json
import random
from datetime import datetime, timedelta

users = ["j.doe", "a.smith", "m.brown"]
ips = ["203.0.113.45", "198.51.100.23", "192.0.2.10"]

logs = []
start_time = datetime.utcnow()

for i in range(15):
    log = {
        "timestamp": (start_time + timedelta(seconds=i * 30)).isoformat() + "Z",
        "user": random.choice(users),
        "src_ip": random.choice(ips),
        "action": random.choice(["failure", "failure", "failure", "success"])
    }
    logs.append(log)

with open("authentication_logs_generated.json", "w") as f:
    json.dump(logs, f, indent=2)

print("Authentication logs generated successfully.")
