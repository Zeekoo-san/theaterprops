# === Stage 24: Топ записей ===
# Project: TheaterProps
from typing import Iterable, List, Sequence, TypeVar

T = TypeVar("T")


def top_n(records: Iterable[T], key: str, n: int = 5) -> List[T]:
    """Return the n records having the largest value for the given key.

    The key is the name of an attribute (or index) accessed on each record.
    Records are compared by their key values; ties are broken by the original
    order so the result is stable.

    Args:
        records: any iterable of objects supporting the key access.
        key: attribute or index name used for ranking.
        n: how many records to return (clamped to the available count).

    Returns:
        A list with at most n records, ordered from strongest to weakest.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    # Collect (key_value, original_index, record) preserving input order.
    scored = []
    for offset, record in enumerate(records):
        key_value = getattr(record, key)
        scored.append((key_value, offset, record))

    # Sort by key descending, then by original index ascending for stability.
    scored.sort(key=lambda item: item[1], reverse=True)
    scored.sort(key=lambda item: item[0], reverse=True)

    return [item[2] for item in scored[:n]]


if __name__ == "__main__":
    class Prop:
        def __init__(self, name, category, location, condition):
            self.name = name
            self.category = category
            self.location = location
            self.condition = condition

    inventory = [
        Prop("Sword", "weapon", "armory", 0.9),
        Prop("Tent", "set", "warehouse", 0.6),
        Prop("Crown", "prop", "dressing", 0.95),
        Prop("Chair", "furniture", "warehouse", 0.4),
        Prop("Robe", "costume", "dressing", 0.8),
    ]

    for prop in top_n(inventory, "condition", n=3):
        print(f"{prop.name}: {prop.condition}")
