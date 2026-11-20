# === Stage 23: Серии по дням ===
# Project: TheaterProps
"""Stage23: calculate runs of consecutive days with props activity.

A self-contained module. It only depends on the standard library and
does not import anything from the TheaterProps codebase.
"""

from collections import defaultdict


def _day_of_event(event):
    """Return the ISO day (YYYY-MM-DD) of a prop-handling event.

    The event is expected to carry a ``date`` attribute in ISO format.
    Anything without a date is treated as day zero.
    """

    date = getattr(event, "date", None)
    if date is None:
        return 0
    return date[:10]


def consecutive_days(events):
    """Group prop events by the day they happened and order the days.

    Parameters
    ----------
    events : sequence of event-like objects

        Each event should expose a ``date`` string (``YYYY-MM-DD``).

    Returns
    -------
    list of int

        The distinct event days sorted chronologically.
    """

    days = defaultdict(int)
    for event in events:
        days[_day_of_event(event)] += 1
    return sorted(days)


def run_lengths(days):
    """Compute the lengths of consecutive-day runs.

    Parameters
    ----------
    days : sequence of int

        Days (already sorted) on which prop activity occurred.

    Returns
    -------
    list of tuple

        Each tuple is ``(start_day, end_day, length)`` describing one
        uninterrupted run of consecutive days.
    """

    if not days:
        return []

    runs = []
    start = days[0]
    prev = days[0]

    for day in days[1:]:
        if day == prev + 1:
            prev = day
        else:
            runs.append((start, prev, prev - start + 1))
            start = day
            prev = day

    runs.append((start, prev, prev - start + 1))
    return runs


def longest_run(events):
    """Return the longest consecutive-day run for a set of events.

    The function delegates to :func:`consecutive_days` and
    :func:`run_lengths` and returns the run with the greatest length.
    """

    days = consecutive_days(events)
    runs = run_lengths(days)
    return max(runs, key=lambda run: run[2]) if runs else None
