# Attendance tracker for students
import json
import os
from datetime import datetime

DATA_FILE = "attendance_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_student(data, name):
    name = name.strip()
    if not name:
        raise ValueError("Student name cannot be empty")
    if name in data:
        raise ValueError(f"Student '{name}' already exists")
    data[name] = {}


def mark_attendance(data, name, date_str=None, status="present"):
    if name not in data:
        raise ValueError(f"Student '{name}' not found")
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    if status not in ["present", "absent", "late"]:
        raise ValueError("Status must be 'present', 'absent', or 'late'")
    data[name][date_str] = status


def print_report(data):
    if not data:
        print("No attendance data yet.")
        return
    for name, records in sorted(data.items()):
        print(f"\n{name}")
        if not records:
            print("  [No records]")
        else:
            for date in sorted(records):
                print(f"  {date}: {records[date]}")


def main():
    data = load_data()
    while True:
        print("\n--- Student Attendance Tracker ---")
        print("1. Add student")
        print("2. Mark attendance")
        print("3. Show report")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                name = input("Student name: ").strip()
                add_student(data, name)
                save_data(data)
                print(f"Added student: {name}")

            elif choice == "2":
                name = input("Student name: ").strip()
                date_str = input("Date (YYYY-MM-DD) [enter for today]: ").strip() or None
                status = input("Status (present/absent/late): ").strip().lower() or "present"
                mark_attendance(data, name, date_str, status)
                save_data(data)
                print(f"Marked {name} as {status} on {date_str or datetime.now().strftime('%Y-%m-%d')}")

            elif choice == "3":
                print_report(data)

            elif choice == "4":
                print("Goodbye")
                break

            else:
                print("Invalid choice, please try again")

        except ValueError as ve:
            print("Error:", ve)


if __name__ == "__main__":
    main()