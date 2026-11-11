# === Stage 3: Хранилище в памяти ===
# Project: TheaterProps
"""In-memory store for TheaterProp entities.

This module provides a simple, self-contained repository that keeps
theater props (items) in memory. It supports adding props, retrieving
them by identifier, and listing all stored props.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TheaterProp:
    """A single piece of theater equipment.

    Attributes:
        name: The human-readable label of the prop.
        category: The group the prop belongs to, e.g. "costume" or "set".
        storage: The location where the prop is kept.
        condition: The current state of the prop, e.g. "new" or "worn".
        prop_id: A unique identifier assigned by the store.
    """

    name: str
    category: str
    storage: str
    condition: str
    prop_id: str = ""


class PropStore:
    """A minimal in-memory collection of TheaterProp objects."""

    def __init__(self) -> None:
        """Initialize an empty store and prepare the identifier counter."""
        self._props: Dict[str, TheaterProp] = {}
        self._counter = 0

    def add_prop(self, name: str, category: str, storage: str, condition: str) -> TheaterProp:
        """Create a new prop, assign it an id, and store it.

        Args:
            name: The human-readable label of the prop.
            category: The group the prop belongs to.
            storage: The location where the prop is kept.
            condition: The current state of the prop.

        Returns:
            The newly created and stored TheaterProp instance.

        Raises:
            ValueError: If name, category, storage, or condition is empty.
        """
        if not name or not category or not storage or not condition:
            raise ValueError("All fields must be non-empty strings.")

        self._counter += 1
        prop_id = f"PROP-{self._counter:04d}"
        prop = TheaterProp(
            name=name,
            category=category,
            storage=storage,
            condition=condition,
            prop_id=prop_id,
        )
        self._props[prop_id] = prop
        return prop

    def get_prop(self, prop_id: str) -> Optional[TheaterProp]:
        """Return the prop with the given identifier, or None if absent.

        Args:
            prop_id: The identifier to look up.

        Returns:
            The matching TheaterProp, or None if not found.
        """
        return self._props.get(prop_id)

    def list_props(self) -> List[TheaterProp]:
        """Return all stored props.

        Returns:
            A list of all TheaterProp instances currently in the store,
            ordered by identifier.
        """
        return [self._props[prop_id] for prop_id in sorted(self._props)]
