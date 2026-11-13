# === Stage 7: Связи между сущностями ===
# Project: TheaterProps
from typing import Dict, List, Optional, Tuple


class Prop:
    def __init__(self, name: str, category: str, storage: str, condition: str):
        self.name = name
        self.category = category
        self.storage = storage
        self.condition = condition

    def __repr__(self) -> str:
        return f"Prop(name={self.name!r}, category={self.category!r}, storage={self.storage!r}, condition={self.condition!r})"


class Issue:
    def __init__(self, issue_id: str, prop_name: str, actor: str, scene: str, timestamp: str):
        self.issue_id = issue_id
        self.prop_name = prop_name
        self.actor = actor
        self.scene = scene
        self.timestamp = timestamp

    def __repr__(self) -> str:
        return f"Issue(issue_id={self.issue_id!r}, prop_name={self.prop_name!r}, actor={self.actor!r}, scene={self.scene!r}, timestamp={self.timestamp!r})"


class IntegrityError(Exception):
    pass


def get_issues_for_prop(
    issues: List[Issue],
    prop_name: str,
    check_integrity: bool = True,
) -> List[Issue]:
    result: List[Issue] = []
    for issue in issues:
        if issue.prop_name == prop_name:
            if check_integrity:
                if not issue.issue_id:
                    raise IntegrityError(f"Issue without issue_id referencing prop {prop_name!r}")
                if not issue.actor:
                    raise IntegrityError(f"Issue without actor referencing prop {prop_name!r}")
                if not issue.scene:
                    raise IntegrityError(f"Issue without scene referencing prop {prop_name!r}")
            result.append(issue)
    return result


def get_issues_by_id(
    issues: List[Issue],
    issue_ids: List[str],
    check_integrity: bool = True,
) -> List[Issue]:
    wanted: set = set(issue_ids)
    result: List[Issue] = []
    for issue in issues:
        if issue.issue_id in wanted:
            if check_integrity:
                if not issue.prop_name:
                    raise IntegrityError(f"Issue {issue.issue_id!r} references no prop")
                if not issue.actor:
                    raise IntegrityError(f"Issue {issue.issue_id!r} has no actor")
                if not issue.scene:
                    raise IntegrityError(f"Issue {issue.issue_id!r} has no scene")
            result.append(issue)
    return result


def index_issues_by_prop(
    issues: List[Issue],
    check_integrity: bool = True,
) -> Dict[str, List[Issue]]:
    index: Dict[str, List[Issue]] = {}
    for issue in issues:
        if check_integrity:
            if not issue.prop_name:
                raise IntegrityError("Issue references an empty prop name")
            if not issue.issue_id:
                raise IntegrityError(f"Issue has empty issue_id for prop {issue.prop_name!r}")
            if not issue.actor:
                raise IntegrityError(f"Issue {issue.issue_id!r} has no actor")
            if not issue.scene:
                raise IntegrityError(f"Issue {issue.issue_id!r} has no scene")
        index.setdefault(issue.prop_name, []).append(issue)
    return index


def validate_prop_name(prop_name: Optional[str]) -> None:
    if prop_name is None:
        raise IntegrityError("prop_name cannot be None")
    if prop_name == "":
        raise IntegrityError("prop_name cannot be empty")
    if not isinstance(prop_name, str):
        raise IntegrityError("prop_name must be a string")


def find_issue_by_id(issues: List[Issue], issue_id: str) -> Optional[Issue]:
    for issue in issues:
        if issue.issue_id == issue_id:
            return issue
    return None


def summarize_prop_usage(issues: List[Issue], prop_name: str) -> Tuple[int, List[str]]:
    validated = get_issues_for_prop(issues, prop_name, check_integrity=True)
    scenes: List[str] = []
    for issue in validated:
        if issue.scene not in scenes:
            scenes.append(issue.scene)
    return len(validated), sorted(scenes)


def collect_all_issue_ids(issues: List[Issue], check_integrity: bool = True) -> List[str]:
    ids: List[str] = []
    for issue in issues:
        if check_integrity:
            if not issue.issue_id:
                raise IntegrityError("Issue has an empty issue_id")
        ids.append(issue.issue_id)
    return ids


def build_issue_lookup(
    issues: List[Issue],
    check_integrity: bool = True,
) -> Dict[str, Issue]:
    lookup: Dict[str, Issue] = {}
    for issue in issues:
        if check_integrity:
            if not issue.issue_id:
                raise IntegrityError("Issue has an empty issue_id")
            if not issue.prop_name:
                raise IntegrityError(f"Issue {issue.issue_id!r} has no prop")
            if not issue.actor:
                raise IntegrityError(f"Issue {issue.issue_id!r} has no actor")
            if not issue.scene:
                raise IntegrityError(f"Issue {issue.issue_id!r} has no scene")
        lookup[issue.issue_id] = issue
    return lookup
