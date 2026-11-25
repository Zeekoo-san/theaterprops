# === Stage 34: Экспорт в CSV ===
# Project: TheaterProps
import csv
import io
from theaterprops.items import Item


def item_to_csv_row(item: Item) -> list:
    return [
        item.name,
        item.category,
        item.storage_location,
        item.condition,
    ]


def export_items_to_csv_string(items) -> str:
    items = list(items)
    buffer = io.StringIO()
    writer = csv.writer(buffer, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow(["name", "category", "storage_location", "condition"])
    for item in items:
        writer.writerow(item_to_csv_row(item))
    return buffer.getvalue()


def export_issue_to_csv_string(issues) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow(["issue_id", "item_name", "scene_id", "issued_by", "issued_at"])
    for issue in issues:
        writer.writerow([issue.issue_id, issue.item_name, issue.scene_id,
                         issue.issued_by, issue.issued_at])
    return buffer.getvalue()


def export_scenes_to_csv_string(scenes) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow(["scene_id", "scene_name", "hall", "capacity"])
    for scene in scenes:
        writer.writerow([scene.scene_id, scene.scene_name,
                         scene.hall, scene.capacity])
    return buffer.getvalue()


def export_returns_to_csv_string(returns) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow(["return_id", "issue_id", "returned_by", "returned_at", "note"])
    for return_record in returns:
        writer.writerow([return_record.return_id, return_record.issue_id,
                         return_record.returned_by, return_record.returned_at,
                         return_record.note])
    return buffer.getvalue()
