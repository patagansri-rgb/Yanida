import json
import os

FILENAME = "study_records.json"

def save_record(subject, duration, category):
    records = load_records()
    new_record = {
        "subject": subject,
        "duration": duration,
        "category": category
    }
    records.append(new_record)
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)

def load_records():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    