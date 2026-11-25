# === Stage 36: Ротация резервных копий ===
# Project: TheaterProps
import os
import shutil
import time


def rotate_backups(source_path, max_backups):
    """Keep only the last ``max_backups`` files created from ``source_path``.

    A backup is stored with a timestamp suffix to preserve ordering.
    Files that are older than the allowed number of backups are deleted.
    """
    if not os.path.exists(source_path):
        return

    backups = []
    directory = os.path.dirname(source_path)
    base = os.path.basename(source_path)

    for name in os.listdir(directory):
        if not name.startswith(base + ".bak"):
            continue
        full = os.path.join(directory, name)
        try:
            mtime = os.path.getmtime(full)
        except OSError:
            continue
        backups.append((mtime, full))

    backups.sort()
    for stale in backups[:-max_backups] if max_backups else backups:
        try:
            os.remove(stale[1])
        except OSError:
            pass


def make_backup(source_path, target_dir, max_backups):
    """Copy ``source_path`` into ``target_dir`` and rotate old backups.

    The backup filename embeds the creation timestamp so that the most
    recent copies are retained when ``max_backups`` is exceeded.
    """
    if not os.path.exists(source_path):
        return False

    os.makedirs(target_dir, exist_ok=True)
    timestamp = time.strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(target_dir, f"{os.path.basename(source_path)}.{timestamp}.bak")

    shutil.copy2(source_path, backup_path)
    rotate_backups(backup_path, max_backups)
    return True


def list_backups(target_dir, base_name):
    """Return backup filenames in ``target_dir`` matching ``base_name``.

    The list is ordered from the oldest backup to the newest one.
    """
    if not os.path.isdir(target_dir):
        return []

    backups = []
    for name in os.listdir(target_dir):
        if not name.startswith(base_name + ".bak"):
            continue
        backups.append(name)

    backups.sort(key=lambda name: os.path.getmtime(os.path.join(target_dir, name)))
    return backups
