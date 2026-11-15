# === Stage 11: Постраничный вывод ===
# Project: TheaterProps
from typing import List, Dict, Any


DEFAULT_PAGE_SIZE = 20


def paginate(items: List[Any], page: int, page_size: int) -> Dict[str, Any]:
    """Return a page of items plus navigation metadata.

    Items are 1-indexed for the user, so page 1 returns the first page_size
    elements. Invalid pages fall back to page 1.
    """
    if page_size <= 0:
        page_size = DEFAULT_PAGE_SIZE
    if page < 1:
        page = 1

    total = len(items)
    total_pages = (total + page_size - 1) // page_size
    if total_pages < 1:
        total_pages = 1
    if page > total_pages:
        page = total_pages

    start = (page - 1) * page_size
    end = start + page_size
    page_items = items[start:end]

    return {
        "page": page,
        "page_size": page_size,
        "total_items": total,
        "total_pages": total_pages,
        "items": page_items,
    }


def build_props_list_query(
    items: List[Dict[str, Any]],
    page: int = 1,
    page_size: int = DEFAULT_PAGE_SIZE,
) -> Dict[str, Any]:
    """Convenience wrapper for paginating a list of props."""
    return paginate(items, page, page_size)


def get_page_info(page: int, page_size: int) -> Dict[str, Any]:
    """Return navigation info without the items themselves."""
    if page_size <= 0:
        page_size = DEFAULT_PAGE_SIZE
    if page < 1:
        page = 1
    total_pages = max(1, (page + page_size - 1) // page_size)
    return {
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
    }
