# === Stage 42: Настройки приложения ===
# Project: TheaterProps
APP_CONFIG = {
    "app_name": "TheaterProps",
    "version": "1.0.0",
    "max_items_per_category": 10,
    "min_item_name_length": 2,
    "max_item_name_length": 64,
    "allowed_categories": ["props", "costumes", "lighting", "sound", "set", "accessories"],
    "allowed_storage_locations": ["prop_room", "costume_wardrobe", "stage_storage", "tech_room", "dressing_rooms"],
    "allowed_conditions": ["new", "used", "damaged", "missing"],
    "default_condition": "new",
    "default_storage_location": "prop_room",
    "item_id_prefix": "PRP",
    "item_id_length": 6,
    "max_items_in_database": 1000,
    "log_level": "INFO",
    "allowed_log_levels": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
}


def validate_category(value):
    if value not in APP_CONFIG["allowed_categories"]:
        raise ValueError("Category not allowed: {}".format(value))
    return value


def validate_condition(value):
    if value not in APP_CONFIG["allowed_conditions"]:
        raise ValueError("Condition not allowed: {}".format(value))
    return value


def validate_storage_location(value):
    if value not in APP_CONFIG["allowed_storage_locations"]:
        raise ValueError("Storage location not allowed: {}".format(value))
    return value


def validate_item_name(value):
    name = value.strip()
    if len(name) < APP_CONFIG["min_item_name_length"]:
        raise ValueError("Item name too short: {}".format(value))
    if len(name) > APP_CONFIG["max_item_name_length"]:
        raise ValueError("Item name too long: {}".format(value))
    return name


def validate_log_level(value):
    if value not in APP_CONFIG["allowed_log_levels"]:
        raise ValueError("Log level not allowed: {}".format(value))
    return value


def build_config_overrides(overrides):
    valid_overrides = {}
    for key, value in overrides.items():
        if key not in APP_CONFIG:
            raise KeyError("Unknown config key: {}".format(key))
        if key == "allowed_categories":
            valid_overrides[key] = set(value)
        elif key == "allowed_storage_locations":
            valid_overrides[key] = set(value)
        elif key == "allowed_log_levels":
            valid_overrides[key] = set(value)
        else:
            valid_overrides[key] = value
    return valid_overrides


def get_effective_config(overrides=None):
    merged = dict(APP_CONFIG)
    merged.update(build_config_overrides(overrides or {}))
    return merged
