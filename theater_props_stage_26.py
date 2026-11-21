# === Stage 26: Текстовая гистограмма ===
# Project: TheaterProps
def render_warehouse_histogram(data):
    """
    Render a text histogram of warehouse-storage values.

    Each value is a category label; each block represents one item.
    The label is padded to a fixed width so all rows align.
    """
    if not data:
        return "No items recorded.\n"

    labels = sorted(set(data.keys()))
    max_count = max(data.values())
    block = "#"

    lines = []
    for label in labels:
        count = data[label]
        bar = block * count
        lines.append(f"{label:<12} {bar}")

    lines.append("")
    lines.append(f"{'':<12} {'#' * max_count}")
    lines.append("")
    lines.append(f"Total items: {sum(data.values())}")

    return "\n".join(lines) + "\n"


def print_warehouse_histogram(data):
    """Print the warehouse-storage histogram to standard output."""
    print(render_warehouse_histogram(data))


if __name__ == "__main__":
    sample = {
        "prop-room": 4,
        "stage-left": 7,
        "stage-right": 5,
        "prop-closet": 9,
        "backstage": 3,
    }
    print_warehouse_histogram(sample)
