# === Stage 41: Карточка записи ===
# Project: TheaterProps
def render_prop_card(prop):
    """Render a compact card for one prop record with nested issuances."""
    lines = []
    lines.append(f"• {prop.name} [{prop.category}]")
    lines.append(f"    stored at: {prop.storage}")
    lines.append(f"    condition: {prop.condition}")
    if prop.issuances:
        lines.append(f"    issued {len(prop.issuances)} time(s):")
        for issue in prop.issuances:
            lines.append(f"      - to: {issue.recipient}, scene: {issue.scene}")
    else:
        lines.append("    issued: never")
    return "\n".join(lines)


def render_prop_card(prop):
    lines = []
    lines.append(f"• {prop.name} [{prop.category}]")
    lines.append(f"    stored at: {prop.storage}")
    lines.append(f"    condition: {prop.condition}")
    if prop.issuances:
        lines.append(f"    issued {len(prop.issuances)} time(s):")
        for issue in prop.issuances:
            lines.append(f"      - to: {issue.recipient}, scene: {issue.scene}")
    else:
        lines.append("    issued: never")
    return "\n".join(lines)
