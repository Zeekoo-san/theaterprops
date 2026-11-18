# === Stage 17: Просмотр истории ===
# Project: TheaterProps
from datetime import datetime


def format_record_history(record):
    """Render a single 'item' record as a compact history entry.

    Accepts a dictionary with keys: title, category, storage, status,
    issued_by, issued_at, returned_at, notes. Returns a single-line
    string suitable for display in a compact history view.
    """
    title = record.get("title", "Unknown")
    category = record.get("category", "-")
    storage = record.get("storage", "-")
    status = record.get("status", "-")
    issued_by = record.get("issued_by", "-")
    issued_at = record.get("issued_at", "-")
    returned_at = record.get("returned_at", "-")
    notes = record.get("notes", "")

    parts = [
        f"[{status}] {title} ({category})",
        f"stored at {storage}",
        f"issued by {issued_by} at {issued_at}",
    ]

    if returned_at:
        parts.append(f"returned at {returned_at}")

    if notes:
        parts.append(f"note: {notes}")

    return " | ".join(parts)


def format_history_lines(records):
    """Render a list of item records into a compact history block.

    Each record is formatted with format_record_history and joined
    with blank lines between entries for readability.
    """
    lines = [format_record_history(record) for record in records]
    return "\n".join(lines)
