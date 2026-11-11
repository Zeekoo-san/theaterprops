# === Stage 2: Проверка полей ===
# Project: TheaterProps
import re

VALID_CATEGORIES = {"weapon", "costume", "prop", "furniture", "lighting", "sound", "special"}
VALID_STATES = {"good", "damaged", "missing", "reserved"}


def normalize_text(value):
    return value.strip().title()


def normalize_category(value):
    return value.strip().lower()


def normalize_state(value):
    return value.strip().lower()


def normalize_storage(value):
    return value.strip()


def validate_name(value):
    if value is None:
        return "Название предмета обязательно."
    if len(value.strip()) < 1:
        return "Название предмета не может быть пустым."
    if len(value.strip()) > 100:
        return "Название предмета не должно превышать 100 символов."
    return None


def validate_category(value):
    if value is None:
        return "Категория обязательна."
    normalized = normalize_category(value)
    if normalized not in VALID_CATEGORIES:
        valid = ", ".join(sorted(VALID_CATEGORIES))
        return f"Недопустимая категория '{value}'. Допустимые значения: {valid}."
    return None


def validate_storage(value):
    if value is None:
        return "Место хранения обязательно."
    if len(value.strip()) < 1:
        return "Место хранения не может быть пустым."
    if len(value.strip()) > 100:
        return "Место хранения не должно превышать 100 символов."
    return None


def validate_state(value):
    if value is None:
        return "Состояние предмета обязательно."
    normalized = normalize_state(value)
    if normalized not in VALID_STATES:
        valid = ", ".join(sorted(VALID_STATES))
        return f"Недопустимое состояние '{value}'. Допустимые значения: {valid}."
    return None


def validate_props_entity(props):
    errors = []
    name_error = validate_name(props.get("name"))
    if name_error:
        errors.append(name_error)
    category_error = validate_category(props.get("category"))
    if category_error:
        errors.append(category_error)
    storage_error = validate_storage(props.get("storage"))
    if storage_error:
        errors.append(storage_error)
    state_error = validate_state(props.get("state"))
    if state_error:
        errors.append(state_error)
    return errors
