class AttendanceModel:
    """Handles attendance logic."""

    def __init__(self) -> None:
        self._present: int = 0
        self._absent: int = 0

    def mark_present(self) -> None:
        """Increment present count."""
        self._present += 1

    def mark_absent(self) -> None:
        """Increment absent count."""
        self._absent += 1

    def reset(self) -> None:
        """Reset all counts."""
        self._present = 0
        self._absent = 0

    def get_totals(self) -> tuple[int, int, int]:
        """Return present, absent, total."""
        total = self._present + self._absent
        return self._present, self._absent, total

    def set_data(self, present: int, absent: int) -> None:
        """Set data from file."""
        if present < 0 or absent < 0:
            raise ValueError("Invalid data")
        self._present = present
        self._absent = absent