import csv
from typing import List, Tuple


class FileHandler:
    FILE_PATH = "data/attendance.csv"

    @staticmethod
    def save_entry(name: str, status: str) -> None:
        """Append a student record."""
        try:
            with open(FileHandler.FILE_PATH, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, status])
        except Exception as e:
            print("Error saving:", e)

    @staticmethod
    def load_all() -> List[Tuple[str, str]]:
        """Load all attendance records."""
        try:
            with open(FileHandler.FILE_PATH, "r") as file:
                reader = csv.reader(file)
                return [(row[0], row[1]) for row in reader]
        except:
            return []