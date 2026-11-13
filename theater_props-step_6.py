# === Stage 6: Связанная сущность ===
# Project: TheaterProps
"""Stage 6: Issue records (выдача) linked to props by identifier."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Issue:
    """A single prop hand-out record (выдача).

    Attributes:
        prop_id: identifier of the prop being issued (идентификатор предмета).
        scene_id: identifier of the scene requesting the prop.
        actor_name: name of the actor receiving the prop.
        issued_at: timestamp of the hand-out.
    """

    prop_id: str
    scene_id: str
    actor_name: str
    issued_at: str = field(default_factory=lambda: __import__("datetime").datetime.now().isoformat())

    def __post_init__(self) -> None:
        if not self.prop_id:
            raise ValueError("prop_id cannot be empty")
        if not self.scene_id:
            raise ValueError("scene_id cannot be empty")


class IssueManager:
    """Manages issue records and their relation to props (выдача и реквизит)."""

    def __init__(self) -> None:
        self._issues: Dict[str, Issue] = {}

    def add_issue(
        self,
        prop_id: str,
        scene_id: str,
        actor_name: str,
        issued_at: str | None = None,
    ) -> Issue:
        """Create and store an issue record.

        Args:
            prop_id: identifier of the prop to hand out.
            scene_id: identifier of the requesting scene.
            actor_name: name of the receiving actor.
            issued_at: optional timestamp; defaults to the current time.

        Returns:
            The created Issue instance.

        Raises:
            ValueError: if prop_id or scene_id is empty.
        """
        if not prop_id:
            raise ValueError("prop_id cannot be empty")
        if not scene_id:
            raise ValueError("scene_id cannot be empty")
        if issued_at is None:
            issued_at = __import__("datetime").datetime.now().isoformat()
        issue = Issue(prop_id=prop_id, scene_id=scene_id, actor_name=actor_name, issued_at=issued_at)
        self._issues[issue.prop_id] = issue
        return issue

    def get_issue(self, prop_id: str) -> Issue | None:
        """Return the issue record for a prop, or None if not issued."""
        return self._issues.get(prop_id)

    def list_issues(self) -> list[Issue]:
        """Return all issue records sorted by identifier."""
        return sorted(self._issues.values(), key=lambda i: i.prop_id)

    def __len__(self) -> int:
        return len(self._issues)
