# === Stage 9: Сортировка записей ===
# Project: TheaterProps
import datetime


def create_record(name, category, storage, status):
    return {
        "name": name,
        "category": category,
        "storage": storage,
        "status": status,
        "created_at": datetime.datetime.now(),
    }


def sort_by_name(records, ascending=True):
    key = lambda rec: rec["name"].lower()
    if ascending:
        return sorted(records, key=key)
    return sorted(records, key=key, reverse=True)


def sort_by_created_at(records, ascending=True):
    key = lambda rec: rec["created_at"]
    if ascending:
        return sorted(records, key=key)
    return sorted(records, key=key, reverse=True)


def sort_records(records, field, ascending=True):
    if field == "name":
        return sort_by_name(records, ascending)
    if field == "created_at":
        return sort_by_created_at(records, ascending)
    raise ValueError(f"Unknown field: {field}")


if __name__ == "__main__":
    demo = [
        create_record("Hammer", "tools", "workshop", "available"),
        create_record("Crown", "props", "wardrobe", "available"),
        create_record("Sword", "props", "wardrobe", "available"),
    ]

    print("By name ascending:")
    for rec in sort_by_name(demo, True):
        print(rec["name"])

    print("By name descending:")
    for rec in sort_by_name(demo, False):
        print(rec["name"])

    print("By created_at ascending:")
    for rec in sort_by_created_at(demo, True):
        print(rec["name"])

    print("By created_at descending:")
    for rec in sort_by_created_at(demo, False):
        print(rec["name"])
