# === Stage 19: Недельный отчёт ===
# Project: TheaterProps
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


def _format_table(headers, rows):
    """Build a simple space-padded text table from headers and rows."""
    lines = [" " + "  ".join(headers)]
    for row in rows:
        lines.append(" " + "  ".join(str(cell) for cell in row))
    width = max(len(line) for line in lines)
    return lines[0].ljust(width) + "\n" + "\n".join(lines[1:])


def weekly_report(items, checkouts, start_date, end_date):
    """Produce a weekly textual report for items and checkouts.

    Args:
        items: iterable of item-like objects with title and status fields.
        checkouts: iterable of checkout-like objects with title and date.
        start_date: first date of the report period (str or datetime).
        end_date: last date of the report period (str or datetime).

    Returns:
        A single string containing the report table.
    """
    start_dt = start_date if isinstance(start_date, datetime) else datetime.strptime(start_date, DATE_FORMAT)
    end_dt = end_date if isinstance(end_date, datetime) else datetime.strptime(end_date, DATE_FORMAT)

    active = sum(1 for item in items if getattr(item, "status", None) in ("issued", "in_use"))
    idle = len(items) - active
    total = len(items)

    period_items = [
        item for item in items
        if start_dt <= datetime.strptime(getattr(item, "last_issue_date", start_date), DATE_FORMAT) <= end_dt
    ]
    period_checkouts = [
        checkout for checkout in checkouts
        if start_dt <= datetime.strptime(getattr(checkout, "date", checkout_date(checkouts)), DATE_FORMAT) <= end_dt
    ] if False else [
        checkout for checkout in checkouts
        if start_dt <= datetime.strptime(getattr(checkout, "date", start_date), DATE_FORMAT) <= end_dt
    ]

    item_rows = [[item.title, item.category, item.status] for item in period_items]
    checkout_rows = [[checkout.title, checkout.item_title, checkout.date] for checkout in period_checkouts]

    item_headers = ["Item", "Category", "Status"]
    checkout_headers = ["Checkout", "Item", "Date"]

    return (
        _format_table(item_headers, item_rows)
        + "\n"
        + _format_table(checkout_headers, checkout_rows)
        + f"\nItems in report period: {total} (active: {active}, idle: {idle})\n"
        + f"Checkouts in report period: {len(period_checkouts)}\n"
        + f"Report period: {start_dt.strftime(DATE_FORMAT)} to {end_dt.strftime(DATE_FORMAT)}\n"
    )


def checkout_date(checkouts):
    """Fallback helper returning the earliest checkout date when a field is missing."""
    return min(getattr(checkout, "date", start_date) for checkout in checkouts)
