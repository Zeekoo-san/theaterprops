# === Stage 13: Слияние записей ===
# Project: TheaterProps
def merge_records(records, fields):
    """Merge two records by choosing a winner for each field."""
    if len(records) != 2:
        raise ValueError("merge_records expects exactly two records")

    first, second = records
    if first is None or second is None:
        raise ValueError("merge_records requires two non-None records")

    merged = {}
    for field in fields:
        if first.get(field) is None and second.get(field) is None:
            merged[field] = None
        elif first.get(field) is None:
            merged[field] = second.get(field)
        elif second.get(field) is None:
            merged[field] = first.get(field)
        else:
            merged[field] = second.get(field)

    return merged


def merge_with_tiebreak(first, second, fields, tiebreak=None):
    """Merge two records with a custom tiebreak function for each field."""
    if len(fields) != 2:
        raise ValueError("tiebreak merge expects exactly two fields")

    merged = {}
    for index, field in enumerate(fields):
        first_value = first.get(field)
        second_value = second.get(field)

        if first_value is None and second_value is None:
            merged[field] = None
        elif first_value is None:
            merged[field] = second_value
        elif second_value is None:
            merged[field] = first_value
        else:
            if tiebreak is not None:
                merged[field] = tiebreak(first_value, second_value)
            else:
                merged[field] = second_value

    return merged


def merge_field_wise(first, second, field):
    """Merge two records choosing a winner for a single field."""
    first_value = first.get(field)
    second_value = second.get(field)

    if first_value is None:
        return second_value
    if second_value is None:
        return first_value

    return second_value


def field_wins(first, second, field, winner="second"):
    """Return the value of field from the chosen winner record."""
    if winner == "first":
        return first.get(field)
    if winner == "second":
        return second.get(field)

    raise ValueError("winner must be 'first' or 'second'")


def merge_all_fields(first, second):
    """Merge two records by choosing the second value for every field."""
    merged = {}

    for key in first:
        merged[key] = second.get(key, first[key])

    for key in second:
        if key not in merged:
            merged[key] = second[key]

    return merged
