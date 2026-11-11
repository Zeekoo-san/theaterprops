# === Stage 1: Каркас модуля ===
# Project: TheaterProps
from dataclasses import dataclass, field
from typing import List


@dataclass
class Prop:
    name: str
    category: str
    storage: str
    condition: str


def make_demo_props() -> List[Prop]:
    return [
        Prop("mask", "costume", "wardrobe-A", "new"),
        Prop("sword", "prop-weapon", "armory-B", "used"),
        Prop("crown", "accessory", "jeweler-C", "new"),
    ]


def main() -> None:
    for prop in make_demo_props():
        print(f"{prop.name} ({prop.category}) -> {prop.storage} [{prop.condition}]")


if __name__ == "__main__":
    main()
