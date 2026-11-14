# === Stage 10: Теги ===
# Project: TheaterProps
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Tag:
    name: str


class TagCollection:
    def __init__(self) -> None:
        self._tags: Dict[str, Tag] = {}

    def add(self, name: str) -> Tag:
        tag = Tag(name)
        self._tags[name.lower()] = tag
        return tag

    def remove(self, name: str) -> bool:
        return self._tags.pop(name.lower(), None) is not None

    def search(self, name: str) -> List[Tag]:
        result = []
        for tag in self._tags.values():
            if name.lower() in tag.name.lower():
                result.append(tag)
        return result


@dataclass
class TaggedItem:
    item_name: str
    category: str
    storage_location: str
    condition: str
    tags: TagCollection


def create_tagged_item(
    item_name: str,
    category: str,
    storage_location: str,
    condition: str,
    tags: Optional[List[str]] = None,
) -> TaggedItem:
    item = TaggedItem(
        item_name=item_name,
        category=category,
        storage_location=storage_location,
        condition=condition,
        tags=TagCollection(),
    )
    for tag_name in tags or []:
        item.tags.add(tag_name)
    return item


def search_by_tag(
    items: List[TaggedItem], tag_name: str
) -> List[TaggedItem]:
    return [
        item
        for item in items
        if any(tag.name.lower() == tag_name.lower() for tag in item.tags.search(tag_name))
    ]


def remove_tag(item: TaggedItem, tag_name: str) -> bool:
    return item.tags.remove(tag_name)
