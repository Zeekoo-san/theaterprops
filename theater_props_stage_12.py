# === Stage 12: Быстрые фильтры ===
# Project: TheaterProps
from datetime import date


def is_today(item):
    return item.get("issued_date") == date.today()


def is_this_week(item):
    today = date.today()
    if item.get("issued_date") is None:
        return False
    issued = item["issued_date"]
    return 0 <= (today - issued).days <= 7


def is_overdue(item):
    return (
        item.get("category") == "equipment"
        and item.get("due_date") is not None
        and item.get("returned") is False
        and item["due_date"] < date.today()
    )


def filter_props(props, filter_name):
    if filter_name == "today":
        return [p for p in props if is_today(p)]
    if filter_name == "this_week":
        return [p for p in props if is_this_week(p)]
    if filter_name == "overdue":
        return [p for p in props if is_overdue(p)]
    return []


if __name__ == "__main__":
    demo = [
        {"title": "Hammer", "category": "equipment", "stored_at": "Toolroom", "status": "checked_out", "issued_date": date.today().isoformat(), "due_date": (date.today() - date(days=1)).isoformat()},
        {"title": "Ladder", "category": "equipment", "stored_at": "Toolroom", "status": "checked_out", "issued_date": (date.today() - date(days=3)).isoformat(), "due_date": (date.today() + date(days=5)).isoformat()},
        {"title": "Curtain", "category": "decor", "stored_at": "Wardrobe", "status": "in_storage", "issued_date": None, "due_date": None},
    ]
    print(filter_props(demo, "today"))
    print(filter_props(demo, "this_week"))
    print(filter_props(demo, "overdue"))
