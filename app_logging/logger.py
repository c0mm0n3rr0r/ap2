import json
from datetime import datetime, timezone
import os

class Logger:
    def __init__(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.file = open(path, "a", encoding="utf-8")

    def log(self, event_type, data):
        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event_type,
            "data": data,
        }
        self.file.write(json.dumps(record) + "\n")
        self.file.flush()

    def close(self):
        self.file.close()
