# === Stage 30: Активность по дням недели ===
# Project: TheaterProps
from collections import defaultdict


def activity_map_by_weekday(
    checkouts: dict,
    returns: dict,
) -> dict:
    """
    Build a textual activity map of TheaterProps movements, grouped by weekday.

    Parameters
    ----------
    checkouts : dict
        Mapping of item identifier -> number of times handed out during the
        tracked period.
    returns : dict
        Mapping of item identifier -> number of times handed back during the
        tracked period.

    Returns
    -------
    dict
        Day-of-week keys (English short names) each mapping to a list of
        (item_id, value) tuples, ordered by item id.  Days with no activity are
        omitted so the map only shows what actually happened.
    """
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    net = defaultdict(int)
    for item_id, count in checkouts.items():
        net[item_id] += count
    for item_id, count in returns.items():
        net[item_id] -= count

    active_days = defaultdict(list)
    for item_id, value in net.items():
        if value:
            active_days[item_id].append(value)

    ordered = {}
    for item_id in sorted(active_days):
        ordered[item_id] = active_days[item_id]

    result = {}
    for day in weekdays:
        total = sum(ordered.get(item_id, []) for item_id in ordered)
        if total:
            result[day] = total

    return result


def render_activity_map(
    activity_map: dict,
    label: str = "Activity by Weekday",
) -> str:
    """
    Render the activity map produced by :func:`activity_map_by_weekday` as text.

    Parameters
    ----------
    activity_map : dict
        Output of :func:`activity_map_by_weekday`.
    label : str
        Header printed above the table, used to identify the report.

    Returns
    -------
    str
        Human-readable table with one line per item id summarising the net
        movements across every weekday that saw activity.
    """
    lines = [label, "=" * len(label)]
    for item_id in sorted(activity_map):
        values = activity_map[item_id]
        net = sum(values)
        lines.append(f"{item_id}: {net} (net)")
    return "\n".join(lines)
