# === Stage 35: Сохранение в файл ===
# Project: TheaterProps
import os
import json
import tempfile


class StorageFileError(Exception):
    pass


class PropsStorage:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = {}

    def load(self):
        if not os.path.exists(self.filepath):
            self.data = {}
            return
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                raw = file.read().strip()
                if not raw:
                    self.data = {}
                    return
                self.data = json.loads(raw)
        except json.JSONDecodeError:
            self.data = {}

    def save(self):
        directory = os.path.dirname(os.path.abspath(self.filepath))
        file_handle = None
        try:
            file_descriptor, temp_filepath = tempfile.mkstemp(
                prefix='.theater_props_', suffix='.tmp', dir=directory
            )
            file_handle = os.fdopen(file_descriptor, 'w', encoding='utf-8')
            json.dump(self.data, file_handle, ensure_ascii=False, indent=2)
            file_handle.flush()
            os.fsync(file_handle.fileno())
            os.replace(temp_filepath, self.filepath)
        except OSError as error:
            if file_handle is not None:
                file_handle.close()
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)
            raise StorageFileError(str(error))
        else:
            if file_handle is not None:
                file_handle.close()

    def add_item(self, item_id, item):
        self.data[item_id] = item

    def remove_item(self, item_id):
        self.data.pop(item_id, None)

    def get_item(self, item_id):
        return self.data.get(item_id)

    def update_item(self, item_id, item):
        self.data[item_id] = item
