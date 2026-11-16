# === Stage 15: Смена статуса ===
# Project: TheaterProps
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional


class ItemStatus(Enum):
    STORED = "stored"
    CHECKED_OUT = "checked_out"
    DAMAGED = "damaged"
    RETIRED = "retired"


class TransitionError(Exception):
    pass


@dataclass
class PropsItem:
    name: str
    category: str
    storage_location: str
    status: ItemStatus = ItemStatus.STORED
    history: list = field(default_factory=list)

    def check_transition(self, new_status: ItemStatus) -> bool:
        if new_status == self.status:
            return False
        allowed = {
            ItemStatus.STORED: {ItemStatus.CHECKED_OUT, ItemStatus.RETIRED},
            ItemStatus.CHECKED_OUT: {ItemStatus.STORED, ItemStatus.DAMAGED},
            ItemStatus.DAMAGED: {ItemStatus.STORED, ItemStatus.RETIRED},
            ItemStatus.RETIRED: set(),
        }
        return new_status in allowed.get(self.status, set())

    def change_status(self, new_status: ItemStatus, reason: str) -> None:
        if not self.check_transition(new_status):
            raise TransitionError(
                f"Invalid transition for '{self.name}': "
                f"'{self.status.value}' -> '{new_status.value}'"
            )
        self.status = new_status
        self.history.append({
            "from": self.status.value,
            "to": new_status.value,
            "reason": reason,
        })
