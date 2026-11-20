# === Stage 22: Аномальные значения ===
# Project: TheaterProps
"""
Anomaly detection for a single numeric property of a theater prop.

Simple statistical outlier detection using the 1.5 * IQR rule.
Standard library only, no dependencies on other project modules.
"""

import statistics


def find_anomalies(values, k=1.5):
    """Return the list of anomaly values in *values*.

    Uses the inter-quartile-range (IQR) method: a value is considered
    anomalous when it lies below Q1 - k*IQR or above Q3 + k*IQR.

    Args:
        values: an iterable of numbers.
        k: the multiplier of the IQR (default 1.5, the common Tukey value).

    Returns:
        A list of numbers that fall outside the acceptable range.

    Raises:
        TypeError: if *values* is empty or contains non-numeric items.
        ValueError: if *values* has fewer than four elements (Q1/Q3 need
                     a sufficiently large sample to be meaningful).
    """
    if not values:
        raise TypeError("values must contain at least one number")
    for item in values:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError("all values must be numbers")
    if len(values) < 4:
        raise ValueError("need at least 4 values to compute IQR anomalies")

    ordered = sorted(values)
    q1 = statistics.quantiles(ordered, n=4)[0]
    q3 = statistics.quantiles(ordered, n=4)[2]
    iqr = q3 - q1

    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr

    return [v for v in values if v < lower_bound or v > upper_bound]


def detect_anomalies_by_key(records, key):
    """Extract the numeric field *key* from *records* and find anomalies.

    Args:
        records: an iterable of mappings (e.g. dicts) that expose *key*.
        key: the name of the numeric field to inspect.

    Returns:
        A list of anomaly values found in the *key* field.
    """
    return find_anomalies([record[key] for record in records])


if __name__ == "__main__":
    sample = [10, 12, 11, 13, 10, 12, 14, 11, 100, 9]
    print("Anomalies:", find_anomalies(sample))
