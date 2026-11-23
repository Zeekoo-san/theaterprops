# === Stage 29: Ключевые метрики ===
# Project: TheaterProps
from collections import Counter


def compute_metrics(checked_out, returned):
    """Compute key theater-props metrics from checkout/return records.

    checked_out: list of dicts with keys 'name', 'category', 'status'
    returned:    list of dicts with keys 'name', 'category', 'status'
    """
    total_items = len(checked_out)
    total_returns = len(returned)

    active_items = sum(1 for item in checked_out if item["status"] == "checked_out")
    returned_items = sum(1 for item in returned if item["status"] == "checked_out")

    categories = Counter(
        item["category"] for item in checked_out if item["status"] == "checked_out"
    )
    category_share = {
        cat: count / total_items for cat, count in categories.items()
    }

    overdue = sum(
        1 for item in returned if item["status"] == "overdue"
    )
    overdue_rate = overdue / total_returns if total_returns else 0.0

    return {
        "total_active": total_items,
        "total_returns": total_returns,
        "returned_count": returned_items,
        "return_rate": (
            total_returns / total_items if total_items else 0.0
        ),
        "overdue_count": overdue,
        "overdue_rate": overdue_rate,
        "categories": category_share,
    }


def format_metrics_report(metrics, width=60):
    """Render the metrics dict into a neatly aligned text report."""
    return (
        f"{'THEATER PROPS METRICS':^={width}}\n\n"
        f"Active items ............ {metrics['total_active']}\n"
        f"Total returns ........... {metrics['total_returns']}\n"
        f"Returned items .......... {metrics['returned_count']}\n"
        f"Return rate ............. {metrics['return_rate']:.1%}\n"
        f"Overdue items ........... {metrics['overdue_count']}\n"
        f"Overdue rate ............ {metrics['overdue_rate']:.1%}\n\n"
        "Items by category:\n"
    ) + "".join(
        f"  {cat:<15} {count:>4}  ({share:.1%})\n"
        for cat, share in sorted(metrics["categories"].items())
    )
