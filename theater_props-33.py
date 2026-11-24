# === Stage 33: Сериализация ===
# Project: TheaterProps
from datetime import datetime

FORMAT_VERSION = 1


def serialize_item(item):
    """Serialize an item dict to a version-checked representation."""
    if not isinstance(item, dict):
        raise TypeError("item must be a dict")
    required_keys = {"name", "category", "storage_location", "condition"}
    missing = required_keys - item.keys()
    if missing:
        raise ValueError(f"item missing keys: {sorted(missing)}")
    if "id" in item:
        item["id"] = str(item["id"])
    record = {"version": FORMAT_VERSION, "item": item}
    return record


def deserialize_item(record):
    """Deserialize an item record back to an item dict."""
    if not isinstance(record, dict):
        raise TypeError("record must be a dict")
    if "version" not in record:
        raise ValueError("record missing version")
    if record["version"] != FORMAT_VERSION:
        raise ValueError(f"unsupported format version: {record['version']}")
    if "item" not in record:
        raise ValueError("record missing item")
    item = record["item"]
    if not isinstance(item, dict):
        raise TypeError("item must be a dict")
    item.pop("id", None)
    return item


def serialize_checkout(checkout):
    """Serialize a checkout dict to a version-checked representation."""
    if not isinstance(checkout, dict):
        raise TypeError("checkout must be a dict")
    required_keys = {"item_id", "scene_id", "issued_at"}
    missing = required_keys - checkout.keys()
    if missing:
        raise ValueError(f"checkout missing keys: {sorted(missing)}")
    checkout["issued_at"] = _normalize_datetime(checkout["issued_at"])
    record = {"version": FORMAT_VERSION, "checkout": checkout}
    return record


def deserialize_checkout(record):
    """Deserialize a checkout record back to a checkout dict."""
    if not isinstance(record, dict):
        raise TypeError("record must be a dict")
    if "version" not in record:
        raise ValueError("record missing version")
    if record["version"] != FORMAT_VERSION:
        raise ValueError(f"unsupported format version: {record['version']}")
    if "checkout" not in record:
        raise ValueError("record missing checkout")
    checkout = record["checkout"]
    if not isinstance(checkout, dict):
        raise TypeError("checkout must be a dict")
    checkout["issued_at"] = _restore_datetime(checkout["issued_at"])
    return checkout


def _normalize_datetime(value):
    """Normalize various datetime inputs into an ISO string."""
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value).isoformat()
        except ValueError:
            return value
    raise TypeError("issued_at must be a datetime or ISO string")


def _restore_datetime(value):
    """Restore issued_at to a datetime object from an ISO string."""
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            return value
    raise TypeError("issued_at must be a datetime or ISO string")
