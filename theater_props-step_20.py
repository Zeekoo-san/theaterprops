# === Stage 20: Месячный отчёт ===
# Project: TheaterProps
from datetime import datetime

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


class MonthlyReport:
    def __init__(self, year, month, issued, returned):
        self.year = year
        self.month = month
        self.issued = issued
        self.returned = returned

    @property
    def month_name(self):
        return MONTHS[self.month - 1]

    @property
    def total_movements(self):
        return self.issued + self.returned

    def previous_month(self):
        if self.month == 1:
            return MonthlyReport(self.year - 1, 12, 0, 0)
        return MonthlyReport(self.year, self.month - 1, 0, 0)

    @property
    def issued_delta(self):
        return self.issued - self.previous_month().issued

    @property
    def returned_delta(self):
        return self.returned - self.previous_month().returned

    @property
    def movements_delta(self):
        return self.total_movements - self.previous_month().total_movements

    def growth_rate(self, current, previous):
        if previous == 0:
            return None
        return (current - previous) / previous * 100

    def as_dict(self):
        return {
            "month": self.month_name,
            "year": self.year,
            "issued": self.issued,
            "returned": self.returned,
            "total": self.total_movements,
            "issued_delta": self.issued_delta,
            "returned_delta": self.returned_delta,
            "movements_delta": self.movements_delta,
            "issued_growth": self.growth_rate(self.issued, self.previous_month().issued),
            "returned_growth": self.growth_rate(self.returned, self.previous_month().returned),
        }

    def summary_line(self):
        return (f"{self.month_name} {self.year}: issued={self.issued}, "
                f"returned={self.returned}, total={self.total_movements}, "
                f"vs prev total_delta={self.movements_delta}")
