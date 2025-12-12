"""
Day 02 — Version Control & Project Structure
--------------------------------------------
This file demonstrates:
- Basic Git workflow (tracking changes, staging, committing)

"""

import datetime
import sys

# ensure utf-8 stdout where possible (safe)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def show_project_info():
    """Return a short message showing that version control is working."""
    return {
        "message": "Day 2 — Version Control working successfully!",
        "timestamp": str(datetime.datetime.now()),
        "status": "tracked by Git"
    }

if __name__ == "__main__":
    info = show_project_info()
    # use plain ASCII prefix to avoid encoding issues on Windows terminals
    print("START:", info["message"])
    print("Timestamp:", info["timestamp"])
    print("Status:", info["status"])
