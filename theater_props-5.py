# === Stage 5: Удаление и восстановление ===
# Project: TheaterProps
from uuid import uuid4


class TheaterError(Exception):
    """Base error for TheaterProps operations."""


class ItemNotFoundError(TheaterError):
    """Raised when an item does not exist or is not available."""


class AlreadyExistsError(TheaterError):
    """Raised when an item with the given identifier already exists."""


class PropsRepository:
    """In-memory repository supporting soft deletion of items."""

    def __init__(self):
        self._items = {}
        self._deleted = {}

    def add(self, identifier, name, category, storage, condition):
        self._validate_unique(identifier)
        self._items[identifier] = {
            "identifier": identifier,
            "name": name,
            "category": category,
            "storage": storage,
            "condition": condition,
        }

    def get(self, identifier):
        item = self._items.get(identifier)
        if item is None:
            raise ItemNotFoundError(identifier)
        return dict(item)

    def delete(self, identifier):
        item = self._items.pop(identifier, None)
        if item is None:
            raise ItemNotFoundError(identifier)
        self._deleted[identifier] = item
        return item

    def restore(self, identifier):
        record = self._deleted.get(identifier)
        if record is None:
            raise ItemNotFoundError(identifier)
        self._items[identifier] = record
        self._deleted.pop(identifier)
        return record

    def is_deleted(self, identifier):
        return identifier in self._deleted

    def list_active(self):
        return [dict(item) for item in self._items.values()]

    def list_deleted(self):
        return [dict(item) for item in self._deleted.values()]

    def _validate_unique(self, identifier):
        if identifier in self._items or identifier in self._deleted:
            raise AlreadyExistsError(identifier)


def build_demo_repository():
    repo = PropsRepository()
    repo.add("prop-001", "Royal Crown", "Regalia", "Armory", "good")
    repo.add("prop-002", "Magic Wand", "Props", "Wardrobe", "excellent")
    return repo


def find_item_by_name(repo, name):
    return next((item for item in repo.list_active() if item["name"] == name), None)


def summarize_condition(repo):
    active = repo.list_active()
    excellent = sum(1 for item in active if item["condition"] == "excellent")
    good = sum(1 for item in active if item["condition"] == "good")
    return f"{len(active)} active items: {excellent} excellent, {good} good"


def soft_delete_all_expired(repo):
    identifiers = [i for i, item in repo.list_active().items() if "expired" in item.get("note", "")]
    for identifier in identifiers:
        repo.delete(identifier)
    return len(identifiers)


def main():
    repo = build_demo_repository()
    print(summarize_condition(repo))

    deleted = repo.delete("prop-001")
    print(f"Deleted {deleted['name']}, status: {repo.is_deleted('prop-001')}")

    restored = repo.restore("prop-001")
    print(f"Restored {restored['name']}")

    missing = repo.delete("does-not-exist")
    print(f"Missing delete returned: {missing}")

    print(f"Active: {len(repo.list_active())}, Deleted: {len(repo.list_deleted())}")


if __name__ == "__main__":
    main()
