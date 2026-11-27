# === Stage 39: HTML-отчёт ===
# Project: TheaterProps
import html
from datetime import datetime


def build_props_report(props, checkouts, return_count):
    lines = []
    lines.append("<!DOCTYPE html>")
    lines.append("<html lang=\"en\">")
    lines.append("<head><meta charset=\"utf-8\"><title>TheaterProps Report</title></head>")
    lines.append("<body>")
    lines.append("<h1>Theater Props Report</h1>")
    lines.append("<p>Generated: " + html.escape(str(datetime.now())) + "</p>")
    lines.append("<h2>Inventory</h2>")
    lines.append("<table border=\"1\" cellpadding=\"4\">")
    lines.append("<tr><th>Name</th><th>Category</th><th>Storage</th><th>Condition</th></tr>")
    for prop in props:
        lines.append("<tr>")
        lines.append("<td>" + html.escape(str(prop["name"])) + "</td>")
        lines.append("<td>" + html.escape(str(prop["category"])) + "</td>")
        lines.append("<td>" + html.escape(str(prop["storage"])) + "</td>")
        lines.append("<td>" + html.escape(str(prop["condition"])) + "</td>")
        lines.append("</tr>")
    lines.append("</table>")
    lines.append("<h2>Active Checkouts</h2>")
    lines.append("<table border=\"1\" cellpadding=\"4\">")
    lines.append("<tr><th>Item</th><th>Scene</th><th>Checked Out</th></tr>")
    for item in checkouts:
        lines.append("<tr>")
        lines.append("<td>" + html.escape(str(item["item"])) + "</td>")
        lines.append("<td>" + html.escape(str(item["scene"])) + "</td>")
        lines.append("<td>" + html.escape(str(item["checked_out"])) + "</td>")
        lines.append("</tr>")
    lines.append("</table>")
    lines.append("<h2>Summary</h2>")
    lines.append("<p>Total items: " + str(len(props)) + "</p>")
    lines.append("<p>Returned items: " + str(return_count) + "</p>")
    lines.append("</body>")
    lines.append("</html>")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sample_props = [
        {"name": "Sword", "category": "Weapon", "storage": "Armory", "condition": "Good"},
        {"name": "Crown", "category": "Royalty", "storage": "Wardrobe", "condition": "Fair"},
    ]
    sample_checkouts = [
        {"item": "Sword", "scene": "Hamlet Act 5", "checked_out": "2024-01-15"},
    ]
    report = build_props_report(sample_props, sample_checkouts, 1)
    print(report)
