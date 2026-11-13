# === Stage 8: Генерация идентификаторов ===
# Project: TheaterProps
import string
import secrets


PROJECT_PREFIX = "THP"


def generate_unique_id(length=10, charset=string.ascii_letters + string.digits):
    while True:
        candidate = PROJECT_PREFIX + secrets.token_hex(length // 2)
        if not any(candidate in db for db in _id_databases):
            return candidate


_id_databases = {}


def register_id(id_value, database_name="default"):
    db = _id_databases.setdefault(database_name, set())
    if id_value in db:
        raise ValueError(f"Duplicate identifier {id_value!r} in database {database_name!r}")
    db.add(id_value)


def is_available(id_value, database_name="default"):
    db = _id_databases.get(database_name)
    return db is None or id_value not in db
