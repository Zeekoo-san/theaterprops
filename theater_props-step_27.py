# === Stage 27: Прогноз сроков ===
# Project: TheaterProps
"""theater_props_forecast: predict next-use intervals for props from history."""

from collections import defaultdict
from statistics import median


class IntervalHistory:
    """Stores observed intervals between consecutive checkouts of a prop.

    Each call appends an interval measured in days.  The history can then
    be queried to estimate how often the prop is handed out again.
    """

    def __init__(self):
        self._intervals = []

    def add(self, days):
        if days < 0:
            raise ValueError("interval days must not be negative")
        self._intervals.append(days)

    def count(self):
        return len(self._intervals)

    def mean(self):
        if not self._intervals:
            return 0.0
        return sum(self._intervals) / len(self._intervals)

    def median(self):
        if not self._intervals:
            return 0.0
        return median(self._intervals)

    def minimum(self):
        if not self._intervals:
            return 0.0
        return min(self._intervals)


def predict_next_interval(history):
    """Return the most representative forecast for the next checkout interval.

    The forecast prefers the median because interval data is skewed by long
    gaps between uses; it falls back to the mean when only a single sample is
    available and to a conservative one-day estimate when nothing is known.
    """
    if history.count() == 0:
        return 1
    if history.count() == 1:
        return history.mean()
    return history.median()


def forecast_window(history, days=14):
    """Produce a simple forecast window: the next interval plus its range.

    The range is built from the historical minimum and mean so that the
    returned window expresses the earliest and latest plausible next use.
    """
    if history.count() == 0:
        return {
            "next_interval": 1,
            "earliest": 1,
            "latest": days,
        }
    median_days = predict_next_interval(history)
    minimum_days = history.minimum()
    mean_days = history.mean()

    if history.count() == 1:
        earliest = min(median_days, mean_days)
        latest = max(median_days, mean_days)
    else:
        earliest = max(1, median_days - int(mean_days))
        latest = max(median_days, int(mean_days) + int(median_days))

    return {
        "next_interval": median_days,
        "earliest": earliest,
        "latest": min(latest, days),
    }


SAMPLE = IntervalHistory()
SAMPLE.add(3)
SAMPLE.add(7)
SAMPLE.add(10)
SAMPLE.add(5)

print("history count:", SAMPLE.count())
print("mean:", round(SAMPLE.mean(), 2))
print("median:", round(SAMPLE.median(), 2))
print("predict_next_interval:", predict_next_interval(SAMPLE))
print("forecast_window:", forecast_window(SAMPLE, days=14))
