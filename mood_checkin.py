"""Ask how you're doing every 60 seconds and log your answers.

Run:  python mood_checkin.py
Stop: Ctrl+C (or type "stop")
"""

import random
import time
from datetime import datetime

INTERVAL_SECONDS = 60
LOG_FILE = "mood_log.txt"

QUESTIONS = [
    "Hey, how are you doing today?",
    "Checking in: how are you feeling right now?",
    "How's your day going?",
    "Quick check: how are things?",
]


def main():
    print(f"Mood check-in started. Asking every {INTERVAL_SECONDS} seconds.")
    print('Type "stop" or press Ctrl+C to quit.\n')
    try:
        while True:
            answer = input(random.choice(QUESTIONS) + " ").strip()
            if answer.lower() == "stop":
                break
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(f"{timestamp}  {answer}\n")
            print(f"Thanks! See you in {INTERVAL_SECONDS} seconds.\n")
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        pass
    print(f"\nBye! Your answers are saved in {LOG_FILE}.")


if __name__ == "__main__":
    main()
