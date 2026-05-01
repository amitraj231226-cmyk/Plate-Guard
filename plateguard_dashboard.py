import json
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path("scan_history.json")


def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_scan(plate, status, state="Unknown", district="Unknown"):
    history = load_history()

    history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "plate": plate,
        "status": status,
        "state": state,
        "district": district
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def show_dashboard():
    history = load_history()

    if not history:
        print("\nNo scan history found.")
        return

    print("\n===== PlateGuard Scan History Dashboard =====")

    for i, scan in enumerate(history, 1):
        print(f"{i}. [{scan['timestamp']}] {scan['plate']} | {scan['status']} | {scan['district']}, {scan['state']}")

def clear_history():
    with open("scan_history.json", "w") as f:
        f.write("[]")
    print("Scan history cleared.")