# === Stage 25: Список по сцене ===
# Project: TheaterProps
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class TheaterScene:
    id: str
    name: str
    props: List[str] = field(default_factory=list)
    assigned_to: Dict[str, str] = field(default_factory=dict)


def format_prop_line(item: str) -> str:
    title, category, storage, condition = item.split("|")
    return f"{title:<20} {category:<12} {storage:<18} {condition}"


def build_scene_props_report(scene: TheaterScene) -> List[str]:
    report = []
    report.append(f"Scene: {scene.name}")
    report.append("=" * 64)
    report.append("")
    if not scene.props:
        report.append("No props required for this scene.")
    else:
        report.append(f"Props list ({len(scene.props)} items):")
        report.append("-" * 64)
        for item in scene.props:
            report.append(format_prop_line(item))
    report.append("")
    if scene.assigned_to:
        report.append("Current assignments:")
        report.append("-" * 64)
        for role, prop in scene.assigned_to.items():
            report.append(f"{role:<16} -> {prop}")
    return report


def render_scene_props_report(scene: TheaterScene) -> str:
    return "\n".join(build_scene_props_report(scene))
