# === Stage 38: Отчёт в Markdown ===
# Project: TheaterProps
import datetime


def render_markdown_report(rows, title="Theater Props Report"):
    """Render a list of row lists as a Markdown table with a title."""
    if not rows:
        return f"# {title}\n\n_No data._\n"

    headers = rows[0]
    table = [f"| {' | '.join(headers)} |",
             f"| {' | '.join(['---'] * len(headers))} |"]

    for record in rows[1:]:
        table.append(f"| {' | '.join(str(value) for value in record)} |")

    return f"# {title}\n\n" + "\n".join(table) + "\n"


def write_markdown_report(path, rows, title="Theater Props Report"):
    """Render a Markdown table and write it to the given file path."""
    content = render_markdown_report(rows, title)
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return path


def export_props_report(props, scenes, path="report.md"):
    """Export a props inventory report as a Markdown table."""
    inventory_rows = [
        ["Item", "Category", "Storage Location", "Status"]
    ]
    for prop in props:
        inventory_rows.append([
            prop["name"],
            prop["category"],
            prop["storage_location"],
            prop["status"],
        ])

    sections = [
        ["Scene", "Props"],
    ]
    for scene in scenes:
        sections.append([scene["name"], ", ".join(scene["props"] or [])])

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_rows = [
        ["Generated", timestamp],
        ["Total Props", str(len(props))],
        ["Total Scenes", str(len(scenes))],
    ]

    full_rows = [
        render_markdown_report(inventory_rows, "Props Inventory"),
        render_markdown_report(sections, "Scenes"),
        render_markdown_report(report_rows, "Summary"),
    ]
    return write_markdown_report(path, full_rows)
