# === Stage 40: Табличный вывод ===
# Project: TheaterProps
"""Stage module: render prop records as a neatly aligned console table."""

from datetime import datetime


def truncate(value, limit):
    """Squeeze a string down to `limit` characters, trimming the tail."""
    text = "" if value is None else str(value)
    return text[:limit]


def format_row(cells, widths):
    """Build one padded line, slicing each cell to fit its allotted width."""
    return "".join(
        truncate(str(cell), width).ljust(width) for cell, width in zip(cells, widths)
    )


def column_widths(records, headers):
    """Measure the widest cell per column, including the header labels."""
    widths = [len(h) for h in headers]
    for record in records:
        cells = record.values()
        for index, cell in enumerate(cells):
            widths[index] = max(widths[index], len(truncate(cell, 30)))
    return widths


def render_table(headers, records):
    """Compose a readable table: header, a divider, then every record row."""
    widths = column_widths(records, headers)
    header_line = format_row(headers, widths)
    divider = "-+-".join("-" * width for width in widths)
    lines = [header_line, divider]
    for record in records:
        lines.append(format_row(record.values(), widths))
    return "\n".join(lines)


if __name__ == "__main__":
    items = [
        {"name": "Sword", "category": "Weapon", "storage": "Armory", "state": "Good"},
        {"name": "Royal Robe", "category": "Costume", "storage": "Wardrobe", "state": "Worn"},
        {"name": "Old Wooden Mask", "category": "Prop", "storage": "Basement", "state": "Damaged"},
        {"name": "Silver Crown", "category": "Regalia", "storage": "Vault", "state": "Mint"},
    ]

    headers = ["Item", "Category", "Storage", "State"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Inventory snapshot generated on {timestamp}")
    print()
    print(render_table(headers, items))
