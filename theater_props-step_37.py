# === Stage 37: Восстановление из копии ===
# Project: TheaterProps
import json
import copy
import os


class BackupManager:
    """Manages backup creation and restoration for TheaterProps data."""

    def __init__(self, backup_dir="theater_props_backup"):
        self.backup_dir = backup_dir

    def _ensure_dir(self):
        if not os.path.isdir(self.backup_dir):
            os.makedirs(self.backup_dir)

    def create_backup(self, props_data):
        """Serialize props data and write it to a backup file."""
        self._ensure_dir()
        filename = "theater_props.json"
        filepath = os.path.join(self.backup_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(props_data, f, indent=4, ensure_ascii=False)
        return filepath

    def _validate_structure(self, props_data):
        """Validate that the restored data has the expected structure."""
        if not isinstance(props_data, dict):
            raise ValueError("Backup data must be a JSON object")

        required_keys = {"items", "scenes", "checkouts"}
        missing = required_keys - set(props_data.keys())
        if missing:
            raise ValueError(f"Missing required keys: {sorted(missing)}")

        if not isinstance(props_data["items"], list):
            raise ValueError("'items' must be a list")
        if not isinstance(props_data["scenes"], list):
            raise ValueError("'scenes' must be a list")
        if not isinstance(props_data["checkouts"], list):
            raise ValueError("'checkouts' must be a list")

        item_fields = {"name", "category", "storage", "status"}
        for i, item in enumerate(props_data["items"]):
            if not isinstance(item, dict):
                raise ValueError(f"Item {i} must be an object")
            missing_fields = item_fields - set(item.keys())
            if missing_fields:
                raise ValueError(f"Item {i} missing fields: {sorted(missing_fields)}")

        return True

    def restore_backup(self, props_data):
        """Validate and deep-copy props data from a backup file."""
        if not self._validate_structure(props_data):
            raise ValueError("Invalid backup structure")
        restored = copy.deepcopy(props_data)
        return restored

    def has_backup(self):
        filepath = os.path.join(self.backup_dir, "theater_props.json")
        return os.path.isfile(filepath)
