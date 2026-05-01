import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi

from services.file_handler import FileHandler


class MainWindow(QMainWindow):
    """Main GUI window for attendance tracker."""

    def __init__(self) -> None:
        super().__init__()

        loadUi("gui/main_window.ui", self)

        self.presentBtn.clicked.connect(self.mark_present)
        self.absentBtn.clicked.connect(self.mark_absent)
        self.resetBtn.clicked.connect(self.reset_data)

        self.update_label()

    def get_name(self) -> str:
        """Get and validate student name."""
        name = self.nameInput.text().strip()

        if not name:
            QMessageBox.warning(self, "Input Error", "Please enter a name.")
            return ""

        return name

    def mark_present(self) -> None:
        """Mark student as present."""
        name = self.get_name()
        if not name:
            return

        try:
            FileHandler.save_entry(name, "Present")
            self.nameInput.clear()
            self.update_label()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save:\n{e}")

    def mark_absent(self) -> None:
        """Mark student as absent."""
        name = self.get_name()
        if not name:
            return

        try:
            FileHandler.save_entry(name, "Absent")
            self.nameInput.clear()
            self.update_label()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save:\n{e}")

    def reset_data(self) -> None:
        """Clear all attendance records."""
        try:
            # overwrite file with nothing
            open(FileHandler.FILE_PATH, "w").close()
            self.update_label()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Reset failed:\n{e}")

    def update_label(self) -> None:
        """Update summary label."""
        try:
            records = FileHandler.load_all()

            present = sum(1 for _, status in records if status == "Present")
            absent = sum(1 for _, status in records if status == "Absent")
            total = present + absent

            self.resultLabel.setText(
                f"Present: {present} | Absent: {absent} | Total: {total}"
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())