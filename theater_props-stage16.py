# === Stage 16: История изменений ===
# Project: TheaterProps
from datetime import datetime


class HistoryEntry:
    def __init__(self, changed_at, description):
        self.changed_at = changed_at
        self.description = description

    def __repr__(self):
        return "HistoryEntry({!r}, {!r})".format(self.changed_at, self.description)


class Item:
    def __init__(self, name, category, storage_location, condition):
        self.name = name
        self.category = category
        self.storage_location = storage_location
        self.condition = condition
        self.history = []

    def add_history(self, description):
        self.history.append(HistoryEntry(datetime.now(), description))

    def get_history(self):
        return list(self.history)

    def __repr__(self):
        return "Item({!r}, category={!r}, storage={!r}, condition={!r}, history={})".format(
            self.name, self.category, self.storage_location, self.condition, self.history
        )


def create_sample_item():
    item = Item("Royal Sword", "Weapons", "Armory Room", "Excellent")
    item.add_history("Created in the props database")
    item.add_history("Condition updated: minor scratches noted")
    return item


def print_item_history(item):
    print("Change history for '{}'".format(item.name))
    for entry in item.get_history():
        print("  {} - {}".format(entry.changed_at, entry.description))


if __name__ == "__main__":
    sample = create_sample_item()
    print(sample)
    print_item_history(sample)
