# === Stage 18: Общая сводка ===
# Project: TheaterProps
from collections import Counter


def summarize_items(items):
    """Return a summary dict for a list of item records.

    The summary contains the total count, the distribution by category
    and the three most recently issued records.  Records are ordered by
    their issue timestamp, so the newest ones appear first.

    Parameters
    ----------
    items : list of dict
        Each record must contain the keys ``name``, ``category`` and
        ``issued_at``.  ``issued_at`` should be sortable (for example a
        ``datetime`` or an ISO-8601 string).

    Returns
    -------
    dict
        ``{``total``: int, ``by_category``: dict, ``latest``: list}``

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not items:
        raise ValueError("cannot summarize an empty list of items")

    by_category = Counter(item["category"] for item in items)
    latest = sorted(items, key=lambda item: item["issued_at"], reverse=True)
    latest = latest[:3]

    return {
        "total": len(items),
        "by_category": dict(by_category),
        "latest": latest,
    }


def print_summary(summary):
    """Print a human readable report built from a summary dict.

    Parameters
    ----------
    summary : dict
        The dict returned by :func:`summarize_items`.
    """
    print("Total items: {}".format(summary["total"]))
    print("By category:")
    for category, count in sorted(summary["by_category"].items()):
        print("  {}: {}".format(category, count))
    print("Most recent issues:")
    for record in summary["latest"]:
        print("  {} ({}) - {}".format(
            record["name"], record["category"], record["issued_at"]))
