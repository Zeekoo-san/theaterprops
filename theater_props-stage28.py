# === Stage 28: Сравнение периодов ===
# Project: TheaterProps
from datetime import date
from typing import Optional


class Period:
    def __init__(self, start: date, end: date, metric: float):
        self.start = start
        self.end = end
        self.metric = metric

    def length(self) -> int:
        return (self.end - self.start).days

    def __repr__(self) -> str:
        return f"Period({self.start}, {self.end}, {self.metric})"


def compare_periods(periods: list, metric: str = "metric") -> dict:
    if not periods:
        return {
            "best": None,
            "worst": None,
            "average": None,
            "total_length": 0,
            "average_metric": None,
        }

    best = max(periods, key=lambda p: getattr(p, metric))
    worst = min(periods, key=lambda p: getattr(p, metric))
    total_length = sum(p.length() for p in periods)
    average_metric = sum(p.metric for p in periods) / len(periods)

    return {
        "best": best,
        "worst": worst,
        "average": sum(p.metric for p in periods) / len(periods),
        "total_length": total_length,
        "average_metric": average_metric,
    }


def compare_periods_by_length(periods: list) -> list:
    return sorted(periods, key=lambda p: p.length(), reverse=True)


def compare_periods_by_metric(periods: list) -> list:
    return sorted(periods, key=lambda p: p.metric, reverse=True)


def find_peak_period(periods: list, threshold: float) -> Optional[Period]:
    for period in periods:
        if period.metric >= threshold:
            return period
    return None


def compare_two_periods(period_a: Period, period_b: Period) -> dict:
    length_diff = period_a.length() - period_b.length()
    metric_diff = period_a.metric - period_b.metric

    if period_a.metric > period_b.metric:
        winner = "period_a"
    elif period_b.metric > period_a.metric:
        winner = "period_b"
    else:
        winner = "tie"

    return {
        "a": period_a,
        "b": period_b,
        "length_difference": length_diff,
        "metric_difference": metric_diff,
        "winner": winner,
    }


def summarize_periods(periods: list) -> str:
    result = compare_periods(periods)
    best = result["best"]
    worst = result["worst"]

    if best is None:
        return "No periods to summarize."

    return (
        f"Total length: {result['total_length']} days. "
        f"Best: {best}. Worst: {worst}. "
        f"Average metric: {result['average_metric']:.2f}."
    )
