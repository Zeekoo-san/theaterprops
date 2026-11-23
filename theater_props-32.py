# === Stage 32: Рекомендации ===
# Project: TheaterProps
def suggest_next_action(props, scenes, handed_out, recommendations):
    available = []
    for item in props:
        if not any(hand["item_id"] == item["id"] for hand in handed_out):
            available.append(item)
    if not available:
        return "No items available. Return existing props or add new ones."
    for scene in scenes:
        needed = scene["required_items"]
        provided = [i for i in needed if any(hand["item_id"] == i for hand in handed_out)]
        missing = [i for i in needed if i not in provided]
        if missing:
            candidates = [it for it in available if it["id"] in missing]
            if candidates:
                return f"Assign '{candidates[0]['name']}' to scene '{scene['name']}'."
            else:
                return f"Request '{missing[0]}' storage location or add to inventory."
    for hand in handed_out:
        if hand["returned"] is False and hand["returned_at"] is None:
            return f"Return '{hand['item_name']}' to '{hand['storage_location']}'."
    for item in available:
        if item["category"] == "damaged" and not recommendations.get(item["id"], False):
            return f"Repair or replace item '{item['name']}'."
        if item["category"] == "clean" and item["storage_location"] == "staging":
            return f"Place item '{item['name']}' into active scene."
    return "All props accounted for. Ready for next rehearsal."
