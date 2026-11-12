# === Stage 4: Редактирование записей ===
# Project: TheaterProps
import uuid


class EditItemError(Exception):
    pass


ALLOWED_FIELDS = {
    "name",
    "category",
    "storage_location",
    "condition",
}


def is_valid_update(payload):
    if not isinstance(payload, dict):
        return False
    for key in payload:
        if key not in ALLOWED_FIELDS:
            return False
    if not payload:
        return False
    return True


def normalize_update(payload):
    return {
        key: value for key, value in payload.items() if key in ALLOWED_FIELDS
    }


def edit_item_by_id(item_id, payload):
    try:
        item_id = str(item_id)
    except (TypeError, ValueError):
        raise EditItemError("item_id must be convertible to str")

    if not is_valid_update(payload):
        raise EditItemError("update payload must be a non-empty dict with allowed fields")

    for item in items_by_id:
        if item["id"] == item_id:
            allowed = normalize_update(payload)
            for key, value in allowed.items():
                if not isinstance(value, str) or value == "":
                    raise EditItemError(f"field '{key}' must be a non-empty string")
                item[key] = value
            return item

    raise EditItemError(f"item with id '{item_id}' not found")


def get_item_by_id(item_id):
    try:
        item_id = str(item_id)
    except (TypeError, ValueError):
        raise EditItemError("item_id must be convertible to str")

    for item in items_by_id:
        if item["id"] == item_id:
            return item

    raise EditItemError(f"item with id '{item_id}' not found")


def create_item(name, category, storage_location, condition):
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "category": category,
        "storage_location": storage_location,
        "condition": condition,
    }


items_by_id = []
