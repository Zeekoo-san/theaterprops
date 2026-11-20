# === Stage 21: Скользящее среднее ===
# Project: TheaterProps
from collections import deque


def moving_average(values, window):
    """Return a list of trailing moving averages for a numeric series.

    Each output element is the mean of at most ``window`` consecutive
    values ending at the current position.  ``window`` must be a positive
    integer and ``values`` must contain only numbers.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")
    if not values:
        return []

    window = min(window, len(values))
    result = []
    total = 0.0
    count = 0
    queue = deque(maxlen=window)

    for value in values:
        total += value
        queue.append(value)
        count += 1
        if count > window:
            total -= queue[0]
            count = window
        result.append(total / count)

    return result


def trend(direction):
    """Classify a numeric trend from a moving-average list.

    ``direction`` is a callable mapping a moving-average value to a
    comparable number (for example the current item's condition score).
    Returns one of ``"rising"``, ``"falling"`` or ``"stable"``.
    """
    if not direction:
        return "stable"

    history = direction()
    if len(history) < 2:
        return "stable"

    first, last = history[0], history[-1]
    delta = last - first
    threshold = abs(delta) * 0.05

    if delta > threshold:
        return "rising"
    if delta < -threshold:
        return "falling"
    return "stable"
